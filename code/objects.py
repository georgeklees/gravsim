import math

import physics

# Sphere object
class Sphere(physics.Object):
    def __init__(self, img, x, y, radius, mass, batch, group):
        # Calculate the cross-sectional surface area
        surface_area = math.pi * (radius ** 2)

        # Initialize the Object class
        super().__init__(img=img, x=x, y=y, mass=mass, surface_area=surface_area, batch=batch, group=group)

        # Radius
        self.radius = radius
    def on_load(self):
        pass
