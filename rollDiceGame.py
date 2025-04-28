import random

def roll():
    min_value=1
    max_value=6
    roll =random.randint(min_value, max_value)
    return roll
value =roll()
print(value)

while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<= players<=4:
            break
        else:
            print("Must Be Between 2-4 Players")
    else:
         print("Must Be Between 2-4 Players, Try Entering the number between 2-4")
print(players)
 
max_Score =50
player_Score= [0 for _ in range(players)]
print(player_Score)

while max(player_Score)< max_Score:
    for player_idx in range(players):
        print("\n Player", player_idx+1, "Turn starting now")
        current_score = 0
        while True:
            should_roll =input("Would you like to roll (y)? ")
            if should_roll.lower()!="y":
                break
            value = roll()
            if value ==1:
                print("You rolled a 1! Turn Done!")
                current_score=0
                break
                
            else:
                current_score+=value
                print("You rolled a:", value)
            print("Your Socre is :", current_score)
        player_Score[player_idx]+=current_score
        print("Your Total Score is:", player_Score[player_idx])