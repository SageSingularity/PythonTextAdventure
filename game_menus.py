# Game Menus

# This script stores the blueprints for different menu's
import os
import game

def title_screen():
	os.system('clear') # Clears the screen
	print(
		"""
		##############################
		#  Welcome to the Text RPG!  #
		##############################
		          - Play -            
		          - Help -            
		     - View Character -       
		          - Quit -
		""")

def help_menu():
	os.system('clear') # Clears the screen
	print(
		"""
		##############################
		#  Welcome to the Text RPG!  #
		##############################
		- Use up, down, left, right to move
		- Type your commands to do them
		- Use "look" to inspect something
		- Good luck and have fun!')
		- (Any key to return to title menu)
		""")

def view_character():
	os.system('clear') # Clears the screen
	with open("character.txt", "r") as character:
		print(character.read())
