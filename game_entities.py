# Game entities

# This script stores the blueprints for the player and the creatures
# that you can encounter in the game.
import re
#### Player class ####
class player():
	def __init__(self):
		self.name = ""
		self.hp = 0
		self.hp_max = 0
		self.mp = 0
		self.mp_max = 0
		self.status_effects = []
		self.level = 0
		self.location = "start" # Store players location
		self.experience = 0
		self.description = ""
		self.abilities = []

	def load_player_stats(self):
		parameters = ["name", "hp", "hp_max", "mp", "mp_max", "status_effects",
					  "level", "experience", "location", "description", "abilities"]
		with open("character.txt", "r") as character:
			lines = character.readlines()
			for line in lines:
				for parameter in parameters:
					if parameter in line:
						self.__dict__[parameter] = re.findall(r'\"(.+?)\"', line)[0]


#### Monster class ####
class monster():
	def __init__(self):
		self.name = ""
		self.hp = 0
		self.mp = 0
		self.status_effects = []
		self.monster_dictionary = monster_dictionary

dire_wolf = {}

monster_dictionary = { 
	"dire_wolf": {
		"name": "Dire Wolf",
		"hp": 10,
		"mp": 0,
		"abilities": ["Bite",
				      "Snarl"]
	},

	"magma_wolf": {
		"name": "Magma Wolf",
		"hp": 40,
		"mp": 5,
		"abilities": ["Bite",
					  "Snarl",
					  "Flamethrower"]
	},

	"undead_swordsman": {
		"name": "Undead Swordsman",
		"hp": 20,
		"mp": 5,
		"abilities": ["Swing Sword",
					  "Vampiric Ray"]
	},

	"undead_archer": {
		"name": "Undead Archer",
		"hp": 20,
		"mp": 5,
		"abilities": ["Fire Arrow",
				 	  "Vampiric Ray"]
	},
}