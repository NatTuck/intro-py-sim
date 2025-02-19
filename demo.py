
import sim
from sim.funs import *

# from collections import namedtuple
# Posn = namedtuple('Posn', ['x', 'y'])

def init():
    return (0, 0)
    #return Posn(0, 0)

bat = mirror(contain(load_image("bat.png"), (200, 200)))

def draw(state):
    (x, y) = state
    return place_at(empty_scene(), bat, x % 800, y % 600)


def tick(state):
    (x, y) = state
    return (x + 2, y + 4)


def mouse_click(state, x, y, btn):
    return (x, y)


def key_press(state, key):
    return state


if __name__ == '__main__':
    sim.run()
