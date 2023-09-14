# Define the base class Player
class Player:
  def play (self):
    print ("The Player is playing cricket.")

#Define the derived class Batsman
class Batsman  (Player):
  def play (self):
    print  ("The batsman is batting.")

#Define the derived class bowler
class Bowler (Player):
  def play (self):
    print ("The bowler is bowling.")

#Create objects of Batsman and Bowler classes
batsman = Batsman ()
bowler  = Bowler ()

#call the play () method for each object
batsman.play ()
bowler.play ()
