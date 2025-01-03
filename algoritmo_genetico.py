import random


def calcular_custo_total(grafo, rota):
    """
    Calcula o custo total de uma rota no grafo.

    :param grafo: Instância da classe Grafo.
    :param rota: Lista representando a ordem das cidades a serem visitadas.
    :return: Custo total da rota.
    """
    custo = 0
    for i in range(len(rota)):
        origem = rota[i]
        destino = rota[(i + 1) % len(rota)]  # Retorna à cidade inicial
        peso = grafo.obter_peso(origem, destino)
        if peso is None:
            # Se não houver aresta direta, retorna um custo alto
            return float("inf")
        custo += peso
    return custo


# Função para gerar a população inicial
def gerar_populacao_inicial(vertices, tamanho_populacao):
    """
    Gera a população inicial com cromossomos aleatórios.

    :param vertices: Lista de vértices (cidades).
    :param tamanho_populacao: Número de cromossomos na população.
    :return: Lista de cromossomos (rotas).
    """
    populacao = []
    for _ in range(tamanho_populacao):
        cromossomo = vertices.copy()
        random.shuffle(cromossomo)
        populacao.append(cromossomo)
    return populacao


def fitness(grafo, rota):
    """
    Calcula a fitness de uma rota. Fitness é inverso do custo total.

    :param grafo: Instância da classe Grafo.
    :param rota: Lista representando a ordem das cidades a serem visitadas.
    :return: Valor da fitness.
    """
    custo = calcular_custo_total(grafo, rota)
    if custo == 0:
        return float("inf")  # Evita divisão por zero
    return 1 / custo


# Função de seleção usando roleta
def selecionar_pais(populacao, fitness_populacao, tamanho_pais=2):
    """
    Seleciona pais usando o método de roleta (fitness proporcional).

    :param populacao: Lista de cromossomos.
    :param fitness_populacao: Lista de valores de fitness correspondentes.
    :param tamanho_pais: Número de pais a serem selecionados.
    :return: Lista de cromossomos selecionados como pais.
    """
    total_fitness = sum(fitness_populacao)
    if total_fitness == 0:
        # Se todos os fitness são zero, seleciona aleatoriamente
        return random.sample(populacao, tamanho_pais)
    roleta = [f / total_fitness for f in fitness_populacao]
    pais = random.choices(populacao, weights=roleta, k=tamanho_pais)
    return pais


# Função de crossover Order Crossover (OX)
def crossover_order(parent1, parent2):
    """
    Realiza o crossover do tipo Order Crossover (OX).

    :param parent1: Primeiro cromossomo pai.
    :param parent2: Segundo cromossomo pai.
    :return: Dois cromossomos filhos.
    """
    size = len(parent1)
    a, b = sorted(random.sample(range(size), 2))
    # Copia o segmento de parent1 para o filho1
    child1 = [None] * size
    child1[a:b] = parent1[a:b]
    # Preenche o restante na ordem de parent2
    fill_pos = b % size
    for gene in parent2:
        if gene not in child1:
            child1[fill_pos] = gene
            fill_pos = (fill_pos + 1) % size
    # Repetir para child2 com parent1 e parent2 invertidos
    child2 = [None] * size
    child2[a:b] = parent2[a:b]
    fill_pos = b % size
    for gene in parent1:
        if gene not in child2:
            child2[fill_pos] = gene
            fill_pos = (fill_pos + 1) % size
    return child1, child2


# Função de mutação por troca
def mutacao_swap(cromossomo, taxa_mutacao=0.1):
    """
    Realiza a mutação por troca de duas cidades.

    :param cromossomo: Cromossomo a ser mutado.
    :param taxa_mutacao: Probabilidade de mutação por gene.
    :return: Cromossomo mutado.
    """
    for i in range(len(cromossomo)):
        if random.random() < taxa_mutacao:
            j = random.randint(0, len(cromossomo) - 1)
            # Troca as cidades nas posições i e j
            cromossomo[i], cromossomo[j] = cromossomo[j], cromossomo[i]
    return cromossomo


def algoritmo_genetico_tsp(
    grafo,
    vertices,
    tamanho_populacao=10,
    geracoes=50,
    taxa_mutacao=0.01,
    elitismo=True,
):
    """
    Executa o Algoritmo Genético para resolver o TSP.

    :param grafo: Instância da classe Grafo.
    :param vertices: Lista de vértices (cidades).
    :param tamanho_populacao: Número de cromossomos na população.
    :param geracoes: Número máximo de gerações.
    :param taxa_mutacao: Taxa de mutação.
    :param elitismo: Booleano indicando se o elitismo é utilizado.
    :return: Melhor rota encontrada e seu custo.
    """
    # Inicialização
    populacao = gerar_populacao_inicial(vertices, tamanho_populacao)
    melhor_cromossomo = None
    melhor_fitness = -1

    for geracao in range(geracoes):
        # Avaliação
        fitness_populacao = [fitness(grafo, cromossomo) for cromossomo in populacao]

        # Encontrar o melhor cromossomo da geração atual
        for i in range(len(populacao)):
            if fitness_populacao[i] > melhor_fitness:
                melhor_fitness = fitness_populacao[i]
                melhor_cromossomo = populacao[i]

        # Calcula o custo
        if melhor_fitness == 0:
            custo_melhor = float("inf")
        else:
            custo_melhor = 1 / melhor_fitness

        print(
            f"Geração {geracao}: Melhor Fitness = {melhor_fitness:.6f}, Custo = {custo_melhor:.2f}"
        )

        # Seleção
        nova_populacao = []
        if elitismo:
            # Adiciona o melhor cromossomo à nova população
            nova_populacao.append(melhor_cromossomo.copy())

        while len(nova_populacao) < tamanho_populacao:
            # Seleciona dois pais
            pais = selecionar_pais(populacao, fitness_populacao, tamanho_pais=2)
            # Cruzamento
            filho1, filho2 = crossover_order(pais[0], pais[1])
            # Mutação
            filho1 = mutacao_swap(filho1, taxa_mutacao)
            filho2 = mutacao_swap(filho2, taxa_mutacao)
            # Adiciona os filhos à nova população
            nova_populacao.extend([filho1, filho2])

        # Atualiza a população
        populacao = nova_populacao[:tamanho_populacao]

    # Retorna a melhor rota encontrada
    custo_melhor = calcular_custo_total(grafo, melhor_cromossomo)
    return melhor_cromossomo, custo_melhor
