# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:25:27 2019

@author: nj2418
"""


import time
import random
import copy
import string
from pprint import pprint
start_time = time.time()
print("to start the game type in game_mode(dif)")
#from pprint import pprint
#width = int(input("what is the width"))
#height = int(input("what is the height"))
#mine_num = int(input("how many mines do you want"))
death_screen = "***********************\n*      You            *\n*      Lost           *\n***********************"
win_screen = "***********************\n*      You            *\n*      Win!           *\n***********************"
def create_board(width, height):
    gameboard = []
    for row in range(0, height):
        this_row = []
        for col in range(0, width):
            this_row.append(None)
        gameboard.append(this_row)
    return gameboard
mine = "-1"

def create_copy(printboard):    
    
    #gameboard2 = []
    #for row in gameboard: 
    #    gameboard2.append(row[:])
    #return gameboard2
    
    cop = copy.deepcopy(printboard)
    print(cop)
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


def user_view(gameboard):
 #   x = input("in what column is the block you want to reveal: ")
  #  y = input("in what row is the block you want to reveal: ")
    row_string = "  |"
    header_string = "   "
    full_list = []
    y = 0
    for i in range(0, len(gameboard[0])):
        full_list.append("{:^4d}".format(i))
        row_string += "{:^4d}".format(i)
        header_string += "{:^4d}".format(i)
    p = '-' * (len(header_string))
    row_string += ('\n')
    row_string += (p + '\n')
    full_list.append(p)
    while y < len(gameboard):
        x = 0
        row_list = ["{:>2d}|".format(y)]
        row_string += "{:>2d}|".format(y)
        while x < len(gameboard[0]):
          #  if str(gameboard[y][x]) == 'X' :
           #      1 = 1
            if str(gameboard[y][x]) == '0' :
                row_string += "{:^4s}".format(".")
                row_list.append("{:^4s}".format("."))
            #elif gameboard[y][x] == 'n':
             #   print('dict is working')
              #  row_string += bombs([y][x])
               # row_list.append(str(bombs[y][x]))
            elif gameboard[y][x] == None or gameboard[y][x] == '-1' or gameboard[y][x] == '*' :
                if gameboard[y][x] == '*':
                    gameboard[y][x] = "-1"
                row_string += "{:^4s}".format("?")
                row_list.append("{:^4s}".format("?"))
            elif gameboard[y][x] == 'X':
                row_string += "{:^4s}".format("▶")
                row_list.append("{:^4s}".format("X"))
            elif gameboard[y][x] == 'x':
                row_string += "{:^4s}".format("▶")
                row_list.append("{:^4s}".format("x"))
                 
            elif str(gameboard[y][x]) in '12345678':
                row_string += "{:^4s}".format(str(gameboard[y][x]))
                row_list.append(str(gameboard[y][x]))
            x += 1
           
       
        row_list = ["|{:<3d}".format(y)]
        row_string += "|{:<3d}".format(y)
        row_string += '\n' 
        y += 1
        row_string.strip('')
        full_list.append(row_list)
    row_string = row_string[:-2]
    print(row_string)
    print(p)
    print(header_string)
    return full_list, row_string

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
    print(gameboard)
    return gameboard    

def place_flag(gameboard, gameboard2, x, y):

    if gameboard[y][x] == 'X' or gameboard[y][x] == 'x':
        gameboard[y][x] = gameboard2[y][x]
    else:    
        if gameboard2[y][x] == '*':
            gameboard[y][x] = 'X'
        else:
            gameboard[y][x] = 'x'
"""
def uncover_board(gameboard, x, y):
    if print_board[y][x] == '0':
        gameboard[y][x] = '0'
        get_mine_count[y-1][x]
    elif print_board[y][x] > '0':
        gameboard[y][x] = print_board[y][x]
"""        
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
    print('mines left: ', (checker-thing))
    if checker == thing :
        return True
    else:
        return False
    



    
    
    

def game_mode(dif):
    dif = input("press e for easy, m for medium, h for hard or c for custom: ")
    if dif == 'e':
        game(6, 6, 6)
    if dif == 'm':
        game(12, 12, 18)
    if dif == 'h':
        game(22, 22, 30)
    if dif == 'c':
        print('type in game(height, width, number of mines)')
        
        
    
    
    
def game(height, width, n):
    #width = int(input("what is the width"))
    #height = int(input("what is the height"))
    #mine_num = int(input("how many mines do you want"))
    z = create_board(width, height)
    bury_mines(z, n) 
    user_view(z)
    p = print_board(z)
    c = create_copy(p)
    start_time = time.time()
    elapsed_time = time.time() - start_time
    print("start time is: ", elapsed_time)
    print_board(z)
    while 1 == 1:
        if check_won(z, p) == True:
            print(win_screen)
            elapsed_time = time.time() - start_time
            print("final time is {:.1f}".format(elapsed_time))

            break
        else:
                xy = input("type in coordinates type in m before to place flag: ")
#                if 'n' or '.' or 'b' or 'j'or 'k' or 'l' or 'a' or '/' \
#                or 'v' or 'h'or 'g' or 'd' or 'o'or 'p' or 'y' or '[' in xy:
#                    xy = '0,0'
#                    print('please type in again. only use m, numbers, and commas: ')
                
                if not xy[0].isdigit() and xy[0] != 'm':
                    print('error try again')
    
                elif 'm' in xy:
                    xy = xy[1:].split(',')
                    x = int(xy[0])
                    y = int(xy[1]) 
                    #if user_view(z)[y][x] == '▶' :
                    #    z[y][x] = print_board(z)[y][x]
                    #    print(user_view(z))
                    place_flag(z, c, x, y)
                    user_view(z)
                    elapsed_time = time.time() - start_time
                    print("current time is {:.1f}".format(elapsed_time))

                else:
                            xy = xy.split(',')
                            x = int(xy[0])
                            y = int(xy[1]) 
                            if z[y][x] == '-1' :
                                print(death_screen)
                                break
                            else:    
                                uncover_board(z, x, y)
                                user_view(z)
                                elapsed_time = time.time() - start_time
                                print("current time is {:.1f}".format(elapsed_time))

        
    # y = random.randint(0, height) game(10, 10, 5)
    

    
    #width = 5
   # height = 5
   # blank = "None"
   # row = blank * width
    #print(row, "\n", * height)