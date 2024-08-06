from matplotlib import pyplot as plt
import math

class Point:
    def __init__(self, x:float, y:float):
        self.x:float = 2
        self.y:float = 4

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center: Point = center
        self.radius: float = 3

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()




