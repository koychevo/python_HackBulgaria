def board_to_string(board):
    string = ""

    for row in range(len(board)):
        string += "|"
        for col in range(len(board[row])):
            string += " " + board[row][col] + " |"
        string += "\n"
    return string


board = [ ["X", "O", "#"],
          ["X", "X", "X"],
          ["#", "#", "#"] ]

result = board_to_string(board)

print(result)

