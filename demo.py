
import sim
from sim.funs import *

def init():
    return 0


def draw(state):
    return sim.empty_scene()


def tick(state):
    return state


if __name__ == '__main__':
    sim.run()
