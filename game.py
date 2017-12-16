# Python Text RPG


import cmd
import textwrap
import sys
import os
import time
import random
import string

screen_width = 100

#### Player Setup ####
class player:
	def __init__(self):
		self.name = ""
		self.hp = 0
		self.mp = 0
		self.status_effects = []
		self.location = "start" # Store players location

myPlayer = player()

#### Title Screen ####
def title_screen_selections():
	option = raw_input("> ") # Captures players input
	print option
	if option.lower() == "play": # lower() enforces lowercase on string
		start_game() # TODO: Create this function
	elif option.lower() == ("help"):
		help_menu()
	elif option.lower() == ("title"):
		title_screen()
	elif option.lower() == ("quit"):
		sys.exit()

	# Loop until a valid option is selected
	while option.lower() not in ['play', 'help', 'quit']:
		print("Please enter a valid command.")
		option = raw_input("> ") # Captures players input
		if option.lower() == ("play"):
			start_game() # TODO: Create this function
		elif option.lower() == ("help"):
			help_menu()
		elif option.lower() == ("quit"):
			sys.exit()

def title_screen():
	os.system('clear') # Clears the screen
	print('##############################')
	print('#  Welcome to the Text RPG!  #')
	print('##############################')
	print('          - Play -            ')
	print('          - Help -            ')
	print('          - Quit -            ')
	title_screen_selections()

def help_menu():
	os.system('clear') # Clears the screen
	print('##############################')
	print('#  Welcome to the Text RPG!  #')
	print('##############################')
	print('- Use up, down, left, right to move')
	print('- Type your commands to do them')
	print('- Use "look" to inspect something')
	print('- Good luck and have fun!')
	print('- (Type Title to go back to Title page)')
	title_screen_selections()

#### GAME FUNCTIONALITY ####
def start_game():
	pass

#### MAP ####
"""
a1 a2... # PLAYER STARTS AT b2
----------------
|  |  |  |  |  | a4
----------------
|  |  |  |  |  | b3 ...
----------------
|  |  |  |  |  |
----------------
|  |  |  |  |  |
----------------
"""

ZONENAME = ""
DESCRIPTION = "description"
EXAMINATION = "examine"
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

solved_places = {"a1": False, "a2": False, "a3": False, "a4": False,
				 "b1": False, "b2": False, "b3": False, "b4": False,
				 "c1": False, "c2": False, "c3": False, "c4": False,
				 "d1": False, "d2": False, "d3": False, "d4": False,
				}

zonemap = {
	'a1': {
		ZONENAME: "Town Market",
		DESCRIPTION: "",
		EXAMINATION: "",
		SOLVED: False,
		UP: "",
		DOWN: "b1",
		LEFT: "",
		RIGHT: "a2",
	},
	'a2': {
		ZONENAME: "Town Entrance",
		DESCRIPTION: "",
		EXAMINATION: "",
		SOLVED: False,
		UP: "",
		DOWN: "b2",
		LEFT: "a1",
		RIGHT: "a3",
	},
	'a3': {
		ZONENAME: "Town Square",
		DESCRIPTION: "",
		EXAMINATION: "",
		SOLVED: False,
		UP: "",
		DOWN: "b3",
		LEFT: "a2",
		RIGHT: "a4",
	},
	'a4': {
		ZONENAME: "Town Hall",
		DESCRIPTION: "",
		EXAMINATION: "",
		SOLVED: False,
		UP: "",
		DOWN: "b4",
		LEFT: "a3",
		RIGHT: "",
	},

	'b1': {
		ZONENAME: "",
		DESCRIPTION: "",
		EXAMINATION: "",
		SOLVED: False,
		UP: "a1",
		DOWN: "c1",
		LEFT: "",
		RIGHT: "b2",
	},
	'b2': { # Home / Starting point
		ZONENAME: "Home",
		DESCRIPTION: "This is your home!",
		EXAMINATION: "Your home looks the same - nothing has changed.",
		SOLVED: False,
		UP: "a2",
		DOWN: "c2",
		LEFT: "b1",
		RIGHT: "b3",
	},
	'b3': {
		ZONENAME: "",
		DESCRIPTION: "",
		EXAMINATION: "",
		SOLVED: False,
		UP: "a3",
		DOWN: "c3",
		LEFT: "b2",
		RIGHT: "b4",
	},
	'b4': {
		ZONENAME: "",
		DESCRIPTION: "",
		EXAMINATION: "",
		SOLVED: False,
		UP: "a4",
		DOWN: "c4",
		LEFT: "b3",
		RIGHT: "",
	},
	
	'c1': {
		ZONENAME: "",
		DESCRIPTION: "",
		EXAMINATION: "",
		SOLVED: False,
		UP: "b1",
		DOWN: "d1",
		LEFT: "",
		RIGHT: "c2",
	},
	'c2': {
		ZONENAME: "",
		DESCRIPTION: "",
		EXAMINATION: "",
		SOLVED: False,
		UP: "b2",
		DOWN: "d2",
		LEFT: "c1",
		RIGHT: "c3",
	},
	'c3': {
		ZONENAME: "",
		DESCRIPTION: "",
		EXAMINATION: "",
		SOLVED: False,
		UP: "b3",
		DOWN: "d3",
		LEFT: "c2",
		RIGHT: "c4",
	},
	'c4': {
		ZONENAME: "",
		DESCRIPTION: "",
		EXAMINATION: "",
		SOLVED: False,
		UP: "b4",
		DOWN: "d4",
		LEFT: "c3",
		RIGHT: "",
	},

	'd1': {
		ZONENAME: "",
		DESCRIPTION: "",
		EXAMINATION: "",
		SOLVED: False,
		UP: "c1",
		DOWN: "",
		LEFT: "",
		RIGHT: "d2",
	},
	'd2': {
		ZONENAME: "",
		DESCRIPTION: "",
		EXAMINATION: "",
		SOLVED: False,
		UP: "c2",
		DOWN: "",
		LEFT: "d1",
		RIGHT: "d3",
	},
	'd3': {
		ZONENAME: "",
		DESCRIPTION: "",
		EXAMINATION: "",
		SOLVED: False,
		UP: "c3",
		DOWN: "",
		LEFT: "d2",
		RIGHT: "d4",
	},
	'd4': {
		ZONENAME: "",
		DESCRIPTION: "",
		EXAMINATION: "",
		SOLVED: False,
		UP: "c4",
		DOWN: "",
		LEFT: "d3",
		RIGHT: "",
	},

}