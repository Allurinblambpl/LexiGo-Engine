import time

class Button:
    def __init__(self, label, x, y, width, height, action):
        self.label = label
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.action = action

    def is_clicked(self, mouse_x, mouse_y):
        """Check if the button is clicked."""
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height

class UI:
    def __init__(self):
        self.buttons = []

    def add_button(self, button):
        self.buttons.append(button)

    def render(self):
        """Render buttons."""
        for button in self.buttons:
            print(f"Rendering button: {button.label}")

    def handle_click(self, mouse_x, mouse_y):
        """Handle button clicks."""
        for button in self.buttons:
            if button.is_clicked(mouse_x, mouse_y):
                button.action()
