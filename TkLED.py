from tkinter import *
import serial

def LEDOn():
    serialPort.write(b"1")
    print(1)

def LEDOff():
    serialPort.write(b"0")
    print(0)

# main
serialPort = serial.Serial(port = "COM13", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

window = Tk()
window.geometry("400x300")

Button(window, text = "On", command = LEDOn).pack()
Button(window, text = "Off", command = LEDOff).pack()

window.mainloop()
