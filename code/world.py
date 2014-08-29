import math

import pyglet

import music

class Background(pyglet.sprite.Sprite):
    def __init__(self, img, x, y, batch, group):
        # Initialize the Sprite class
        super().__init__(img=img, x=x, y=y, batch=batch, group=group)
    def on_load(self):
        pass
    def on_unload(self):
        pass

class World:
    def __init__(self, filename, mode):
        # Read
        if mode == 0:
            # Create an object list and graphics batch for the word
            self.objects = []
            self.batch = pyglet.graphics.Batch()
            
            self.background = pyglet.graphics.OrderedGroup(0)
            self.foreground = pyglet.graphics.OrderedGroup(1)
            
            self.read(filename)
        # Create
        elif mode == 1:
            pass
    def read(self, filename):
        # Open the world file
        fin = open(filename, 'r')

        # Current object being parsed
        obj = None

        # Read each object from the file
        for line in fin.readlines():
            line = line.split(' ')

            # Parsing existing object
            if line[0] == '\t':
                # Get the name of the sub-object
                name = line[1]

                # Object force
                if name == "Force":
                    # Get the force acceleration and angle
                    acceleration = float(line[2])
                    angle = int(line[3])

                    # Common angle measurements
                    if angle == 0 or angle == 360:
                        # Upward
                        acceleration = physics.Vector2D(tail=(obj.x,obj.y), direction=(0,acceleration))
                    elif angle == 90:
                        # Left
                        acceleration = physics.Vector2D(tail=(obj.x,obj.y), direction=(-acceleration,0))
                    elif angle == 180:
                        # Downward
                        aceleration = physics.Vector2D(tail=(obj.x,obj.y), direction=(0,-acceleration))
                    elif angle == 270:
                        # Right
                        aceleration = physics.Vector2D(tail=(obj.x,obj.y), direction=(acceleration,))

                    # Other arbitrary angles require trigonometry "magic"
                    if angle > 0 and angle < 90:
                        # Calculate the Y-increment with right-triangle trig
                        angle = 90 - angle
                        y_inc = acceleration * (math.sin(angle))

                        # Use the Pythagorean theorem to calculate the X-decrement
                        x_dec = math.sqrt((acceleration**2) - (y_inc**2))

                        # Create the vector
                        acceleration = physics.Vector2D(tail=(obj.x,obj.y), direction=(-x_dec,y_inc))
                    if angle > 90 and angle < 180:
                        # Calculate the X-decrement with right-triangle trig
                        angle = 180 - angle
                        x_dec = acceleration * (math.sin(angle))

                        # Use the Pythagorean theorem to calculate the Y-decrement
                        y_dec = math.sqrt((acceleration**2) - (x_dec**2))

                        # Create the vector
                        acceleration = physics.Vector2D(tail=(obj.x,obj.y), direction=(-x_dec,-y_dec))
                    if angle > 180 and angle < 270:
                        # Calculate the X-increment with right-triangle trig
                        angle = angle - 180
                        x_inc = acceleration * (math.sin(angle))

                        # Use the Pythagorean theorem to calculate the Y-decrement
                        y_dec = math.sqrt((acceleration**2) - (x_inc**2))

                        # Create the vector
                        acceleration = physics.Vector2D(tail=(obj.x,obj.y), direction=(x_inc,-y_dec))
                    if angle > 270 and angle < 360:
                        # Calculate the X-increment with right-triangle trig
                        angle = angle - 270
                        x_inc = acceleration * (math.sin(angle))

                        # Use the Pythagorean theorem to calculate the Y-increment
                        y_inc = math.sqrt((acceleration**2) - (x_inc**2))

                        # Create the vector
                        acceleration = physics.Vector2D(tail=(obj.x,obj.y), direction=(x_inc,y_inc))

            # Get the name of the object
            name = line[0]

            # Create a blank object
            obj = None

            # Audio/visual stuff
            if name == "Background":
                obj = Background(img=pyglet.image.load(properties), x=0, y=0, batch=self.batch, group=self.background)
            if name == "MusicPlayer":
                obj = music.MusicPlayer(name=properties)

            self.objects.append(obj)
    def play(self):
        global current_area

        old_area = current_area
        current_area = self

        window = graphics.get_current_window()

        # Pop all the old handlers
        if old_area:
            for obj in old_area.objects:
                obj.on_unload()
                window.remove_handlers(obj)

        # Push all the new handlers
        for obj in self.objects:
            obj.on_load()
            window.push_handlers(obj)

        # Switch to the new graphics
        graphics.set_current_batch(self.batch)
    def end(self):
        window = graphics.get_current_window()
        
        for obj in self.objects:
            obj.on_unload()
            window.remove_handlers(obj)
            
