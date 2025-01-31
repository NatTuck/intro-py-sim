
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw, ImageOps
from PIL.Image import Image as Im
from PIL.ImageOps import *


def empty_scene(ww = 800, hh = 600):
    """Create an empty scene with a white background."""
    return Image.new("RGBA", (ww, hh), "white")


def text(text, size = 100.0, color = "black"):
    font = ImageFont.load_default(size)
    (l, t, r, b) = font.getbbox(text)

    ww = r + l
    hh = b + t
    bg = Image.new("RGBA", (ww, hh), (0, 0, 0, 0))
    dr = ImageDraw.Draw(bg)
    dr.text((ww//2, hh//2), text, fill=color, font_size=size, anchor='mm')

    return bg


def rectangle(ww, hh, color = "black"):
    bg = Image.new("RGBA", (ww, hh), (0, 0, 0, 0))
    dr = ImageDraw.Draw(bg)
    dr.rectangle([0, 0, ww, hh], color)
    return bg


def circle(rad, color = "black"):
    bg = Image.new("RGBA", (2*rad + 1, 2*rad + 1), (0, 0, 0, 0))
    dr = ImageDraw.Draw(bg)
    dr.ellipse((0, 0, 2*rad, 2*rad), color)
    return bg
   

def overlay(top, bot):
    tmp = Image.new("RGBA", (bot.width, bot.height), (0, 0, 0, 0))
    tt = bot.height // 2 - top.height // 2
    ll = bot.width // 2 - top.width // 2
    tmp.paste(top, (ll, tt))
    return Image.alpha_composite(bot, tmp)


def place_at(bot: Im, top: Im, xx: int, yy: int) -> Im:
    tmp = Image.new("RGBA", (bot.width, bot.height), (0, 0, 0, 0))
    tmp.paste(top, (xx - top.width // 2, yy - top.height // 2))
    return Image.alpha_composite(bot, tmp)


def load_image(path):
    if not Path(path).exists():
        path = Path(__file__).parent / "images" / path
    with Image.open(path) as im:
        return im.convert('RGBA')
        

