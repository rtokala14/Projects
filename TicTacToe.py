
# Initialize the Board
board = ["_", "_", "_", 
         "_", "_", "_", 
         "_", "_", "_"]

# Initialize the players and the respective sumbols
player1 = {
    "name" : "NULL",
    "token" : "NULL"
}
player2 = {
    "name" : "NULL",
    "token" : "NULL"
}

# Function to display the current board
def display_board():
    print("")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("")

# Variable that keeps track of the status of the game
game_status = 0
    # 0 - In progress
    # 1 - Win

# Iterative function to run the game
def play_game():
    player = set_players() # Sets the player names and characters (X or O)
    turn_count = 0
    display_board()
    while turn_count < 9:
        handle_turn(player)
        display_board()
        if check_status(player):
            break
        player = switch_players(player)
        turn_count += 1
    
    if turn_count == 9:
        print("Well played. Game is a TIE.")

# Function to check if the current player won
def check_status(player):
    token = player["token"]
    if (check_rows(token) or check_cols(token) or check_diags(token)) == 1:
        print(player["name"] + " has won the game! Congratulations!!!")
        return True

    return False

def check_rows(token):
    flag = 0
    
    if (board[0] == token and board[1] == token and board[2] == token):
       flag =  1
    if (board[3] == token and board[4] == token and board[5] == token):
       flag =  1
    if (board[6] == token and board[7] == token and board[8] == token):
       flag =  1

    return flag

def check_cols(token):
    flag = 0

    if (board[0] == token and board[3] == token and board[6] == token):
        flag = 1
    if (board[1] == token and board[4] == token and board[7] == token):
        flag = 1
    if (board[2] == token and board[5] == token and board[8] == token):
        flag = 1

    return flag

def check_diags(token):
    flag = 0

    if (board[0] == token and board[4] == token and board[8] == token):
        flag = 1
    if (board[2] == token and board[4] == token and board[6] == token):
        flag = 1

    return flag

# Function to handle the current turn
def handle_turn(player):
    position = input(player["name"] + ", Choose a position from 1 - 9: ")
    while board[int(position) - 1] != "_":
        position = input("Invalid position, Choose a different one - ")
    board[int(position) - 1] = player["token"]


def switch_players(player):    
    if player["name"] == player1["name"]:
        return player2
    else:
        return player1


# Function to set the names of the players and returns the player with the first turn
def set_players():
    player1["name"] = str(input("Enter the name of the first player - "))
    player2["name"] = str(input("Enter the name of the second player - "))
    player1["token"] = str(input("Choose the token for " + player1["name"] + " (X or O) - "))

    if player1["token"] == "X":
        player2["token"] = "O"
    else:
        player2["token"] = "X"

    print("The token for " + player2["name"] + " is " + player2["token"])
    init_player = input("Who would like to go first? (1 or 2) - ")

    if init_player == "1":
        return player1
    else:
        return player2



play_game()

