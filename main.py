import math
import sys
import tkinter
import numpy as np


location = ""
windSpeed = 0
windDirection = "000"
resolution = 0.25

routePoints = {}

map = tkinter.Tk()
canvas = tkinter.Canvas(map, bg="white", height=500, width=500)

def points():
    print("Select the area in which you would like to survey!")
    map.title("Mission planner")
    map.resizable(width=False, height=False)
    map.geometry("500x600")
    map.configure(background='blue')
    button = tkinter.Button(map, text="Finished", command=finishRoute)
    button.pack(side=tkinter.BOTTOM)
    label = tkinter.Label(map)

    canvas.pack()
    label.pack()
    canvas.bind("<Button 1>", click)
    canvas.bind("<Key>", key)

    tkinter.mainloop()


def setup():
    inputs()
    points()


def drawRoute():
    while():
        pass


def inputs():
    global windSpeed
    global windDirection
    while True:
        windSpeed = input("Wind speed: \n")
        if not windSpeed.isdigit():
            print("Please re-enter an applicable wind speed")
        else:
            break
    print(f'WindSpeed = {windSpeed}')
    while True:
        windDirection = input("Wind Direction (As a bearing): \n")
        if not windDirection.isdigit():
            print("Please re-enter an applicable wind direction")
        elif len(windDirection) != 3:
            print("Please re-enter an applicable bearing")
        elif int(windDirection) > 359:
            print("Please re-enter an applicable wind direction")
        else:
            break
    print(f'Wind Direction = {windDirection}')


def main():
    setup()
    #calcRoute()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def click(event):
    x, y = event.x, event.y
    routePoints[len(routePoints)] = Point(x, y)
    canvas.create_oval(x-10, y+10, x+10, y-10)
    canvas.create_text(x, y, font="Arial", text="{}".format(len(routePoints)))
    if len(routePoints) < 2:
        print("Need more points!")
    else:
        canvas.create_line(routePoints[len(routePoints)-2].x, routePoints[len(routePoints)-2].y,
                           routePoints[len(routePoints)-1].x, routePoints[len(routePoints)-1].y )
    print('Point {} = {}, {}'.format(len(routePoints), x, y))


def key(event):
    print("pressed {}".format(repr(event.char)))
    map.quit()


def finishRoute():
    routePoints[len(routePoints)] = routePoints[0]
    canvas.create_line(routePoints[len(routePoints) - 2].x, routePoints[len(routePoints) - 2].y,
                       routePoints[len(routePoints) - 1].x, routePoints[len(routePoints) - 1].y)
    fillPolygon()
    calcRoute()


def fillPolygon():
    array = convertPointsToArray()
    canvas.create_polygon(*array, fill="Red")
    canvas.update()


def convertPointsToArray():
    array = []
    for i in routePoints:
        array.extend((routePoints[i].x, routePoints[i].y))
    return array

def calcRoute():
    #windDirection
    startX = 0
    startY = 0
    endY = 500
    endX = endY/math.tan(math.radians(int(windDirection)))

    canvas.create_line(startX, startY, endX, endY)
    canvas.update()

    grad = (endY-startY)/(endX-startX)
    tanGrad = -1/grad
    startPoints = {}
    endPoints = {}
    val = int(1/resolution)
    endPoint = 0
    endX = 500
    i = 0
    while not endPoint > 500:
        endPoint = tanGrad*endX + i*500*resolution
        print(endPoint)
        i = i + 1
        canvas.create_line(startX, i*500*resolution, endX, endPoint)
    canvas.update()



#MAIN PROGRAM
main()
print(windSpeed, windDirection)
