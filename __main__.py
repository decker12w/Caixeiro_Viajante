from algoritmo_genetico import algoritmo_genetico_tsp
from grafo import Grafo
from grafo_utils import gerar_grafo_completo

# Exemplo de Uso Completo Ajustado
if __name__ == "__main__":
    # Define os vértices (cidades)
    lista_vertices = ["A", "B", "C", "D", "E", "F", "G", "H"]

    # Cria uma instância de Grafo não direcionado
    meu_grafo = Grafo(direcionado=False)

    # Gera um grafo completo
    gerar_grafo_completo(
        grafo=meu_grafo,
        vertices=lista_vertices,
        peso_min=1,
        peso_max=20,
    )

    # Exibe as adjacências do grafo gerado
    print("\nAdjacências do Grafo Completo:")
    meu_grafo.listar_adjacencias()

    # Executa o Algoritmo Genético para resolver o TSP
    melhor_rota, custo_melhor = algoritmo_genetico_tsp(
        grafo=meu_grafo,
        vertices=lista_vertices,
        tamanho_populacao=100,
        geracoes=50,
        taxa_mutacao=0.01,
        elitismo=True,
    )

    # Exibe a melhor rota encontrada
    print("\nMelhor Rota Encontrada:")
    print(" -> ".join(melhor_rota) + f" -> {melhor_rota[0]}")
    print(f"Custo Total: {custo_melhor}")
