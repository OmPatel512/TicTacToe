board = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']
currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board):
    inp = int(input("Enter a number between 1-9: "))
    if inp >= 1 and inp <= 9 and board == '-':
        board[inp-1] = currentPlayer
    else:
        print("Ooops that spot already used!")
        

