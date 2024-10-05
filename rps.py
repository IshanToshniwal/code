import random #random rock paper scissors
options = ("rock", "paper", "scissors")
player_name = input('Enter your name: ')
player_score = 0
computer_score = 0
print(player_name + ' we will play a game of rock paper scissors')
no_of_plays = 0

while no_of_plays < 10:
    if no_of_plays > 10:
        break
    comp_choice = random.choice(options)
    player_choice = input("!rock paper scissors!: ")
    player_choice = player_choice.lower()
    no_of_plays += 1
    print('you choose ' + player_choice)
    print('computer choose ' + comp_choice)

    if player_choice == comp_choice:
        print('it is a tie!')
        print('your score is ' + str(player_score))
        print('computer score is ' + str(computer_score))
        print(no_of_plays)

    elif (player_choice == "paper" and comp_choice == "rock") or (player_choice == "scissors" and comp_choice == "paper") or (player_choice == "rock" and comp_choice == "scissors"):
        print('you win!')
        player_score += 1
        print('computer score is ' + str(computer_score))
        print('your score is ' + str(player_score))
        print(no_of_plays)

    else:
        print('computer wins (-_-)')
        computer_score += 1
        print('computer score is ' + str(computer_score))
        print('your score is ' + str(player_score))
        print(no_of_plays)

print("your score is " + str(player_score))
print("computer score is " + str(computer_score))
if computer_score > player_score:
    print("finally computer wins (-_-)")

if computer_score == player_score:
    print('it is a tie!')

else:
    print("finally player wins!")
if (player_score == 1) or (player_score == 2) or (player_score == 3):
    print("very bad you can do better")
elif (player_score == 4) or (player_score == 5) or (player_score == 6):
    print("bad but can do better")
elif (player_score == 7) or (player_score == 8) or (player_score == 9) or (player_score == 10):
    print("very good")
elif (computer_score == 1) or (computer_score == 2) or (computer_score == 3):
    print("bad")
elif (computer_score == 4) or (computer_score == 5) or (computer_score == 6):
    print('very bad')
elif (computer_score == 7) or (computer_score == 8) or (computer_score == 9) or (computer_score == 10):
    print("super bad")