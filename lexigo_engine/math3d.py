import math

class Vector3:
    def __init__(self, x, y, z):
        """
        Klasa reprezentująca wektor 3D.
        
        :param x: Składowa X wektora.
        :param y: Składowa Y wektora.
        :param z: Składowa Z wektora.
        """
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        """Dodaje dwa wektory 3D."""
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def subtract(self, other):
        """Odejmuje dwa wektory 3D."""
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def scale(self, factor):
        """Skaluje wektor 3D przez podany współczynnik."""
        return Vector3(self.x * factor, self.y * factor, self.z * factor)

    def dot(self, other):
        """Oblicza iloczyn skalarny dwóch wektorów 3D."""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        """Oblicza iloczyn wektorowy dwóch wektorów 3D."""
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def magnitude(self):
        """Oblicza długość wektora."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        """Normalizuje wektor (zwraca wektor jednostkowy)."""
        mag = self.magnitude()
        if mag == 0:
            return Vector3(0, 0, 0)
        return self.scale(1 / mag)

    def __str__(self):
        """Zwraca reprezentację tekstową wektora."""
        return f"({self.x}, {self.y}, {self.z})"


class Matrix4:
    def __init__(self, values=None):
        """
        Klasa reprezentująca macierz 4x4. Jeśli brak wartości, tworzy macierz jednostkową.
        
        :param values: Wartości macierzy jako lista list 4x4.
        """
        if values:
            self.values = values
        else:
            self.values = [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]

    def multiply(self, other):
        """Mnoży dwie macierze 4x4."""
        result = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                result[i][j] = sum(self.values[i][k] * other.values[k][j] for k in range(4))
        return Matrix4(result)

    def transform(self, vector):
        """Przemieszcza wektor 3D za pomocą macierzy 4x4."""
        x = vector.x
        y = vector.y
        z = vector.z
        w = 1  # Wektor jednorodny

        # Mnożenie macierzy przez wektor
        new_x = self.values[0][0] * x + self.values[0][1] * y + self.values[0][2] * z + self.values[0][3] * w
        new_y = self.values[1][0] * x + self.values[1][1] * y + self.values[1][2] * z + self.values[1][3] * w
        new_z = self.values[2][0] * x + self.values[2][1] * y + self.values[2][2] * z + self.values[2][3] * w

        return Vector3(new_x, new_y, new_z)

    def __str__(self):
        """Zwraca reprezentację tekstową macierzy."""
        return "\n".join(["\t".join(map(str, row)) for row in self.values])
