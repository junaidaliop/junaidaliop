#!/usr/bin/env python3
"""Generate the GitHub profile hero banner — simple, sharp, centered."""

from __future__ import annotations

from pathlib import Path
import subprocess

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = ROOT / "assets" / "profile"

HERO_SIZE = (1600, 460)
SCALE = 2  # render at 2x and downscale for crispness

DARK = {
    "bg_top":     (15, 11, 31),
    "bg_bottom":  (4, 4, 12),
    "grid":       (124, 58, 237, 22),
    "text":       (246, 240, 252),
    "muted":      (180, 168, 210),
    "violet":     (167, 139, 250),
    "violet_deep":(124, 58, 237),
    "cyan":       (34, 211, 238),
    "lavender":   (196, 181, 253),
    "glow_a":     (124, 58, 237),
    "glow_b":     (34, 211, 238),
}

LIGHT = {
    "bg_top":     (250, 246, 254),
    "bg_bottom":  (235, 226, 248),
    "grid":       (124, 58, 237, 32),
    "text":       (26, 14, 46),
    "muted":      (102, 84, 138),
    "violet":     (91, 33, 182),
    "violet_deep":(76, 29, 149),
    "cyan":       (14, 116, 144),
    "lavender":   (124, 58, 237),
    "glow_a":     (167, 139, 250),
    "glow_b":     (103, 232, 249),
}


def ensure_dirs() -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)


def font_path(pattern: str) -> str:
    result = subprocess.run(
        ["fc-match", "-f", "%{file}\n", pattern],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


FIRA_REGULAR = font_path("Fira Code")
FIRA_BOLD = font_path("Fira Code:style=Bold")


def load_font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = FIRA_BOLD if bold else FIRA_REGULAR
    return ImageFont.truetype(path, size=size)


def vertical_gradient(size, top, bottom):
    width, height = size
    base = Image.new("RGB", size, top)
    draw = ImageDraw.Draw(base)
    for y in range(height):
        t = y / max(height - 1, 1)
        color = tuple(int(top[i] * (1 - t) + bottom[i] * t) for i in range(3))
        draw.line((0, y, width, y), fill=color)
    return base


def draw_glow(image, center, radius, color, alpha):
    layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    x, y = center
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color, alpha))
    blurred = layer.filter(ImageFilter.GaussianBlur(radius=radius * 0.55))
    image.alpha_composite(blurred)


def draw_grid(draw, size, color):
    width, height = size
    spacing = 80 * SCALE
    for x in range(0, width, spacing):
        draw.line((x, 0, x, height), fill=color, width=1)
    for y in range(0, height, spacing):
        draw.line((0, y, width, y), fill=color, width=1)


def text_width(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def build_hero(name: str, palette: dict) -> None:
    # Render at SCALE x size then downscale — sharper text edges
    render_size = (HERO_SIZE[0] * SCALE, HERO_SIZE[1] * SCALE)
    image = vertical_gradient(render_size, palette["bg_top"], palette["bg_bottom"]).convert("RGBA")
    draw = ImageDraw.Draw(image, "RGBA")

    # very subtle coordinate grid
    draw_grid(draw, render_size, palette["grid"])

    # ambient glows — restrained, behind text
    draw_glow(image, (render_size[0] // 2, 110 * SCALE), 260 * SCALE, palette["glow_a"], 70)
    draw_glow(image, (render_size[0] // 2, 360 * SCALE), 240 * SCALE, palette["glow_b"], 45)
    draw = ImageDraw.Draw(image, "RGBA")

    # Fonts (scaled) — name dominant, headline 2nd, sub 3rd
    name_font     = load_font(66 * SCALE, bold=True)
    headline_font = load_font(40 * SCALE, bold=True)
    sub_font      = load_font(26 * SCALE)

    cx = render_size[0] // 2

    # NAME — dominant, centered (slightly higher on the canvas)
    full_name = "MUHAMMAD JUNAID ALI ASIF RAJA"
    nw = text_width(draw, full_name, name_font)
    ny = 130 * SCALE
    draw.text((cx - nw // 2, ny), full_name, font=name_font, fill=(*palette["text"], 255))

    # Divider rule — short, centered, violet
    rule_w = 160 * SCALE
    rule_y = ny + 92 * SCALE
    draw.rounded_rectangle(
        (cx - rule_w // 2, rule_y, cx + rule_w // 2, rule_y + 6 * SCALE),
        radius=3 * SCALE,
        fill=(*palette["violet"], 235),
    )

    # Headline — secondary, smaller
    headline = "Fractional Deep Learning"
    hw = text_width(draw, headline, headline_font)
    hy = rule_y + 30 * SCALE
    draw.text((cx - hw // 2, hy), headline, font=headline_font, fill=(*palette["violet"], 255))

    # Sub-tag — three motifs separated by mid-dots
    sub = "scientific machine learning  ·  fractional calculus  ·  deep learning"
    sw = text_width(draw, sub, sub_font)
    sy = hy + 68 * SCALE
    draw.text((cx - sw // 2, sy), sub, font=sub_font, fill=(*palette["lavender"], 240))

    # Downsample with high-quality filter for crisper output
    final = image.resize(HERO_SIZE, Image.LANCZOS)
    final.convert("RGB").save(ASSETS_DIR / name, "PNG", optimize=True)


def main() -> None:
    ensure_dirs()
    build_hero("hero-dark.png",  DARK)
    build_hero("hero-light.png", LIGHT)
    print(f"Built assets in {ASSETS_DIR}")


if __name__ == "__main__":
    main()
