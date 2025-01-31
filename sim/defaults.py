
from PIL import Image, ImageDraw


def config():
   return {
       'title': "Simulation",
       'width': 800,
       'height': 600,
       'resizable': False
   }


def init():
    return {}


def draw(state):
    im = Image.new("RGBA", (800, 600), "white")
    dr = ImageDraw.Draw(im)
    dr.text((400, 300), "hello", fill=(0, 0, 0), font_size=100, anchor='mm')
    return im


def tick(state):
    return state
