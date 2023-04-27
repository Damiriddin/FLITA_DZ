 # Graphviz библиотека для визуализации данных
import graphviz

# Считываем матрицу из файла преобразуя в нужный формат
with open(r"adjacency_matrix_0.txt") as f:
    adj_matrix = []
    for line in f:
        row = [int(x) for x in line.split()]
        adj_matrix.append(row)


# Создаем граф
graph = graphviz.Graph(strict=False)

# Добавляем узлы в граф
for i in range(len(adj_matrix)):
    graph.node(str(i))

# Добавляем ребра в граф
for i in range(len(adj_matrix)):
    for j in range(i, len(adj_matrix[i])):
        if adj_matrix[i][j] != 0:
            graph.edge(str(i), str(j), label=str(adj_matrix[i][j]))
# Визуализируем графы
graph.view()
