class Object3D:
    def __init__(self, vertices):
        """
        Klasa reprezentująca obiekt 3D.

        :param vertices: Lista wierzchołków obiektu 3D (każdy wierzchołek to krotka (x, y, z)).
        """
        self.vertices = vertices  # Wierzchołki obiektu 3D
        self.position = (0, 0, 0)  # Pozycja obiektu w przestrzeni (x, y, z)
        self.rotation = (0, 0, 0)  # Obrót obiektu (pitch, yaw, roll)

    def translate(self, dx, dy, dz):
        """
        Przesuwa obiekt 3D o podane wartości.

        :param dx: Przesunięcie wzdłuż osi X.
        :param dy: Przesunięcie wzdłuż osi Y.
        :param dz: Przesunięcie wzdłuż osi Z.
        """
        self.vertices = [(x + dx, y + dy, z + dz) for x, y, z in self.vertices]
        self.position = (
            self.position[0] + dx,
            self.position[1] + dy,
            self.position[2] + dz,
        )

    def rotate(self, pitch, yaw, roll):
        """
        Obraca obiekt 3D. Na razie pusta (do implementacji w przyszłości).
        
        :param pitch: Obrót wokół osi X.
        :param yaw: Obrót wokół osi Y.
        :param roll: Obrót wokół osi Z.
        """
        self.rotation = (
            self.rotation[0] + pitch,
            self.rotation[1] + yaw,
            self.rotation[2] + roll,
        )
        # Rotacja może być zaimplementowana później dla bardziej złożonych obiektów.

    def scale(self, factor):
        """
        Skaluje obiekt 3D.

        :param factor: Współczynnik skalowania.
        """
        self.vertices = [(x * factor, y * factor, z * factor) for x, y, z in self.vertices]
