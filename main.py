from random import randint

print("Nhap Dam, La, Keo: ")
player = input()
computer = randint(0,2)

if computer == 0:
	computer = "Dam"
if computer == 1:
	computer = "La"
if computer == 2:
	computer = "Keo"

print("----")
print("You choose: " + player)
print("Computer chooses: " + computer)
print("----")

if player == computer:
	print("Draw")
else:
	if player == "Keo":
		if computer == "Dam":
			print("You Lose")
		else:
			print("You Win")

	elif player =="La":
		if computer == "Keo":
			print("You Lose")
		else:
			print("You Win")

	elif player =="Dam":
		if computer == "La":
			print("You Lose")
		else:
			print("You Win")

	else:
		print("Chi nhap Dam, La, Keo")