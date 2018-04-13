import random
from math import *
import datetime


class Ball(object):
    dt = 0.1

    def __init__(self, idd):
        self.vx0 = -1
        self.vy0 = -1
        self.x0 = -1
        self.y0 = -1
        self.vx = -1
        self.vy = -1
        self.x = -1
        self.y = -1
        self.R = 25
        self.id = idd  # ball id
        self.collisionBallNr = 99999
        self.ifCollisionCompleted = False
        self.color = "blue"
        self.setInitialBallVelocity()

    def nextStep(self):
        # t=1
        self.x = self.x + self.vx * Ball.dt
        self.y = self.y + self.vy * Ball.dt

    def ifCollisionWithBall(self, balls):  # set new velocities after collision

        Xcoll = 0
        Ycoll = 0
        distanceFromBall = 99999
        for i in balls:
            if i.id != self.id:
                distanceFromBall = sqrt((self.x - i.x) ** 2 + (self.y - i.y) ** 2)
                if distanceFromBall <= 2 * self.R and self.ifCollisionCompleted == False:
                    self.collisionBallNr = i.id
                    Xcoll = (self.x + i.x) / 2
                    Ycoll = (self.y + i.y) / 2
                    alpha = 3.14159 / 2 - atan(float(self.y - i.y) / (self.x - i.x))  # collision angle

                    Vs = cos(alpha) * self.vx - sin(alpha) * self.vy
                    Vn = sin(alpha) * self.vx + cos(alpha) * self.vy
                    Vs_i = cos(alpha) * i.vx - sin(alpha) * i.vy
                    Vn_i = sin(alpha) * i.vx + cos(alpha) * i.vy
                    Vn_po = Vn_i
                    Vni_po = Vn
                    self.vx = cos(alpha) * Vs + Vn_po * sin(alpha)
                    self.vy = cos(alpha) * Vn_po - sin(alpha) * Vs
                    i.vx = cos(alpha) * Vs_i + Vni_po * sin(alpha)
                    i.vy = cos(alpha) * Vni_po - sin(alpha) * Vs_i
                    # print("Vx po:",self.vx, "Vy=",self.vy,"Vxi=",i.vx," Vyi=",i.vy)

                    i.ifCollisionCompleted = True
                    self.ifCollisionCompleted = True
                elif distanceFromBall > 2 * self.R and self.ifCollisionCompleted == True and i.id == self.collisionBallNr:
                    # print(datetime.datetime.now(), "ELSE odl od kuli z id {0}: ".format(i.id), distanceFromBall)
                    self.ifCollisionCompleted = False
                    i.ifCollisionCompleted = False

    def ifCollisionWithEdge(self):
        if self.x + self.R >= Table.borderCoordinatesX[1] and self.vx > 0:
            self.vx = -self.vx
        if self.x - self.R <= Table.borderCoordinatesX[0] and self.vx < 0:
            self.vx = -self.vx
        if self.y - self.R <= Table.borderCoordinatesY[0] and self.vy < 0:
            self.vy = -self.vy
        if self.y + self.R >= Table.borderCoordinatesY[1] and self.vy > 0:
            self.vy = -self.vy

    def setInitialBallVelocity(self):
        self.vx0 = random.randint(-10, 10)
        self.vy0 = random.randint(-10, 10)
        self.vx = self.vx0
        self.vy = self.vy0


class Table(object):
    L = 500  # table size
    W = 400
    borderCoordinatesX = [0, L]  # border coordinates of the table
    borderCoordinatesY = [0, W]
    colors = ['yellow', 'blue', 'red', 'green', 'white', 'grey', 'purple', 'black', 'brown', 'orange', 'yellow', 'blue',
              'red', 'green', 'white', 'grey', 'purple', 'black', 'brown', 'orange']

    def __init__(self, Nn, dtt):
        self.N = Nn  # number of balls
        self.dt = dtt  # time step size
        Ball.dt = dtt
        self.balls = [Ball(i) for i in range(self.N)]
        for i in range(0, self.N):
            self.balls[i].color = self.colors[i]
        self.initialBallsPositions = {}  # have to be unique for each ball
        self.setInitialBallsPositions(self.balls)
        self.getInitialPositionsAndVelocities(self.balls)

    def setInitialBallsPositions(self, balls):

        for i in balls:
            while i.x0 == -1 and i.y0 == -1:
                x = random.randint(i.R, Table.L - i.R)
                y = random.randint(i.R, Table.W - i.R)
                for j in balls:
                    if i.id != j.id and x <= (j.x + 2 * j.R) and y <= (j.y + 2 * j.R) and x >= (
                            j.x - 2 * j.R) and y >= (j.y - 2 * j.R):
                        x = -1
                        y = -1
                i.x0 = x
                i.y0 = y
                i.x = i.x0
                i.y = i.y0

    def getInitialPositionsAndVelocities(self, balls):

        for i in range(self.N):
            self.initialBallsPositions[balls[i].color] = [balls[i].x, balls[i].y]
            self.initialBallsPositions[balls[i].color] = [balls[i].vx0, balls[i].vy0]
        print("Initial balls positions: ", self.initialBallsPositions)
        print("Initial balls velocities: ", self.initialBallsPositions)

    def actualVelocity(self, ballNr, t):

        return [self.balls[ballNr].vx, self.balls[ballNr].vy]

    def actualPosition(self, ballNr, t):

        for i in range(0, self.N):
            self.balls[i].nextStep()
            self.balls[i].ifCollisionWithEdge()
            self.balls[i].ifCollisionWithBall(self.balls)
        return [self.balls[ballNr].x, self.balls[ballNr].y]













