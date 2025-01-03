# ...existing code...
from grafo import Grafo
from grafo_utils import gerar_grafo_aleatorio

# ...existing code...

if __name__ == "__main__":
    # Código de exemplo de uso
    # Defina os vértices
    lista_vertices = ["A", "B", "C", "D", "E"]

    # Cria uma instância de Grafo não direcionado
    meu_grafo = Grafo(direcionado=False)

    # Gera um grafo aleatório
    gerar_grafo_aleatorio(
        grafo=meu_grafo,
        vertices=lista_vertices,
        probabilidade=0.5,  # 50% de chance de existir uma aresta entre dois vértices
        peso_min=1,
        peso_max=10,
    )

    # Exibe as adjacências do grafo gerado
    print("\nAdjacências do Grafo Aleatório:")
    meu_grafo.listar_adjacencias()

    # Exibe todas as arestas do grafo
    print("\nArestas do Grafo Aleatório:")
    for aresta in meu_grafo.obter_arestas():
        print(aresta)
