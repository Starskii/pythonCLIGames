def generate_board():
    board = []
    for row in range(0, 3):
        board.append(list('   '))
    return board

def tally_score(c):
    if c == 'x':
        return 1
    elif c == 'o':
        return -1
    else:
        return 0

def check_win(board):
    win_cond = []
    # check ul - br
    win_cond.append(tally_score(board[0][0]) +
            tally_score(board[1][1]) +
            tally_score(board[2][2]))
    # check ur - bl
    win_cond.append(tally_score(board[2][0]) +
            tally_score(board[1][1]) +
            tally_score(board[0][2]))
    
    # check horiz
    for x in range(0, 3):
        win_cond.append(tally_score(board[x][0]) +
                tally_score(board[x][1]) +
                tally_score(board[x][2]))
        
    # check vert
    for y in range(0, 3):
        win_cond.append(tally_score(board[0][y]) +
                tally_score(board[1][y]) +
                tally_score(board[2][y]))

    for cond in win_cond:
        if cond == 3:
            print('x wins')
            return True
        elif cond == -3:
            print('o wins')
            return True
    return False
     

def display_board(board):
    for row in board:
        print('')
        for col in row:
            print('|' + col, end='')
        print('|', end='')

def modify_board(board, active_char):
    ui = input('\nenter move: ')
    x = int(ui[0])
    y = int(ui[1])
    board[y][x] = active_char
    return board

playing = True
board = generate_board()
active_char = 'o'
while playing:
    if active_char == 'o':
        active_char = 'x'
    else:
        active_char = 'o'
    display_board(board)
    board = modify_board(board, active_char)
    if check_win(board):
        break
print('\n')
