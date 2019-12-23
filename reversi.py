'''
REVERSI
by Rafael de Moura Moreira
rafaelmmoreira@gmail.com
Available at https://github.com/rafaelmmoreira/PyReversiTK

A simple implementation of Reversi in Python using tkinter.
Made just for fun to celebrate 10 years from my first
programming assignment in college: Reversi in C, which
is also available: https://github.com/rafaelmmoreira/Reversi-C
'''

from tkinter import *
from tkinter import messagebox

FONT = ('Consolas', 10)

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Reversi')
        BoardButton.reset(self)
        self.mainloop()
        self.nowplaying = 0
        self.score = 0

    

class BoardButton(Button):
    board = tuple()
    player = 'red'
    
    
    def __init__(self, x, y, window, font):
        self.x = x
        self.y = y
        self.new = False
        self.window = window
        if x == 3 and y == 4 or x == 4 and y == 3:
            super().__init__(window, relief='groove', bg='white', font=font, text='O', foreground='red', height=2, width=3, command=lambda:BoardButton.move(self))
        elif x == 3 and y == 3 or x == 4 and y == 4:
            super().__init__(window, relief='groove', bg='white', font=font, text='O', foreground='blue', height=2, width=3, command=lambda:BoardButton.move(self))
        else:
            super().__init__(window, relief='groove', bg='white', font=font, text=' ', foreground='black', height=2, width=3, command=lambda:BoardButton.move(self))

    def reset(window):
        BoardButton.board = tuple([tuple([BoardButton(i, j, window, font=FONT) for j in range(8)]) for i in range(8)]) 
        for i in range(8):
            for j in range(8):
                BoardButton.board[i][j].grid(row=i, column=j)
        BoardButton.player = 'red'
        window.nowplaying = Label(window, text="RED's turn", fg='red')
        window.nowplaying.grid(row=10, column=2, sticky=W+E, columnspan=4)
        window.scoreRed = Label(window, text='RED 02', fg='red')
        window.scoreRed.grid(row=10, column=0, sticky=W, columnspan=2)
        window.scoreBlue = Label(window, text='BLUE 02', fg='blue')
        window.scoreBlue.grid(row=10, column=6, sticky=E, columnspan=2)
                
    def move(self, allowmove = True):
        if self.cget('foreground') == 'black':
            played = False
            
            '''
            Direction UP
            '''
            x = self.x
            y = self.y
            diff = False
            if x > 0:
                x-= 1
                while x > 0 and BoardButton.board[x][y].cget('foreground') != 'black' and BoardButton.board[x][y].cget('foreground') != BoardButton.player:
                    x-=1
                    diff = True
                if diff and BoardButton.board[x][y].cget('foreground') == BoardButton.player:           
                    played = True
                    while x < self.x and allowmove:
                        BoardButton.board[x][y].config(foreground=BoardButton.player, text='O')
                        x+=1
                        
            '''
            Direction UP+RIGHT
            '''
            x = self.x
            y = self.y
            diff = False
            if x > 0 and y < 7:
                x-=1
                y+=1
                while x > 0 and y < 7 and BoardButton.board[x][y].cget('foreground') != 'black' and BoardButton.board[x][y].cget('foreground') != BoardButton.player:
                    x-=1
                    y+=1                            
                    diff = True
                if diff and BoardButton.board[x][y].cget('foreground') == BoardButton.player:  
                    played = True
                    while x < self.x and y > self.y and allowmove:
                        BoardButton.board[x][y].config(foreground=BoardButton.player, text='O')
                        x+=1
                        y-=1
            '''
            Direction RIGHT
            '''
            x = self.x
            y = self.y
            diff = False
            if y < 7:
                y+=1
                while y < 7 and BoardButton.board[x][y].cget('foreground') != 'black' and BoardButton.board[x][y].cget('foreground') != BoardButton.player:
                    y+=1
                    diff = True
                if diff and BoardButton.board[x][y].cget('foreground') == BoardButton.player:  
                    played = True
                    while y > self.y and allowmove:
                        BoardButton.board[x][y].config(foreground=BoardButton.player, text='O')
                        y-=1
            '''
            Direction BOTTOM+RIGHT
            '''
            x = self.x
            y = self.y
            diff = False
            if x < 7 and y < 7:
                x+=1
                y+=1
                while x < 7 and y < 7 and BoardButton.board[x][y].cget('foreground') != 'black' and BoardButton.board[x][y].cget('foreground') != BoardButton.player:
                    x+=1
                    y+=1
                    diff = True
                if diff and BoardButton.board[x][y].cget('foreground') == BoardButton.player:  
                    played = True
                    while x > self.x and y > self.y and allowmove:
                        BoardButton.board[x][y].config(foreground=BoardButton.player, text='O')
                        x-=1
                        y-=1
            '''
            Direction BOTTOM
            '''
            x = self.x
            y = self.y
            diff = False
            if x < 7:
                x+=1
                while x < 7 and BoardButton.board[x][y].cget('foreground') != 'black' and BoardButton.board[x][y].cget('foreground') != BoardButton.player:
                    x+=1
                    diff = True
                if diff and BoardButton.board[x][y].cget('foreground') == BoardButton.player:  
                    played = True
                    while x > self.x and allowmove:
                        BoardButton.board[x][y].config(foreground=BoardButton.player, text='O')
                        x-=1
            '''
            Direction BOTTOM+LEFT
            '''
            x = self.x
            y = self.y
            diff = False
            if x < 7 and y > 0:
                x+=1
                y-=1
                while x < 7 and y > 0 and BoardButton.board[x][y].cget('foreground') != 'black' and BoardButton.board[x][y].cget('foreground') != BoardButton.player:
                    x+=1
                    y-=1
                    diff = True
                if diff and BoardButton.board[x][y].cget('foreground') == BoardButton.player:  
                    played = True
                    while x > self.x and y < self.y and allowmove:
                        BoardButton.board[x][y].config(foreground=BoardButton.player, text='O')
                        x-=1
                        y+=1
            '''
            Direction LEFT
            '''
            x = self.x
            y = self.y
            diff = False
            if y > 0:
                y-=1
                while y > 0 and BoardButton.board[x][y].cget('foreground') != 'black' and BoardButton.board[x][y].cget('foreground') != BoardButton.player:
                    y-=1
                    diff = True
                if diff and BoardButton.board[x][y].cget('foreground') == BoardButton.player:  
                    played = True
                    while y < self.y and allowmove:
                        BoardButton.board[x][y].config(foreground=BoardButton.player, text='O')
                        y+=1
            
            '''
            Direction UP+LEFT
            '''
            x = self.x
            y = self.y
            diff = False
            if x > 0 and y > 0:
                x-=1
                y-=1
                while x > 0 and y > 0 and BoardButton.board[x][y].cget('foreground') != 'black' and BoardButton.board[x][y].cget('foreground') != BoardButton.player:
                    x-=1
                    y-=1
                    diff = True
                if diff and BoardButton.board[x][y].cget('foreground') == BoardButton.player:  
                    played = True
                    while x < self.x and y < self.y and allowmove:
                        BoardButton.board[x][y].config(foreground=BoardButton.player, text='O')
                        x+=1
                        y+=1
    
            if played:
                if allowmove:
                    self.config(foreground=BoardButton.player, text='O')
                    red, blue = BoardButton.points()
                    self.window.scoreRed.config(text='RED {:02d}'.format(red))
                    self.window.scoreBlue.config(text='BLUE {:02d}'.format(blue))
                    if BoardButton.player == 'red':
                        BoardButton.player = 'blue'
                        self.window.nowplaying.config(text="BLUE's turn", fg='blue')
                    else:
                        BoardButton.player = 'red'
                        self.window.nowplaying.config(text="RED's turn", fg='red')
                    if BoardButton.gameover():
                        red, blue = BoardButton.points()
                        if red > blue:
                            msg = 'Red wins. '
                        elif blue > red:
                            msg = 'Blue wins. '
                        else:
                            msg = 'Tie!'
                        messagebox.showinfo("GAME OVER", msg + '- RED ' + str(red) + ' x ' + str(blue) + ' BLUE')
                        BoardButton.reset(self.window)
            return played

    def gameover():
        for line in BoardButton.board:
            for button in line:
                if button.move(False):
                    return False                    
        return True

    def points():
        red = 0
        blue = 0
        for line in BoardButton.board:
            for button in line:
                if button.cget('foreground') == 'red':
                    red += 1
                elif button.cget('foreground') == 'blue':
                    blue += 1
        return (red, blue)
    
App()
