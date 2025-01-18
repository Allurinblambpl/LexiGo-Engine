from engine.math3d import Vector3
import math

class Camera:
    def __init__(self, position, look_at, up_vector=Vector3(0, 1, 0), fov=90, aspect_ratio=1.0, near=0.1, far=100.0):
        """
        Inicjalizuje kamerę w 3D.
        
        :param position: Pozycja kamery w przestrzeni (Vector3).
        :param look_at: Wektor wskazujący, na co kamera patrzy (Vector3).
        :param up_vector: Wektor "do góry" (Vector3).
        :param fov: Kąt widzenia kamery w stopniach (Field of View).
        :param aspect_ratio: Stosunek szerokości do wysokości.
        :param near: Odległość do najbliższego obiektu w widoku.
        :param far: Odległość do najdalszego obiektu w widoku.
        """
        self.position = position
        self.look_at = look_at
        self.up_vector = up_vector
        self.fov = fov
        self.aspect_ratio = aspect_ratio
        self.near = near
        self.far = far

        # Tworzymy macierz widoku (View Matrix)
        self.view_matrix = self.calculate_view_matrix()

        # Tworzymy macierz rzutowania (Projection Matrix)
        self.projection_matrix = self.calculate_projection_matrix()

    def calculate_view_matrix(self):
        """
        Oblicza macierz widoku (View Matrix) na podstawie pozycji kamery, kierunku patrzenia i wektora "do góry".
        
        :return: Macierz widoku (4x4).
        """
        forward = self.look_at.subtract(self.position).normalize()
        right = self.up_vector.cross(forward).normalize()
        up = forward.cross(right)

        # Transponowana macierz widoku (na podstawie odwrotnej macierzy rotacji)
        view_matrix = [
            [right.x, up.x, -forward.x, 0],
            [right.y, up.y, -forward.y, 0],
            [right.z, up.z, -forward.z, 0],
            [-right.dot(self.position), -up.dot(self.position), forward.dot(self.position), 1]
        ]
        
        return view_matrix

    def calculate_projection_matrix(self):
        """
        Oblicza macierz rzutowania (Projection Matrix) na podstawie parametrów kamery.
        
        :return: Macierz rzutowania (4x4).
        """
        fov_rad = math.radians(self.fov)
        f = 1 / math.tan(fov_rad / 2)
        range_inv = 1 / (self.near - self.far)

        projection_matrix = [
            [f / self.aspect_ratio, 0, 0, 0],
            [0, f, 0, 0],
            [0, 0, (self.near + self.far) * range_inv, 2 * self.near * self.far * range_inv],
            [0, 0, -1, 0]
        ]
        
        return projection_matrix

    def get_view_matrix(self):
        """
        Zwraca macierz widoku kamery.
        
        :return: Macierz widoku.
        """
        return self.view_matrix

    def get_projection_matrix(self):
        """
        Zwraca macierz rzutowania kamery.
        
        :return: Macierz rzutowania.
        """
        return self.projection_matrix
