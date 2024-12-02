
class Matrix:
    def __init__(self, N, M):
        self.rows = N
        self.cols = M
        self.data = []
        for _ in range(N):
            row = [0] * M
            self.data.append(row)

    def get(self, i, j):
        return self.data[i][j]

    def set(self, i, j, value):
        self.data[i][j] = value

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(j, i, self.data[i][j])

        return transposed

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Dimensions don't match")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))

        return result

    def transform(self,func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = func(self.data[i][j])

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

matrix = Matrix(2, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)

print("Original matrix:")
print(matrix)

transposed = matrix.transpose()
print("\nTransposed matrix:")
print(transposed)

other = Matrix(3, 2)
other.set(0, 0, 7)
other.set(0, 1, 8)
other.set(1, 0, 9)
other.set(1, 1, 10)
other.set(2, 0, 11)
other.set(2, 1, 12)

product = matrix.multiply(other)
print("\nMatrix multiplication result:")
print(product)


matrix.transform(lambda x: x * 2)
print("\nTransformed matrix:")
print(matrix)

