"""
This class will create the ship that the user will board.
This class maps out the entire ship.
Each individual part of the ship will have its own class.
one final class controls the flow of how you move between them.
"""

import shipRooms as shipR

jail = shipR.Jail()
medR = shipR.MedicineRoom()
weaponR = shipR.WeaponsRoom()
radioR = shipR.RadioRoom()
armourR = shipR.ArmourRoom()
centralCommandR = shipR.CentralCommandRoom()
escapeR = shipR.EscapeRoom()


class ShipRooms(object):
	def __init__(self):
		"""You start in jail, and work out from there"""
		toHere = jail.enter()
		changeRooms(toHere)

def changeRooms(toHere):
	print "-" * 10
	print("[Moving rooms to: %r.]") % (toHere)
	if toHere == "medicalRoom":
		medR.enter()
	elif toHere == "weaponsRoom":
		weaponR.enter()
	else:
		"error in changeRooms method..."
	print "-" * 10