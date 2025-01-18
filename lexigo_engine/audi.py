import pygame

class Audio:
    def __init__(self):
        pygame.mixer.init()

    def play_sound(self, sound_file):
        """Play a sound effect."""
        sound = pygame.mixer.Sound(sound_file)
        sound.play()

    def play_music(self, music_file):
        """Play background music."""
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)  # Loop the music indefinitely

    def stop_music(self):
        """Stop playing background music."""
        pygame.mixer.music.stop()
