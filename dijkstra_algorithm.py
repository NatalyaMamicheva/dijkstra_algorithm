import numpy as np

with open('input.txt', 'r', encoding='UTF-8') as fin:
    matrix = [line.replace("\n", " ").split() for line in fin][1:]

with open('input.txt', 'r', encoding='UTF-8') as fin:
    NSF = [line.replace("\n", " ").split() for line in fin][0]

N, S, F = int(NSF[0]), int(NSF[1]), int(NSF[2])

INF = np.inf
D = [INF] * N
D[S] = 0
Colored = [False] * N
while True:
    min_distance = INF
    min_vertex = D[S]
    # Вершины
    for i in range(N):
        if not Colored[i] and D[i] < min_distance:
            min_vertex = i  # нумерация неокрашенных вершин
            min_distance = D[i]  # направление ребер от одной промежуточной вершины к другой
    i = min_vertex  # промежуточные вершины до финального узла графа
    Colored[i] = True

    # Ребра
    for j in range(N):
        # D[i] - в файле input по столбцу(например работаем с 0 вершиной и стартовая точка 2 вершина,
        # значит 2 индекс в строке по матрице и здесь же 0 индекс в столбце)
        # matrix[i][j] - в файле input построчно(работаем с 0 вершиной значит числа из 0 строки по матрице)
        # D[j] - 12 строка в коде (работаем с 0 вершиной значит 0 индекс и тд)
        if D[i] + int(matrix[i][j]) < D[j] and int(matrix[i][j]) != -1:
            D[j] = D[i] + int(matrix[i][j])
    if min_distance == INF:
        break
if D[F] == INF or D[F] == -1:
    with open('output.txt', 'w', encoding='UTF-8') as fout:
        print(f"Пути не существует! Значит {-1}", file=fout)
else:
    with open('output.txt', 'w', encoding='UTF-8') as fout:
        print(D[F], file=fout)
