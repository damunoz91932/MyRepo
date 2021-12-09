import tkinter as tk
import tkinter.font as tkFont

#create tkinter object
app = tk.Tk()
#set app title
app.winfo_toplevel().title("Python GUI Project 5.8")
#set object size
app.geometry("640x480")

#create font style to use in app
fontStyle = tkFont.Font(family="Lucida Grande", size = 20)

#create label
labelExample = tk.Label(app, text="The system is idle", font=fontStyle)

def normal():
    #change label Text
    labelExample.config(text= "The system is idle")    


def SysOn():
    
    #change label text
    labelExample.config(text= "System Running")
    #call normal reset method after 2 seconds
    app.after(2000, normal)

def SysOff():
    
    #change label text
    labelExample.config(text= "System Off")
    #call normal reset method after 2 seconds
    app.after(2000, normal)

#create a vitual image to be used for sizing the buttons in pixels instead of text units
pixelVirtual = tk.PhotoImage(width=1, height=1)

#put the label in the app using pack example (top, bottom, left, right)
labelExample.pack(side=tk.TOP)

#button example - what window, button text, background color, foreground color, use virtual image for sizing, width, height, compound="c" to show text
buttonExample1 = tk.Button(app, text="System On", bg="red", fg="White", image=pixelVirtual, width=200, height=100, compound="c", command = SysOn) 
#use the place to give the button a pixel location on screen
buttonExample1.place(x=100, y=400)

buttonExample2 = tk.Button(app, text="System Off", bg="green", fg="White", image=pixelVirtual, width=200, height=100, compound="c", command = SysOff)
buttonExample2.place(x=340, y=400)

#minimal exit button and pack example (top, bottom, right, left)
buttonExample4 = tk.Button(app, text="EXIT", command = app.quit)
buttonExample4.pack(side=tk.LEFT)

app.mainloop()
