import Tkinter as tk
from Tkinter import *
from pool2D import *
import time

# main window
window = tk.Tk()
window.title("2D Pool simulation")
L = 505  # window size
W = 473
window.geometry(str(L) + "x" + str(W))

yy = 5  # pozycjonowanie elementow GUI
# labelki
var = tk.StringVar()
labelN = tk.Label(window, textvariable=var)
var.set("Number of balls: N")
labelN.place(in_=window, x=94 + 35, y=4 + yy)

vardt = tk.StringVar()
labeldt = tk.Label(window, textvariable=vardt)
vardt.set("Time step size: dt")
labeldt.place(in_=window, x=103 + 35, y=33 + yy)

# pola input N i dt
varN = tk.StringVar(window)
varN.set("4")
inputN = tk.Spinbox(window, from_=1, to=10, textvariable=varN)
inputN.place(in_=window, x=200 + 35, y=2 + yy, width=30, height=25)
varDt = tk.StringVar(window)
varDt.set("0.3")
inputDt = tk.Spinbox(window, values=(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), textvariable=varDt)
inputDt.place(in_=window, x=200 + 35, y=33 + yy, width=30, height=25)


class Simulation(object):
    ifSimulationWorks = False
    ifPause = False
    t = 0

    def __init__(self):
        Nn = inputN.get()
        dtt = inputDt.get()
        self.N = int(Nn)
        self.Table = Table(int(Nn), float(dtt))
        startButton = tk.Button(window, text="Simulation start",
                                command=self.runSimulation)  # ,command=symulacja.runSimulation)
        startButton.place(in_=window, x=233 + 35, y=2 + yy, height=25)
        stopButton = tk.Button(window, text="Stop", command=self.stop)
        stopButton.place(in_=window, x=233 + 35, y=33 + yy, height=25)

    def getNDt(self):
        Nn = inputN.get()
        dtt = inputDt.get()
        self.N = int(Nn)
        self.Table = Table(int(Nn), float(dtt))

    def runSimulation(self):
        self.getNDt()
        self.ifPause = False
        if self.ifSimulationWorks == False:
            self.ifSimulationWorks = True
            while self.ifSimulationWorks:
                position = []
                velocity = []
                N = self.N
                for i in range(0, N):
                    position.append(self.Table.actualPosition(i, self.t))
                    velocity.append(self.Table.actualVelocity(i, self.t))
                ballSymbol = []
                velocityWektor = []
                for i in range(0, N):
                    ballSymbol.append(canvas.create_circle(position[i][0], position[i][1], 25, width=2,
                                                           fill=self.Table.balls[i].color, tags=('ball' + str(i))))
                # velocityWektor.append(canvas.create_line(position[i][0], position[i][1], position[i][0]+velocity[i][0]*10, position[i][1]+velocity[i][1]*10))
                canvas.update()
                canvas.after(40)
                for i in range(0, N):
                    canvas.delete(ballSymbol[i])

                self.t += 1

    def stop(self):
        self.ifSimulationWorks = False


canvas = tk.Canvas(width=Table.L, height=Table.W, bg='green')
canvas.create_line(2, 2, 500, 2, dash=(4, 2))  # gorna
canvas.create_line(2, 2, 2, 400, dash=(4, 2))  # lewa
canvas.create_line(500, 2, 500, 400, dash=(4, 2))  # prawa
canvas.create_line(2, 400, 500, 400, dash=(4, 2))  # dolna
canvas.place(in_=window, x=0, y=63 + yy)


# canvas.pack(expand=tk.YES, fill=tk.BOTH)

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


tk.Canvas.create_circle = _create_circle
sym = Simulation()

window.mainloop()


