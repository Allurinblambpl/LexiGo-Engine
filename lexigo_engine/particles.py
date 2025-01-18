import random
from math3d import Vector3

class Particle:
    def __init__(self, position, velocity, life):
        self.position = position
        self.velocity = velocity
        self.life = life

    def update(self, delta_time):
        """Update particle's position and decrease its life."""
        self.position = self.position.add(self.velocity.scale(delta_time))
        self.life -= delta_time

    def is_alive(self):
        """Check if the particle is still alive."""
        return self.life > 0

class ParticleSystem:
    def __init__(self, position, num_particles=100):
        self.position = position
        self.particles = []
        for _ in range(num_particles):
            velocity = Vector3(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
            life = random.uniform(1, 5)
            self.particles.append(Particle(position, velocity, life))

    def update(self, delta_time):
        """Update all particles."""
        for particle in self.particles:
            particle.update(delta_time)
        self.particles = [p for p in self.particles if p.is_alive()]

    def render(self):
        """Render particles (just print their positions)."""
        for particle in self.particles:
            print(f"Particle at {particle.position}")
