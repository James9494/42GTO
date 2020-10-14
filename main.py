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
				
def CreateHand(suit, hand):
	AmountOf = 0
	temp = 0
	for i in range(len(hand)):
		if hand[i].High == suit or hand[i].Low == suit:
			AmountOf += 1
	if AmountOf == 0:
		tempArray = [D0] * (len(hand) - hand.count(D99))
		for i in range(len(hand)):
			tempArray[i] = hand[i]
	else:
		tempArray = [D0] * AmountOf
		for i in range(AmountOf):
			if hand[i].High == suit or hand[i].Low == suit:
				tempArray[temp] = hand[i]
				temp +=1
#	print(str(len(tempArray)))
	return tempArray
	
def Score(d0, d1, d2, d3, trump):
	if d0.Low == trump and d0.High == trump:
		PS[0] += d0.Points + d1.Points + d2.Points + d3.Points
		Won0()
	elif d1.Low == trump and d1.High == trump:
		Won1()
	elif d2.Low == trump and d2.High == trump:
		PS[0] += d0.Points + d1.Points + d2.Points + d3.Points
		Won2()
	elif d3.Low == trump and d3.High == trump:
		Won3()
	elif d0.Low == trump and d1.High != trump and d1.Low != trump and d2.High != trump and d2.Low != trump and d3.High != trump and d3.Low != trump:
		PS[0] += d0.Points + d1.Points + d2.Points + d3.Points
		Won0()
	elif d0.High == trump and d1.High != trump and d1.Low != trump and d2.High != trump and d2.Low != trump and d3.High != trump and d3.Low != trump:
		PS[0] += d0.Points + d1.Points + d2.Points + d3.Points
		Won0()
	elif d1.Low == trump and d0.High != trump and d0.Low != trump and d2.High != trump and d2.Low != trump and d3.High != trump and d3.Low != trump:
		Won1()
	elif d1.High == trump and d0.High != trump and d0.Low != trump and d2.High != trump and d2.Low != trump and d3.High != trump and d3.Low != trump:
		Won1()
	elif d2.Low == trump and d1.High != trump and d1.Low != trump and d0.High != trump and d0.Low != trump and d3.High != trump and d3.Low != trump:
		PS[0] += d0.Points + d1.Points + d2.Points + d3.Points
		Won2()
	elif d2.High == trump and d1.High != trump and d1.Low != trump and d0.High != trump and d0.Low != trump and d3.High != trump and d3.Low != trump:
		PS[0] += d0.Points + d1.Points + d2.Points + d3.Points
		Won2()
	elif d3.low == trump and d1.High != trump and d1.Low != trump and d2.High != trump and d2.Low != trump and d0.High != trump and d0.Low != trump:
		Won3()
	elif d3.High == trump and d1.High != trump and d1.Low != trump and d2.High != trump and d2.Low != trump and d0.High != trump and d0.Low != trump:
		Won3()


def Won0():
	
	for a in range(len(Player0)):
		if Player0[a] == D99:
			continue
		if len(Player0) == 0:
			break
		if Player0[a].High == Trump or Player0[a].Low == Trump:
			Suit = Trump
		else:
			Suit = Player0[a].High
	
		Playable0 = CreateHand(Suit, Player0)
		Playable1 = CreateHand(Suit, Player1)
		Playable2 = CreateHand(Suit, Player2)
		Playable3 = CreateHand(Suit, Player3)
#		print(str(len(Playable1)))
	
		for b in range(len(Playable1)):
			for c in range(len(Playable2)):
				for d in range(len(Playable3)):
					Play0 = Player0[a]
					Play1 = Playable1[b]
					Play2 = Playable2[c]
					Play3 = Playable3[d]
					Player0[a] = D99
					Playable1[b] = D99
					Playable2[c] = D99
					Playable3[d] = D99
					Score(Play0, Play1, Play2, Play3, Trump)

def Won1():
	i = 0
	
def Won2():
	i = 0	
	
def Won3():
	i = 0
	
	
	
	

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
D99 = Domino(False, False, 99, 99, 99, 0)

Dominos = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27]

Suit = 0

Trump = 6

P0 = 0.0
P1 = 0.0
P2 = 0.0
P3 = 0.0

Player0 = [D27, D26, D21, D12, D7, D2, D3]       #6/6  6/5  3/6  1/6  1/1  0/2  0/3
Player1 = [D25, D22, D15, D10, D11, D6, D24]     #5/5  4/4  2/4  1/4  1/5  0/6  4/6
Player2 = [D23, D20, D0, D1, D8, D18, D14]       #4/5  3/5  0/0  0/1  1/2  3/3  2/3
Player3 = [D4, D5, D9, D13, D16, D17, D19]       #0/4  0/5  1/3  2/5  2/2  2/6  3/4



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
	
for a in range(len(Player0)):
	if Player0[a].High == Trump or Player0[a].Low == Trump:
		Suit = Trump
	else:
		Suit = Player0[a].High
	
	Playable0 = CreateHand(Suit, Player0)
	Playable1 = CreateHand(Suit, Player1)
	Playable2 = CreateHand(Suit, Player2)
	Playable3 = CreateHand(Suit, Player3)
#	print(str(len(Playable1)))
	
	for b in range(len(Playable1)):
		for c in range(len(Playable2)):
			for d in range(len(Playable3)):
				Play0 = Player0[a]
				Play1 = Playable1[b]
				Play2 = Playable2[c]
				Play3 = Playable3[d]
				Player0[a] = D99
				Playable1[b] = D99
				Playable2[c] = D99
				Playable3[d] = D99
				Score(Play0, Play1, Play2, Play3, Trump)
	
	
	
	


#ps0 = team 1 ps1 = team 2

print(str(PS[0]) + " " + str(PS[1]) + " " + str(PS[2]) + " " + str(PS[3]))

#print(D0.High)
#D0.printDom()
