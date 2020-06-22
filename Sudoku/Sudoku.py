


# Load the board
def loadBoard():
    Board = []

    fileHandle = open("Board.txt", "r")
    data = fileHandle.readlines()
    for line in range(len(data)):
        if line != len(data) - 1:
            data[line] = data[line][:-1]
        Board.append(list(map(int, data[line].split(","))))
    fileHandle.close()

    return Board

Board = loadBoard()
for x in range(len(Board)):
    for y in range(len(Board[0])):
        print(Board[x][y], end=" ")
    print()
