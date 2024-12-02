
def replace_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            if row>col:
                matrix[row][col]=0

    return matrix

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

new_matrix=replace_matrix(matrix)

for row in new_matrix:
    print(row)
