board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]


def player_one_move():
    try:
        player_one_row = int(input("Player One... choose a row (0-2): "))
        player_one_column = int(input("Player One... choose a column (0-2): "))
        if board[player_one_row][player_one_column] != '_':
            print("Space already occupied! Please try again.")
            player_one_move()
        else:
            board[player_one_row][player_one_column] = "X"
            print_board()
            if check_victory():
                print("Player One Wins!")
            elif check_tie():
                print("No more available moves. It's a tie!")
            else:
                player_two_move()
    except:
        print("Invalid entry! Please try again.")
        player_one_move()


def player_two_move():
    try:
        player_two_row = int(input("Player Two... choose a row (0-2): "))
        player_two_column = int(input("Player Two... choose a column (0-2): "))
        if board[player_two_row][player_two_column] != '_':
            print("Space already occupied! Please try again.")
            player_two_move()
        else:
            board[player_two_row][player_two_column] = "O"
            print_board()
            if check_victory():
                print("Player Two Wins!")
            elif check_tie():
                print("No more available moves. It's a tie!")
            else:
                player_one_move()
    except:
        print("Invalid entry! Please try again.")
        player_two_move()


def print_board():
    for i in board:
        print(i)

def main():
    print_board()
    player_one_move()

main()
