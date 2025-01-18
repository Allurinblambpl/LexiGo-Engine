from math3d import Vector3

class Light:
    def __init__(self, position, intensity):
        """
        Inicjalizuje źródło światła.
        
        :param position: Pozycja źródła światła (Vector3).
        :param intensity: Intensywność światła (skalar).
        """
        self.position = position
        self.intensity = intensity

    def calculate_light(self, point):
        """
        Oblicza oświetlenie punktu w przestrzeni.
        
        :param point: Punkt, dla którego obliczamy oświetlenie (Vector3).
        :return: Skalarne natężenie światła w tym punkcie.
        """
        direction = self.position.subtract(point)
        distance = direction.magnitude()
        intensity = self.intensity / (distance**2)  # Model odwrotnej kwadratu
        return max(intensity, 0)  # Upewnij się, że intensywność nie jest ujemna
