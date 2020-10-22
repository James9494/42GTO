#create any function here you want to send while not messing with main.py

#HandCreation Function     *** Based on the lead domino
#Use ^^^ function above to create each hand at each phase of game
#need to know winning path and potential the indices at that point to re create when "going back"
"""
/*def CreateHand(suit, hand):
	AmountOf = 0
	DTemp = Domino(False, True, 0, 0, 0, .25)
	temp = 0
	for i in range(len(hand)):
		if hand[i].High == Suit or hand[i].Low == suit:
			AmountOf += 1
	if AmountOf = 0:
		tempArray[len(hand)]
		for i in range len(hand):
			tempArray[i] = hand[i]
	else:
		tempArray[AmountOf]
		for i in range(AmountOf):
		if hand[i].High == Suit or hand[i].Low == suit:
			tempArray[temp] = hand[i]
			temp +=1
Date 10/13/20

************************************************************************************************************************
"""

TRUMP = {
	0: [0, 1, 3, 6, 10, 15, 21],
	1: [1, 2, 4, 7, 11, 16, 22],
	2: [3, 4, 5, 8, 12, 17, 23],
	3: [6, 7, 8, 9, 13, 18, 24]
}

print(TRUMP[0])
tempArray = TRUMP[3]
print(tempArray[0])