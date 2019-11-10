from tkinter import Tk
import tkinter.font
Font = []
Tk()
for name in sorted(tkinter.font.families()):
    Font.append(name)

print(Font)

Counter1 = Label(Window, textvariable = Present_Queue_A, font=myFont, background= color_gray, foreground=color_pink_white).place(x=0, y=0)
Counter2 = Label(Window, textvariable = Present_Queue_A, font=myFont, background= color_gray, foreground=color_pink_white).place(x=0, y=150)
Counter3 = Label(Window, textvariable = Present_Queue_A, font=myFont, background= color_gray, foreground=color_pink_white).place(x=0, y=150)
Counter4 = Label(Window, textvariable = Present_Queue_A, font=myFont, background= color_gray, foreground=color_pink_white).place(x=0, y=150)
Counter5 = Label(Window, textvariable = Present_Queue_A, font=myFont, background= color_gray, foreground=color_pink_white).place(x=0, y=150)
