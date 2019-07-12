# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:13:54 2019

@author: nj2418
"""



from tkinter import Tk, Text, Label, Button, Frame, IntVar, Checkbutton, Radiobutton, Canvas, Menu
from tkinter.messagebox import showinfo

import time
import random
import copy
import string
from pprint import pprint
def create_board(width, height):
    gameboard = []
    for row in range(0, height):
        this_row = []
        for col in range(0, width):
            this_row.append(None)
        gameboard.append(this_row)
    return gameboard
mine = "-1"

def create_copy(gameboard):    
    
    #gameboard2 = []
    #for row in gameboard: 
    #    gameboard2.append(row[:])
    #return gameboard2
    
    cop = copy.deepcopy(gameboard)
    return cop

def bury_mines(gameboard, n):
    i = 0 
    
    while i < n:
        y = random.randint(0, len(gameboard) - 1)
        x = random.randint(0, len(gameboard[0]) - 1)
        if  gameboard[y][x] == None:
            gameboard[y][x] = mine
            i += 1
          
    #pprint(gameboard)
    #random.randint(0, width)
 
def get_mine_count(gameboard, x, y):
    mine_count = 0 
    width = len(gameboard[0])
    height = len(gameboard)       
    if x > 0 and (gameboard[y][x-1] == mine or gameboard[y][x-1] == 'X'):
        mine_count += 1
    if x < width -1 and (gameboard[y][x+1] == mine or gameboard[y][x+1] == 'X'):
        mine_count += 1
    if y > 0 and (gameboard[y-1][x] == mine or gameboard[y-1][x] == 'X'):
        mine_count += 1
    if y < height - 1 and (gameboard[y+1][x] == mine or gameboard[y+1][x] == 'X'):
        mine_count += 1
    if y > 0 and x > 0 and (gameboard[y-1][x-1] == mine or gameboard[y-1][x-1] == 'X'):
        mine_count += 1
    if y > 0 and x < width -1 and (gameboard[y-1][x+1] == mine or gameboard[y-1][x+1] == 'X'):
        mine_count += 1
    if y < height -1 and x > 0 and (gameboard[y+1][x-1] == mine or gameboard[y+1][x-1] == 'X'):
        mine_count += 1
    if y < height -1 and x < width -1 and (gameboard[y+1][x+1] == mine or gameboard[y+1][x+1] == 'X'):
        mine_count += 1
    return mine_count


def print_mines(gameboard):
    row_string = ""
    for row in range(0, len(gameboard)):
        for col in range (0, len(gameboard[0])):
            if gameboard[row][col] == None :
                row_string += " . "
            else:
                row_string += " * " 
        row_string += "\n"
 #   print(row_string)
    return row_string

def print_board(gameboard):
    full_list = []
    row_string = ""
    
    y = 0
  #  for row in range(0, len(gameboard)):
    while y < len(gameboard):
        x = 0
        row_list = []
        while x < len(gameboard[0]):
       # for col in range (0, len(gameboard[0])):
            if gameboard[y][x] == None :
                row_string += str(" " + str(get_mine_count(gameboard, x, y)) + " ")
                row_list.append(str(get_mine_count(gameboard, x, y)))
                x += 1
            else:
                row_string += ' * '
                row_list.append("*")
                x += 1
        full_list.append(row_list)
        y += 1
        row_string += '\n'
        
    # row_string = str(row_list)
    return full_list
def uncover_board(gameboard, x, y):
#    if gameboard[x][y] == '-1' :
#        print(death_screen)
    width = len(gameboard[0])
    height = len(gameboard)
    if gameboard[y][x] == None :
        get_mine_count(gameboard, x, y)
        if get_mine_count(gameboard, x, y) > 0:
            gameboard[y][x] = get_mine_count(gameboard, x, y)
        if get_mine_count(gameboard, x, y) == 0:
            gameboard[y][x] = get_mine_count(gameboard, x, y)
            if y > 0:
                uncover_board(gameboard, x, y-1)
            if y < height - 1:
                uncover_board(gameboard, x, y+1)
            if y > 0 and x < width - 1:
                uncover_board(gameboard, x+1, y-1)
            if y > 0 and x > 0:
                uncover_board(gameboard, x-1, y-1)
            if y < height -1 and x < width -1:
                uncover_board(gameboard, x+1, y+1)
            if y < height - 1 and x > 0:
                uncover_board(gameboard, x-1, y+1)
            if x < width - 1:
                uncover_board(gameboard, x+1, y)
            if x > 0:
                uncover_board(gameboard, x-1, y)
    return gameboard    

def check_won(gameboard, printboard):
    checker = 0
    i = 0
    while i < len(printboard):
        o = 0
        while o < len(printboard[0]):
            if printboard[i][o] == '*':
                checker += 1
            o += 1
        i += 1
        
    thing = 0
    ip = 0
    while ip < len(printboard):
        z = 0
        while z < len(printboard[0]):
            if gameboard[ip][z] == 'X' or gameboard[ip][z] == 'x':
                thing += 1
            z += 1
        ip += 1
    if checker == thing :
        return True
    else:
        return False
    
def place_flag(gameboard, gameboard2, x, y):

    if gameboard[y][x] == 'X' or gameboard[y][x] == 'x':
        gameboard[y][x] = gameboard2[y][x]
    else:    
        if gameboard2[y][x] == '*' or gameboard2[y][x] == '-1':
            gameboard[y][x] = 'X'
        else:
            gameboard[y][x] = 'x'

def display_board(board, canvas):
    canvas.delete("all")
    heightpxl =  len(board) * 31
    widthpxls = len(board[0]) * 31
    y = 0
    while y < heightpxl:
        x = 0
        while x < widthpxls:
            if board[y//31][x//31] == 'X' or board[y//31][x//31] == 'x': 
                canvas.create_rectangle(x,y,x+31,y+31, fill = 'white')
                canvas.create_text(x+15, y + 15, text= '▶', font=("Arial",15))
                
            if board[y//31][x//31] == None or board[y//31][x//31] == '-1': 
                canvas.create_rectangle(x,y,x+31,y+31, fill = 'grey')
                canvas.create_text(x+15, y + 15, text= ' ', font=("Arial",10,))
            elif board[y//31][x//31] == 0: 
                canvas.create_rectangle(x,y,x+31,y+31, fill = 'light blue')
                canvas.create_text(x+15, y + 15, text= ' ', font=("Arial",10,))
            elif board[y//31][x//31] == 1: 
                canvas.create_rectangle(x,y,x+31,y+31, fill = 'light green')
                canvas.create_text(x+15, y + 15, text= str(board[y//31][x//31]), font=("Arial",10,))
            elif board[y//31][x//31] == 2: 
                canvas.create_rectangle(x,y,x+31,y+31, fill = 'yellow')
                canvas.create_text(x+15, y + 15, text= str(board[y//31][x//31]), font=("Arial",10,))
            elif board[y//31][x//31] == 3: 
                canvas.create_rectangle(x,y,x+31,y+31, fill = 'orange')
                canvas.create_text(x+15, y + 15, text= str(board[y//31][x//31]), font=("Arial",10,))
            elif str(board[y//31][x//31]) in '4,5,6,7,8': 
                canvas.create_rectangle(x, y, x+31, y+31,  fill = 'red')
                canvas.create_text(x+15, y + 15, text= str(board[y//31][x//31]), font=("Arial",10))
            
            x +=31
        y += 31
def run_gui():    
    
    root = Tk()
    root.wm_title("Minesweeper")

    frame = Frame(master=root, height=400,width=400)
    frame.pack_propagate(0) # don't shrink
    label = Label(master=frame, text="Minesweeper", font=("Times",20)) # need to specify the parent
    label.pack(side="top") # add the label into the root window
    label = Label(master=frame, text="Welcome, press a difficulty to begin. \n Before starting a new game \n please close the old game window", font=("Times",10)) # need to specify the parent
    label.pack(side="bottom") # add the label into the root window
    def gui_game(w,h,m):
        # w = width
        # h = height
        # m = number of mines
        
       
        labelmine = Label(master=root, text= '0', font=("Times",20)) # need to specify the parent
        labelmine.pack(side="bottom") # add the label into the root window
        def NewFile():
            canvas.delete("all")
            root.destroy()
            run_gui()          
        def OpenFile():
            name = 'hello'
            print (name)
        def About():
           showinfo("Window", "left click to reveal a cell and right click to place a flag")
            
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Game Options", menu=filemenu)
        filemenu.add_command(label="New Game", command=NewFile)
        filemenu.add_command(label="Open...", command=OpenFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        
        helpmenu = Menu(menu)
        menu.add_cascade(label="instructions", menu=helpmenu)
        helpmenu.add_command(label="how to play", command=About)
        
        start_time = time.time()
        z = create_board(w, h)         #hieght and width dont exist yet
        bury_mines(z,m)       
        def popup(event):
            menu.post(event.x_root, event.y_root)
             
        heightpxls = len(z)*30 +len(z)
        widthpxls = len(z[0])*30 + len(z[0])
        canvas = Canvas(master = root, height= heightpxls+50, width = widthpxls)
        canvas.pack()  
        canvas.bind("<Button-2>", popup)
        start_time = time.time()

        frame1 = Frame(master=root, height=(heightpxls + 50),width=widthpxls)
        frame1.pack_propagate(0) # don't shrink 
        label = Label(master=root, text= '0', font=("Times",20)) # need to specify the parent
        label.pack(side="bottom") # add the label into the root window
        def label_time():
            elapsed_time = time.time() - start_time
            label['text'] = str("time: {:.1f}".format(elapsed_time))
        #    label = Label(master=canvas, text=str(datetime.now()), font=("Times",20)) # need to specify the parent
        #    label.pack(side="top") # add the label into the root windo
    
        
    
        
        display_board(z, canvas) 
        p = print_board(z)
        c = create_copy(z)   
        def mines_left(gameboard, printboard):
            checker = 0
            i = 0
            while i < len(printboard):
                o = 0
                while o < len(printboard[0]):
                    if printboard[i][o] == '*':
                        checker += 1
                    o += 1
                i += 1
                
            thing = 0
            ip = 0
            while ip < len(printboard):
                z = 0
                while z < len(printboard[0]):
                    if gameboard[ip][z] == 'X' or gameboard[ip][z] == 'x':
                        thing += 1
                    z += 1
                ip += 1
            p = checker-thing
           
            labelmine['text'] = 'mines left: ' + str(p)

    
        def handle_click(event):
            root.after(50,label_time())
            x = event.x //31
            y = event.y //31
            uncover_board(z, x, y)
            display_board(z, canvas)
            c = create_copy(z)
            mines_left(z,p)

            check_won(z,p)
            if z[y][x] == '-1' :
                #canvas.delete("all")            
                canvas.create_rectangle(0,0, widthpxls,heightpxls,fill="red") 
                canvas.create_text(widthpxls/2,heightpxls/2, text= 'You Lost', font=("Arial",40))
                canvas.unbind('<Button-1>', handle_click)
                canvas.unbind('<Button-3>', handle_click_right)
            if check_won(z,p) == True:
                #canvas.delete("all")
                canvas.create_rectangle(0,0, widthpxls,heightpxls,fill="green") 
                canvas.create_text(widthpxls/2,heightpxls/2, text= 'You Win', font=("Arial",40))
                canvas.unbind('<Button-1>', handle_click)
                canvas.unbind('<Button-3>', handle_click_right)
    
        def handle_click_right(event):
            root.after(50,label_time())
            x = event.x //31
            y = event.y //31
            place_flag(z, c, x, y)
            display_board(z, canvas)
            check_won(z,p) 
            mines_left(z,p)

            if check_won(z,p) == True:
                #canvas.delete("all")
                canvas.create_rectangle(0,0, widthpxls,heightpxls, fill="green") 
                canvas.create_text(widthpxls/2,heightpxls/2, text= 'You Win', font=("Arial",40))
                canvas.unbind('<Button-1>', handle_click)
                canvas.unbind('<Button-3>', handle_click_right)
   
#        if z[y][x] != None or z[y][x] != '-1':
#            display_board(z, canvas)
    
        
        canvas.bind('<Button-1>', handle_click)
        canvas.bind('<Button-3>', handle_click_right)


    def easy_clicked():                  #for easy
        frame.pack_forget()
        p = 10
        q = 10
        r = 15
        gui_game(p,q,r)
        

    def med_clicked():                  #for med
        frame.pack_forget()
        p = 20
        q = 20
        r = 25
        gui_game(p,q,r)
    
    
    def hard_clicked():                  #for med
        frame.pack_forget()
        p = 30
        q = 28
        r = 55
        gui_game(p,q,r)

    def ext_clicked():                  #for extreme
        frame.pack_forget()
        p = 40
        q = 28
        r = 100
        
        gui_game(p,q,r)
        
    def cust_clicked():                  #for custom
#        frame.pack_forget()
#        frames = Frame(master=root, height=800,width=800)
#        frames.pack_propagate(0)
#        def retrieve_input():
#            inputValue=textheight.get("1.0","end-1c")
#            p = inputValue
#            return p
#        def retrieve_input1():
#            inputValue=textwidth.get("1.0","end-1c")
#            q = inputValue   
#            return q
#        def retrieve_input2():
#            inputValue=textmines.get("1.0","end-1c")
#            r = inputValue
#            return r
#
#        textheight=Text(master = frames, height=2, width=10)
#        textheight.pack()
#        buttonCommit=Button(master = frames, height=1, width=10, text="height", 
#                            command=lambda: retrieve_input())
#        textwidth=Text(root, height=2, width=10)
#        textwidth.pack()
#        buttonCommit1=Button(master = frames, height=1, width=10, text="width", 
#                            command=lambda: retrieve_input1())
#        textmines=Text(root, height=2, width=10)
#        textmines.pack()
#        buttonCommit2=Button(master = frames, height=1, width=10, text="mine number", 
#                            command=lambda: retrieve_input2())
#        def start():
#            gui_game(retrieve_input(), retrieve_input1(), retrieve_input2())
#        #command=lambda: retrieve_input() >>> just means do this when i press the button
#        buttonCommit.pack()
#        buttonCommit1.pack()
#        buttonCommit2.pack()
#        checkbox_var = IntVar()
#        checkbox_var.set(1)
#        button=Button(master = frames, height=1, width=10, text="width", command=start )  
#        button.pack()

        frame.pack_forget()
        def retrieve_input():
            inputValue=textheight.get("1.0","end-1c")
            p = inputValue
            return p
        def retrieve_input1():
            inputValue=textwidth.get("1.0","end-1c")
            q = inputValue   
            return q
        def retrieve_input2():
            inputValue=textmines.get("1.0","end-1c")
            r = inputValue
            return r

        textheight=Text(root, height=2, width=10)
        textheight.pack()
        buttonCommit=Button(root, height=1, width=10, text="height", 
                            command=lambda: retrieve_input())
        textwidth=Text(root, height=2, width=10)
        textwidth.pack()
        buttonCommit1=Button(root, height=1, width=10, text="width", 
                            command=lambda: retrieve_input1())
        textmines=Text(root, height=2, width=10)
        textmines.pack()
        buttonCommit2=Button(root, height=1, width=10, text="mine number", 
                            command=lambda: retrieve_input2())
        def clear():
            thing = root.pack_slaves()
            for l in thing:
                l.destroy()
        def start():
            p = int(retrieve_input())
            q = int(retrieve_input1())
            r = int(retrieve_input2())
            clear()
            gui_game(q, p, r)
        #command=lambda: retrieve_input() >>> just means do this when i press the button
        buttonCommit.pack()
        buttonCommit1.pack()
        buttonCommit2.pack()
        checkbox_var = IntVar()
        checkbox_var.set(1)
        button=Button(root, height=1, width=10, text="start", command=start )  
        button.pack()
        

#        frame.pack_forget()
#        frames = Frame(master=root, height=400,width=400)
#        frame.pack_propagate(0) # don't shrink
#        wLabel = Label(master = frames, text="width")
#        hLabel = Label(master = frames, text="Height")
#        mLabel = Label(master= frames, text="mine number")
#        wLabel.pack(side="left")
#        hLabel.pack(side="left")
#        mLabel.pack(side="left")
#        
#        wEntry = Tk.Entry(master=frames)
#        wEntry.pack(side="right")
#        hEntry = Tk.Entry(master=frames)
#        wEntry.pack(side="right")
#        mEntry = Tk.Entry(master=frames)
#        mEntry.pack(side="right")
#        
#        checkbox_var = IntVar()
#        checkbox_var.set(1)
#        checkbox = Checkbutton(master=frame, text="ready?", var = checkbox_var, onvalue=-1, offvalue=1)    
#        checkbox.pack()
##        
##        e1.grid(row=0, column=1)
##        e2.grid(row=1, column=1)
##        e2.grid(row=2, column=1)
#        p = wEntry.get()
#        q = hEntry.get()
#        r = mEntry.get()
#        
#        if checkbox_var.get() == -1:
#            gui_game(p,q,r)


    button = Button(master=frame, text="easy", command=easy_clicked)
    button.pack()
    
    button2 = Button(master=frame, text="medium", command=med_clicked)
    button2.pack()
    
    button = Button(master=frame, text="hard", command=hard_clicked)
    button.pack()
    
    button2 = Button(master=frame, text="extreme", command=ext_clicked)
    button2.pack()
    
    button2 = Button(master=frame, text="custom", command=cust_clicked)
    button2.pack()
#    

    frame.pack()
    
    root.mainloop()        
    
        
run_gui()