#needed to quit the game
from sys import exit
import ship



class Engine(object):
	"""
This class starts the game and pulls the Map of the ship together.
	"""
	def launch(self):
		play = self.welcomeMsg()
		if play == "true" or play == "t":
			shipRooms = ship.ShipRooms()
		else:
			print "these are the settings blah blah."

	def welcomeMsg(self):
		print "Welcome to Aliens vs Timers"
		print "Would you like to play a game or read some boring settings"
		print "(If you want to play, type true. Or else, type false)"
		play = raw_input(">")
		return play
