"""
https://open.kattis.com/problems/nineknights
"""
import sys

def test():
    b1 = [[".", ".", "k", "k", "."], [".", ".", ".", ".", "."], [
        ".", "k", "k", "k", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."]]
    b2 = [[".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [
        ".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."]]
    b3 = [[".", ".", ".", ".", "k"], [".", ".", ".", "k", "."], [
        "k", ".", "k", ".", "."],  [".", "k", ".", "k", "."], ["k", ".", "k", ".", "k"]]

    assert checkValidity(b1) == 'invalid'
    assert checkValidity(b2) == 'invalid'
    assert checkValidity(b3) == 'valid'

def readBoard():
    board = [[".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."]]

    for i in range(5):
        x = input()
        for j in range(5):
            board[i][j] = x[j]

    return board

def checkValidity(board):
    count = 0
    moves = [
        [-1,  2],
        [-1, -2],
        [ 1,  2],
        [ 1, -2],
        [ 2, -1],
        [ 2,  1],
        [-2, -1],
        [-2,  1]
    ]
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'k':
                count += 1

                # print("Moves for board[%d][%d] 'k' are:" %(i,j))

                for move in moves:
                    try:
                        a = i+move[0]
                        b = j+move[1]
                        if a >= 0 and b >= 0 and board[a][b] == 'k':
                            return 'invalid'
                            # print("board[%d][%d]: " % (i+move[0], j+move[1]) + board[a][b])
                    except: pass
    if count != 9:
        return "invalid"
    return 'valid'

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        board = readBoard()
        # for row in board:
        #     print(row)
        print(checkValidity(board))
