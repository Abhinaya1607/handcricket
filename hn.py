import random

def play_hand_cricket():
    print("Welcome to Hand Cricket!")
    print("Enter a number between 1 and 6 to bat, u are player1.And ur device is player2 is playing against you, both the scores are going to be comapred.")
    
    player1_score = 0
    player2_score = 0
    
    while True:
        player1_runs = int(input("Your turn to bat: "))
        player2_runs = random.randint(1, 6)
        
        print("player2's turn to bat: " + str(player2_runs))
        
        if player1_runs < 1 or player1_runs > 6:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue
        
        if player1_runs == player2_runs:
            print("You're out!")
            break
        
        player1_score += player1_runs
        player2_score += player2_runs
        
        print(" your current score: " + str(player1_score))
        print("device's current score: " + str(player2_score))
        print("-------------")
    
    print("Game Over")
    print("Your total score: " + str(player1_score))
    print("Computer's total score: " + str(player2_score))
    
    if player1_score < player2_score:
         print("You lost. Better luck next time!")
    elif player1_score > player2_score:
       
        print("Hurray! You won!")
    else:
        print("It's a tie!")

play_hand_cricket()