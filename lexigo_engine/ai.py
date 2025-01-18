from math3d import Vector3

class NPC:
    def __init__(self, position, speed=0.1):
        self.position = position
        self.speed = speed

    def follow(self, target):
        """NPC follows the target's position."""
        direction = target.position.subtract(self.position)
        direction = direction.normalize()
        self.position = self.position.add(direction.scale(self.speed))

    def avoid(self, obstacle, threshold=1):
        """NPC avoids an obstacle if it's too close."""
        distance = self.position.subtract(obstacle.position).magnitude()
        if distance < threshold:
            direction = self.position.subtract(obstacle.position).normalize()
            self.position = self.position.add(direction.scale(self.speed))
