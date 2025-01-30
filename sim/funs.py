
from PIL import Image, ImageFont, ImageDraw

def empty_scene(ww = 800, hh = 600):
    return Image.new("RGBA", (ww, hh), "white")


def draw_text(text, size, color):
    font = ImageFont.load_default(size)
    (l, t, r, b) = font.getbbox(text)

    ww = r + l
    hh = b + t
    bg = Image.new("RGBA", (ww, hh), (0, 0, 0, 0))
    dr = ImageDraw.Draw(bg)
    dr.text((ww//2, hh//2), text, fill=color, font_size=size, anchor='mm')

    return bg
    
    

def overlay(top, bot):
    pass
