import pyglet

import world
import graphics

# Update event loop
def update(dt):
    # Get the current world
    current_world = world.get_current_world()

    # Move each object in the world
    for obj in current_world.objects:
        # Sum each of the object forces themselves
        net_force = obj.forces[0]
        for force in obj.forces[1:]:
            net_force += force

        # Now sum each environmental force
        for force in current_world.forces:
            net_force += (force * obj.mass)

        # We have the net force
        print(net_force.direction)

# Initialize the graphics
graphics.init_graphics()

# Begin playing the title screen
title = world.World("../worlds/test.txt")
title.play()

# Start the event loop
pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()
    
