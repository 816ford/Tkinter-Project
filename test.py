import random

def checkHorizontal(board, row):
    for i in board[row]:
        if i == "Q":
            return False
    return True

def checkVertical(board, column):
    for i in board:
        if i[column] == "Q":
            return False
    return True

def checkDiagonal(board, y, x):
    permX = x
    permY = y
    while x <=6 and y<= 6:
        x+=1
        y+=1
        if board[y][x] == "Q":
            return False
    x = permX
    y = permY
    while x <= 6 and y >= 1:
        x+=1
        y-=1
        if board[y][x] == "Q":
            return False
    x = permX
    y = permY
    while x >= 1 and y >= 1:
        x-=1
        y-=1
        if board[y][x] == "Q":
            return False
    x = permX
    y = permY
    while x >= 1 and y <= 6:
        x-=1
        y+=1
        if board[y][x] == "Q":
            return False
    return True

def resetBoard():
    board = []
    for i in range(8):
        board.append(["*"]*8)
    return(board)

def find8queens():
    queens = 0
    board = resetBoard()
    for i,v in enumerate(board):
        totalChecks = []
        while len(totalChecks) != 8:
            j = random.randint(0,7)
            while totalChecks.__contains__(j):
                j = random.randint(0,7)
            totalChecks.append(j)
        for j in totalChecks:
            if checkHorizontal(board, i) and checkVertical(board, j) and checkDiagonal(board, i, j):
                board[i][j] = "Q"
                queens+=1
    return board

def printBoard(board):
    for i in board:
        print(i)
    print()

def main():
    board = find8queens()
    printBoard(board)
main()