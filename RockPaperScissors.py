"""Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a
message of congratulations to the winner, and ask if the players want to
start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
def winner(user1, user2):
    if user1 == user2:
        return "Tied"
    else:
        if user1 == "rock":
            if user2 == "scissors":
                return "user1"
            else:
                return "user2"
        elif user1 == "scissors":
            if user2 == "rock":
                return "user2"
            else:
                return "user1"
        else:
            if user2 == "scissors":
                return "user2"
            else:
                return "user1"

while True:
    user1Name = input("Enter player1 name : ")
    user2Name = input("Enter player2 name : ")
    while True:
        user1Role = (input("Enter the role for {} (Rock/Scissors/Paper): ".format(user1Name))).lower()
        if user1Role in ('rock', 'scissors','paper'):
            break
    while True:
        user2Role = (input("Enter the role for {} (Rock/Scissors/Paper): ".format(user2Name))).lower()
        if user2Role in ('rock', 'scissors','paper'):
            break
    game = winner(user1Role,user2Role)
    if game == "Tied":
        print ("{} ties with {}".format(user1Name,user2Name))
    elif game == "User1":
        print ("{} is the winner".format(user1Name))
    else:
        print ("{} is the winner".format(user2Name))

    choice = input("Do you want to play another game (Y/N)")
    if choice in ("nNNoNO"):
        print ("******* Thank You for playing ROCK-SCISSOR-PAPER game. Please come again ******")
        break
