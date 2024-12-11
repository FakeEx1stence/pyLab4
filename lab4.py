import matplotlib.pyplot as plt
import math

class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = float(x)
        self.y = float(y)

    def find_length(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def move(self, x_skip, y_skip):
        self.x += x_skip
        self.x = self.check_x()
        self.y += y_skip
        self.y = self.check_y()

    def show(self):
        print(self.x, self.y)

    def check_x(self):
        if self.x >= 100 or self.x <= -100:
            self.x = 0
        else:
            return self.x

    def check_y(self):
        if self.y >= 100 or self.y <= -100:
            self.y = 0
        else:
            return self.y



def task():
     point_list = [
        Point("A", float(input("Enter x for A: ")), float(input("Enter y for A: "))),
        Point("B", float(input("Enter x for B: ")), float(input("Enter y for B: "))),
        Point("C", float(input("Enter x for C: ")), float(input("Enter y for C: ")))
        ]

     for point in point_list:
          print(point.name,": (", point.x,";" ,point.y, ") ")

     distance = point_list[0].find_length(point_list[2])
     print(f"Відстань між точками {point_list[0].name} та {point_list[2].name}: {distance}")

     print("Перед изменением:"), point_list[1].show()
     point_list[1].move(-25, -15)
     print("После изменения(Точка перемещена на 25 единиц влево и на 15 вниз):"), point_list[1].show()

     graph(point_list)


def graph(point_list):
    x = [point.x for point in point_list]
    y = [point.y for point in point_list]

    for i, point in enumerate(point_list):
        plt.text(point.x + 1, point.y + 1, point.name, fontsize=10, color='black')

    plt.plot(x,y, 'ro')
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()





