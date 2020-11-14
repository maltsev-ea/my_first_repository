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
        self.posx = posx
        self.posy = posy
        self.shape = canvas.create_rectangle(self.posx,
                                             self.posy,
                                             self.posx + self.size,
                                             self.posy + self.size,
                                             fill = 'green')

    def body(self, body_x, body_y):
        global body_array
        self.tail = canvas.create_rectangle(body_x,
                                            body_y,
                                            body_x + self.size,
                                            body_y + self.size,
                                            fill = 'green')
        body_array.append(speed_multiplier)

    def delete_tail(self):
        canvas.delete(snake.tail)
        snake.body(snake.posx, snake.posy)

    def move_body(self):
        root.after(snake_speed, snake.delete_tail)
        
            

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
        snakes = []
        if self.posx == apple.posx and self.posy == apple.posy:
            canvas.delete(apple.shape)
            if snake.vx == 40:
                snake.body(snake.posx-40*speed_multiplier, snake.posy)
            elif snake.vx == -40:
                snake.body(snake.posx+40*speed_multiplier, snake.posy)
            elif snake.vy == 40:
                snake.body(snake.posx, snake.posy-40*speed_multiplier)
            elif snake.vy == -40:
                snake.body(snake.posx, snake.posy+40*speed_multiplier)
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
    root.after(snake_speed, snake.move)
    root.after(snake_speed, snake.check_collision)
    root.after(snake_speed, snake.move_body)
    root.after(snake_speed, refresh)
    
    
     

def main():
    global body_array, canvas, root, snake, positions, apple, speed_multiplier, snake_speed, snakes
    root = tk.Tk()
    speed_multiplier = 1
    body_array = []
    snake_speed = 500
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
