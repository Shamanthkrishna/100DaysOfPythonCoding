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
list1=["rock","paper","scissors"]
while True:
    user=int(input("What do you chose? Type 0 for Rock, 1 for Paper and 2 for Scissors:\n"))
    pc=int(random.randint(0,2))
    print("You chose "+ list1[user])
    if list1[user]=='rock':
        print(rock)
    elif list1[user]=='paper':
        print(paper)
    elif list1[user]=='scissors':
        print(scissors)

    print("Computer chose "+ list1[pc])
    if list1[pc]=='rock':
        print(rock)
    elif list1[pc]=='paper':
        print(paper)
    elif list1[pc]=='scissors':
        print(scissors)


    if user == pc:
        print("It's a Tie")
    elif (user==0 and pc==1) or (user==1 and pc==2) or (user==2 and pc==0):
        print("Computer wins!!")
    else:
        print("You win!!")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again!='y':
        break