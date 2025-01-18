class Renderer:
    def __init__(self, width, height):
        """
        Inicjalizuje silnik renderujący.

        :param width: Szerokość okna renderowania.
        :param height: Wysokość okna renderowania.
        """
        self.width = width
        self.height = height
        self.frame_buffer = self.create_frame_buffer()

    def create_frame_buffer(self):
        """
        Tworzy pustą ramkę bufora wypełnioną znakami pustymi (np. spacjami).

        :return: Ramka bufora (lista 2D).
        """
        return [[" " for _ in range(self.width)] for _ in range(self.height)]

    def clear_frame(self):
        """
        Czyści bufor ramki, wypełniając go spacjami.
        """
        for y in range(self.height):
            for x in range(self.width):
                self.frame_buffer[y][x] = " "

    def set_pixel(self, x, y, char="*"):
        """
        Ustawia piksel w buforze ramki.

        :param x: Pozycja x (kolumna).
        :param y: Pozycja y (wiersz).
        :param char: Znak reprezentujący piksel (domyślnie "*").
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.frame_buffer[y][x] = char

    def render_frame(self):
        """
        Wyświetla aktualny bufor ramki w konsoli.
        """
        print("\n" * 2)  # Dwa puste wiersze, aby odświeżyć widok
        for row in self.frame_buffer:
            print("".join(row))

    def draw_line(self, x1, y1, x2, y2, char="*"):
        """
        Rysuje linię między dwoma punktami (algorytm Bresenhama).

        :param x1: Początkowa pozycja x.
        :param y1: Początkowa pozycja y.
        :param x2: Końcowa pozycja x.
        :param y2: Końcowa pozycja y.
        :param char: Znak reprezentujący linię.
        """
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            self.set_pixel(x1, y1, char)
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    def draw_triangle(self, vertices, char="*"):
        """
        Rysuje trójkąt na podstawie podanych wierzchołków.

        :param vertices: Lista wierzchołków [(x1, y1), (x2, y2), (x3, y3)].
        :param char: Znak reprezentujący trójkąt.
        """
        v1, v2, v3 = vertices
        self.draw_line(v1[0], v1[1], v2[0], v2[1], char)
        self.draw_line(v2[0], v2[1], v3[0], v3[1], char)
        self.draw_line(v3[0], v3[1], v1[0], v1[1], char)

    def draw_point_cloud(self, points, char="*"):
        """
        Rysuje chmurę punktów.

        :param points: Lista punktów [(x1, y1), (x2, y2), ...].
        :param char: Znak reprezentujący punkty.
        """
        for point in points:
            self.set_pixel(point[0], point[1], char)
