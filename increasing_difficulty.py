import random
choices = ["rock", "paper", "scissor"]
track_rock, track_paper, track_scissor = 0,0,0
comp_score, player_score = 0, 0

no_of_rounds = int(input("How many rounds do you want to play?"))
print("Let's begin the game of Rock, Paper and Scissors \(^_^)/ "+"\n") 
for i in range(no_of_rounds):

    #Player chooses
    player_choice = input("Choose your move: ")
    while player_choice not in choices:
        print(choices)
        player_choice = input("Please choose an apprpriate move: "+" \n")      
    if player_choice == choices[0]:
        track_rock += 1
    elif player_choice == choices[1]:
        track_paper += 1
    elif player_choice == choices[2]:
        track_scissor += 1

    #Computer chooses
    if track_rock + track_paper + track_scissor == 0:
        comp_choice = random.randint(0,2)
    elif track_rock > track_paper and track_rock > track_scissor:
        comp_choice = 1
    elif track_paper > track_scissor and track_paper > track_rock:
        comp_choice = 2
    elif track_scissor > track_rock and track_scissor > track_paper:
        comp_choice = 0
    else:
        comp_choice = random.randint(0,2)
    #print(track_rock, track_paper, track_scissor)
    print("Computer's move: ",choices[comp_choice]) 

    #who wins this round?
    if abs(choices.index(player_choice)-comp_choice)==1:
        if comp_choice > choices.index(player_choice):
            print("Oops, You lose!!")
            comp_score += 1
        else:
            print("You have won this round!")
            player_score += 1
    elif abs(choices.index(player_choice)-comp_choice)==2:
        if comp_score < choices.index(player_choice):
            print("You have lost this round!")
            comp_score += 1
        else:
            print("Yay, You win!!")
            player_score += 1
    else:
        print("It's a draw!")
        
#Who wins the game?
print("Scoreboard:\n" ,"Computer Score: ",comp_score,"\n","Player Score: ", player_score)
print("-----GAME OVER! -----")
if comp_score > player_score:
    print("You lost the game!!")
elif player_score > comp_score:
    print("You win this game!!")
else:
    print("It's a draw! ")