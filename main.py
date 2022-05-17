import random

def score_at_end_of_round(comp_choice, player_choice):
    global comp_score
    global player_score
    if comp_choice == 1: #comp choose rock
        if player_choice == 1:
            print("Oh! its a draw!")
        elif player_choice == 3:
            print("You lose")
            comp_score += 1
        else:
            print("Yay!! you win") #if you choose paper you win
            player_score  +=1
    elif comp_choice == 2: #comp chooses paper
        if player_choice == 2:
            print("Oh! its a draw!")
        elif player_choice == 1:
            print("You lose")
            comp_score += 1
        else:
            print("Yay!! you win")#if you choose scissor you win
            player_score += 1

    elif comp_choice == 3: #comp chooses scissor
        if player_choice == 3:
            print("Oh! its a draw!")
        elif player_choice == 2:
            print("You lose")
            comp_score += 1
        else:
            print("Yay!! you win")#you choose rock you win
            player_score += 1
    return comp_score, player_score

#def who_wins():
#    comp_score, player_score = score_at_end_of_round(comp_choice, player_choice)
#    print("Scores:\n" ,"Computer Score: ",comp_score,"\n","Player Score: ", player_score)
n = int(input("How many rounds would you like to play?: "))
player_score =0
comp_score = 0    
for i in range(n):
    print("Choose Rock or Paper or Scisssor")
    Player1 = input("Your turn to choose: \o _o/: ")
    word = Player1.strip()
    Rock = ["ROCK", "Rock", "rock", "R", "r"]
    Paper = ["PAPER", "Paper","paper","p", "P"]
    Scissor = ["SCISSOR", "Scissor", "scissor", "S", "s"]
    if word in Rock:
        player_choice = 1
        print("Player's choice  : Rock")
    elif word in Paper:
        player_choice = 2
        print("Player's choice  : Paper")
    elif word in Scissor:
        player_choice = 3
        print("Player's choice  : Scissor")
    elif word not  in Rock or Paper or Scissor:
        print("Choose Rock or Paper or Scisssor")
        Player1 = input("Your turn to choose: \o _o/: ")
    comp_choice = random.randint(1,3)
    print("Computer's choice: ", end ="")
    if comp_choice == 1:
        print("Rock")
    elif comp_choice == 2:
        print("Paper")
    else:
        print("Scissor")
    score_at_end_of_round(comp_choice, player_choice)
    print("====End of Round",i,"====")
#who_wins()
print("Scoreboard:\n" ,"Computer Score: ",comp_score,"\n","Player Score: ", player_score)
print("-----GAME OVER! -----")
if comp_score > player_score:
    print("You lost the game!!")
elif player_score > comp_score:
    print("You win this game!!")
else:
    print("It's a draw! ")
        
        