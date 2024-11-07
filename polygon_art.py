import turtle
import random


class Polygon:
    def __init__(self, num_sides):
        self.__num_sides = num_sides
        self.__size = 0
        self.__orientation = 0
        self.__location = []
        self.__color = 0
        self.__border_size = 0

    def random_atr(self):
        self.__size = random.randint(50, 150)
        self.__orientation = random.randint(0, 90)
        self.__location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.__color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.__border_size = random.randint(1, 10)

    def draw(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        turtle.penup()
        turtle.goto(self.__location[0], self.__location[1])
        turtle.setheading(self.__orientation)
        turtle.color(self.__color)
        turtle.pensize(self.__border_size)
        turtle.pendown()
        for _ in range(self.__num_sides):
            turtle.forward(self.__size)
            turtle.left(360/self.__num_sides)
        turtle.penup()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation):
        self.__orientation = orientation

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def border_size(self):
        return self.__border_size

    @border_size.setter
    def border_size(self, border_size):
        self.__border_size = border_size


class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, num_levels, reduction_ratio):
        Polygon.__init__(self, num_sides)
        self.__num_sides = num_sides
        self.__num_levels = num_levels
        self.__reduction_ratio = reduction_ratio

    def draw(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        for _ in range(self.__num_levels):
            turtle.penup()
            turtle.goto(self.location[0], self.location[1])
            turtle.setheading(self.orientation)
            turtle.color(self.color)
            turtle.pensize(self.border_size)
            turtle.pendown()
            for _ in range(self.__num_sides):
                turtle.forward(self.size)
                turtle.left(360 / self.__num_sides)
            turtle.penup()
            turtle.forward(self.size * (1 - self.__reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(self.size * (1 - self.__reduction_ratio) / 2)
            turtle.right(90)
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]
            self.size *= self.__reduction_ratio


class Run:
    def __init__(self):
        while True:
            self.__n_art = int(input('Which art do you want to generate? Enter a number between 1 to 9 : '))
            if self.__n_art < 1 or self.__n_art > 9:
                print('Please enter a number between 1 to 9')
            elif self.__n_art == 1:
                self.n_1()
                break
            elif self.__n_art == 2:
                self.n_2()
                break
            elif self.__n_art == 3:
                self.n_3()
                break
            elif self.__n_art == 4:
                self.n_4()
                break
            elif self.__n_art == 5:
                self.n_5()
                break
            elif self.__n_art == 6:
                self.n_6()
                break
            elif self.__n_art == 7:
                self.n_7()
                break
            elif self.__n_art == 8:
                self.n_8()
                break
            elif self.__n_art == 9:
                self.n_9()
                break

    def n_1(self):
        triangle = Polygon(3)
        for _ in range(30):
            triangle.random_atr()
            triangle.draw()
        turtle.done()

    def n_2(self):
        rectangle = Polygon(4)
        for _ in range(30):
            rectangle.random_atr()
            rectangle.draw()
        turtle.done()

    def n_3(self):
        pentagon = Polygon(5)
        for _ in range(30):
            pentagon.random_atr()
            pentagon.draw()
        turtle.done()

    def n_4(self):
        triangle = Polygon(3)
        rectangle = Polygon(4)
        pentagon = Polygon(5)
        for _ in range(10):
            triangle.random_atr()
            triangle.draw()
            rectangle.random_atr()
            rectangle.draw()
            pentagon.random_atr()
            pentagon.draw()
        turtle.done()

    def n_5(self):
        triangle = EmbeddedPolygon(3, 3, 0.618)
        for _ in range(30):
            triangle.random_atr()
            triangle.draw()
        turtle.done()

    def n_6(self):
        rectangle = EmbeddedPolygon(4, 3, 0.618)
        for _ in range(30):
            rectangle.random_atr()
            rectangle.draw()
        turtle.done()

    def n_7(self):
        pentagon = EmbeddedPolygon(5, 3, 0.618)
        for _ in range(30):
            pentagon.random_atr()
            pentagon.draw()
        turtle.done()

    def n_8(self):
        triangle = EmbeddedPolygon(3, 3, 0.618)
        rectangle = EmbeddedPolygon(4, 3, 0.618)
        pentagon = EmbeddedPolygon(5, 3, 0.618)
        for _ in range(10):
            triangle.random_atr()
            triangle.draw()
            rectangle.random_atr()
            rectangle.draw()
            pentagon.random_atr()
            pentagon.draw()
        turtle.done()

    def n_9(self):
        for _ in range(10):
            triangle = EmbeddedPolygon(3, random.randint(1, 5), 0.618)
            rectangle = EmbeddedPolygon(4, random.randint(1, 5), 0.618)
            pentagon = EmbeddedPolygon(5, random.randint(1, 5), 0.618)
            triangle.random_atr()
            triangle.draw()
            rectangle.random_atr()
            rectangle.draw()
            pentagon.random_atr()
            pentagon.draw()
        turtle.done()


Run()
