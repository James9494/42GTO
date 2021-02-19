import csv
#create any function here you want to send while not messing with main.py

#HandCreation Function     *** Based on the lead domino
#Use ^^^ function above to create each hand at each phase of game
#need to know winning path and potential the indices at that point to re create when "going back"

# TODO
# Find a way to calculate the amount of possibilites per a dominoe played. One round at a time
#    -  Say the First dominoe is played by player 1, player 2 could have 3 valid, player 3 could have 2, and player 4 has 7
#       This could lead to an combinaiton of 1,3,2,7 with: 1,1,1,1, ... 1,2,1,1 ... 1,2,1,2  ... 1,2,1,3 ... 1,2,1,4 ... until all are made
# 		Information needed to find after is who wins and with what dominoe. EX: 1,2,1,1,2(Player 2 won)
#		Next run the information out to a CSV and then run it again for round 2 with the information previous
#		Function needed Round(Domino P1[], Dominoe P2[], Dominoe P3[], Dominoe P4[], int winner, int WinningDominoe)
#
#		CSV EXAMPLE
#		ROUND 1,Player possibilities, Player 2 possibilities, Player 3 possibilites, Player 4 possibilites
#
#		Round 1, Player 1, Player 2, Player 3, Player 4, Winner (1-4)
#		Round 2 Possiblities
#		Round 2, Playe 1, Player 2, Player 3, Player 4, Winner(1-4)
#		Round 3 Possibliites
#		.
#		.
#		.
#		Round 6 Possiblities
#		Round 6, Player 1, Player 2, Player 3, Player 4, Winner(1-4)
#		Round 7, Player 1, Player 2, Player 3, Player 4, Winner(1-4)
#		Round 1, ETC
#		Round 2 Possiblites

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


TestArray = [[1, 2, 3, 4, 1],
			 [1, 2, 3, 4, 4]
			 [1, 2, 3, 4, 2]]
with open('test.csv', 'w', newline = '') as file:
	write = csv.writer(file)
	write.writerow(["Test 1", "Test 2", "Test 3"])
	write.writerows(TestArray)
