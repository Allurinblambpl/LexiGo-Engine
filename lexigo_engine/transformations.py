import math
from engine.math3d import Vector3

def translate(object3d, dx, dy, dz):
    """
    Przesuwa obiekt 3D o zadane wartości wzdłuż osi X, Y, Z.
    
    :param object3d: Obiekt 3D, który ma być przesunięty.
    :param dx: Przesunięcie wzdłuż osi X.
    :param dy: Przesunięcie wzdłuż osi Y.
    :param dz: Przesunięcie wzdłuż osi Z.
    """
    object3d.translate(dx, dy, dz)

def rotate(object3d, pitch, yaw, roll):
    """
    Obraca obiekt 3D o zadane kąty (pitch, yaw, roll) wokół osi X, Y, Z.
    
    :param object3d: Obiekt 3D, który ma być obrócony.
    :param pitch: Obrót wokół osi X (w stopniach).
    :param yaw: Obrót wokół osi Y (w stopniach).
    :param roll: Obrót wokół osi Z (w stopniach).
    """
    # Obliczanie obrotów w radianach
    pitch_rad = math.radians(pitch)
    yaw_rad = math.radians(yaw)
    roll_rad = math.radians(roll)
    
    # Obracanie obiektu
    object3d.rotate(pitch_rad, yaw_rad, roll_rad)

def scale(object3d, factor):
    """
    Skaluje obiekt 3D przez zadany współczynnik.
    
    :param object3d: Obiekt 3D, który ma być skalowany.
    :param factor: Współczynnik skalowania.
    """
    object3d.scale(factor)

def rotate_matrix(matrix, pitch, yaw, roll):
    """
    Tworzy macierz obrotu dla danego obiektu w przestrzeni 3D.

    :param matrix: Macierz transformacji, którą chcemy obrócić.
    :param pitch: Obrót wokół osi X (w stopniach).
    :param yaw: Obrót wokół osi Y (w stopniach).
    :param roll: Obrót wokół osi Z (w stopniach).
    :return: Nowa macierz po obrocie.
    """
    pitch_rad = math.radians(pitch)
    yaw_rad = math.radians(yaw)
    roll_rad = math.radians(roll)

    # Macierze rotacji wokół osi X, Y, Z
    rotation_x = [
        [1, 0, 0, 0],
        [0, math.cos(pitch_rad), -math.sin(pitch_rad), 0],
        [0, math.sin(pitch_rad), math.cos(pitch_rad), 0],
        [0, 0, 0, 1]
    ]

    rotation_y = [
        [math.cos(yaw_rad), 0, math.sin(yaw_rad), 0],
        [0, 1, 0, 0],
        [-math.sin(yaw_rad), 0, math.cos(yaw_rad), 0],
        [0, 0, 0, 1]
    ]

    rotation_z = [
        [math.cos(roll_rad), -math.sin(roll_rad), 0, 0],
        [math.sin(roll_rad), math.cos(roll_rad), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]
    
    # Łączenie macierzy rotacji
    rotation_matrix = multiply_matrices(rotation_x, rotation_y)
    rotation_matrix = multiply_matrices(rotation_matrix, rotation_z)

    return multiply_matrices(rotation_matrix, matrix)

def multiply_matrices(m1, m2):
    """
    Mnoży dwie macierze 4x4.
    
    :param m1: Pierwsza macierz 4x4.
    :param m2: Druga macierz 4x4.
    :return: Wynaik mnożenia macierzy.
    """
    result = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            result[i][j] = sum(m1[i][k] * m2[k][j] for k in range(4))
    return result
