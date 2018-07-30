from tkinter import *
import math
import time

root = Tk()
T = Text(root, height=50, width=100)
T.pack()
print('hi')
# 50 x 50 grid of rays

# 100 'steps' checked per ray

global xorientation
xorientation = 0

global yorientation
yorientation = 0

class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

global perspective_center

perspective_center = Coordinate(0,0,0)

class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def contains(self, point):
        return (point.x - self.center.x)**2 + (point.y - self.center.y)**2 + (point.z - self.center.z)**2 < self.radius**2

def cast_ray(coord, steps):
    global xorientation
    start = Coordinate(coord.x, coord.y, coord.z)
    proximity = 0
    for n in range(steps):
        for object in objects:
            if object.contains(coord):
                return proximity

        # because the 'camera' can be located at different coordinates, the offset must be subtracted to get the current ray's location relative to the camera, not to the origin (0,0,0)
        coord.x += math.sin(xorientation) + (start.x - perspective_center.x/50)
        coord.y += math.sin(yorientation) + (start.y - perspective_center.y/50)
        coord.z += math.cos(xorientation) - (start.z - perspective_center.z)

        #print(perspective_center.x)
    # math.sin(orientation) * (x+perspective_center.x-25)/50 + perspective_center.z/50

    # perspective_center.z + (x + perspective_center.x - 25)/50 * math.sin(orientation)

        #print(coord.x)

        proximity += 1

    #print(coord.x, coord.y, coord.z)
    return None

objects = [

    Sphere(Coordinate(0, 0, 50), 15),

    Sphere(Coordinate(-3, -1, 10), 2),

    Sphere(Coordinate(30, 20, 70), 20),

    ]

xmove = 0
ymove = 0
zmove = 0

def update():
    stringout = ''

    #print(orientation)

    global xmove
    global zmove
    global ymove

    perspective_center.z += zmove
    perspective_center.x += xmove
    perspective_center.y += ymove

    for y in range(50):
        for x in range(50):

            #print(x, y)
            ray_origin = Coordinate(math.cos(xorientation)*((x - 25) / 50) + perspective_center.x/50, math.cos(yorientation)* -1 * (y - perspective_center.y - 25) / 50, math.sin(xorientation) * (x-25)/50 + perspective_center.z)
            #print(ray_origin.x, ray_origin.y, ray_origin.z)
            collision = cast_ray(ray_origin, 100)

            if(collision == None):
                stringout += '  '
            elif(collision < 38):
                stringout += '░░'
            elif (collision < 60):
                stringout += '▒▒'
            else:
                stringout += '▓▓'


        stringout += '\n'



    T.delete(1.0, END)
    T.insert(END, stringout)

    #root.after(100, update)


def moveleft():
    global xmove
    global ymove
    global zmove
    xmove = -50
    ymove = 0
    zmove = 0
    update()

def moveright():
    global xmove
    global ymove
    global zmove
    xmove = 50
    ymove = 0
    zmove = 0
    update()

def moveup():
    global xmove
    global ymove
    global zmove
    ymove = 50
    xmove = 0
    zmove = 0
    update()

def movedown():
    global xmove
    global ymove
    global zmove
    ymove = -50
    xmove = 0
    zmove = 0
    update()

def moveforwards():
    global xmove
    global ymove
    global zmove
    zmove = 5
    xmove = 0
    ymove = 0
    update()

def movebackwards():
    global xmove
    global ymove
    global zmove
    zmove = -5
    xmove = 0
    ymove = 0
    update()

def lookleft():
    global xorientation
    global xmove
    global ymove
    global zmove
    xmove = 0
    ymove = 0
    zmove = 0
    xorientation -= math.pi / 8
    update()

def lookright():
    global xorientation
    global xmove
    global ymove
    global zmove
    xmove = 0
    ymove = 0
    zmove = 0
    xorientation += math.pi / 8
    update()

def lookup():
    global yorientation
    global xmove
    global ymove
    global zmove
    xmove = 0
    ymove = 0
    zmove = 0
    yorientation += math.pi / 8
    update()

def lookdown():
    global yorientation
    global xmove
    global ymove
    global zmove
    xmove = 0
    ymove = 0
    zmove = 0
    yorientation -= math.pi / 8
    update()

panbutton = Button(root, text='Move')
rotatebutton = Button(root, text='Rotate')

panbutton.pack()
panbutton.place(x=35,y=40)
rotatebutton.pack()
rotatebutton.place(x=35,y=150)


leftbutton = Button(root, text="<-", command=moveleft)
rightbutton = Button(root, text="->", command=moveright)
upbutton = Button(root, text="^", command=moveup)
downbutton = Button(root, text="v", command=movedown)
forwardsbutton = Button(root, text="^\n/", command=moveforwards)
backwardsbutton = Button(root, text="/\nv", command=movebackwards)

lookleftbutton = Button(root, text="<-", command=lookleft)
lookrightbutton = Button(root, text="->", command=lookright)

lookupbutton = Button(root, text="^", command=lookup)
lookdownbutton = Button(root, text="v", command=lookdown)

leftbutton.pack()
leftbutton.place(x=15,y=40)
rightbutton.pack()
rightbutton.place(x=75,y=40)
upbutton.pack()
upbutton.place(x=50,y=10)
downbutton.pack()
downbutton.place(x=50,y=70)
forwardsbutton.pack()
forwardsbutton.place(x=110,y=5)
backwardsbutton.pack()
backwardsbutton.place(x=110,y=55)

lookleftbutton.pack()
lookleftbutton.place(x=15,y=150)
lookrightbutton.pack()
lookrightbutton.place(x=75,y=150)

lookupbutton.pack()
lookupbutton.place(x=50,y=120)
lookdownbutton.pack()
lookdownbutton.place(x=50,y=180)

update()

root.mainloop()