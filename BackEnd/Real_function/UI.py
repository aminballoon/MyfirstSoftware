from tkinter import *
from time import sleep
import time
from tkinter.font import Font
font = ['@Adobe Heiti Std R', '@Adobe Ming Std L', '@Adobe Myungjo Std M', '@Adobe Song Std L', '@HYSWLongFangSong', '@Kozuka Gothic Pr6N M', '@Kozuka Mincho Pr6N R', '@MS Gothic', '@MS PGothic', '@MS UI Gothic', '@Malgun Gothic', '@Malgun Gothic Semilight', '@Microsoft JhengHei', '@Microsoft JhengHei Light', '@Microsoft JhengHei UI', '@Microsoft JhengHei UI Light', '@Microsoft YaHei', '@Microsoft YaHei Light', '@Microsoft YaHei UI', '@Microsoft YaHei UI Light', '@MingLiU-ExtB', '@MingLiU_HKSCS-ExtB', '@NSimSun', '@PMingLiU-ExtB', '@SimSun', '@SimSun-ExtB', '@Yu Gothic', '@Yu Gothic Light', '@Yu Gothic Medium', '@Yu Gothic UI', '@Yu Gothic UI Light', '@Yu Gothic UI Semibold', '@Yu Gothic UI Semilight', 'Adobe Heiti Std R', 'Adobe Ming Std L', 'Adobe Myungjo Std M', 'Adobe Pi Std', 'Adobe Song Std L', 'Angsana New', 'AngsanaUPC', 'Arabic Transparent', 'Arial', 'Arial Baltic', 'Arial Black', 'Arial CE', 'Arial CYR', 'Arial Greek', 'Arial TUR', 'Bahnschrift', 'Bahnschrift Condensed', 'Bahnschrift Light', 'Bahnschrift Light Condensed', 'Bahnschrift Light SemiCondensed', 'Bahnschrift SemiBold', 'Bahnschrift SemiBold Condensed', 'Bahnschrift SemiBold SemiConden', 'Bahnschrift SemiCondensed', 'Bahnschrift SemiLight', 'Bahnschrift SemiLight Condensed', 'Bahnschrift SemiLight SemiConde', 'Browallia New', 'BrowalliaUPC', 'Calibri', 'Calibri Light', 'Cambria', 'Cambria Math', 'Candara', 'Candara Light', 'Cascadia Code', 'Century Gothic', 'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Corbel Light', 'Cordia New', 'CordiaUPC', 'Courier', 'Courier New', 'Courier New Baltic', 'Courier New CE', 'Courier New CYR', 'Courier New Greek', 'Courier New TUR', 'Courier Std', 'DilleniaUPC', 'Ebrima', 'EucrosiaUPC', 'Fixedsys', 'Franklin Gothic Medium', 'FreesiaUPC', 'Gabriola', 'Gadugi', 'Georgia', 'HYSWLongFangSong', 'HoloLens MDL2 Assets', 'Impact', 'Ink Free', 'IrisUPC', 'JasmineUPC', 'Javanese Text', 'KodchiangUPC', 'Kozuka Gothic Pr6N M', 'Kozuka Mincho Pr6N R', 'Leelawadee', 'Leelawadee UI', 'Leelawadee UI Semilight', 'LilyUPC', 'Lucida Console', 'Lucida Sans Unicode', 'MS Gothic', 'MS PGothic', 'MS Sans Serif', 'MS Serif', 'MS UI Gothic', 'MV Boli', 'Malgun Gothic', 'Malgun Gothic Semilight', 'Marlett', 'Microsoft Himalaya', 'Microsoft JhengHei', 'Microsoft JhengHei Light', 'Microsoft JhengHei UI', 'Microsoft JhengHei UI Light', 'Microsoft New Tai Lue', 'Microsoft PhagsPa', 'Microsoft Sans Serif', 'Microsoft Tai Le', 'Microsoft YaHei', 'Microsoft YaHei Light', 'Microsoft YaHei UI', 'Microsoft YaHei UI Light', 'Microsoft Yi Baiti', 'MingLiU-ExtB', 'MingLiU_HKSCS-ExtB', 'Modern', 'Mongolian Baiti', 'Myanmar Text', 'Myriad CAD', 'NSimSun', 'Nirmala UI', 'Nirmala UI Semilight', 'OLF SimpleSansOC', 'PMingLiU-ExtB', 'Palatino Linotype', 'Roman', 'SWAstro', 'SWComp', 'SWGDT', 'SWGothe', 'SWGothg', 'SWGothi', 'SWGrekc', 'SWGreks', 'SWIsop1', 'SWIsop2', 'SWIsop3', 'SWIsot1', 'SWIsot2', 'SWIsot3', 'SWItal', 'SWItalc', 'SWItalt', 'SWLink', 'SWMap', 'SWMath', 'SWMeteo', 'SWMono', 'SWMusic', 'SWRomnc', 'SWRomnd', 'SWRomns', 'SWRomnt', 'SWScrpc', 'SWScrps', 'SWSimp', 'SWTxt', 'Script', 'Segoe MDL2 Assets', 'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Black', 'Segoe UI Emoji', 'Segoe UI Historic', 'Segoe UI Light', 'Segoe UI Semibold', 'Segoe UI Semilight', 'Segoe UI Symbol', 'SimSun', 'SimSun-ExtB', 'Sitka Banner', 'Sitka Display', 'Sitka Heading', 'Sitka Small', 'Sitka Subheading', 'Sitka Text', 'Small Fonts', 'Sylfaen', 'Symbol', 'System', 'Tahoma', 'Terminal', 'Times New Roman', 'Times New Roman Baltic', 'Times New Roman CE', 'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 'Trebuchet MS', 'Verdana', 'Webdings', 'Wingdings', 'Yu Gothic', 'Yu Gothic Light', 'Yu Gothic Medium', 'Yu Gothic UI', 'Yu Gothic UI Light', 'Yu Gothic UI Semibold', 'Yu Gothic UI Semilight']

Round = 0
Set_Queue = ['A001','A002','A003','A004','A005']
Set_Counter = ['1','2','3','4','5']
Now_Queue = "A001"
Now_Counter = "Counter: 1"
Past_Queue = ['','','','','']
Past_Counter = ['','','','','']
Window = Tk()
Window.title("Bank สาขา บางมด")
Window.geometry('1920x1080')
color_gray = '#363636'
color_blue = '#A8A7A7'
color_pink_white = '#E84A5F'
Window.configure(background = color_gray)
Show_now = StringVar()
Show_pass_1 = StringVar()
Show_pass_2 = StringVar()
Show_pass_3 = StringVar()
Show_pass_4 = StringVar()
Show_counter_now = StringVar()
Show_counter_pass1 = StringVar()
Show_counter_pass2 = StringVar()
Show_counter_pass3 = StringVar()
Show_counter_pass4 = StringVar()
Show_now.set('')
Show_pass_1.set('')
Show_pass_2.set('')
Show_pass_3.set('')
Show_pass_4.set('')
Show_counter_pass1.set('')
Show_counter_pass2.set('')
Show_counter_pass3.set('')
Show_counter_pass4.set('')
set_x = 550
set_y = 220
plus_x = 710
plus_y = 160
myFont = Font(family=font[59], size=60)
Font_head = Font(family=font[59], size=70)
photo = PhotoImage(file = "C:/Users/Xprize/Documents/solfdev/MyfirstSoftware/FrontEnd/Display/Untitled-1.gif")
backgrand = Label(Window, image=photo)
backgrand.pack()
con = Label(Window, text = 'Queue', font=Font_head,background= color_gray,
                 foreground=color_blue).place(x=500, y=40)
con1 = Label(Window, text = 'Counter', font=Font_head,background= color_gray,
                 foreground=color_blue).place(x=1130, y=40)

Row1_Queue = Label(Window, textvariable = Show_now, font=myFont, background= color_gray,
                 foreground=color_pink_white).place(x=set_x, y=set_y)
Row1_Counter = Label(Window, textvariable = Show_counter_now, font=myFont, background= color_gray,
                 foreground=color_pink_white).place(x=set_x+plus_x, y=set_y)

Row2_Queue = Label(Window, textvariable = Show_pass_1, font=myFont, background= color_gray,
                 foreground=color_pink_white).place(x=set_x, y=set_y+(plus_y))
Row2_Counter = Label(Window, textvariable = Show_counter_pass1, font=myFont, background= color_gray,
                 foreground=color_pink_white).place(x=set_x+plus_x, y=set_y+(plus_y))

Row3_Queue = Label(Window, textvariable = Show_pass_2, font=myFont, background= color_gray,
                 foreground=color_pink_white).place(x=set_x, y=set_y+(2*plus_y))
Row3_Counter = Label(Window, textvariable = Show_counter_pass2, font=myFont, background= color_gray,
                 foreground=color_pink_white).place(x=set_x+plus_x, y=set_y+(2*plus_y))

Row4_Queue = Label(Window, textvariable = Show_pass_3, font=myFont, background= color_gray,
                 foreground=color_pink_white).place(x=set_x, y=set_y+(3*plus_y))
Row4_Counter = Label(Window, textvariable = Show_counter_pass3, font=myFont, background= color_gray,
                 foreground=color_pink_white).place(x=set_x+plus_x, y=set_y+(3*plus_y))

Row5_Queue = Label(Window, textvariable = Show_pass_4, font=myFont, background= color_gray,
                 foreground=color_pink_white).place(x=set_x, y=set_y+(4*plus_y))
Row5_Counter = Label(Window, textvariable = Show_counter_pass4, font=myFont, background= color_gray,
                 foreground=color_pink_white).place(x=set_x+plus_x, y=set_y+(4*plus_y))

def ui(Queue_input,Counter_input):
    global Set_Counter,Set_Queue
    Set_Counter.append(Counter_input)
    Set_Queue.append(Queue_input)
    Set_Counter.pop(0)
    Set_Queue.pop(0)
    Show_now.set(Set_Queue[4])
    Show_counter_now.set(Set_Counter[4])
    Show_pass_1.set(Past_Queue[3])
    Show_counter_pass1.set(Past_Counter[3])
    Show_pass_2.set(Past_Queue[2])
    Show_counter_pass2.set(Past_Counter[2])
    Show_pass_3.set(Past_Queue[1])
    Show_counter_pass3.set(Past_Counter[1])
    Show_pass_4.set(Past_Queue[0])
    Show_counter_pass4.set(Past_Counter[0])
    Past_Queue[0] = Past_Queue[1]
    Past_Queue[1] = Past_Queue[2]
    Past_Queue[2] = Past_Queue[3]
    Past_Queue[3] = Set_Queue[4]
    Past_Counter[0] = Past_Counter[1]
    Past_Counter[1] = Past_Counter[2]
    Past_Counter[2] = Past_Counter[3]
    Past_Counter[3] = Set_Counter[4]
    Window.update()