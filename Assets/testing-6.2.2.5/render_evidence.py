"""Render clean full-bleed white evidence PNGs for the report."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
W = 960
PAD = 28
GREEN = (2, 122, 72)
GREEN_BG = (236, 253, 243)
GREEN_BD = (171, 239, 198)
GRAY = (102, 112, 133)
DARK = (16, 24, 40)
ROW = (29, 41, 57)
LINE = (242, 244, 247)
HEAD_BG = (249, 250, 251)
CHIP_BG = (242, 244, 247)
CHIP_BD = (228, 231, 236)
WHITE = (255, 255, 255)
BORDER = (228, 231, 236)


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(fr"C:\Windows\Fonts\{name}", size)


F_REPO = font("segoeuil.ttf", 13)
F_TITLE = font("segoeuib.ttf", 30)
F_BADGE = font("segoeuib.ttf", 14)
F_CHIP = font("segoeui.ttf", 13)
F_TH = font("segoeuisemibold.ttf", 11) if Path(r"C:\Windows\Fonts\segoeuisemibold.ttf").exists() else font("segoeuib.ttf", 11)
F_OK = font("segoeuib.ttf", 14)
F_NAME = font("consola.ttf", 13)
F_DUR = font("segoeui.ttf", 13)
F_FOOT = font("segoeui.ttf", 12)
F_SUB = font("segoeui.ttf", 14)
F_CELL = font("segoeui.ttf", 15)
F_REPO_B = font("segoeuib.ttf", 15)


def text_w(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> int:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def text_h(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> int:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[3] - box[1]


def rounded_rect(draw: ImageDraw.ImageDraw, xy, fill, outline=None, radius=8, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def render_table(path: Path, repo: str, title: str, badge: str, chips: list[str], rows: list[tuple[str, str, str]]):
    # Measure height
    tmp = Image.new("RGB", (W, 10), WHITE)
    d = ImageDraw.Draw(tmp)
    y = PAD
    y += text_h(d, repo, F_REPO) + 6
    y += text_h(d, title, F_TITLE) + 14
    y += 28 + 16  # chips row
    y += 36  # header
    y += len(rows) * 34
    y += 18 + text_h(d, "foot", F_FOOT) + PAD

    img = Image.new("RGB", (W, y), WHITE)
    draw = ImageDraw.Draw(img)

    x = PAD
    cy = PAD
    draw.text((x, cy), repo.upper(), font=F_REPO, fill=GRAY)
    cy += text_h(draw, repo, F_REPO) + 6
    draw.text((x, cy), title, font=F_TITLE, fill=DARK)

    bw = text_w(draw, badge, F_BADGE) + 28
    bh = 30
    bx1 = W - PAD - bw
    by1 = PAD + 8
    rounded_rect(draw, (bx1, by1, bx1 + bw, by1 + bh), GREEN_BG, GREEN_BD, radius=16)
    draw.text((bx1 + 14, by1 + 6), badge, font=F_BADGE, fill=GREEN)

    cy += text_h(draw, title, F_TITLE) + 14
    cx = x
    for chip in chips:
        cw = text_w(draw, chip, F_CHIP) + 20
        rounded_rect(draw, (cx, cy, cx + cw, cy + 26), CHIP_BG, CHIP_BD, radius=6)
        draw.text((cx + 10, cy + 4), chip, font=F_CHIP, fill=ROW)
        cx += cw + 8
    cy += 26 + 16

    # table
    col_ok, col_dur = 100, 80
    col_name = W - 2 * PAD - col_ok - col_dur
    table_top = cy
    table_bottom = cy + 36 + len(rows) * 34
    rounded_rect(draw, (PAD, table_top, W - PAD, table_bottom), WHITE, BORDER, radius=8)

    # header fill
    draw.rectangle((PAD + 1, table_top + 1, W - PAD - 1, table_top + 36), fill=HEAD_BG)
    draw.text((PAD + 12, table_top + 10), "RESULTADO", font=F_TH, fill=GRAY)
    draw.text((PAD + col_ok, table_top + 10), "PRUEBA", font=F_TH, fill=GRAY)
    dur_label = "DURACIÓN"
    draw.text((W - PAD - 12 - text_w(draw, dur_label, F_TH), table_top + 10), dur_label, font=F_TH, fill=GRAY)
    draw.line((PAD, table_top + 36, W - PAD, table_top + 36), fill=BORDER)

    ry = table_top + 36
    for i, (status, name, dur) in enumerate(rows):
        if i:
            draw.line((PAD + 1, ry, W - PAD - 1, ry), fill=LINE)
        draw.text((PAD + 12, ry + 9), status, font=F_OK, fill=GREEN)
        draw.text((PAD + col_ok, ry + 10), name, font=F_NAME, fill=ROW)
        draw.text((W - PAD - 12 - text_w(draw, dur, F_DUR), ry + 10), dur, font=F_DUR, fill=GRAY)
        ry += 34

    cy = table_bottom + 16
    draw.text((PAD, cy), "FreshSense · Evidencia Testing Suite · Sprint Review", font=F_FOOT, fill=(152, 162, 179))
    img.save(path, "PNG", optimize=True)
    print(f"wrote {path.name} {img.size}")


def render_summary(path: Path):
    rows = [
        ("Freshsense-EDGE", "9", "16", "25", "Passed"),
        ("BackEnd", "4", "3", "7", "Passed · BUILD SUCCESS"),
    ]
    h = PAD + 40 + 24 + 40 + len(rows) * 48 + 70 + PAD
    img = Image.new("RGB", (W, h), WHITE)
    draw = ImageDraw.Draw(img)
    y = PAD
    draw.text((PAD, y), "Testing Suite Evidence", font=F_TITLE, fill=DARK)
    y += text_h(draw, "Testing Suite Evidence", F_TITLE) + 8
    draw.text((PAD, y), "Sprint Review · Freshsense-EDGE y BackEnd · unitarios e integrales", font=F_SUB, fill=GRAY)
    y += 28

    table_top = y
    table_bottom = y + 40 + len(rows) * 48
    rounded_rect(draw, (PAD, table_top, W - PAD, table_bottom), WHITE, BORDER, radius=8)
    draw.rectangle((PAD + 1, table_top + 1, W - PAD - 1, table_top + 40), fill=HEAD_BG)
    headers = [("COMPONENTE", PAD + 12), ("UNITARIOS", PAD + 280), ("INTEGRALES", PAD + 420), ("TOTAL", PAD + 580), ("RESULTADO", PAD + 700)]
    for label, hx in headers:
        draw.text((hx, table_top + 12), label, font=F_TH, fill=GRAY)
    draw.line((PAD, table_top + 40, W - PAD, table_top + 40), fill=BORDER)

    ry = table_top + 40
    for i, (comp, u, integ, total, res) in enumerate(rows):
        if i:
            draw.line((PAD + 1, ry, W - PAD - 1, ry), fill=LINE)
        draw.text((PAD + 12, ry + 14), comp, font=F_REPO_B, fill=DARK)
        draw.text((PAD + 280, ry + 14), u, font=F_CELL, fill=DARK)
        draw.text((PAD + 420, ry + 14), integ, font=F_CELL, fill=DARK)
        draw.text((PAD + 580, ry + 14), total, font=F_CELL, fill=DARK)
        draw.text((PAD + 700, ry + 14), res, font=F_OK, fill=GREEN)
        ry += 48

    y = table_bottom + 16
    banner = "32 pruebas ejecutadas · 0 fallos · 0 errores"
    bw = W - 2 * PAD
    rounded_rect(draw, (PAD, y, PAD + bw, y + 44), GREEN_BG, GREEN_BD, radius=8)
    draw.text((PAD + 16, y + 12), banner, font=F_BADGE, fill=GREEN)
    y += 56
    draw.text((PAD, y), "FreshSense · Evidencia Testing Suite · Sprint Review", font=F_FOOT, fill=(152, 162, 179))
    img.save(path, "PNG", optimize=True)
    print(f"wrote {path.name} {img.size}")


def main():
    render_summary(OUT / "testing-resumen.png")
    render_table(
        OUT / "edge-unitarios.png",
        "Freshsense-EDGE",
        "Pruebas unitarias",
        "9 passed",
        ["pytest", "frescura + claim"],
        [
            ("Passed", "verde cuando los 3 ejes están en rango", "2 ms"),
            ("Passed", "verde en frutas con etileno bajo", "1 ms"),
            ("Passed", "amarillo cerca del límite", "1 ms"),
            ("Passed", "rojo lejos del rango", "1 ms"),
            ("Passed", "gana el peor eje (humedad)", "1 ms"),
            ("Passed", "rojo por etileno alto en frutas", "1 ms"),
            ("Passed", "amarillo por etileno cerca del límite", "1 ms"),
            ("Passed", "guarda el secreto del dispositivo", "2 ms"),
            ("Passed", "rechaza código inválido", "1 ms"),
        ],
    )
    render_table(
        OUT / "edge-integrales.png",
        "Freshsense-EDGE",
        "Pruebas de integración",
        "16 passed",
        ["pytest", "API Edge / sensor-readings"],
        [
            ("Passed", "acepta lectura válida", "20 ms"),
            ("Passed", "clasifica por categoría del dispositivo", "6 ms"),
            ("Passed", "verde dentro del rango de frutas", "6 ms"),
            ("Passed", "rojo cuando el etileno es alto", "7 ms"),
            ("Passed", "acepta aliases del firmware embebido", "7 ms"),
            ("Passed", "acepta ruta física y device UUID", "7 ms"),
            ("Passed", "unknown si el dispositivo no tiene categoría", "7 ms"),
            ("Passed", "umbrales incluyen etileno", "5 ms"),
            ("Passed", "registra categoría del dispositivo", "7 ms"),
            ("Passed", "rechaza categoría desconocida", "6 ms"),
            ("Passed", "rechaza lectura sin etileno", "5 ms"),
            ("Passed", "rechaza campo faltante", "6 ms"),
            ("Passed", "rechaza humedad fuera de rango", "6 ms"),
            ("Passed", "rechaza formato de hora inválido", "16 ms"),
            ("Passed", "sirve la página de setup", "5 ms"),
            ("Passed", "claim falla con gracia sin BackEnd", "7 ms"),
        ],
    )
    render_table(
        OUT / "backend-unitarios.png",
        "BackEnd",
        "Pruebas unitarias",
        "4 passed · BUILD SUCCESS",
        ["Maven / JUnit 5", "TS41 · US06"],
        [
            ("Passed", "acepta lectura Edge completa", "OK"),
            ("Passed", "rechaza deviceId vacío", "OK"),
            ("Passed", "rechaza temperatura nula", "OK"),
            ("Passed", "rechaza etileno nulo (TS41 / US06)", "OK"),
        ],
    )
    render_table(
        OUT / "backend-integrales.png",
        "BackEnd",
        "Pruebas de integración",
        "3 passed · BUILD SUCCESS",
        ["Maven / MockMvc", "POST /api/edge/readings"],
        [
            ("Passed", "POST /api/edge/readings con clave válida → 201", "OK"),
            ("Passed", "POST /api/edge/readings con clave inválida → 401", "OK"),
            ("Passed", "POST /api/edge/readings sin etileno → 400", "OK"),
        ],
    )


if __name__ == "__main__":
    main()
