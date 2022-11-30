# Krestiki i noliki
import random

rangeNum = 0

print("Welcome to Tic-Tac-Toe!\n"
      "At the beginning you should choose size of board and playing side\n"
      "If you want to stop the game - write 'exit'")

while True:
    try:
        size = input('Choose a size of board:\n A: 3x3\n B: 5x5 \n C: 7x7\n')
        if size == 'exit':
            print('Player left tha game')
            quit()
        if size == 'a' or size == 'A':
            rangeNum = 10
            break

        elif size == 'b' or size == 'B':
            rangeNum = 26
            break

        elif size == 'c' or size == 'C':
            rangeNum = 50
            break

        else:
            print('Choose A/B/C')
    except TypeError:
        print('Choose A/B/C')

while True:
    try:
        playerSide = input('Choose side by writing X or O\n')
        if playerSide == 'exit':
            print('Player left tha game')
            quit()
        if playerSide == 'x' or playerSide == 'X':
            player = 'X'
            bot = 'O'
            break
        elif playerSide == 'o' or playerSide == 'O':
            player = 'O'
            bot = 'X'
            break
        else:
            print('Choose X/O')
    except TypeError:
        print('Choose X/O')


def printBoard(desk):
    if size == 'a' or size == 'A':
        # print('   |   |')
        print(' ' + desk[1] + ' | ' + desk[2] + ' | ' + desk[3])
        # print('   |   |')
        print('-----------')
        # print('   |   |')
        print(' ' + desk[4] + ' | ' + desk[5] + ' | ' + desk[6])
        # print('   |   |')
        print('-----------')
        # print('   |   |')
        print(' ' + desk[7] + ' | ' + desk[8] + ' | ' + desk[9])
        # print('   |   |')
    elif size == 'b' or size == 'B':
        # print('   |   |   |   |')
        print(' ' + desk[1] + ' | ' + desk[2] + ' | ' + desk[3] + ' | ' + desk[4] + ' | ' + desk[5])
        # print('   |   |   |   |')
        print('-------------------')
        # print('   |   |   |   |')
        print(' ' + desk[6] + ' | ' + desk[7] + ' | ' + desk[8] + ' | ' + desk[9] + ' | ' + desk[10])
        # print('   |   |   |   |')
        print('-------------------')
        # print('   |   |   |   |')
        print(' ' + desk[11] + ' | ' + desk[12] + ' | ' + desk[13] + ' | ' + desk[14] + ' | ' + desk[15])
        # print('   |   |   |   |')
        print('-------------------')
        # print('   |   |   |   |')
        print(' ' + desk[16] + ' | ' + desk[17] + ' | ' + desk[18] + ' | ' + desk[19] + ' | ' + desk[20])
        # print('   |   |   |   |')
        print('-------------------')
        # print('   |   |   |   |')
        print(' ' + desk[21] + ' | ' + desk[22] + ' | ' + desk[23] + ' | ' + desk[24] + ' | ' + desk[25])
        # print('   |   |   |   |')

    elif size == 'c' or size == 'C':
        # print('   |   |   |   |   |   |')
        print(' ' + desk[1] + ' | ' + desk[2] + ' | ' + desk[3] + ' | ' + desk[4] + ' | ' + desk[5] + ' | ' + desk[
            6] + ' | ' + desk[7])
        print('----------------------------')
        print(' ' + desk[8] + ' | ' + desk[9] + ' | ' + desk[10] + ' | ' + desk[11] + ' | ' + desk[12] + ' | ' + desk[
            13] + ' | ' + desk[14])
        print('----------------------------')
        print(' ' + desk[15] + ' | ' + desk[16] + ' | ' + desk[17] + ' | ' + desk[18] + ' | ' + desk[19] + ' | ' + desk[
            20] + ' | ' + desk[21])
        print('----------------------------')
        print(' ' + desk[22] + ' | ' + desk[23] + ' | ' + desk[24] + ' | ' + desk[25] + ' | ' + desk[26] + ' | ' + desk[
            27] + ' | ' + desk[28])
        print('----------------------------')
        print(' ' + desk[29] + ' | ' + desk[30] + ' | ' + desk[31] + ' | ' + desk[32] + ' | ' + desk[33] + ' | ' + desk[
            34] + ' | ' + desk[35])
        print('----------------------------')
        print(' ' + desk[36] + ' | ' + desk[37] + ' | ' + desk[38] + ' | ' + desk[39] + ' | ' + desk[40] + ' | ' + desk[
            41] + ' | ' + desk[42])
        print('----------------------------')
        print(' ' + desk[43] + ' | ' + desk[44] + ' | ' + desk[45] + ' | ' + desk[46] + ' | ' + desk[47] + ' | ' + desk[
            48] + ' | ' + desk[49])


board = [' ' for x in range(rangeNum)]


def insertLetter(char, pos):
    board[pos] = char


def cellIsFree(pos):
    return board[pos] == ' '


def isWinner(bo, le):
    # 3x3
    if rangeNum == 10:
        return (bo[7] == le and bo[8] == le and bo[9] == le) or (
                bo[4] == le and bo[5] == le and bo[6] == le) or (
                       bo[1] == le and bo[2] == le and bo[3] == le) or (
                       bo[1] == le and bo[4] == le and bo[7] == le) or (
                       bo[2] == le and bo[5] == le and bo[8] == le) or (
                       bo[3] == le and bo[6] == le and bo[6] == le) or (
                       bo[1] == le and bo[5] == le and bo[9] == le) or (
                       bo[3] == le and bo[5] == le and bo[7] == le)
    elif rangeNum == 26:
        # 5x5
        i = 1
        # rows
        while i != 25:
            if board[i] == board[i + 1] and board[i + 2] == board[i + 1] and board[i + 2] == le:
                return 1
            elif board[i] == board[i + 1] and board[i + 2] == board[i + 1] and board[i + 2] == bot:
                return -1
            else:
                if i % 5 == 3:
                    i += 2
                else:
                    i += 1

        i = 6
        # Columns
        while i != 25:
            if board[i] == board[i - 5] and board[i + 5] == board[i] and board[i - 5] == player:
                return 1
            elif board[i] == board[i - 5] and board[i + 5] == board[i] and board[i - 5] == bot:
                return -1
            else:
                if i in [16, 17, 18, 19]:
                    i -= 9
                else:
                    i += 5

        # Win cases are columns 1, 2, 3; rows 1, 6, 11
        # Diagonals
        x = [1, 2, 3, 6, 11, 7, 8, 12, 13]

        for i in x:
            if board[i] == board[i + 6] and board[i + 12] == board[i] and board[i] == player:
                return 1
            elif board[i] == board[i + 6] and board[i + 12] == board[i] and board[i] == bot:
                return -1

        x = [3, 4, 5, 10, 15, 9, 8, 14, 13]

        for i in x:
            if board[i] == board[i + 4] and board[i + 8] == board[i] and board[i] == player:
                return 1
            elif board[i] == board[i + 4] and board[i + 8] == board[i] and board[i] == bot:
                return -1

    elif rangeNum == 50:
        # 7x7
        # Rows
        i = 1

        while i != 50:
            if board[i] == board[i + 1] and board[i + 2] == board[i + 1] and board[i + 2] == player:
                return 1
            elif board[i] == board[i + 1] and board[i + 2] == board[i + 1] and board[i + 2] == bot:
                return -1
            else:
                if i % 7 == 5:
                    i += 3
                else:
                    i += 1

        # Columns
        i = 8
        while i != 49:
            if board[i] == board[i - 7] and board[i + 7] == board[i] and board[i - 7] == player:
                return 1
            elif board[i] == board[i - 7] and board[i + 7] == board[i] and board[i - 7] == bot:
                return -1
            else:
                if i in [36, 37, 38, 39, 40, 41]:
                    i -= 27
                else:
                    i += 7

        # Diagonals
        i = 1

        while i <= 33:
            if board[i] == board[i + 8] and board[i + 16] == board[i] and board[i] == player:
                return 1
            elif board[i] == board[i + 8] and board[i + 16] == board[i] and board[i] == bot:
                return -1
            else:
                if i % 7 == 6:
                    i += 2
                else:
                    i += 1

        i = 3

        while i <= 35:
            if board[i] == board[i + 6] and board[i + 12] == board[i] and board[i] == player:
                return 1
            elif board[i] == board[i + 6] and board[i + 12] == board[i] and board[i] == bot:
                return -1
            else:
                if i % 7 == 0:
                    i += 3
                else:
                    i += 1

    return 0


def AIMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(board, let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i % 2 == 0:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i % 2 == 1:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


#     bestScore = -800
#     bestMove = 0
#     i = 1
#     while i < rangeNum:
#         if board[i] == ' ':
#             board[i] = bot
#             score = minimax(board, 0, False)
#             board[i] = ' '
#             if score > bestScore:
#                 bestScore = score
#                 bestMove = i
#         i += 1
#
#     # insertLetter(bot, bestMove)
#     return bestMove
#
#
# def minimax(board, depth, isMaximizing):
#     if isWinner(board, bot):
#         return 1
#     elif isWinner(board, player):
#         return -1
#     elif isWinner(board, player) == 0:
#         return 0
#
#     if isMaximizing:
#         bestScore = -800
#         for key in board.keys():
#             if board[key] == ' ':
#                 board[key] = bot
#                 score = minimax(board, depth + 1, False)
#                 board[key] = ' '
#                 if score > bestScore:
#                     bestScore = score
#         return bestScore
#
#     else:
#         bestScore = 800
#         for key in board.keys():
#             if board[key] == ' ':
#                 board[key] = player
#                 score = minimax(board, depth + 1, True)
#                 board[key] = ' '
#                 if score < bestScore:
#                     bestScore = score
#         return bestScore


def selectRandom(x):
    ln = len(x)
    r = random.randrange(0, ln)
    return x[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def playerMove():
    run = True
    while run:
        move = input('Select position to place ' + player + ' (1-' + str(rangeNum - 1) + '): ')
        if move == 'exit':
            print('Player left tha game')
            quit()
        try:
            move = int(move)
            if 0 < move < rangeNum:
                if cellIsFree(move):
                    run = False
                    insertLetter(player, move)
                else:
                    print('This cell is occupied')
            else:
                print('Type a number within range (1-' + str(rangeNum - 1) + ')')
        except:
            print('Number is required')


def main():
    # print('Welcome to Tic-Tac-Toe game')
    # printBoard(board)

    if bot == 'X':
        insertLetter(bot, AIMove())
        print('Computer placed an ' + bot + ' in position', AIMove(), ':')
        printBoard(board)
    else:
        printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, bot)):
            playerMove()
            printBoard(board)
        else:
            print('AI player won!')
            break

        if not (isWinner(board, player)):
            move = AIMove()
            if move == 0:
                print('Tie')
            else:
                insertLetter(bot, move)
                print('Computer placed an O in position', move, ':')
                printBoard(board)
        else:
            print('You won!')
            break

    if isBoardFull(board):
        print('Tie')


main()