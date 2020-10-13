class Dominoe():
    def __init__(self, isTrump, isDouble, High, Low, ID, Points):
    self.isTrump = isTrump    # Value to see if a trump
    self.isDouble = isDouble  # Value to test for a double
    self.High = High          # The large side of the dominoe
    self.Low = Low            # The small side of the dominoe
    self.ID = ID              # The ID representing domonies in an order
    self.Points = .25         # The value of the dominoe when adding for tricks