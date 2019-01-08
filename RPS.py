import time 
import random



print("Rock")
print()
time.sleep(1)

print("Paper")
time.sleep(1)
print()

print("Scissors")
time.sleep(1)
print()

print("says")
time.sleep(1)
print()

print("Shoot")
time.sleep(1)
print()

choice = input("")

computer_choice = random.randint(1,3)

if computer_choice == 1:
	computer_choice = 'Rock'
	print("Rock")
elif computer_choice == 2:
	computer_choice = 'Paper'
	print("Paper")
else:
	computer_choice = 'Scissors'
	print("Scissors")


if choice == "Rock" and computer_choice == "Scissors":
	print("You Win!")
elif choice == "Scissors" and computer_choice == "Paper":
	print("You Win!")
elif choice == "Paper" and computer_choice== "Rock":
	print("You Win!")
elif choice == "Scissors" and computer_choice == "Scissors":
	print("Game tied!")
elif choice == "Rock" and computer_choice == "Rock":
	print("Game tied!")
elif choice == "Paper" and computer_choice == "Paper":
	print("Game tied!")
else:
	print("You Lose!")











 
