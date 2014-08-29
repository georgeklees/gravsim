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
            angle = args[1]

            # Common angle measurements
            if angle == 0 or angle == 360:
                # Upward
                self.direction=(0,magnitude)
            elif angle == 90:
                # Left
                self.direction=(-magnitude,0)
            elif angle == 180:
                # Downward
                self.direction=(0,-magnitude)
            elif angle == 270:
                # Right
                self.direction=(magnitude,0)

            # Other arbitrary angles require trigonometry "magic"
            if angle > 0 and angle < 90:
                # Calculate the Y-increment with right-triangle trig
                angle = 90 - angle
                y_inc = magnitude * (math.sin(angle))

                # Use the Pythagorean theorem to calculate the X-decrement
                x_dec = math.sqrt((magnitude**2) - (y_inc**2))

                # Create the vector
                self.direction=(-x_dec,y_inc)
            if angle > 90 and angle < 180:
                # Calculate the X-decrement with right-triangle trig
                angle = 180 - angle
                x_dec = magnitude * (math.sin(angle))

                # Use the Pythagorean theorem to calculate the Y-decrement
                y_dec = math.sqrt((magnitude**2) - (x_dec**2))

                # Create the vector
                self.direction=(-x_dec,-y_dec)
            if angle > 180 and angle < 270:
                # Calculate the X-increment with right-triangle trig
                angle = angle - 180
                x_inc = magnitude * (math.sin(angle))

                # Use the Pythagorean theorem to calculate the Y-decrement
                y_dec = math.sqrt((magnitude**2) - (x_inc**2))

                # Create the vector
                self.direction=(x_inc,-y_dec)
            if angle > 270 and angle < 360:
                # Calculate the X-increment with right-triangle trig
                angle = angle - 270
                x_inc = magnitude * (math.sin(angle))

                # Use the Pythagorean theorem to calculate the Y-increment
                y_inc = math.sqrt((magnitude**2) - (x_inc**2))

                # Create the vector
                self.direction=(x_inc,y_inc)
            else:
                raise Exception("Invalid angle value")
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
