import math
from math3d import Vector3

# Prosta grawitacja
GRAVITY = Vector3(0, 0, -9.81)  # Grawitacja w kierunku Z

class PhysicsObject:
    def __init__(self, mass, position, velocity):
        """
        Inicjalizuje obiekt fizyczny.
        
        :param mass: Masa obiektu.
        :param position: Pozycja obiektu (Vector3).
        :param velocity: Prędkość obiektu (Vector3).
        """
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def apply_gravity(self, delta_time):
        """
        Zastosuj grawitację do obiektu.
        
        :param delta_time: Czas, który minął od ostatniej klatki (s).
        """
        self.velocity = self.velocity.add(GRAVITY.scale(delta_time))

    def update(self, delta_time):
        """
        Zaktualizuj pozycję obiektu na podstawie prędkości i grawitacji.
        
        :param delta_time: Czas, który minął od ostatniej klatki (s).
        """
        self.apply_gravity(delta_time)
        self.position = self.position.add(self.velocity.scale(delta_time))

    def check_collision(self, other):
        """
        Sprawdzenie kolizji z innym obiektem. Prosta detekcja na podstawie odległości.
        
        :param other: Inny obiekt fizyczny.
        :return: True jeśli doszło do kolizji, False w przeciwnym razie.
        """
        distance = self.position.subtract(other.position).magnitude()
        return distance < 1  # Zakładając, że obiekty mają promień 1 jednostki
