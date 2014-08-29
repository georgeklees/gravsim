# 2D vector class
class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self, other):
        if type(other) != Vector2:
            raise Exception("Both operands of vector addition must be vectors")

        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        if type(other) != Vector2:
            raise Exception("Both operands of vector subtraction must be vectors")

        return Vector2(self.x - other.x, self.y - other.y)
