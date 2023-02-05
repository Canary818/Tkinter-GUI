from tkinter import *
import serial

def display():
    Label(window, text = "Button pressed").pack()

# main
serialPort = serial.Serial(port = "COM13", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

window = Tk()
window.geometry("400x300")

received = False

while not received:
    if serialPort.read() == b"1":
        display()
        print(serialPort.read())
        received = True

window.mainloop()
