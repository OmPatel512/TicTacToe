board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
currentPlayer = "X"
winner = None
gameRunning = True
inputted = True

def printBoard(board):
    print(f'Current Player is {currentPlayer}')
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board):
    global inputted
    inputted = True
    inp = int(input("Enter a number between 1-9: "))
    if (inp >= 1 and inp <= 9) and board[inp - 1] == '-':
        board[inp - 1] = currentPlayer
    else:
        print("Ooops that spot already used!")
        inputted = False


#check for win or tie
def checkHorizontale(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[3]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[6]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[4] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[3]
        return True

def checkWin():
    global gameRunning
    if checkDiagonal(board) or checkVertical(board) or checkHorizontale(board):
        print(f'The winner is {winner}')
        gameRunning = False

def CheckTie(board):
    global gameRunning
    if '-' not in board:
        printBoard(board)
        print('It is Tie')
        gameRunning = False

#Switch PLayer
def SwitchPlayer():
    global currentPlayer
    if currentPlayer == 'X' and inputted:
        currentPlayer = 'O'
    elif currentPlayer == 'O' and inputted:
        currentPlayer = 'X'

#Game Run
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    CheckTie(board)
    SwitchPlayer()
