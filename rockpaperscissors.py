from random import randint

player = input ("rock (r), paper (p), or scissors (s)?")

chosen = randint(1,3)
if chosen == 1:
	computer = "r"
elif chosen == 2:
	computer = "p"
else:
	computer = "s"

print (player, "vs", computer)

if player == computer:
	print ("DRAW")
elif player == "r" and computer == "s":
	print ("Player Wins!")
elif player == "r" and computer == "p":
	print ("Computer Wins!")
elif player == "p" and computer == "r":
	print ("Player Wins!")
elif player == "p" and computer == "s":
	print ("Computer Wins!")
elif player == "s" and computer == "p":
	print ("Player Wins!")
elif player == "s" and computer == "r":
	print ("Computer Wins!")