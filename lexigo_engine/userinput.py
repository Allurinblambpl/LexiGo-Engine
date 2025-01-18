import keyboard  # Będzie używane do monitorowania klawiatury

class UserInput:
    def __init__(self):
        self.move_forward = False
        self.move_backward = False
        self.move_left = False
        self.move_right = False

    def update(self):
        """
        Sprawdza, które klawisze zostały naciśnięte i ustawia odpowiednie zmienne.
        """
        self.move_forward = keyboard.is_pressed('w')
        self.move_backward = keyboard.is_pressed('s')
        self.move_left = keyboard.is_pressed('a')
        self.move_right = keyboard.is_pressed('d')
