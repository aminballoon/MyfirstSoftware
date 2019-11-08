# from tkinter import *
# import time
# window = Tk()
# i = "aa"
# window.title("Welcome to LikeGeeks app")
# window.geometry('1080x720')
# window.title("Welcome to LikeGeeks app")
#
# lbl = Label(window, text="Hello1", font=("Arial Bold", 150))
# lbl1 = Label(window, text="Hello2", font=("Arial Bold", 150))
# Q = Label(window, text="Hello2", font=("Arial Bold", 150))
# Q1 = Label(window, text=i, font=("Arial Bold", 150))
# lbl.grid(column=0, row=0)
# lbl1.grid(column=0, row=1)
# Q.grid(column=1, row=0)
# Q1.grid(column=1, row=1)
# i += "v"
# window.mainloop()

# from tkinter import *
#
# sensor_value =300.4#said sensor value
# master = Tk()
# x = sensor_value #assigned to variable x like you showed
# master.minsize(width=400, height=400)
# w = Label(master, text=x) #shows as text in the window
# w.pack() #organizes widgets in blocks before placing them in the parent.
# sensor_value += 1
# mainloop()

#
# from tkinter import *
#
#
# class Window(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master = master
#         self.pack(fill=BOTH, expand=1)
#         j = "Just do it"
#         text = Label(self, text=j)
#         text.place(x=70, y=90)
#         # text.pack()
#
# while(1):
#     root = Tk()
#     app = Window(root)
#     root.wm_title("Tkinter window")
#     root.geometry("200x200")
#     root.mainloop()


import tkinter as tk
import datetime

def set_label():
    currentTime = datetime.datetime.now()
    label['text'] = currentTime
    root.after(1, set_label)

root = tk.Tk()
label = tk.Label(root, text="placeholder")
label.pack()

set_label()
root.mainloop()
