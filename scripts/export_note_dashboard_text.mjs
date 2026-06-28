#!/usr/bin/env node
// Export the logged-in note dashboard body text through a local Chrome/Edge CDP port.

import { mkdir, writeFile } from "node:fs/promises";
import { dirname, resolve } from "node:path";

const DEFAULT_URL = "https://note.com/sitesettings/stats";
const DEFAULT_OUTPUT = ".tmp/note_dashboard_current.txt";

function parseArgs(argv) {
  const args = {
    port: "9222",
    host: "127.0.0.1",
    url: DEFAULT_URL,
    output: DEFAULT_OUTPUT,
    refresh: false,
    waitMs: 1500,
  };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--port") args.port = argv[++i];
    else if (arg === "--host") args.host = argv[++i];
    else if (arg === "--url") args.url = argv[++i];
    else if (arg === "--output") args.output = argv[++i];
    else if (arg === "--refresh") args.refresh = true;
    else if (arg === "--wait-ms") args.waitMs = Number(argv[++i]);
    else if (arg === "--help" || arg === "-h") {
      printHelp();
      process.exit(0);
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }
  return args;
}

function printHelp() {
  console.log(`Usage: node scripts/export_note_dashboard_text.mjs [options]

Options:
  --host HOST        CDP host, default 127.0.0.1
  --port PORT        CDP port, default 9222
  --url URL          note dashboard URL, default ${DEFAULT_URL}
  --output PATH      Output UTF-8 text file, default ${DEFAULT_OUTPUT}
  --refresh          Reload the dashboard tab before reading text
  --wait-ms N        Wait after opening/reloading before reading, default 1500
`);
}

class CdpClient {
  constructor(webSocketDebuggerUrl) {
    this.url = webSocketDebuggerUrl;
    this.nextId = 0;
    this.pending = new Map();
  }

  async connect() {
    this.ws = new WebSocket(this.url);
    await new Promise((resolve, reject) => {
      const timer = setTimeout(() => reject(new Error("CDP websocket connect timeout")), 5000);
      this.ws.onopen = () => {
        clearTimeout(timer);
        resolve();
      };
      this.ws.onerror = (event) => {
        clearTimeout(timer);
        reject(event.error || new Error("CDP websocket error"));
      };
    });
    this.ws.onmessage = (event) => {
      const message = JSON.parse(event.data);
      if (!message.id || !this.pending.has(message.id)) return;
      const handlers = this.pending.get(message.id);
      this.pending.delete(message.id);
      if (message.error) handlers.reject(new Error(JSON.stringify(message.error)));
      else handlers.resolve(message.result);
    };
  }

  send(method, params = {}, timeoutMs = 20000) {
    const id = ++this.nextId;
    this.ws.send(JSON.stringify({ id, method, params }));
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => {
        this.pending.delete(id);
        reject(new Error(`${method} timeout`));
      }, timeoutMs);
      this.pending.set(id, {
        resolve: (value) => {
          clearTimeout(timer);
          resolve(value);
        },
        reject: (error) => {
          clearTimeout(timer);
          reject(error);
        },
      });
    });
  }

  async evaluate(expression) {
    return this.send("Runtime.evaluate", {
      expression,
      awaitPromise: true,
      returnByValue: true,
    });
  }

  close() {
    this.ws.close();
  }
}

async function sleep(ms) {
  await new Promise((resolve) => setTimeout(resolve, ms));
}

async function fetchJson(url, options = {}) {
  const response = await fetch(url, options);
  if (!response.ok) throw new Error(`${url} returned HTTP ${response.status}`);
  return response.json();
}

async function findOrOpenTarget(baseUrl, dashboardUrl) {
  let pages = await fetchJson(`${baseUrl}/json/list`);
  let target = pages.find((page) => page.url && page.url.includes("/sitesettings/stats"));
  if (target) return target;

  await fetchJson(`${baseUrl}/json/new?${encodeURIComponent(dashboardUrl)}`, { method: "PUT" });
  await sleep(1500);
  pages = await fetchJson(`${baseUrl}/json/list`);
  target = pages.find((page) => page.url && page.url.includes("/sitesettings/stats"));
  if (!target) throw new Error("Could not find or open note dashboard CDP target.");
  return target;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const baseUrl = `http://${args.host}:${args.port}`;
  const target = await findOrOpenTarget(baseUrl, args.url);
  const client = new CdpClient(target.webSocketDebuggerUrl);
  await client.connect();
  try {
    await client.send("Runtime.enable");
    await client.send("Page.enable");
    if (args.refresh) {
      await client.send("Page.reload", { ignoreCache: true });
    }
    await sleep(args.waitMs);
    const result = await client.evaluate("document.body ? document.body.innerText : ''");
    const text = result.result?.value || "";
    const outputPath = resolve(args.output);
    await mkdir(dirname(outputPath), { recursive: true });
    await writeFile(outputPath, text, "utf8");
    console.log(`Wrote ${outputPath} from ${target.url} (${text.length} chars)`);
  } finally {
    client.close();
  }
}

main().catch((error) => {
  console.error(error.message || String(error));
  process.exit(1);
});
