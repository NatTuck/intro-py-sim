
import sys
import pyglet
from PIL import Image

if __name__ == '__main__':
    print("This is a library.")
    sys.exit(1)

app = sys.modules['__main__']
import sim.defaults

callbacks = {}
for name in ['init', 'draw', 'config']:
    if name in app.__dict__:
        callbacks[name] = getattr(app, name)
    else:
        callbacks[name] = getattr(defaults, name)
        
state = callbacks['init']()
config = callbacks['config']()

    
def run():
    window = pyglet.window.Window(
        caption=config['title'],
        width=config['width'],
        height=config['height'],
        resizable=config['resizable'])

    # bat_image = load_image("images/bat.png")
    # bat = pyglet.sprite.Sprite(bat_image, x=100, y=100)
    # bat.scale = 0.5

    state = callbacks['init']()
    
    @window.event
    def on_draw():
        window.clear()
        scene = convert_image(callbacks['draw'](state))
        sp = pyglet.sprite.Sprite(scene, x=0, y=0)
        sp.draw()


    def tick(state):
        return callbacks['tick'](state)


    if 'tick' in app.__dict__:
        pyglet.clock.schedule_interval(tick, 1 / 30.0)

        
    pyglet.app.run()


def load_image(path):
    with Image.open(path) as im:
        return im.convert('RGBA')


def convert_image(im):
    data = im.convert('RGBA').transpose(Image.Transpose.FLIP_TOP_BOTTOM).tobytes()
    tx = pyglet.image.ImageData(im.width, im.height, 'RGBA', data)
    return tx


def empty_scene(ww = 800, hh = 600):
    return Image.new("RGBA", (ww, hh), "white")
