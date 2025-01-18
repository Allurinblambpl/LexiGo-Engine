def dot_product(v1, v2):
    """
    Oblicza iloczyn skalarny dwóch wektorów 3D.

    :param v1: Pierwszy wektor (x1, y1, z1).
    :param v2: Drugi wektor (x2, y2, z2).
    :return: Iloczyn skalarny v1 i v2.
    """
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]


def cross_product(v1, v2):
    """
    Oblicza iloczyn wektorowy dwóch wektorów 3D.

    :param v1: Pierwszy wektor (x1, y1, z1).
    :param v2: Drugi wektor (x2, y2, z2).
    :return: Wektor będący wynikiem iloczynu wektorowego.
    """
    return (
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0],
    )


def magnitude(vector):
    """
    Oblicza długość (magnitude) wektora 3D.

    :param vector: Wektor (x, y, z).
    :return: Długość wektora.
    """
    return (vector[0]**2 + vector[1]**2 + vector[2]**2)**0.5


def normalize(vector):
    """
    Normalizuje wektor 3D (skaluje go do długości 1).

    :param vector: Wektor (x, y, z).
    :return: Znormalizowany wektor.
    """
    length = magnitude(vector)
    if length == 0:
        return (0, 0, 0)  # Unikamy dzielenia przez zero
    return (vector[0] / length, vector[1] / length, vector[2] / length)


def add_vectors(v1, v2):
    """
    Dodaje dwa wektory 3D.

    :param v1: Pierwszy wektor (x1, y1, z1).
    :param v2: Drugi wektor (x2, y2, z2).
    :return: Wektor będący sumą v1 i v2.
    """
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])


def subtract_vectors(v1, v2):
    """
    Odejmuje dwa wektory 3D.

    :param v1: Pierwszy wektor (x1, y1, z1).
    :param v2: Drugi wektor (x2, y2, z2).
    :return: Wektor będący różnicą v1 i v2.
    """
    return (v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2])


def scale_vector(vector, factor):
    """
    Skaluje wektor 3D przez podany współczynnik.

    :param vector: Wektor (x, y, z).
    :param factor: Współczynnik skalowania.
    :return: Skalowany wektor.
    """
    return (vector[0] * factor, vector[1] * factor, vector[2] * factor)
