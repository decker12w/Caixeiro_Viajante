import random


def gerar_grafo_completo(grafo, vertices, peso_min=1, peso_max=20):
    """
    Gera um grafo completo adicionando todas as arestas possíveis com pesos aleatórios.

    :param grafo: Instância da classe Grafo.
    :param vertices: Lista de vértices a serem adicionados.
    :param peso_min: Peso mínimo das arestas.
    :param peso_max: Peso máximo das arestas.
    """
    # Adiciona todos os vértices ao grafo
    for vertice in vertices:
        grafo.adiciona_vertice(vertice)

    # Adiciona todas as arestas possíveis com pesos aleatórios
    num_vertices = len(vertices)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            origem = vertices[i]
            destino = vertices[j]
            peso = random.randint(peso_min, peso_max)
            grafo.adiciona_aresta(origem, destino, peso)
