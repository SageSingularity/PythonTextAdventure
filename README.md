# PythonTextAdventure
A work-in-progress text adventure.

## Loading/Saving the Game
All data for the player character is stored in `character.txt`. This is accessed via file handle for writing when saving the character, and reading upon initialization of the player class (which always happens when the player opens up the game).

## Maps
Maps are contained in Dictionaries in `game_maps.py`. These can then be randomly accessed to achieve a sort of simple procedural generation when the player "explores a new area".

## Game Entities
Game entities are stored in `game_entities.py` and consist of the player and monster classes. The player class handles loading the players stats from previous games, and the monster class handles creating different instances of monsters to fight. By using a class structure, many monsters can be created from a single class which simplifies the code. Monster parameters are stored in dictionaries, and can later be randomized using pythons random module.

## Game Menus
The menus for the game are stored here, where each menu calls `clear` before printing. This removes the previous menus contents. In addition to normal text menus that allow choise, there is a `view character` menu that lets the player check their stats. This could be called from the main menu or anytime during play.

The `game.py` script handles the actual logic for gathering user input and calling the different maps. By separating the two files, things can be kept clean.
