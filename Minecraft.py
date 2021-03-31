from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import datetime
import math

app = Ursina()
score = 0
time_past = int(datetime.datetime.now().second)
level = 1


def nivel():
    global text_level, level
    level += 1
    text_level.text = 'Level '+str(level)


def update():
    global time_past
    time = datetime.datetime.now().second-time_past
    if time < 0:
        time += 60
    text_time.text = 'Time: '+str(time)


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='chano.jpeg'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)))


class Voxel_target(Button):
    def __init__(self, position=(0, 0, 0), texture='chano.jpeg'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)))

    def input(self, key):
        global score, time_past
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)
                score += 1
                text_score.text = 'Score: '+str(score)

            if score == 10:
                score = 0
                text_score.text = 'Score: '+str(score)
                time_past = datetime.datetime.now().second
                for z in range(10):
                    Voxel_target(position=(random.randint(0, 20),
                                 random.randint(1, 20), random.randint(0, 20)))
                nivel()


for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))

for z in range(10):
    target = Voxel_target(position=(random.randint(
        0, 20), random.randint(1, 20), random.randint(0, 20)))

text_score = Text('Score: '+str(score), y=.48, x=-.8)
text_score.scale = (2, 2)

text_time = Text('Time: '+str(time_past), y=.48, x=-.5)
text_time.scale = (2, 2)

text_level = Text(text='Level '+str(level), x=0, y=.48)
text_level.scale = (2, 2)

player = FirstPersonController(speed=10)
app.run()
