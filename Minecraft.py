from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import serial as sr
import threading
gData=[]
gData.append([0.0])
gData.append([0.0])
app = Ursina()
score = 0
abc=0
ser=sr.Serial('COM3',19200)
ser.reset_input_buffer
a=0
a1=0
b=0
p=0
def getData(out_data):
    while True:
        
        global a,b,p
        ser.reset_input_buffer
        line = ser.readline().decode('utf-8').replace('\r\n','').split(',')
        
      
        try:
            if(float(line[0])>0.000000001):
            
                a=float(line[0])/3000000

            else:
            
                a=float(line[0])/300000

            if(float(line[1])>0.000000001):
            
                b=float(line[1])/3000000

            else:
            
                b=float(line[1])/300000

            
            player.vely=b
            player.velx=a
            p=float(line[2])
            if(p==1 and a1==0):
                p=1
                a1=1
            
        
        except:
            pass
dataCollector = threading.Thread(target=getData, args=(gData,))
dataCollector.start()           

   


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
        global score,p
        if self.hovered:
            if key == 'v':
                destroy(self)
                score += 1
                text.text = 'Score: '+str(score)
                Voxel_target(position=(random.randint(
                    -10, 10), random.randint(1, 20), random.randint(0, 20)))


for z in range(20):
    for x in range(-10,10):
        voxel = Voxel(position=(x, 0, z))
 
for z in range(10):
    target = Voxel_target(position=(random.randint(
        -10, 10), random.randint(1, 20), random.randint(0, 20)))

text = Text('Score: '+str(score), y=.48, x=-.8)
text.scale = (2, 2)

player = FirstPersonController(speed=10,velx=a,vely=b)
app.run(),
