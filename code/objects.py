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
        # Calculations for drag
        self.volume = 4/3 * math.pi * (self.height / 2) ** 3
        self.density = self.mass / self.volume
        self.reference_area = 2 * math.pi * (self.height / 2) ** 2
    def on_load(self):
        pass
