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

class RoomLayout(object):
	def enter(self):
		print "Make sure to implement this."

class Jail(RoomLayout):
	"""This is where you start the game."""
	def __init__(self):
		pass

	def enter(RoomLayout):
		print "You have woken up in Jail."
		print "now lets move to the weapons room."
		return 'weaponsRoom'

		

class MedicineRoom(RoomLayout):
	"""This is the room where you can heal up."""
	def __init__(self):
		pass

	def enter(RoomLayout):
		print "This is the medical room."

class WeaponsRoom(RoomLayout):
	"""This is the room with weapons."""
	def __init__(self):
		pass

	def enter(RoomLayout):
		print "You are in the war room."

class RadioRoom(RoomLayout):
	"""This is the radio room to call home"""
	def __init__(self):
		pass

	def enter(RoomLayout):
		print "You are in the radio room."

class ArmourRoom(RoomLayout):
	"""This is where you get armour"""
	def __init__(self):
		pass

	def enter(RoomLayout):
		print "This is where you get armour"

class CentralCommandRoom(RoomLayout):
	"""this is the central command room that you need to destroy."""
	def __init__(self):
		pass

	def enter(RoomLayout):
		print "You are in the central command unit of the ship."

class EscapeRoom(RoomLayout):
	"""This is where you escape the ship from"""
	def __init__(self):
		pass

	def enter(RoomLayout):
		print "You are in the escape room."