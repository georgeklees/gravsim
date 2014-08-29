import math

# 2D vector class
class Vector2:
    def __init__(self, head=(0,0), direction=(0,0)):
        self.head = head
        self.direction = direction
    def __add__(self, other):
        if type(other) != Vector2:
            raise Exception("Both operands of vector addition must be vectors")

        direction = (self.direction[0] + other.direction[0], self.direction[1] + other.direction[1])
        return Vector2(self.head, direction)
    def magnitude(self):
        return math.sqrt((self.direction[0] ** 2) + (self.direction[1] ** 2))
