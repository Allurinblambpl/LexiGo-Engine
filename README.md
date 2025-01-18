# LexiGameEngine
LexiGameEngine is a simple 3D game engine written in Python. It allows you to create 3D objects, perform transformations (translation, rotation, scaling), and render them in the terminal. The engine also includes basic physics (gravity and collision detection), lighting, and user input handling for interactive movement. Additionally, it supports saving and loading game states.

# Installation
You can install the engine via pip:
pip install lexi_game_engine

# Features
- 3D object creation and transformations (translation, rotation, scaling)
- Basic physics including gravity and collision detection
- Simple rendering in the terminal
- Lighting system for simulating light sources
- User input handling for movement with WASD
- Save and load game state (positions, scores, levels)
- Particle system (e.g., fire, smoke effects)
- AI for NPC movement and collision avoidance
- Terrain generation (random terrain grid)
- Networking support (basic multiplayer)

# Example Usage
from lexi_game_engine import GameEngine, Object3D, Camera
from lexi_game_engine.physics import PhysicsObject
from lexi_game_engine.transformations import translate, rotate, scale
from lexi_game_engine.userinput import UserInput
from lexi_game_engine.save_load import SaveLoadSystem

# Create the engine object
engine = GameEngine(800, 600)
camera = Camera(Vector3(0, 0, -5), Vector3(0, 0, 0))

# Create a 3D object (e.g., a cube)
cube = Object3D([
    (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),  # Bottom face
    (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)   # Top face
])

# Add the object to the engine
engine.add_object(cube)

# Create a physics object (e.g., a sphere with gravity)
sphere = PhysicsObject(1, Vector3(0, 0, 10), Vector3(0, 0, 0))

# Handle user input for movement
user_input = UserInput()

# Create the save/load system
save_load = SaveLoadSystem()

# Save the game state
game_data = {
    "objects": [
        {"name": "Cube", "position": {"x": 5, "y": 10, "z": 0}}
    ]
}
save_load.save_game(game_data)

# Main game loop
while True:
    user_input.update()  # Update user input

    # Apply transformations based on user input
    if user_input.move_forward:
        translate(cube, 0, 0, 0.1)
    if user_input.move_backward:
        translate(cube, 0, 0, -0.1)
    if user_input.move_left:
        translate(cube, -0.1, 0, 0)
    if user_input.move_right:
        translate(cube, 0.1, 0, 0)

    # Update physics (e.g., apply gravity to the sphere)
    sphere.update(0.1)

    # Apply rotations and scaling
    rotate(cube, 1, 0, 0)
    scale(cube, 1.02)

    # Render the objects
    engine.render()
Save and Load Game
You can save and load the game state using the SaveLoadSystem class. This allows players to save their progress and resume later.

Save Game:

game_data = {
    "objects": [
        {"name": "Cube", "position": {"x": cube.position.x, "y": cube.position.y, "z": cube.position.z}}
    ],
    "score": score,
    "level": current_level
}

save_load.save_game(game_data)
Load Game:
loaded_data = save_load.load_game()
if loaded_data:
    print("Loaded game data:", loaded_data)
