import pyglet

import world
import graphics

# Update event loop
def update(dt):
    pass

# Initialize the graphics
graphics.init_graphics()

# Begin playing the title screen
title = world.World("../worlds/music_test.txt")
title.play()

# Start the event loop
pyglet.clock.schedule_interval(update, 1/120)
pyglet.app.run()
    
