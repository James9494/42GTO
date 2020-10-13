class Domino():
    def __init__(self, isTrump, isDouble, High, Low, ID, Points):
    self.isTrump = isTrump    # Value to see if a trump
    self.isDouble = isDouble  # Value to test for a double
    self.High = High          # The large side of the dominoe
    self.Low = Low            # The small side of the dominoe
    self.ID = ID              # The ID representing domonies in an order
    self.Points = Points      # The value of the dominoe when adding for tricks
    
 D0 = Domino()
 D0.isTrump = False
 D0.isDouble = True
 D0.High = 0
 D0.Low = 0
 D0.ID = 0
 self.Points = .25
 print(D0.High)