matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]


def transposed_matrix(matrix):
    print(list(map(lambda x: list(x), list(zip(*matrix)))))

transposed_matrix (matrix)
