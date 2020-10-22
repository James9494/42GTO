#  This function will return the winning domino


def trickWinner(d0, d1, d2, d3, dLead, trump):  #  dLead is the first person who is leading a DOM and the next 3 are the 3 ppl to their left in order
	#  Default values to be changed

	dom0Val = 0
	dom1Val = 0
	dom2Val = 0
	dom3Val = 0   # default values to be used if no trump present in hand
	winner = 99  #  this will be set to which person one, 0 - 3
	# dWinner = Domino(False,False,0,0,0,0)  #  creating a domino that will be changed later (FIXME Breaks the program) (TODO)
	leadSuit = 0
	points = 0.0  # this will be changed soon to be the points per each trick and returned at end


	# Actual Code


	# Add points
	points = d0.Points + d1.Points + d2.Points + d3.Points
	
	# set lead value
	if(dLead.isTrump):        #  Check if lead Domino is a trump
		leadSuit = trump      #  if trump set lead domino to the trump value
	if(not dLead.isTrump):       #  Check if not trump
		leadSuit = dLead.High #  set the value of lead suit to the high value
	
	#  if double and trump
	if(d0.isTrump and d0.isDouble):       #  if dom d0 is both trump and double it cannot lose
		winner = 0
		dWinner = d0
		return winner, dWinner, points
	elif(d1.isTrump and d1.isDouble):     #  if dom d1 is both trump and double it cannot lose
		winner = 1
		dWinner = d1
		return winner, dWinner, points
	elif(d2.isTrump and d2.isDouble):     #  if dom d2 is both trump and double it cannot lose
		winner = 2
		dWinner = d2
		return winner, dWinner, points
	elif(d3.isTrump and d3.isDouble):     #  if dom d3 is both trump and double it cannot lose
		winner = 3
		dWinner = d3
		return winner, dWinner, points
	#  if only 1 trump
	if(d0.isTrump and not d1.isTrump and not d2.isTrump and not d3.isTrump):     #  if d0 is the only trump it wins
		winner = 0
		dWinner = d0
		return winner, dWinner, points
	elif(not d0.isTrump and d1.isTrump and not d2.isTrump and not d3.isTrump):   #  if d1 is the only trump it wins
		winner = 1
		dWinner = d1
		return winner, dWinner, points
	elif(not d0.isTrump and not d1.isTrump and d2.isTrump and not d3.isTrump):   #  if d2 is the only trump it wins
		winner = 2
		dWinner = d2
		return winner, dWinner, points
	elif(not d0.isTrump and not d1.isTrump and not d2.isTrump and d3.isTrump):   #  if d3 is the only trump it wins
		winner = 3
		dWinner = d3
		return winner, dWinner, points
	
	#  if 2 trump
	if(d0.isTrump and d1.isTrump and not d2.isTrump and not d3.isTrump):  #  if d0 and d1 doms are trump compare by ID
		if(d0.ID > d1.ID):    #  
			winner = 0
			dWinner = d0
			return winner, dWinner, points
		elif(d1.ID > d0.ID):    #  
			winner = 1
			dWinner = d1
			return winner, dWinner, points
	if(d0.isTrump and not d1.isTrump and d2.isTrump and not d3.isTrump):  #  if d0 and D2 doms are trump compare by ID
		if(d0.ID > d2.ID):    #  
			winner = 0
			dWinner = d0
			return winner, dWinner, points
		elif(d2.ID > d0.ID):    #  
			winner = 2
			dWinner = d2
			return winner, dWinner, points
	if(d0.isTrump and not d1.isTrump and not d2.isTrump and d3.isTrump):  #  if d0 and D3 doms are trump compare by ID
		if(d0.ID > d1.ID):    #  
			winner = 0
			dWinner = d0
			return winner, dWinner, points
		elif(d3.ID > d0.ID):    #  
			winner = 3
			dWinner = d3
			return winner, dWinner, points
	if(not d0.isTrump and d1.isTrump and d2.isTrump and not d3.isTrump):  #  if d1 and D2 doms are trump compare by ID
		if(d1.ID > d2.ID):    #  
			winner = 0
			dWinner = d0
			return winner, dWinner, points
		elif(d2.ID > d1.ID):    #  
			winner = 1
			dWinner = d1
			return winner, dWinner, points
	if(not d0.isTrump and d1.isTrump and not d2.isTrump and d3.isTrump):  #  if d1 and D3 doms are trump compare by ID
		if(d1.ID > d3.ID):    #  
			winner = 1
			dWinner = d1
			return winner, dWinner, points
		elif(d3.ID > d1.ID):    #  
			winner = 3
			dWinner = d3
			return winner, dWinner, points
	if(not d0.isTrump and not d1.isTrump and d2.isTrump and d3.isTrump):  #  if d2 and D3 doms are trump compare by ID
		if(d2.ID > d3.ID):    #  
			winner = 2
			dWinner = d2
			return winner, dWinner, points
		elif(d3.ID > d2.ID):    #  
			winner = 3
			dWinner = d3
			return winner, dWinner, points
	#  if 3 trump
	if(d0.isTrump and d1.isTrump and d2.isTrump and not d3.isTrump):  #  if d0 and d1 and d2 are trump
		if(d0.ID > d1.ID and d0.ID > d2.ID):    #  
			winner = 0
			dWinner = d0
			return winner, dWinner, points
		elif(d1.ID > d0.ID and d1.ID > d2.ID):    #  
			winner = 1
			dWinner = d1
			return winner, dWinner, points
		elif(d2.ID > d1.ID and d2.ID > d0.ID):    #  
			winner = 2
			dWinner = d2
			return winner, dWinner, points
	if(d0.isTrump and d1.isTrump and not d2.isTrump and d3.isTrump):  #  if d0 and d1 and d3 are trump
		if(d0.ID > d1.ID and d0.ID > d2.ID):    #  
			winner = 0
			dWinner = d0
			return winner, dWinner, points
		elif(d1.ID > d0.ID and d1.ID > d2.ID):    #  
			winner = 1
			dWinner = d1
			return winner, dWinner, points
		elif(d2.ID > d1.ID and d2.ID > d0.ID):    #  
			winner = 3
			dWinner = d3
			return winner, dWinner, points
	if(d0.isTrump and not d1.isTrump and d2.isTrump and d3.isTrump):  #  if d0 and d2 and d3 are trump
		if(d0.ID > d1.ID and d0.ID > d2.ID):    #  
			winner = 0
			dWinner = d0
			return winner, dWinner, points
		elif(d1.ID > d0.ID and d1.ID > d2.ID):    #  
			winner = 2
			dWinner = d2
			return winner, dWinner, points
		elif(d2.ID > d1.ID and d2.ID > d0.ID):    #  
			winner = 3
			dWinner = d3
			return winner, dWinner, points
	if(not d0.isTrump and d1.isTrump and d2.isTrump and d3.isTrump):  #  if d1 and d2 and d3 are trump
		if(d0.ID > d1.ID and d0.ID > d2.ID):    #  
			winner = 1
			dWinner = d1
			return winner, dWinner, points
		if(d1.ID > d0.ID and d1.ID > d2.ID):    #  
			winner = 2
			dWinner = d2
			return winner, dWinner, points
		if(d2.ID > d1.ID and d2.ID > d0.ID):    #  
			winner = 3
			dWinner = d3
			return winner, dWinner, points

	#  if 4 trump
	if(d0.isTrump and d1.isTrump and d2.isTrump and d3.isTrump):    #  if all doms are trump compare by ID
		if(d0.ID > d1.ID and d0.ID > d2.ID and d0.ID > d3.ID):      #  if d0 is greater than all return d0
			winner = 0
			dWinner = d0
			return winner, dWinner, points
		elif(d1.ID > d0.ID and d1.ID > d2.ID and d1.ID > d3.ID):    #  if d1 is greater than all return d0
			winner = 1
			dWinner = d1
			return winner, dWinner, points
		elif(d2.ID > d1.ID and d2.ID > d0.ID and d2.ID > d3.ID):    #  if d2 is greater than all return d0
			winner = 2
			dWinner = d2
			return winner, dWinner, points
		elif(d3.ID > d1.ID and d3.ID > d2.ID and d3.ID > d0.ID):    #  if d3 is greater than all return d0
			winner = 3
			dWinner = d3
			return winner, dWinner, points
	#  if no trump
	
	if not d0.isTrump and not d1.isTrump and not d2.isTrump and not d3.isTrump:   #  if no trump
		

	#  if no trump and anyone plays a double matching suit
		if d0.isDouble and d0.High == leadSuit:
			winner = 0
			dWinner = d0
			return winner, dWinner, points
		if d1.isDouble and d1.High == leadSuit:
			winner = 1
			dWinner = d1
			return winner, dWinner, points
		if d2.isDouble and d2.High == leadSuit:
			winner = 2
			dWinner = d2
			return winner, dWinner, points
		if d3.isDouble and d3.High == leadSuit:
			winner = 3
			dWinner = d3
			return winner, dWinner, points

	#  if no trump and no double and no 
		if(d0.High == leadSuit):          #  if d0 high = lead then set d0 low as val
			dom0Val = d0.Low
		elif(d0.Low == leadSuit):     #  if d0 low = lead then set d0 high as val
			dom0Val = d0.High
		else:                         #  if not lead suit then set 0
			dom0Val = 0

		if(d1.High == leadSuit):      #  if d0 high = lead then set d0 low as val
			dom1Val = d1.Low
		elif(d1.Low == leadSuit):     #  if d0 low = lead then set d0 high as val
			dom1Val = d1.High
		else:                         #  if not lead suit then set 0
			dom1Val = 0 

		if(d2.High == leadSuit):     #  if d0 high = lead then set d0 low as val
			dom2Val = d2.Low
		elif(d0.Low == leadSuit):    #  if d0 low = lead then set d0 high as val
			dom2Val = d2.High 
		else:                        #  if not lead suit then set 0
			dom2Val = 0

		if(d3.High == leadSuit):     #  if d0 high = lead then set d0 low as val
			dom3Val = d3.Low
		elif(d3.Low == leadSuit):    #  if d0 low = lead then set d0 high as val
			dom3Val = d3.High
		else:                        #  if not lead suit then set 0
			dom3Val = 0
		if(dom0Val > dom1Val and dom0Val > dom2Val and dom0Val > dom3Val):
			winner = 0
			dWinner = d0
			return winner, dWinner, points
		elif(dom1Val > dom2Val and dom1Val > dom3Val):
			winner = 1
			dWinner = d1
			return winner, dWinner, points
		elif(dom2Val > dom3Val):
			winner = 2
			dWinner = d2
			return winner, dWinner, points
		else:
			winner = 3
			dWinner = d3
			return winner, dWinner, points


	else:
		print("Error in trickWinner Function")