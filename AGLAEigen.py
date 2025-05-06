import numpy as np


matrix = [
    [2, 1, -3, 5],
    [-1, 4, -1, 7],
    [10, 7, 2, 9],
    [0, -3, 8, 13]
]


matrix1 = np.array(matrix, dtype='float')#//матрица в нимпи формате

rows = len(matrix)
for row in matrix:
    if len(row) != rows: #если матрица не квадртаня, то мы не можем посчитать значения
        print("not a square matrix")
        break
else:

    values, vectors = np.linalg.eig(matrix1) #вычисление значений

    print("Eigenvalues:")
    for i, val in enumerate(values):
        print(np.round(val, 3)) # np.rpund потому что обычный round не укмеет читать комлпексные числаб последнюю цифру можно менять для изменения погрешности
    print()
    print("Eigenvectors:")
    for i in range(vectors.shape[1]):
        print(f"Вектор {i+1}: {vectors[:, i].round(3)}")#тут вроде обычный round сравняется, цифра в скобках измкеняет погрешность