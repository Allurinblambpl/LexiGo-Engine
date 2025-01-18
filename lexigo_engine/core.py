class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = []  # Lista obiektów 3D na scenie
        self.running = True

        # Bufor wirtualny do renderowania (symulacja okna gry)
        self.frame_buffer = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def add_object(self, obj):
        """Dodaje obiekt 3D do sceny."""
        self.objects.append(obj)

    def clear_frame(self):
        """Czyści bufor ramki."""
        self.frame_buffer = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def render(self):
        """Renderuje scenę w terminalu."""
        self.clear_frame()

        # Renderowanie obiektów
        for obj in self.objects:
            for vertex in obj.vertices:
                x, y = self.project_to_2d(vertex)
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.frame_buffer[y][x] = "#"

        # Wyświetlanie ramki
        print("\033[H", end="")  # Resetuje kursor terminala
        for row in self.frame_buffer:
            print("".join(row))

    def project_to_2d(self, vertex):
        """Projekcja 3D na 2D (prosta symulacja kamery)."""
        x, y, _ = vertex  # Ignorujemy współrzędną Z
        projected_x = int(x * self.width / 2 + self.width / 2)
        projected_y = int(y * self.height / 2 + self.height / 2)
        return projected_x, projected_y

    def main_loop(self):
        """Główna pętla gry."""
        while self.running:
            self.update()
            self.render()

    def update(self):
        """Aktualizuje logikę gry (pusta, do rozwinięcia w przyszłości)."""
        pass
