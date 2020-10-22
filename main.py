

from TrickWinner import trickWinner




class Domino():
	def __init__(self, isTrump, isDouble, High, Low, ID, Points):
		self.isTrump = isTrump    # Value to see if a trump
		self.isDouble = isDouble  # Value to test for a double
		self.High = High          # The large side of the domino
		self.Low = Low            # The small side of the domino
		self.ID = ID              # The ID representing domonis in an order
		self.Points = Points      # The value of the domino when adding for tricks
		self.isPlayed = False
	def printDom(self):
		print("[" + str(self.High) + "/" + str(self.Low) + "]")
	def trumpCheck(self, Trump):
			if self.High == Trump:
				self.isTrump = True
			elif self.Low == Trump:
				self.isTrump = True
			else :
				self.isTrump = False
				
def createHand(suit, hand):
	amountOf = 0
	temp = 0
	for i in range(len(hand)):
		if hand[i].High == suit or hand[i].Low == suit:
			amountOf += 1
	if amountOf == 0:
		tempArray = [D0] * len(hand)
		for i in range(len(hand)):
			tempArray[i] = hand[i]
	else:
		tempArray = [D0] * amountOf
		for i in range(amountOf):
			if hand[i].High == suit or hand[i].Low == suit:
				tempArray[temp] = hand[i]
				temp +=1
#	print(str(len(tempArray)))
	return tempArray
	






	# Return who one as an int(winner) and then what that domino was(dWinner) points is passed at end to show who wins.
	#return winner, dWinner, points, points




	
	
# Creating Dominos for use later
D0 = Domino(False, True, 0, 0, 0, .25)
D1 = Domino(False, False, 1, 0, 1, .25)
D2 = Domino(False, False, 2, 0, 2, .25)
D3 = Domino(False, False, 3, 0, 3, .25)
D4 = Domino(False, False, 4, 0, 4, .25)
D5 = Domino(False, False, 5, 0, 5, 5.25)
D6 = Domino(False, False, 6, 0, 6, .25)
D7 = Domino(False, True, 1, 1, 7, .25)
D8 = Domino(False, False, 2, 1, 8, .25)
D9 = Domino(False, False, 3, 1, 9, .25)
D10 = Domino(False, False, 4, 1, 10, 5.25)
D11 = Domino(False, False, 5, 1, 11, .25)
D12 = Domino(False, False, 6, 1, 12, .25)
D13 = Domino(False, True, 2, 2, 13, .25)
D14 = Domino(False, False, 3, 2, 14, 5.25)
D15 = Domino(False, False, 4, 2, 15, .25)
D16 = Domino(False, False, 5, 2, 16, .25)
D17 = Domino(False, False, 6, 2, 17, .25)
D18 = Domino(False, True, 3, 3, 18, .25)
D19 = Domino(False, False, 4, 3, 19, .25)
D20 = Domino(False, False, 5, 3, 20, .25)
D21 = Domino(False, False, 6, 3, 21, .25)
D22 = Domino(False, True, 4, 4, 22, .25)
D23 = Domino(False, False, 5, 4, 23, .25)
D24 = Domino(False, False, 6, 4, 24, 10.25)
D25 = Domino(False, True, 5, 5, 25, 10.25)
D26 = Domino(False, False, 6, 5, 26, .25)
D27 = Domino(False, True, 6, 6, 27, .25)
# Domino array for manipulation
Dominos = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27]
#default values
Suit = 0
Trump = 6
Player0 = [D27, D26, D21, D12, D7, D2, D3]       #6/6  6/5  6/3  6/1  1/1  0/2  0/3
Player1 = [D25, D22, D15, D10, D11, D6, D24]     #5/5  4/4  2/4  1/4  1/5  0/6  4/6
Player2 = [D23, D20, D0, D1, D8, D18, D14]       #4/5  3/5  0/0  0/1  1/2  3/3  2/3
Player3 = [D4, D5, D9, D13, D16, D17, D19]       #0/4  0/5  1/3  2/5  2/2  2/6  3/4
Player = [Player0, Player1, Player2, Player3]
# Default Score for each player
P0 = 0.0
P1 = 0.0
P2 = 0.0
P3 = 0.0


#Player Scores Array
PS = [P0, P1, P2, P3]

#Domino played by each player
Play0 = D0
Play1 = D0
Play2 = D0
Play3 = D0

#Set Trumps
for Domino in Dominos:
	Domino.trumpCheck(Trump)
print("Trump check done")
# ****************************************************************************
# *                                                                          *
# *                                 MAIN                                     *
# *                                                                          *
# ****************************************************************************
	











#  maybe make a main() function TODO
intWinner, domWinner, tempPoints = trickWinner(Player0[0], Player1[0], Player2[0], Player3[0], Player0[0], Trump)

domWinner.printDom()

if (intWinner == 0):
	PS[0] += tempPoints
if (intWinner == 1):
	PS[1] += tempPoints
if (intWinner == 2):
	PS[2] += tempPoints
if (intWinner == 3):
	PS[3] += tempPoints











#print out all scores
print(str(PS[0]) + " " + str(PS[1]) + " " + str(PS[2]) + " " + str(PS[3]))

