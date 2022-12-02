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
            print('Player left the game')
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
            print('Player left the game')
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
board[0] = 'n'


def tieCheck():
    i = 0
    while i < rangeNum - 1:
        i += 1
        if board[i] == ' ':
            return False
    return True


def insertLetter(char, pos):
    if cellIsFree(pos):
        board[pos] = char
        # printBoard(board)
        # if tieCheck():
        #     print('Tie!')
        #     quit()
        if checkForWin():
            if char == player:
                print('Player wins\n')
                exit()
            else:
                print('Bott wins\n')
                exit()

        # if tieCheck():
        #     print('Tie1')
        #     exit()

        return

    else:
        print("Can't insert there!\n")
        pos = int(input('Enter new position\n'))
        insertLetter(char, pos)
        return


def cellIsFree(pos):
    return board[pos] == ' '


def isWinner(le):
    # 3x3
    if rangeNum == 10:
        if board[1] == board[2] and board[1] == board[3] and board[1] == le:
            return True
        elif board[4] == board[5] and board[4] == board[6] and board[4] == le:
            return True
        elif board[7] == board[8] and board[7] == board[9] and board[7] == le:
            return True
        elif board[1] == board[4] and board[1] == board[7] and board[1] == le:
            return True
        elif board[2] == board[5] and board[2] == board[8] and board[2] == le:
            return True
        elif board[3] == board[6] and board[3] == board[9] and board[3] == le:
            return True
        elif board[1] == board[5] and board[1] == board[9] and board[1] == le:
            return True
        elif board[7] == board[5] and board[7] == board[3] and board[7] == le:
            return True
        else:
            return False
    elif rangeNum == 26:
        # 5x5
        i = 1
        # rows
        while i != 25:
            if board[i] == board[i + 1] and board[i + 2] == board[i + 1] and board[i + 2] == le:
                return 1
            elif board[i] == board[i + 1] and board[i + 2] == board[i + 1] and board[i + 2] == le:
                return -1
            else:
                if i % 5 == 3:
                    i += 2
                else:
                    i += 1

        i = 6
        # Columns
        while i != 25:
            if board[i] == board[i - 5] and board[i + 5] == board[i] and board[i - 5] == le:
                return 1
            elif board[i] == board[i - 5] and board[i + 5] == board[i] and board[i - 5] == le:
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
            if board[i] == board[i + 6] and board[i + 12] == board[i] and board[i] == le:
                return 1
            elif board[i] == board[i + 6] and board[i + 12] == board[i] and board[i] == le:
                return -1

        x = [3, 4, 5, 10, 15, 9, 8, 14, 13]

        for i in x:
            if board[i] == board[i + 4] and board[i + 8] == board[i] and board[i] == le:
                return 1
            elif board[i] == board[i + 4] and board[i + 8] == board[i] and board[i] == le:
                return -1

    elif rangeNum == 50:
        # 7x7
        # Rows
        i = 1

        while i != 50:
            if board[i] == board[i + 1] and board[i + 2] == board[i + 1] and board[i + 2] == le:
                return 1
            elif board[i] == board[i + 1] and board[i + 2] == board[i + 1] and board[i + 2] == le:
                return -1
            else:
                if i % 7 == 5:
                    i += 3
                else:
                    i += 1

        # Columns
        i = 8
        while i != 49:
            if board[i] == board[i - 7] and board[i + 7] == board[i] and board[i - 7] == le:
                return 1
            elif board[i] == board[i - 7] and board[i + 7] == board[i] and board[i - 7] == le:
                return -1
            else:
                if i in [36, 37, 38, 39, 40, 41]:
                    i -= 27
                else:
                    i += 7

        # Diagonals
        i = 1

        while i <= 33:
            if board[i] == board[i + 8] and board[i + 16] == board[i] and board[i] == le:
                return 1
            elif board[i] == board[i + 8] and board[i + 16] == board[i] and board[i] == le:
                return -1
            else:
                if i % 7 == 6:
                    i += 2
                else:
                    i += 1

        i = 3

        while i <= 35:
            if board[i] == board[i + 6] and board[i + 12] == board[i] and board[i] == le:
                return 1
            elif board[i] == board[i + 6] and board[i + 12] == board[i] and board[i] == le:
                return -1
            else:
                if i % 7 == 0:
                    i += 3
                else:
                    i += 1

    return 0


def AIMove():
    # possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]

    # for let in ['O', 'X']:
    #     for i in possibleMoves:
    #         boardCopy = board[:]
    #         boardCopy[i] = let
    #         if isWinner(board, let):
    #             move = i
    #             return move
    # cornersOpen = []
    # for i in possibleMoves:
    #     if i % 2 == 0:
    #         cornersOpen.append(i)
    # if len(cornersOpen) > 0:
    #     move = selectRandom(cornersOpen)
    #     return move
    #
    # if 5 in possibleMoves:
    #     move = 5
    #     return move
    #
    # edgesOpen = []
    # for i in possibleMoves:
    #     if i % 2 == 1:
    #         edgesOpen.append(i)
    # if len(edgesOpen) > 0:
    #     move = selectRandom(edgesOpen)
    #     return move
    bestScore = -800
    bestMove = 0
    i = 1
    while i < rangeNum:
        if board[i] == ' ':
            board[i] = bot
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = i
        i += 1

    insertLetter(bot, bestMove)
    return


def minimax(board, depth, isMaximizing):
    if isWinner(bot):
        return 1
    elif isWinner(player):
        return -1
    elif isBoardFull():
        return 0

    if isMaximizing:
        bestScore = -800
        i = 1
        while i < rangeNum:
            if board[i] == ' ':
                board[i] = bot
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                if score > bestScore:
                    bestScore = score
            i += 1
        return bestScore

    else:
        bestScore = 800
        i = 1
        while i < rangeNum:
            if board[i] == ' ':
                board[i] = player
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                if score < bestScore:
                    bestScore = score
            i += 1
        return bestScore


def checkForWin():
    for i in range(rangeNum - 1):
        if isWinner(i) == 1 or isWinner(i) == -1:
            return True
        else:
            return False


# def selectRandom(x):
#     ln = len(x)
#     r = random.randrange(0, ln)
#     return x[r]


def isBoardFull():
    for key in range(rangeNum):
        if board[key] == ' ':
            return False
    return True


def playerMove():
    run = True
    while run:
        move = input('Select position to place ' + player + ' (1-' + str(rangeNum - 1) + '): ')
        if move == 'exit':
            print('Player left the game')
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
    # run = True
    # while run:
    #     pos = input('Select position to place ' + player + ' (1-' + str(rangeNum - 1) + '): ')
    #     if pos == 'exit':
    #         print('Player left the game')
    #         quit()
    #     try:
    #         move = int(pos)
    #         if 0 < move < rangeNum:
    #             if cellIsFree(move):
    #                 run = False
    #                 insertLetter(player, move)
    #             else:
    #                 print('This cell is occupied')
    #         else:
    #             print('Type a number within range (1-' + str(rangeNum - 1) + ')')
    #     except:
    #         print('Number is required')
    #     insertLetter(player, pos)


if bot == 'X':

    AIMove()
    printBoard(board)
else:
    printBoard(board)

while not (checkForWin()):
    # AIMove()
    # playerMove()

    if isBoardFull():
        print('Tie')
        exit()

    if not (isWinner(bot)):
        playerMove()
        printBoard(board)
    else:
        print('AI player won!')
        break

    if isBoardFull():
        print('Tie')
        exit()

    if not (isWinner(player)):
        AIMove()
        # print('Computer placed an O in position', move, ':')
        printBoard(board)
    else:
        print('You won!')
        break

