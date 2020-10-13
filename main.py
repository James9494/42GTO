class Domino():
	def __init__(self, isTrump, isDouble, High, Low, ID, Points):
		self.isTrump = isTrump    # Value to see if a trump
		self.isDouble = isDouble  # Value to test for a double
		self.High = High          # The large side of the domino
		self.Low = Low            # The small side of the domino
		self.ID = ID              # The ID representing domonis in an order
		self.Points = Points      # The value of the domino when adding for tricks
	def printDom(self):
		print("[" + str(self.High) + "/" + str(self.Low) + "]")
	def trumpCheck(self, Trump):
			if self.High == Trump:
				self.isTrump = True
			elif self.Low == Trump:
				self.isTrump = True
			else :
				self.isTrump = False

D0 = Domino(False, True, 0, 0, 0, .25)
D1 = Domino(False, False, 1, 0, 0, .25)
D2 = Domino(False, False, 2, 0, 0, .25)
D3 = Domino(False, False, 3, 0, 0, .25)
D4 = Domino(False, False, 4, 0, 0, .25)
D5 = Domino(False, False, 5, 0, 0, .25)
D6 = Domino(False, False, 6, 0, 0, .25)
D7 = Domino(False, True, 1, 1, 0, .25)
D8 = Domino(False, False, 2, 1, 0, .25)
D9 = Domino(False, False, 3, 1, 0, .25)
D10 = Domino(False, False, 4, 1, 0, .25)
D11 = Domino(False, False, 5, 1, 0, .25)
D12 = Domino(False, False, 6, 1, 0, .25)
D13 = Domino(False, True, 2, 2, 0, .25)
D14 = Domino(False, False, 3, 2, 0, .25)
D15 = Domino(False, False, 4, 2, 0, .25)
D16 = Domino(False, False, 5, 2, 0, .25)
D17 = Domino(False, False, 6, 2, 0, .25)
D18 = Domino(False, True, 3, 3, 0, .25)
D19 = Domino(False, False, 4, 3, 0, .25)
D20 = Domino(False, False, 5, 3, 0, .25)
D21 = Domino(False, False, 6, 3, 0, .25)
D22 = Domino(False, True, 4, 4, 0, .25)
D23 = Domino(False, False, 5, 4, 0, .25)
D24 = Domino(False, False, 6, 4, 0, .25)
D25 = Domino(False, True, 5, 5, 0, .25)
D26 = Domino(False, False, 6, 5, 0, .25)
D27 = Domino(False, True, 6, 6, 0, .25)

Dominos = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27]

Trump = 1

Player1 = [D0, D1, D2, D3, D4, D5, D6]
Player2 = [D7, D8, D9, D10, D11, D12, D13]
Player3 = [D14, D15, D16, D17, D18, D19, D20]
Player4 = [D21, D22, D23, D24, D25, D26, D27]


#Check for Trumps
for Domino in Dominos:
	Domino.trumpCheck(Trump)
print("Trump check done")





#print(D0.High)
#D0.printDom()
