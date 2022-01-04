# ==================================================================================================================
# Project - TicTacToe
# ==================================================================================================================
def grid_maker(board):
    '''Prints tic tac toe grid'''
    print(f'''\n {board[0]} | {board[1]} | {board[2]}
---|---|---
 {board[3]} | {board[4]} | {board[5]}
---|---|---
 {board[6]} | {board[7]} | {board[8]}''')
def player_marker_choice():
    '''asks choice for marker, Player one Choses always'''
    player1 = input(
        "Player 1: Enter what type of marker you would like X or O: ")
    while player1.lower() not in ('o', 'x'):
        return player_marker_choice()
    player1 = player1.upper()
    player2 = 'O' if player1 == 'X' else 'X'
    print(f"Player 2: Your marker is {player2}\n")
    return player1, player2
def place_marker(board, marker_position, player_marker):
    '''places marker on board on given position'''
    board[marker_position-1] = player_marker
    grid_maker(board)
    return board
def win_check(board, marker):
    '''Check for which marker/player has won'''
    for item in range(0, 3):
        if [board[item*3], board[item*3+1], board[item*3+2]] == [marker, marker, marker]:
            return True
        if [board[item], board[item+3], board[item+6]] == [marker, marker, marker]:
            return True
    item = 0
    if [board[item], board[item+4], board[item+8]] == [marker, marker, marker]:
        return True
    if [board[item+2], board[item + 4], board[item + 6]] == [marker, marker, marker]:
        return True
    return False
def space_check(board, position):
    '''Check if position is empty to place marker on board'''
    if board[position-1].lower() in ('x', 'o'):
        return False
    return True
def full_board_check(board):
    '''Checks if game is tie or board is full'''
    count = 0
    for item in range(0, 9):
        if board[item].lower() in ('o', 'x'):
            count += 1
    return count == 9
def player_choice(board):
    '''Player tells position to place his marker'''
    player_input = input("Enter Position: ")
    if player_input > '9' or player_input < '1':
        print("Invalid Position, Enter Again\n")
        return player_choice(board)
    if space_check(board, int(player_input)):
        return int(player_input)
    else:
        print("Enter another Position as this position is filled!\n")
        return player_choice(board)
def replay():
    answer = input(f'Do you want to play again? yes or no : ')
    if answer.lower() in ('yes', 'y'):
        return True
    return False
def main():
    '''Game Initaition'''
    while True:
        x_o_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        grid_maker(x_o_list)
        p1_marker, p2_marker = player_marker_choice()

        while True:
            position1 = player_choice(x_o_list)
            x_o_list = place_marker(x_o_list, position1, p1_marker)
            if win_check(x_o_list, p1_marker):
                print(f"{p1_marker}, Has Won the Game\n")
                break

            if full_board_check(x_o_list):
                print("This Game is a Draw\n")
                break
            position2 = player_choice(x_o_list)
            x_o_list = place_marker(x_o_list, position2, p2_marker)
            if win_check(x_o_list, p2_marker):
                print(f"{p2_marker}, Has Won the Game\n")
                break
        if not replay():
            break
if __name__ == '__main__':
    main()
