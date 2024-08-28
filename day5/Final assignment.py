import random

rock = ''' 
     _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper ='''
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

game = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
print("Welcome to the Rock Paper & Scissors game")
user_choice = int(input("Let ppay!\nWhat do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors: "))

# Logic
if user_choice ==  computer_choice:
    print(f"You choose {user_choice}:\n" + game[user_choice])
    print("The computer\n:" + game[computer_choice])
    print("<<<<< That is a draw  >>>>>")
elif user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1 :
    print(f"You choose {user_choice}:\n" + game[user_choice])
    print("The computer\n:" + game[computer_choice])
    print("<<<<< You win!  >>>>>")
else:
    print(f"You choose {user_choice}:\n" + game[user_choice])
    print("The computer\n:" + game[computer_choice])  
    print("<<<<< You lose!  >>>>>")





