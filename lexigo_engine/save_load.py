import json
import os

class SaveLoadSystem:
    def __init__(self, save_file="game_save.json"):
        self.save_file = save_file

    def save_game(self, game_data):
        """Saves the game state to a JSON file."""
        with open(self.save_file, 'w') as file:
            json.dump(game_data, file)
        print("Game saved successfully!")

    def load_game(self):
        """Loads the game state from a JSON file."""
        if os.path.exists(self.save_file):
            with open(self.save_file, 'r') as file:
                game_data = json.load(file)
            print("Game loaded successfully!")
            return game_data
        else:
            print("No save file found.")
            return None

    def delete_save(self):
        """Deletes the save file."""
        if os.path.exists(self.save_file):
            os.remove(self.save_file)
            print("Save file deleted.")
        else:
            print("No save file found to delete.")
