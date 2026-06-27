from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "field_interview_flyer.pdf"
QR_IMAGE = ROOT / "mvp" / "assets" / "qr_offline_shinokubo.png"
TARGET_URL = (
    "https://korean-sesame-oil-mvp.vercel.app/"
    "share?src=offline_shinokubo"
)


def style(name, parent, **kwargs):
    return ParagraphStyle(name=name, parent=parent, **kwargs)


def build_pdf():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))
    pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3"))

    styles = getSampleStyleSheet()
    base = style(
        "JapaneseBase",
        styles["BodyText"],
        fontName="HeiseiKakuGo-W5",
        fontSize=11,
        leading=17,
        textColor=colors.HexColor("#23190f"),
        spaceAfter=8,
    )
    title = style(
        "TitleJP",
        base,
        fontSize=27,
        leading=34,
        fontName="HeiseiKakuGo-W5",
        textColor=colors.HexColor("#23190f"),
        spaceAfter=14,
    )
    eyebrow = style(
        "EyebrowJP",
        base,
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#315b43"),
        spaceAfter=8,
    )
    lead = style(
        "LeadJP",
        base,
        fontSize=13,
        leading=20,
        textColor=colors.HexColor("#685d50"),
        spaceAfter=14,
    )
    small = style(
        "SmallJP",
        base,
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#685d50"),
    )
    url_style = style(
        "URLJP",
        small,
        fontSize=7.8,
        leading=10,
        alignment=1,
        wordWrap="CJK",
    )

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=16 * mm,
        leftMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=12 * mm,
    )

    story = []
    story.append(Paragraph("正式販売前・30秒アンケート", eyebrow))
    story.append(Paragraph("韓国のごま油、<br/>家でも使いたいですか。", title))
    story.append(
        Paragraph(
            "韓国の市場や食堂で記憶に残る、ふたを開けた瞬間の香り。"
            "日本で少量入荷できるかを検証しています。",
            lead,
        )
    )

    questions = [
        "最後に買ったごま油のブランドや購入場所",
        "韓国のごま油の香りを覚えているか",
        "ビビンバ、ナムル、キンパ、卵かけご飯など、使いたい料理",
        "100ml 1,480円 / 3本 3,980円の価格感",
    ]
    question_rows = [
        [Paragraph(f"{idx}.", base), Paragraph(text, base)]
        for idx, text in enumerate(questions, start=1)
    ]
    question_table = Table(question_rows, colWidths=[12 * mm, 80 * mm])
    question_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#315b43")),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )

    qr = Image(str(QR_IMAGE), width=70 * mm, height=70 * mm)
    qr_box = Table(
        [
            [qr],
            [Paragraph("QRから30秒回答", style("QRLabel", base, alignment=1, fontSize=12, leading=16))],
            [Paragraph(TARGET_URL, url_style)],
        ],
        colWidths=[70 * mm],
    )
    qr_box.setStyle(
        TableStyle(
            [
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#e1d1bb")),
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#fffaf1")),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    body = Table(
        [[question_table, qr_box]],
        colWidths=[96 * mm, 74 * mm],
        hAlign="LEFT",
    )
    body.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    story.append(body)
    story.append(Spacer(1, 12))

    notice = (
        "住所・電話番号・メールアドレスなどの個人情報は不要です。"
        "食品として販売する場合は、日本の輸入・食品表示条件を確認してから案内します。"
    )
    story.append(
        Table(
            [[Paragraph(notice, small)]],
            colWidths=[170 * mm],
            style=[
                ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#e1d1bb")),
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#fffaf1")),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ],
        )
    )
    story.append(Spacer(1, 8))
    story.append(Paragraph("Korean sesame oil MVP validation - offline QR flyer", small))

    doc.build(story)


if __name__ == "__main__":
    build_pdf()
    print(OUTPUT)
