# create a two-dimensional list.
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]


def main():
    print_board()
    # start game with player 1
    play_game(1)


def print_board():
    print('Printing board...')
    for i in board:
        print(i)
    print('')


def check_mark(row, col):
    if board[row][col] == '-':
        return True
    else:
        return False


def place_mark(row, col, player_id):
    if player_id == 1:
        board[row][col] = 'X'
    else:
        board[row][col] = 'O'
    print("Player " + str(player_id) + " added mark at the location " + str(row) + "," + str(col))
    if check_win():
        print("Player " + str(player_id) + " wins! Game Over!")
        quit()
    print_board()


def check_win():
    # Check rows for victory
    for row in board:
        if '-' not in row:
            if len(set(row)) == 1:
                return True
    # Check columns for victory
    if board[0][0] == board[1][0] == board[2][0] != '-':
        return True
    if board[0][1] == board[1][1] == board[2][1] != '-':
        return True
    if board[0][2] == board[1][2] == board[2][2] != '-':
        return True
    # Check diagonals for victory
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return True
    else:
        return False


def play_game(player_id):
    player_1 = True
    playerNum = player_id
    win = False
    isError = False
    while not win:
        if playerNum == 1:
            player_1 = True
        else:
            player_1 = False
        # get player input
        print('Player ' + str(playerNum) + ', make your move')
        row_one = int(input('Enter row nos (0-2):'))
        col_one = int(input('Enter col nos (0-2):'))
        # validate input or re-enter input
        if 0 <= row_one <= 2 and 0 <= col_one <= 2:
            # if you can place a mark, place it
            if check_mark(row_one, col_one):
                place_mark(row_one, col_one, playerNum)
                isError = False
                # break
            # otherwise print error and re-enter input
            else:
                print("**** Board [" + str(row_one) + "][" + str(
                    col_one) + "] has already been selected. Please choose somewhere else on the board ****")
                print("**** Invalid choice. Please mark again! ****")
                print_board()
                isError = True
        else:
            print("**** Invalid row or column. Please select row / col between values 0 to 2 ****")
            print_board()
            isError = True
        # if there is no error, switch players
        if not isError:
            if player_1:
                playerNum = 2
            else:
                playerNum = 1


main()
