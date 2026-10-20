#!/usr/bin/env python3
"""Generate docs/demo.gif — IA 385 database platforms."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "demo.gif"
W, H = 720, 200
BG = (15, 23, 42)
PANEL = (30, 41, 59)
SQL = (56, 189, 248)
MYSQL = (251, 191, 36)
ORA = (239, 68, 68)
TEXT = (226, 232, 240)


def load_font(size: int):
    for name in ("consola.ttf", "Consolas.ttf", "segoeui.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def frame(title: str, body: str, accent: tuple[int, int, int]) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((24, 24, W - 24, H - 24), radius=12, fill=PANEL)
    draw.rounded_rectangle((24, 24, 32, H - 24), radius=4, fill=accent)
    draw.text((48, 36), title, fill=accent, font=load_font(22))
    draw.text((48, 82), body, fill=TEXT, font=load_font(16))
    return img


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    frames = [
        frame("Lab build", "Lab 1 environment + Lab 2 MySQL install", MYSQL),
        frame("SQL Server", "Assignment 3 - Community Edition setup", SQL),
        frame("Oracle", "Assignment 4 - install walkthrough", ORA),
        frame("Hardening", "Users, roles, password policy, SQL labs", SQL),
    ]
    frames[0].save(OUT, save_all=True, append_images=frames[1:], duration=2000, loop=0)
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
