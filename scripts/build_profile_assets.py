#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
import math
import random
import subprocess

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = ROOT / "assets" / "profile"

HERO_SIZE = (1600, 460)

DARK = {
    "bg_top": (15, 11, 31),
    "bg_bottom": (4, 4, 12),
    "grid": (124, 58, 237, 28),
    "text": (244, 239, 250),
    "muted": (180, 168, 210),
    "violet": (167, 139, 250),
    "violet_deep": (124, 58, 237),
    "cyan": (34, 211, 238),
    "emerald": (16, 185, 129),
    "lavender": (196, 181, 253),
}

LIGHT = {
    "bg_top": (250, 246, 254),
    "bg_bottom": (236, 227, 248),
    "grid": (124, 58, 237, 38),
    "text": (26, 14, 46),
    "muted": (88, 70, 124),
    "violet": (91, 33, 182),
    "violet_deep": (76, 29, 149),
    "cyan": (14, 116, 144),
    "emerald": (4, 120, 87),
    "lavender": (167, 139, 250),
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


def vertical_gradient(size: tuple[int, int], top: tuple[int, int, int], bottom: tuple[int, int, int]) -> Image.Image:
    width, height = size
    base = Image.new("RGB", size, top)
    draw = ImageDraw.Draw(base)
    for y in range(height):
        t = y / max(height - 1, 1)
        color = tuple(int(top[i] * (1 - t) + bottom[i] * t) for i in range(3))
        draw.line((0, y, width, y), fill=color)
    return base


def draw_glow(
    image: Image.Image,
    center: tuple[int, int],
    radius: int,
    color: tuple[int, int, int],
    alpha: int,
) -> None:
    layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    x, y = center
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color, alpha))
    blurred = layer.filter(ImageFilter.GaussianBlur(radius=radius * 0.5))
    image.alpha_composite(blurred)


def draw_grid(draw: ImageDraw.ImageDraw, size: tuple[int, int], color: tuple[int, int, int, int]) -> None:
    width, height = size
    spacing = 80
    for x in range(0, width, spacing):
        draw.line((x, 0, x, height), fill=color, width=1)
    for y in range(0, height, spacing):
        draw.line((0, y, width, y), fill=color, width=1)


def draw_phase_portrait(
    image: Image.Image,
    palette: dict,
    cx: int,
    cy: int,
    width: int,
    height: int,
) -> None:
    """Draw a stylised fractional-attractor phase portrait."""
    layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer, "RGBA")
    random.seed(42)
    palette_pool = [
        (*palette["violet"], 220),
        (*palette["cyan"], 200),
        (*palette["lavender"], 180),
        (*palette["emerald"], 160),
    ]
    n_curves = 4
    for k in range(n_curves):
        color = palette_pool[k % len(palette_pool)]
        phase = k * math.pi / 3
        amp_x = width / 2 - 12 - k * 14
        amp_y = height / 2 - 10 - k * 8
        points = []
        steps = 380
        for i in range(steps + 1):
            t = i / steps * 2 * math.pi
            r_mod = 1 + 0.15 * math.sin(3 * t + phase) + 0.08 * math.sin(5 * t)
            x = cx + amp_x * r_mod * math.cos(t + phase * 0.7)
            y = cy + amp_y * r_mod * math.sin(t * 1.3 + phase)
            points.append((x, y))
        # main stroke
        draw.line(points, fill=color, width=2, joint="curve")
    image.alpha_composite(layer)


def draw_terminal_panel(
    draw: ImageDraw.ImageDraw,
    palette: dict,
    name: str,
    lines: list[tuple[str, tuple[int, int, int]]],
    origin: tuple[int, int],
    width: int,
) -> None:
    x0, y0 = origin
    panel = (x0, y0, x0 + width, y0 + 30 + len(lines) * 42)
    fill_alpha = 70 if name == "hero-dark.png" else 32
    draw.rounded_rectangle(
        panel,
        radius=18,
        fill=(0, 0, 0, fill_alpha),
        outline=(*palette["violet"], 140),
        width=2,
    )
    small = load_font(22)
    y = y0 + 20
    for label_color, text in lines:
        draw.ellipse((x0 + 22, y + 8, x0 + 34, y + 20), fill=(*label_color, 240))
        draw.text((x0 + 50, y), text, font=small, fill=(*palette["text"], 245))
        y += 42


def add_label(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, font: ImageFont.FreeTypeFont, fill) -> None:
    draw.text(xy, text, font=font, fill=fill)


def build_hero(name: str, palette: dict, headline: str, tagline: str) -> None:
    image = vertical_gradient(HERO_SIZE, palette["bg_top"], palette["bg_bottom"]).convert("RGBA")
    draw = ImageDraw.Draw(image, "RGBA")
    draw_grid(draw, HERO_SIZE, palette["grid"])

    # ambient glows
    draw_glow(image, (220, 110), 220, palette["violet"], 110)
    draw_glow(image, (1320, 250), 250, palette["cyan"], 70)
    draw_glow(image, (1450, 380), 160, palette["lavender"], 60)
    draw = ImageDraw.Draw(image, "RGBA")

    # right-side phase portrait
    draw_phase_portrait(image, palette, cx=1280, cy=230, width=560, height=380)
    draw = ImageDraw.Draw(image, "RGBA")

    # fonts
    micro    = load_font(20)
    sub      = load_font(30)
    eq_font  = load_font(36, bold=True)
    headline_font = load_font(86, bold=True)

    # eyebrow (name in small caps)
    add_label(draw, (96, 70),  "MUHAMMAD JUNAID ALI ASIF RAJA", micro, (*palette["muted"], 245))

    # title bar accent (vertical chip)
    draw.rounded_rectangle((96, 108, 124, 122), radius=6, fill=(*palette["violet"], 235))

    # headline
    add_label(draw, (96, 138), headline, headline_font, (*palette["text"], 255))

    # subline (vectors)
    add_label(draw, (100, 248), tagline, sub, (*palette["violet"], 250))

    # terminal panel bottom-left — role + lab + α only (location is already in the README sub-line)
    draw_terminal_panel(
        draw,
        palette,
        name,
        lines=[
            (palette["violet"],  "role = machine_learning_research :: direct_phd"),
            (palette["cyan"],    "lab  = fractional_intelligent_computing"),
            (palette["emerald"], "α    = caputo · grünwald–letnikov · L1 scheme"),
        ],
        origin=(96, 304),
        width=880,
    )

    image.save(ASSETS_DIR / name)


def main() -> None:
    ensure_dirs()
    headline = "fractional deep learning"
    tagline  = "spiking nets · fractional optimisation · memory kernels · surrogates"
    build_hero("hero-dark.png",  DARK,  headline, tagline)
    build_hero("hero-light.png", LIGHT, headline, tagline)
    print(f"Built assets in {ASSETS_DIR}")


if __name__ == "__main__":
    main()
