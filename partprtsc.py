import tkinter as tk
# from tkinter import *
from PIL import *
import ctypes
import sys


def area_sel():
    def getPress(event):
        global press_x, press_y
        press_x, press_y = event.x, event.y

    def mouseMove(event):
        global press_x, press_y, rectangleId
        fullCanvas.delete(rectangleId)
        rectangleId = fullCanvas.create_rectangle(
            press_x, press_y, event.x, event.y, width=5)

    def getRelease(event):
        global press_x, press_y, rectangleId
        top.withdraw()
        img = ImageGrab.grab((press_x, press_y, event.x, event.y))
        img.show()

    top = tk.Toplevel()
    top.state('zoomed')
    top.overrideredirect(1)
    fullCanvas = tk.Canvas(top)

    background = ImageTk.PhotoImage(ImageGrab.grab().convert("L"))
    fullCanvas.create_image(0, 0, anchor="nw", image=background)

    fullCanvas.bind('<Button-1>', getPress)
    fullCanvas.bind('<B1-Motion>', mouseMove)
    fullCanvas.bind('<ButtonRelease-1>', getRelease)

    fullCanvas.pack(expand="YES", fill="both")
    top.mainloop()


rectangleId = None


def main():
    None
# main()
