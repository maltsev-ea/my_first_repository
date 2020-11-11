import tkinter as tk
from random import *
import time
import math

class Snake:
    def __init__(self, posx, posy, vx, vy):
        '''initializing the snake, main controloble taget in the game'''
        self.size = 40
        self.vx = vx
        self.vy = vy
        self.lenght_mulltiplier = 1 #  when the snake ate an apple increases by 1
        self.posx = posx
        self.posy = posy
        self.shape = canvas.create_rectangle(self.posx,
                                          self.posy,
                                          self.posx + self.size,
                                          self.posy + self.size,
                                          fill = 'green')

    def check_boarders(self):
        '''replaces the snake to the opposite boarder if the field is over'''
        if self.posx > 480:
            self.posx = 0
        if self.posx < 0:
            self.posx = 480
        if self.posy > 480:
            self.posy = 0
        if self.posy < 0:
            self.posy = 480


    def move(self):
        '''reproduce the movement of the snake on the field'''
        self.posx += self.vx
        self.posy += self.vy
        canvas.delete(self.shape)
        self.check_boarders()
        self.__init__(self.posx, self.posy, self.vx, self.vy)
        
        

        
    def check_collision(self):
        '''will must recognize the touch of the apple by the snake'''
        global speed_multiplier
        if self.posx == apple.posx and self.posy == apple.posy:
            canvas.delete(apple.shape)
            apple.__init__()
            speed_multiplier += 1
            
            


    def up(self, event=None):
        if -40 < self.vy < 40:
            self.vx = 0
            self.vy -= 40
    def down(self, event=None):
        if -40 < self.vy < 40:
            self.vx = 0
            self.vy +=40
    def left(self, event=None):
        if -40 < self.vx < 40:
            self.vy = 0
            self.vx -= 40
    def right(self, event=None):
        if -40 < self.vx < 40:
            self.vy = 0
            self.vx += 40


class Apple:
    def __init__(self):
        '''initialize the apples - the main target in the game'''
        self.size = 40
        self.posx = choice(positions)
        self.posy = choice(positions)
        self.shape = canvas.create_rectangle(self.posx,
                                          self.posy,
                                          self.posx + self.size,
                                          self.posy + self.size,
                                          fill = 'red')

def refresh():
    """Set the snake`s speed, by increasing by 100 each 3 eatten apples"""
    root.after(500, snake.move)
    root.after(500, snake.check_collision)
    lambda speed_multiplier: speed_multiplier % 3 == 1, root.after(500-40*speed_multiplier, refresh)
    #need to fix, when speed multiplier rises value % 3 == 1, every recal this fuction increses the snake`s speed
     

def main():
    global canvas, root, snake, positions, apple, speed_multiplier
    root = tk.Tk()
    speed_multiplier = 1
    positions = [40*i for i in range(1,12)]
    posx, posy = choice(positions), choice(positions)
    canvas = tk.Canvas(root, width=480, height=480)
    canvas.pack()    
    apple = Apple()
    snake = Snake(posx, posy, 0, 0)
    root.bind('<Down>', snake.down)
    root.bind('<Up>', snake.up)
    root.bind('<Left>', snake.left)
    root.bind('<Right>', snake.right)
    refresh()
    root.mainloop()
    


if __name__ == '__main__':
    main()
