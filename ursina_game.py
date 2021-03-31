from ursina import *

app = Ursina()
redcube = Entity(model='icosphere', color=color.red)
txt = Text(text='Red cube', scale=2, x=.1, y=-.2)
spd=10

def update():
    redcube.rotation_y += 30 * time.dt
    redcube.rotation_x += 30 * time.dt
    greencube()
    camera_control()


def greencube():
    if held_keys['z']:
        redcube.color = color.green
        txt.text = 'Green cube'
    else:
        redcube.color = color.red
        txt.text = 'Red cube'


def camera_control():
    camera.z += held_keys['q']*spd*time.dt
    camera.z -= held_keys['e']*spd*time.dt
    camera.x -= held_keys['d']*spd*time.dt
    camera.x += held_keys['a']*spd*time.dt
    camera.y += held_keys['s']*spd*time.dt
    camera.y -= held_keys['w']*spd*time.dt

app.run()
