from Tkinter import *
import math

class Drag(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Drag Calculator")
        self.grid()

        self.dragCoefLabel = Label(self, text = "Drag Coefficient")
        self.dragCoefLabel.grid(row = 0, column = 0)
        self.dragCoefVar   = DoubleVar()
        self.dragCoefEntry = Entry(self, textvariable = self.dragCoefVar)
        self.dragCoefEntry.grid(row = 0, column = 1)

        self.veloLabel = Label(self, text = "Velocity")
        self.veloLabel.grid(row = 1, column = 0)
        self.veloVar   = DoubleVar()
        self.veloEntry = Entry(self, textvariable = self.veloVar)
        self.veloEntry.grid(row = 1, column = 1)

        self.densityLabel = Label(self, text = "Fluid Density")
        self.densityLabel.grid(row = 2, column = 0)
        self.densityVar   = DoubleVar()
        self.densityEntry = Entry(self, textvariable = self.densityVar)
        self.densityEntry.grid(row = 2, column = 1)

        self.frontalLabel = Label(self, text = "Frontal Area")
        self.frontalLabel.grid(row = 3, column = 0)
        self.frontalVar   = DoubleVar()
        self.frontalEntry = Entry(self, textvariable = self.frontalVar)
        self.frontalEntry.grid(row = 3, column = 1)

        self.dragAnsLabel = Label(self, text = "Drag Coefficient")
        self.dragAnsLabel.grid(row = 4, column = 0)
        self.dragAnsVar   = DoubleVar()
        self.dragAnsEntry = Entry(self, textvariable = self.dragAnsVar)
        self.dragAnsEntry.grid(row = 4, column = 1)

        self.button = Button(self, text = "Calculate", command = self.calcDrag)
        self.button.grid(row = 5, column = 0, columnspan = 2)

    def calcDrag(self):
        dragCoef  = self.dragCoefVar.get()
        velo      = self.veloVar.get()
        density   = self.densityVar.get()
        frontal   = self.frontalVar.get()
        dragAns   = (dragCoef * density * frontal * (velo**2))/2
        self.dragAnsVar.set(dragAns)
def main():
    Drag().mainloop()

main()

"""
Results: 
Drag Coefficient: 0.014
Speed: 180
Air density: 1.2
Frontal Area: 12
Drag: 326.592
"""