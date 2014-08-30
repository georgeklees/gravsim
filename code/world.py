import math

import pyglet

import graphics
import music

# Current world
current_world = None

class Background(pyglet.sprite.Sprite):
    def __init__(self, img, x, y, batch, group):
        # Initialize the Sprite class
        super().__init__(img=img, x=x, y=y, batch=batch, group=group)
    def on_load(self):
        pass
    def on_unload(self):
        pass

class World:
    def __init__(self, filename):
        # Create an object list, force list, and graphics batch for the word
        self.objects = []
        self.forces = []
        self.batch = pyglet.graphics.Batch()
        
        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(1)
        
        self.read(filename)
    def read(self, filename):
        # Open the world file
        fin = open(filename, 'r')

        # Current object being parsed
        obj = None

        # Read each object from the file
        for line in fin.readlines():
            line = line.split(' ')

            # Parsing existing object
            if line[0] == '':
                # Get the name of the sub-object
                name = line[5]

                # Object force
                if name == "Force":
                    # Get the force acceleration and angle
                    acceleration = float(line[6])
                    angle = int(line[7])

                    # Create force for the object and add it
                    subobj = Force(pos=(obj.x,obj.y), acceleration=acceleration, mass=obj.mass, angle=angle)
                    obj.add_subobj(subobj)
            # New object
            else:
                # Get the name of the object
                name = line[0]

                # Audio/visual stuff
                if name == "Background":
                    obj = Background(img=pyglet.image.load(line[1]), x=0, y=0, batch=self.batch, group=self.background)
                    self.objects.append(obj)
                if name == "MusicPlayer":
                    obj = music.MusicPlayer(name=line[1])
                    self.objects.append(obj)
    def play(self):
        global current_world

        old_world = current_world
        current_world = self

        window = graphics.get_current_window()

        # Pop all the old handlers
        if old_world:
            for obj in old_world.objects:
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

# Get the current world
def get_current_world():
    return current_world
