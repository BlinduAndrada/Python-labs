def check_view(matrix):
    rows = len(matrix)
    blocked_seats = []

    if rows == 0:
        return []

    cols = len(matrix[0])

    for col in range(cols):
        current_max_height = matrix[0][col]

        for row in range(1, rows):
            height = matrix[row][col]

            if height <= current_max_height:
                blocked_seats.append((row, col))
            else:
                current_max_height = height

    return blocked_seats

matrix=[[1, 2, 3, 2, 1, 1],
 [2, 4, 4, 3, 7, 2],
 [5, 5, 2, 5, 6, 4],
 [6, 6, 7, 6, 7, 5]]
print(check_view(matrix))