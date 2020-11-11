import tkinter as tk
from random import *
import time

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

    def move(self):
        '''reproduce the movement of the snake on the field'''
        canvas.move(self.shape, self.vx, self.vy)
        self.posx += self.vx
        self.posy += self.vy
        
    def check_collision(self):
        '''will must recognize the touch of the apple by the snake'''
        pass

    def up(self, event=None):
        if self.vy < 40:
            self.vx = 0
            self.vy -= 40
    def down(self, event=None):
        if self.vy > -40:
            self.vx = 0
            self.vy +=40
    def left(self, event=None):
        if self.vx < 40:
            self.vy = 0
            self.vx -= 40
    def right(self, event=None):
        if self.vx > -40:
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
    snake.move()   
    lambda speed_multiplier: speed_multiplier % 3 == 1, root.after(500+100*speed_multiplier, refresh)
    
     

def main():
    global canvas, root, snake, speed_multiplier, positions
    root = tk.Tk()
    speed_multiplier = 1
    positions = [40*i for i in range(1,12)]
    posx, posy = choice(positions), choice(positions)
    canvas = tk.Canvas(root, width=480, height=480)
    canvas.pack()    
    apple = Apple()
    snake = Snake(posx, posy, 0, 0)
    refresh()
    root.bind('<Down>', snake.down)
    root.bind('<Up>', snake.up)
    root.bind('<Left>', snake.left)
    root.bind('<Right>', snake.right)
    root.mainloop()
    


if __name__ == '__main__':
    main()
