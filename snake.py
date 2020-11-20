import tkinter as tk
from random import *
import time
import math


class Snake:
    def __init__(self, scoords, vx, vy):
        '''
        initializing the snake, main controlable target in the game
        '''
        self.scoords = scoords
        self.size = 40
        self.vx = vx
        self.vy = vy
        self.pos_x = scoords[0]
        self.pos_y = scoords[1]
        self.shape = canvas.create_rectangle(self.pos_x,
                                             self.pos_y,
                                             self.pos_x + self.size,
                                             self.pos_y + self.size,
                                             fill='green')

    def set_coords(self):
        canvas.coords(self.shape,
                      self.pos_x,
                      self.pos_y,
                      self.pos_x + self.size,
                      self.pos_y + self.size)

    def check_boarders(self):
        '''
        replaces the snake to the opposite boarder if the field is over
        '''
        if self.pos_x > 480:
            self.pos_x = 0
        if self.pos_x < 0:
            self.pos_x = 480
        if self.pos_y > 480:
            self.pos_y = 0
        if self.pos_y < 0:
            self.pos_y = 480

    def move(self):
        '''
        reproduce the movement of the snake on the field
        '''
        self.pos_x += self.vx
        self.pos_y += self.vy
        self.check_boarders()
        self.set_coords()

    def check_collision(self):
        '''
        Every tik of the game clocks this functions checks the collision of snake/snake, snake/apple
        refreshing the free parts of the field for the new apples and increasing the snake speed
        '''
        global speed_multiplier, body, i, snake_speed, place
        new_places = list(place)
        if self.pos_x == apple.pos_x and self.pos_y == apple.pos_y:
            speed_multiplier += 1
            snake_speed = 100 + round(500 * 1.2 ** (-speed_multiplier))
            canvas.delete(apple.shape)
            body.append(Body((body[speed_multiplier-2].pos_x, body[speed_multiplier-2].pos_y)))
            new_places.remove((snake.pos_x, snake.pos_y))
            for unable in body:
                if (unable.pos_x, unable.pos_y) in new_places:
                    new_places.remove((unable.pos_x, unable.pos_y))
            apple.__init__(choice(new_places))
        for i in body:
            if i.pos_x == self.pos_x and i.pos_y == self.pos_y:
                game_over()

    def up(self, event=None):
        if -40 < self.vy < 40:
            self.vx = 0
            self.vy -= 40

    def down(self, event=None):
        if -40 < self.vy < 40:
            self.vx = 0
            self.vy += 40

    def left(self, event=None):
        if -40 < self.vx < 40:
            self.vy = 0
            self.vx -= 40

    def right(self, event=None):
        if -40 < self.vx < 40:
            self.vy = 0
            self.vx += 40


class Body(Snake):
    def __init__(self, bcoords, vx=None, vy=None):
        super().__init__(bcoords, vx, vy)

    def set_body_coords(self):
        canvas.coords(self.shape,
                      self.pos_x,
                      self.pos_y,
                      self.pos_x + self.size,
                      self.pos_y + self.size)


class Apple:
    '''An Apple class, the main target to eat in the game'''
    def __init__(self, apple_place):
        '''Initialise the apples at the playground with random location'''
        self.apple_place = apple_place
        self.size = 40
        self.pos_x = self.apple_place[0]
        self.pos_y = self.apple_place[1]
        self.shape = canvas.create_rectangle(self.pos_x,
                                             self.pos_y,
                                             self.pos_x + self.size,
                                             self.pos_y + self.size,
                                             fill='red')


def refresh():
    if snake.vx != 0 or snake.vy != 0:
        for i in range(len(body)-1, -1, -1):
            if not i:
                body[i].pos_x = snake.pos_x
                body[i].pos_y = snake.pos_y
            else:
                body[i].pos_x = body[i - 1].pos_x
                body[i].pos_y = body[i - 1].pos_y
        root.after(snake_speed, snake.move)
        root.after(snake_speed, snake.check_collision)
        if body:
            for i in body:
                root.after(snake_speed, i.set_body_coords)
    root.after(snake_speed, refresh)


def game_over():
    canvas.delete(tk.ALL)
    canvas.create_text(240, 240, text='GAME OVER', font=72, anchor='center')
    root.after(2000, root.destroy)


def main():
    global canvas, root, snake, apple, speed_multiplier, snake_speed, body, x_positions, y_positions, place
    root = tk.Tk()
    speed_multiplier = 1
    snake_speed = 100 + round(500*1.2**(-speed_multiplier))
    place = []
    x_positions = [40 * i for i in range(1, 12)]
    y_positions = [40 * i for i in range(1, 12)]
    for x in x_positions:
        for y in y_positions:
            place.append((x,y))
    canvas = tk.Canvas(root, width=480, height=480)
    canvas.pack()
    snake = Snake(choice(place), 0, 0)
    body = [Body((snake.pos_x - snake.size, snake.pos_y))]
    apple = Apple(choice(place))
    root.bind('<Down>', snake.down)
    root.bind('<Up>', snake.up)
    root.bind('<Left>', snake.left)
    root.bind('<Right>', snake.right)
    refresh()
    root.mainloop()


if __name__ == '__main__':
    main()
