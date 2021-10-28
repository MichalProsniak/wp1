import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    Player_score = 0
    Computer_score = 0
    #number_of_tries = 0
    print("Rock, paper, scissors game - player vs computer to 3 wins. GL & HF")


    while Computer_score < 3 and Player_score < 3:
        computer_choice = random.choice(choices)
        #print(computer_choice)
        print ("Chose rock/paper/scissors")
        guess = str(input())
        #number_of_tries += 1
        

        

        if computer_choice == guess:
            print("Computer chose ", computer_choice)
            print("Draw")
            print("Computer score: ", Computer_score)
            print("Your score: ", Player_score)
            #number_of_tries -= 1
        

        elif computer_choice == "rock" and guess == "paper":
            print("Computer chose ", computer_choice)
            print("You won")
            Player_score += 1
            print("Computer score: ", Computer_score)
            print("Your score: ", Player_score)
        
        

        elif computer_choice == "rock" and guess == "scissors":
            print("Computer chose ", computer_choice)
            print("Computer won")
            Computer_score += 1 
            print("Computer score: ", Computer_score)
            print("Your score: ", Player_score)
        
        
    
        elif computer_choice == "paper" and guess == "rock":
            print("Computer chose ", computer_choice)
            print("Computer won")
            Computer_score += 1 
            print("Computer score: ", Computer_score)
            print("Your score: ", Player_score)
        
        

        elif computer_choice == "paper" and guess == "scissors":
            print("Computer chose ", computer_choice)
            print("You won")
            Player_score += 1
            print("Computer score: ", Computer_score)
            print("Your score: ", Player_score)
        

        elif computer_choice == "scissors" and guess == "paper":
            print("Computer chose ", computer_choice)
            print("Computer won")
            Computer_score += 1 
            print("Computer score: ", Computer_score)
            print("Your score: ", Player_score)
        
        

        elif computer_choice == "scissors" and guess == "rock":
            print("Computer chose ", computer_choice)
            print("You won")
            Player_score += 1 
            print("Computer score: ", Computer_score)
            print("Your score: ", Player_score)
        
        

    if Player_score == 3:
        print("Congratulations - you won the game")
        
    

    elif Computer_score == 3:
        print("You lost - computers are to smart for people")
    



if __name__ == "__main__":
    next_game = True
    while next_game: 
        rock_paper_scissors()
        next_time_input = input("Do you want to play next time? y/n")
        if next_time_input == 'n':
            next_game = False

    


    
