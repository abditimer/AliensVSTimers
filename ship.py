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
deathRoom = shipR.DeathRoom()


class ShipRooms(object):
	def __init__(self):
		"""You start in jail, and work out from there"""
		toHere = jail.enter()
		changeRooms(toHere)

def changeRooms(toHere):
	keepPlaying = True
	while keepPlaying:
		print "-" * 10
		if toHere == "medicalRoom":
			toHere = medR.enter()
		elif toHere == "weaponsRoom":
			toHere = weaponR.enter()
		elif toHere == "radioRoom":
			toHere = radioR.enter()
		elif toHere == "armourRoom":
			toHere = armourR.enter()
		elif toHere == "centralCommandRoom":
			toHere = centralCommandR.enter()
		elif toHere == "escapeRoom":
			escapeR.enter()
			keepPlaying = False
			break
		elif toHere == "deathRoom":
			deathRoom.enter()
			keepPlaying = False
			break
		else:
			"error in changeRooms method..."

		changeRooms(toHere)
		keepPlaying = False