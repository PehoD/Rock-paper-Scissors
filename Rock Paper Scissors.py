import random
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

all = [rock, paper, scissors]
choice = int (input("hat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
print(all[choice])



print("Computer choose: \n")
random_choose = random.randint(0,2)

print(all[random_choose])

if random_choose >= 3 or choice < 0:
    print("You typed an invalid number. You lose!")
elif choice == 0 and random_choose == 2:
    print("You win!")
elif random_choose == 0 and choice == 2:
    print("You lose!")
elif random_choose > choice:
    print("You lose!")
elif choice > random_choose:
    print("You win!")
elif random_choose == choice:
    print("It's a draw!")

