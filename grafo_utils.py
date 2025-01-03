import random


def gerar_grafo_aleatorio(grafo, vertices, probabilidade=0.3, peso_min=1, peso_max=10):
    """
    Gera um grafo aleatório adicionando vértices e arestas com pesos aleatórios.

    :param grafo: Instância da classe Grafo.
    :param vertices: Lista de vértices a serem adicionados.
    :param probabilidade: Probabilidade de existência de uma aresta entre dois vértices.
    :param peso_min: Peso mínimo das arestas.
    :param peso_max: Peso máximo das arestas.
    """
    # Adiciona todos os vértices ao grafo
    for vertice in vertices:
        grafo.adiciona_vertice(vertice)

    # Gera todas as possíveis combinações de vértices para adicionar arestas
    num_vertices = len(vertices)
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                continue  # Ignora laços (arestas que ligam um vértice a ele mesmo)
            origem = vertices[i]
            destino = vertices[j]
            # Para grafos não direcionados, evita adicionar arestas duplicadas
            if not grafo.direcionado and origem > destino:
                continue
            # Decide aleatoriamente se adiciona uma aresta com base na probabilidade
            if random.random() < probabilidade:
                peso = random.randint(peso_min, peso_max)
                grafo.adiciona_aresta(origem, destino, peso)
