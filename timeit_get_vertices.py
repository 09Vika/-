import timeit

def get_vertices(edges):
    """Получение списка вершин из списка ребер."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return list(vertices)

# Пример данных (небольшой набор ребер)
edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]

# Код для замера времени
iterations = 1000  # Количество повторений для более точного измерения

time_taken = timeit.timeit(lambda: get_vertices(edges), number=iterations)

print(f"Время выполнения count_vertices({edges}) {iterations} раз: {time_taken} секунд")
print(f"Среднее время выполнения: {time_taken / iterations} секунд")