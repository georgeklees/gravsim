import math
import itertools
import physics

def distance(objects):
    return math.sqrt((objects[1].x - objects[0].x) ** 2 +
        (objects[1].y - objects[0].y) ** 2)

def detect_collisions(objects):
    collisions = []
    for comb in itertools.combinations(objects, 2):
        # If there is a collision:
        if distance(comb) <= comb[0].height / 2 + comb[1].height / 2:
            collisions.append(comb)
    return collisions

def collided_objects(collisions):
    # Note: only returns the first to prevent duplicate handling
    return set([collision[0] for collision in collisions])

def handle_collision(obj, collided, collisions):
    if obj in collided:
        tobj = collisions[obj]
        if not (obj in tobj.collided_objects or tobj in obj.collided_objects):
            obj.collided_objects.append(tobj)
            tobj.collided_objects.append(obj)
            if physics.almost_equal(tobj.velocity.magnitude(), 0):
                tobj.velocity = obj.velocity * obj.mass / tobj.mass
                obj.velocity = physics.Vector2D((0, 0), 0, 0)
            elif physics.almost_equal(obj.velocity.magnitude(), 0):
                obj.velocity = tobj.velocity * tobj.mass / obj.mass
                tobj.velocity = physics.Vector2D((0, 0), 0, 0)
            # Head on collision
            elif physics.almost_equal(obj.velocity.angle, tobj.velocity.angle):
                print("Head-On collision detected")
                m1, m2 = obj.mass, tobj.mass
                obj.velocity = (m1 - m2) / (m1 + m2) * -obj.velocity
                tobj.velocity = (2 * m1) / (m1 + m2) * -tobj.velocity
            return True
    return False
