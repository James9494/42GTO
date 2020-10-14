create any function here you want to send while not messing with main.py

HandCreation Function     *** Based on the lead domino
Use ^^^ function above to create each hand at each phase of game
need to know winning path and potential the indices at that point to re create when "going back"

def CreateHand(suit, hand):
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