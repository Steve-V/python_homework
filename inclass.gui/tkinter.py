
# Only works in Python 2!

from Tkinter import *

class App:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.val = StringVar()
        self.val.set("Press calculate to convert")
        self.textbox = Entry(frame)
        self.textbox.pack()
        self.button = Button(frame,text="Calculate",command=self.calculate)
        self.button.pack()
        self.label = Label(frame,textvariable=self.val)
        self.label.pack()
    
    def calculate(self):
        value = float(self.textbox.get())
        self.val.set( str((0.3048 * value * 10000.0 + 0.5)/10000.0)+" meters")

root = Tk()
root.title=("Feet to meters")
root.geometry("200x150")
app = App(root)
root.mainloop()
