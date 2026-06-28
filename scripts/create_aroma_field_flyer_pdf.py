from pathlib import Path
import shutil

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "field_aroma_flyer.pdf"
DOCS_OUTPUT = ROOT / "docs" / "field_aroma_flyer.pdf"
DOCS_ALIAS_OUTPUT = ROOT / "docs" / "field-aroma-flyer.pdf"
QR_IMAGE = ROOT / "mvp" / "assets" / "qr_offline_aromaloss.png"
TARGET_URL = "https://korean-sesame-oil-mvp.vercel.app/quick-answer?src=offline_aromaloss"


def style(name, parent, **kwargs):
    return ParagraphStyle(name=name, parent=parent, **kwargs)


def build_pdf():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))

    styles = getSampleStyleSheet()
    base = style(
        "JapaneseBase",
        styles["BodyText"],
        fontName="HeiseiKakuGo-W5",
        fontSize=10.5,
        leading=16,
        textColor=colors.HexColor("#221a13"),
        spaceAfter=7,
    )
    title = style(
        "TitleJP",
        base,
        fontSize=24,
        leading=31,
        textColor=colors.HexColor("#221a13"),
        spaceAfter=12,
    )
    eyebrow = style(
        "EyebrowJP",
        base,
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#2d5b45"),
        spaceAfter=8,
    )
    lead = style(
        "LeadJP",
        base,
        fontSize=12.5,
        leading=19,
        textColor=colors.HexColor("#665c52"),
        spaceAfter=13,
    )
    small = style(
        "SmallJP",
        base,
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#665c52"),
    )
    url_style = style(
        "URLJP",
        small,
        fontSize=7.6,
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
    story.append(Paragraph("正式販売前・30秒メモ", eyebrow))
    story.append(Paragraph("ごま油、炒めるより<br/>最後の香りに使いますか？", title))
    story.append(
        Paragraph(
            "いま家で使っているごま油を仕上げに少しかけるか、"
            "瓶の大きさ、開封後の期間、香りが一番よかった使い方を確認しています。",
            lead,
        )
    )

    questions = [
        "炒め油か、仕上げの香味油として使うか",
        "最後に買った店・ブランド・容量・価格",
        "開封後どのくらい経ったか",
        "香りが一番よかった料理やタイミング",
        "5g・110ml・しぼりたて候補で十分か",
        "製造日・搾りたて感・100ml小瓶・遮光瓶への反応",
    ]
    question_rows = [
        [Paragraph(f"{idx}.", base), Paragraph(text, base)]
        for idx, text in enumerate(questions, start=1)
    ]
    question_table = Table(question_rows, colWidths=[12 * mm, 82 * mm])
    question_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#2d5b45")),
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
                ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#decfba")),
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#fffaf2")),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    body = Table([[question_table, qr_box]], colWidths=[98 * mm, 74 * mm], hAlign="LEFT")
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
        "正式販売前の検証で、決済や配送先は受け付けていません。"
    )
    story.append(
        Table(
            [[Paragraph(notice, small)]],
            colWidths=[170 * mm],
            style=[
                ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#decfba")),
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#fffaf2")),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ],
        )
    )
    story.append(Spacer(1, 8))
    story.append(Paragraph("Korean sesame oil MVP validation - offline aroma retention flyer", small))

    doc.build(story)
    shutil.copyfile(OUTPUT, DOCS_OUTPUT)
    shutil.copyfile(OUTPUT, DOCS_ALIAS_OUTPUT)


if __name__ == "__main__":
    build_pdf()
    print(OUTPUT)
