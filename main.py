board = ["0","0","0",
         "0","0","0",
         "0","0","0",]

PLayer1 = "X"
winner = None
gameRunning = True

def printBoard(board):
    print (" -------------")
    print( " | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print (" -------------")
    print( " | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print (" -------------")
    print( " | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")
    print (" -------------")


def playerInput(board):
    inp = int(input("choisis un nombre entre 1-9:"))
    if inp >= 1 and inp <= 9 and board[inp-1] == "0":
        board[inp-1] = PLayer1
    else:
        print ("erreur, case pleine")

def checkcase(board): 
    global winner 
    if board[0] == board[1] == board[2] and board[0]!= "0":#horizontale
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3]!= "0":#horizontale
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6]!= "0":#horizontale
        winner = board[6]
        return True 
    elif board[0] == board[3] == board[6] and board[0]!= "0": #ligne
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1]!= "0": #ligne
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2]!= "0": #ligne
        winner = board[2]
        return True
    elif board[0] == board[4] == board[8] and board[0]!= "0": #diaguonal
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2]!= "0": #diaguonal
        winner = board[2]
        return True

def checkwin():
    global gameRunning
    if checkcase(board):
         print(f"le gagnant est {winner}!")
         gameRunning = False

def checkegal(board):
    global gameRunning
    if "0" not in board:
        printBoard(board)
        print("Egalité")
        gameRunning = False


def switchPlayer():
    global PLayer1
    if PLayer1 == "X":
        PLayer1 = "O"
    else:
        PLayer1 = "X"


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkwin()
    checkegal(board)
    switchPlayer()
    
