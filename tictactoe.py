

def main():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    winner = False
    next = 'X'

    while not winner:
        printBoard(board)

        print("{}, please input the number of your selected square:".format(next))
        square = input().strip()

        if not square.isdigit() or int(square) > 9:
            print("Invalid input!")
            continue

        if square in board:
            board[int(square) - 1] = next
        else:
            print("Already taken!")
            continue

        if next == 'X':
            next = 'O'
        else:
            next = 'X'

        winner = checkWin(board)

    printBoard(board)
    print("Winner: {}".format(winner))


def printBoard(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('----------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('----------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def checkWin(board):
    lines = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

    for line in lines:
        if board[line[0]] == board[line[1]] and board[line[1]] == board[line[2]]:
            return board[line[0]]

    return False


if __name__ == '__main__':
    main()
