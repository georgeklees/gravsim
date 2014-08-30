import math

# 2D vector class
class Vector2D:
    def __init__(self, tail=(0,0), *args):
        # Set the starting coordinates of the vector
        self.tail = tail

        # Direction provided as a tuple
        if len(args) == 1:
            self.direction = args[0]
        # Direction provided as an angle
        elif len(args) == 2:
            # Get the magnitude and angle
            magnitude = args[0]
            angle = math.radians(args[1] + 90)

            # Calculate the direction from it
            self.direction = (magnitude * math.cos(angle), magnitude * math.sin(angle))
    def __add__(self, other):
        if type(other) != Vector2:
            raise Exception("Both operands of vector addition must be vectors")

        direction = (self.direction[0] + other.direction[0], self.direction[1] + other.direction[1])
        return Vector2D(self.tail, direction)
    def __mul__(self, other):
        # Scalar multiplication
        if type(other) == float:
            self.direction[0] *= other
            self.direction[1] *= other
    def magnitude(self):
        return math.sqrt((self.direction[0] ** 2) + (self.direction[1] ** 2))

class Force(Vector2D):
    def __init__(self, pos=(0,0), acceleration=1, mass=1, angle=0):
        # Initialize the Vector2D class
        super().__init__(tail=pos, magnitude=acceleration, angle=angle)

        # Object mass
        self.mass = mass
