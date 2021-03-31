from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()
score = 0


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
        global score
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)
                score += 1
                text.text = 'Score: '+str(score)
                Voxel_target(position=(random.randint(
                    0, 20), random.randint(1, 20), random.randint(0, 20)))


for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))
 
for z in range(10):
    target = Voxel_target(position=(random.randint(
        0, 20), random.randint(1, 20), random.randint(0, 20)))

text = Text('Score: '+str(score), y=.48, x=-.8)
text.scale = (2, 2)

player = FirstPersonController(speed=10)
app.run()
