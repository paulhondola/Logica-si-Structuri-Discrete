def print_board(board):
    print('\n'.join([' '.join(row) for row in board]))

def check_win(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True
    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False

def handle_move(board, player):
    print(f"Player {player}'s turn. Where would you like to place your piece (1-9)?")
    move = input()
    row = (int(move) - 1) // 3
    col = (int(move) - 1) % 3
    if board[row][col] != ' ':
        print("Invalid move. Try again.")
        handle_move(board, player)
    else:
        board[row][col] = player

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while not check_win(board):
        print_board(board)
        handle_move(board, current_player)
        current_player = 'O' if current_player == 'X' else 'X'
    print(f"Player {current_player} wins!")

play_game()