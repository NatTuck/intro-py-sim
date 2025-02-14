
import sys
import inspect
import gc
from PIL import Image

import pygame
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100)

import sim.defaults

if __name__ == '__main__':
    print("This is a library.")
    sys.exit(1)

def run():
    pygame.init()
    clock = pygame.time.Clock()

    app = sys.modules['__main__']

    callbacks = {}
    for name in ['config', 'init', 'draw', 'tick',
                 'key_press', 'mouse_click']:
        if name in app.__dict__:
            callbacks[name] = getattr(app, name)
        else:
            callbacks[name] = getattr(defaults, name)

    config = callbacks['config']()

    state = callbacks['init']()

    screen = pygame.display.set_mode((800, 600))

    keys = set()

    def on_draw():
        scene = convert_image(callbacks['draw'](state))

        screen.fill("white")
        screen.blit(scene, (0, 0))
        pygame.display.flip()

        
    def on_mouse_press(x, y, _btn, _mods):
        nonlocal state
        hh = config['height']
        state = callbacks['mouse_click'](state, x, hh - y, "left")
        
        
    def tick(dt):
        nonlocal state
        for key in keys:
            state = callbacks['key_press'](state, key)
        if (nparms(callbacks['tick']) == 1):
            state = callbacks['tick'](state)
        else:
            state = callbacks['tick'](state, dt)

    while True:
        dt = clock.tick(60) / 1000.0
        
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if ev.type == pygame.KEYDOWN:
                keys.add(pygame.key.name(ev.key))
            if ev.type == pygame.KEYUP:
                keys.remove(pygame.key.name(ev.key))
            if ev.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                state = callbacks['mouse_click'](state, x, y, "left")

        tick(dt)
        on_draw()


def nparms(fn):
    return len(inspect.signature(fn).parameters)
            

def convert_image(im):
    data = im.convert('RGBA').tobytes()
    return pygame.image.frombuffer(data, (im.width, im.height), "RGBA")


