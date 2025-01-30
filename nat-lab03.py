
import pyglet
import math
import random


BAT_X = 500
mos_y = 100


def move_bat(bat_y, key):
    if key == "up":
        return min(bat_y + 5, 600)
    if key == "down":
        return max(bat_y - 5, 0)


def move_mosquito(mos_x):
    return (mos_x + 3) % 800


def bat_caught_mosquito(bat_y, mos_x):
    dx = BAT_X - mos_x
    dy = bat_y - mos_y
    dist = math.sqrt(pow(dx, 2) + pow(dy, 2))
    return dist < 50 


def reset_mosquito(mos_y):
    return 100


def main():
    # App state
    bat_y = 300
    mos_x = 100


    # Internal state
    up_pressed = False
    down_pressed = False

    # App logic
    window = pyglet.window.Window(width=800, height=600, resizable=False,
                                  caption="Bat Defender")

    # Thanks, Pyglet Sprite example.
    pyglet.resource.path = ['./images']
    pyglet.resource.reindex()

    background = pyglet.shapes.Rectangle(x = 0, y = 0,
                                         width=window.width,
                                         height=window.height,
                                         color=(255, 255, 255))

    def load_image(file, flip=False):
        image = pyglet.resource.image(file, flip_x=flip)
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        return image


    bat = pyglet.sprite.Sprite(load_image("bat.png"), x=BAT_X, y=bat_y)
    bat.scale = 0.5

    mos = pyglet.sprite.Sprite(load_image("mosquito.png", True),
                               x=mos_x, y=mos_y)
    mos.scale = 0.5

    @window.event
    def on_draw():
        window.clear()
        background.draw()
        bat.draw()
        mos.draw()


    @window.event
    def on_key_press(key, _mods):
        nonlocal up_pressed, down_pressed

        if key == pyglet.window.key.UP:
            up_pressed = True
        if key == pyglet.window.key.DOWN:
            down_pressed = True

            
    @window.event
    def on_key_release(key, _mods):
        nonlocal up_pressed, down_pressed

        if key == pyglet.window.key.UP:
            up_pressed = False
        if key == pyglet.window.key.DOWN:
            down_pressed = False

            
    def tick(dt):
        nonlocal bat_y, mos_x, up_pressed, down_pressed
        global mos_y

        assert(dt > 0.02)
        assert(dt < 0.05)

        if up_pressed:
            bat_y = move_bat(bat_y, "up")

        if down_pressed:
            bat_y = move_bat(bat_y, "down")

        mos_x = move_mosquito(mos_x)

        if bat_caught_mosquito(bat_y, mos_x):
            print("You caught the mosquito")
            mos_x = reset_mosquito(mos_x)
            mos_y = random.randint(100, 500)
            
        bat.y = bat_y
        mos.x = mos_x
        mos.y = mos_y


        
    pyglet.clock.schedule_interval(tick, 1 / 30.0)
    pyglet.app.run()


if __name__ == '__main__':
    main()
