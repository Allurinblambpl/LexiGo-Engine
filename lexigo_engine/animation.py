from transformations import translate
import time

class Animator:
    def __init__(self, object3d):
        self.object = object3d
        self.animations = []

    def add_animation(self, translate_vector, duration):
        """Add a translation animation."""
        self.animations.append((translate_vector, duration, time.time()))

    def update(self):
        """Update all animations."""
        current_time = time.time()
        for translate_vector, duration, start_time in self.animations:
            if current_time - start_time < duration:
                translate(self.object, *translate_vector)
            else:
                self.animations.remove((translate_vector, duration, start_time))
