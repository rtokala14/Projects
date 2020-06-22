def BuildBoard():
    """
    Method to build the contents of the play board
    using a text file.

    Arguments:
    None

    Output:
    Board - A list
    """
    Board = []

    fileHandle = open("Board.txt", "r")
    data = fileHandle.readlines()
    for line in range(len(data)):
        if line != len(data) - 1:
            data[line] = data[line][:-1]
        Board.append(list(map(int, data[line].split(","))))
    fileHandle.close()

    return Board

def FindEmptyCell(Board):
    """
    Method to find the next empty cell in the Board.

    Arguments:
    Board - A 9x9 List of numbers

    Output:
    Tuple(x, y) - index of row, column
    """

    for i in range(len(Board)):
        for j in range(len(Board[0])):
            if Board[i][j] == 0:
                return (i,j)
    return None


