import pygame as py
import numpy as np
import random

board = np.array([np.array([0,0,0]),np.array([0,0,0]),np.array([0,0,0]),])
agent1 = 1
agent2 = 2
rv = False
agentTurn = 1

def checkRow():
    i = 0
    while i < 3:
        if np.array_equal(board[i], [agent1, agent1, agent1]) or np.array_equal(board[i], [agent2, agent2, agent2]):
            return board[i][0]
        i += 1
    return False

def checkColumn():
    i = 0
    
    while i < 3:
        if np.array_equal(board.T[i], [agent1, agent1, agent1]) or np.array_equal(board.T[i], [agent2, agent2, agent2]):
            return board.T[i][0]
        i += 1
    return False

def checkDiagonal():
    diagonals = np.diag(board)
    if np.array_equal(diagonals, [agent1, agent1, agent1]) or np.array_equal(diagonals, [agent2, agent2, agent2]):
        return diagonals[1]
    if np.array_equal([board[2][0], board[1][1], board[0][2]], [agent1, agent1, agent1]) or np.array_equal([board[2][0], board[1][1], board[0][2]], [agent2, agent2, agent2]):
        return board[1][1]
    return False

def checkValidMove():
    validMoves = []
    
    y = 0
    x = 0
    while y < len(board):
        x = 0
        while x < len(board[0]):
            if board[y][x] == 0:
                validMoves.append([y,x])
            x+=1
        y+=1
    return validMoves

def checkGameIsOver():
    y = 0
    x = 0
    while y < len(board):
        x = 0
        while x < len(board[y]):
            if board[y][x] == 0:
                return False
            x +=1
        y +=1
    
    return 3

def playAgent1Turn():
    validMoves = np.array(checkValidMove())
    randomRow = random.randint(0, len(validMoves) - 1)
    randomMove = validMoves[randomRow]
    board[randomMove[0]][randomMove[1]] = 1
    return

def playAgent2Turn():
    validMoves = np.array(checkValidMove())
    randomRow = random.randint(0, len(validMoves) - 1)
    randomMove = validMoves[randomRow]
    board[randomMove[0]][randomMove[1]] = 2
    return

def checkEndGame():
    rv = checkRow()
    if rv != False:
        return rv
    rv = checkColumn()
    if rv != False:
        return rv
    rv = checkDiagonal()
    if rv != False:
        return rv
    rv = checkGameIsOver()
    return rv
    

while rv == False:
    if agentTurn == 1:
        agentTurn = 2
        playAgent1Turn()
    else:
        agentTurn = 1
        playAgent2Turn()
    rv = checkEndGame()

print(board)

if rv == 1:
    print("Agent 1 won the game")
elif rv == 2:
    print("Agent 2 won the game")
else:
    print("It's a draw")
    