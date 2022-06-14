print("\033c")


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

# 0 rock
# 1 paper
# 2 scissors
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if player == 0:
  print(rock)
elif player == 1:
  print(paper)
elif player ==2:
  print(scissors)



print("Computer chose:")

computer = random.randint(0,2)
print(computer)
if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
elif computer ==2:
  print(scissors)

if computer == 0 and player == 1:
  print("You win!")
elif computer == 0 and player == 2:
  print("You lose!")
elif computer == 1 and player == 0:
  print("You lose!")
elif computer == 1 and player == 2:
  print("You win!")
elif computer == 2 and player == 0:
  print("You win!")
elif computer == 2 and player == 1:
  print("You lose!")
else:
  print("Draw!")
