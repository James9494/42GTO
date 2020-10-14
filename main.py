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

Dominos = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27]

Suit = 0

Trump = 2

P0 = 0.0
P1 = 0.0
P2 = 0.0
P3 = 0.0

Player0 = [D0, D1, D2, D3, D4, D5, D6]
Player1 = [D7, D8, D9, D10, D11, D12, D13]
Player2 = [D14, D15, D16, D17, D18, D19, D20]
Player3 = [D21, D22, D23, D24, D25, D26, D27]

Player = [Player0, Player1, Player2, Player3]

#Player Scores
PS = [P0, P1, P2, P3]

#Domino played by each player
Play0 = D0
Play1 = D0
Play2 = D0
Play3 = D0

#Check for Trumps
for Domino in Dominos:
	Domino.trumpCheck(Trump)
print("Trump check done")


#Player Picks Trump (TODO)

#Player Picks First Domino
for a in range(7):
	Suit = Player0[a].High
	Play0 = Player0[a]

#Player 1 picks
	for b in range(7):
		if Player1[b].High == Suit or Player1[b].Low == Suit:
			if Player1[b].isPlayed == False:
				Play1 = Player1[b]
				Player1[b].isPlayed = True
				break
			else:
				continue
		elif Player1[b].isPlayed == False:
			Play1 = Player1[b]
			Player1[b].isPlayed = True
			break
		else:
			continue

#Player 2 Picks				
	for b in range(7):
		if Player2[b].High == Suit or Player2[b].Low == Suit:
			if Player2[b].isPlayed == False:
				Play2 = Player2[b]
				Player2[b].isPlayed = True
				break
			else:
				continue
		elif Player2[b].isPlayed == False:
			Play2 = Player2[b]
			Player2[b].isPlayed = True
			break
		else:
			continue
			
#Player 3 Picks
	for b in range(7):
		if Player3[b].High == Suit or Player3[b].Low == Suit:
			if Player3[b].isPlayed == False:
				Play3 = Player3[b]
				Player3[b].isPlayed = True
				break
			else:
				continue
		elif Player3[b].isPlayed == False:
			Play3 = Player3[b]
			Player3[b].isPlayed = True
			break
		else:
			continue
	
	
#Score first round	
	if Play0.High == Trump and Play0.Low == Trump:
		PS[0] += Play0.Points
		PS[2] += Play2.Points
	elif Play1.High == Trump and Play1.Low == Trump:
		PS[1] += Play1.Points
		PS[3] += Play3.Points
	elif Play2.High == Trump and Play2.Low == Trump:
		PS[2] += Play2.Points
		PS[0] += Play0.Points
	elif Play3.High == Trump and Play3.Low == Trump:
		PS[2] += Play3.Points
		PS[0] += Play1.Points
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	




print(str(PS[0]) + " " + str(PS[1]) + " " + str(PS[2]) + " " + str(PS[3]))

#print(D0.High)
#D0.printDom()
