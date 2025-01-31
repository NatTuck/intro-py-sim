
from PIL import Image, ImageFont, ImageDraw, ImageOps
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
    

def overlay(top, bot):
    tmp = Image.new("RGBA", (bot.width, bot.height), (0, 0, 0, 0))
    tt = bot.height // 2 - top.height // 2
    ll = bot.width // 2 - top.width // 2
    tmp.paste(top, (ll, tt))
    return Image.alpha_composite(bot, tmp)


def place_at(bot, top, xx, yy):
    tmp = Image.new("RGBA", (bot.width, bot.height), (0, 0, 0, 0))
    tmp.paste(top, (xx - top.width // 2, yy - top.height // 2))
    return Image.alpha_composite(bot, tmp)
