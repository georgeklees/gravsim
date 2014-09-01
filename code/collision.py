import math
import itertools

def distance(objects):
    return math.sqrt((objects[1].x - objects[0].x) ** 2 +
        (objects[1].y - objects[0].y) ** 2)

def detect_collisions(objects):
    collisions = []
    for comb in itertools.combinations(objects, 2):
        # If there is a collision:
        if distance(comb) <= comb[0].radius + comb[1].radius:
            collisions.append(comb)
    return collisions

def collided_objects(collisions):
    # Note: only returns the first to prevent duplicate handling
    return set([collision[0] for collision in collisions])
