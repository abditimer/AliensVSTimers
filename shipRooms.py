"""
This class creates all the rooms of the ship, and their various quirks.
The following rooms exist:
1. Jail
2. Medicine Cabinet
3. Weapons room
4. Radio room
5. armour room
6. central command unit
7. escape room
"""

from random import randint

class RoomLayout(object):
	def enter(self):
		print "Make sure to implement this."

class Jail(RoomLayout):
	"""This is where you start the game."""
	def __init__(self):
		pass

	def enter(self):
		print "You have woken up in Jail."
		# implement logic to escape from jail
		print "\nIn order to leave jail, you try and throw your jacket on the keys on the table infront."
		self.throwJacket()
		print "now lets move to the med room."
		return 'medicalRoom'

	def throwJacket(self):
		noOfThrowsNeeded = randint(1,5)
		print "Would you like to attempt to throw your jacket on the keys?"
		raw_input(">")
		currentTry = 0
		while currentTry != noOfThrowsNeeded:
			currentTry += 1
			print "Darn! You were so close! Please try again"
			raw_input(">")

class MedicineRoom(RoomLayout):
	"""This is the room where you can heal up."""
	def __init__(self):
		pass

	def enter(self):
		print "This is the medical room."
		#You are low in health. Need to find antibiatocs. take the wrong ones and die.
		returned = self.medRoomExploring()
		return returned
	
	def medRoomExploring(self):
		#this method is for finding the antibiotics. 
		print "You feel a sharp pain in the lower abdomen."
		print "You need to find some antibiotics...quickly"
		self.youFeelFaint()
		print "Lets look for some antibiotics."
		return self.lookForMedicine()

	def youFeelFaint(self):
		print("\n\n\nYou\nFeel\nFaint\n...\n")

	def lookForMedicine(self):
		print("You are approached by a medical robot, who proceeds to print some information on its stomach screen...")
		print("\nI have three different medicines; \none that can cure you, \none that can kill you and the last one can....I'm not sure to be honest. ")
		print("So, which do you pick. A, B or C?")
		return self.pickMed()


	def pickMed(self):
		usersChoice = raw_input(">")
		if usersChoice == 'A' or usersChoice == 'a':
			print "It seems like the robots screen is printing something..."
			print "\'WRONG CHOICE! HAHA YOU DEAD.\'"
			return 'deathRoom'
		else:
			print "You seem to be healed. Well done!"
			return 'weaponsRoom'

class WeaponsRoom(RoomLayout):
	"""This is the room with weapons."""
	def __init__(self):
		pass

	def enter(self):
		print "You are in the war room."
		print "You've taken a weapon"
		return "radioRoom"

class RadioRoom(RoomLayout):
	"""This is the radio room to call home"""
	def __init__(self):
		pass

	def enter(self):
		print "You are in the radio room."
		print "You phone home..."
		return "armourRoom"

class ArmourRoom(RoomLayout):
	"""This is where you get armour"""
	def __init__(self):
		pass

	def enter(self):
		print "This is where you get armour"
		print "you put on armour."
		return "centralCommandRoom"

class CentralCommandRoom(RoomLayout):
	"""this is the central command room that you need to destroy."""
	def __init__(self):
		pass

	def enter(self):
		print "You are in the central command unit of the ship."
		print "you are in the central room of the ship!"
		return "escapeRoom"

class EscapeRoom(RoomLayout):
	"""This is where you escape the ship from"""
	def __init__(self):
		pass

	def enter(self):
		print "You are in the escape room."
		print "you have escaped but you're being chased."

		print "now the chase begins...."

class DeathRoom(RoomLayout):
	def __init__(self):
		pass

	def enter(self):
		print ("Well, this is awkward. \nMate, you're dead.")












