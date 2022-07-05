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

#Write your code below this line 👇
value = True

while value:
    print("""
    1. Rock
    2. Paper
    3. Scissors
    4. Quit
    """)
    choice = int(input("Please choose 1, 2, 3 or 4: "))
    if choice == 1:
        print(rock)
    elif choice == 2:
        print(paper)
    elif choice == 3:
        print(scissors)
    elif choice == 4:
        value = False
        print("Thank you for playing ☺️")
        break
    else:
        print("Please enter a valid number")
        value = True
    print("\n")
    computer_choice = random.randint(1, 4)
    if computer_choice == 1:
        print(rock)
    elif computer_choice == 2:
        print(paper)
    elif computer_choice == 3:
        print(scissors)

    
    if choice == computer_choice:
        print("It's a tie!")
    elif choice == 1 and computer_choice == 2:
        print("You lose!")
    elif choice == 1 and computer_choice == 3:
        print("You win!")
    elif choice == 2 and computer_choice == 1:
        print("You win!")
    elif choice == 2 and computer_choice == 3:
        print("You lose!")
    elif choice == 3 and computer_choice == 1:
        print("You lose!")
    elif choice == 3 and computer_choice == 2:
        print("You win!")
    
    print("\n")
    print("Do you want to play again?")
    play_again = input("Y or N: ")
    if play_again == "N":
        value = False
        print("Thank you for playing ☺️")
        break