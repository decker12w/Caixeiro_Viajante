class Grafo:
    def __init__(self, direcionado=False):
        self.direcionado = direcionado
        self.adjacencias = {}

    def adiciona_vertice(self, vertice):
        if vertice not in self.adjacencias:
            self.adjacencias[vertice] = []
            print(f"Vértice '{vertice}' adicionado.")
        else:
            print(f"Vértice '{vertice}' já existe.")

    def adiciona_aresta(self, origem, destino, peso=1):
        if origem not in self.adjacencias:
            self.adiciona_vertice(origem)
        if destino not in self.adjacencias:
            self.adiciona_vertice(destino)

        for d, p in self.adjacencias[origem]:
            if d == destino:
                print(f"Aresta de '{origem}' para '{destino}' já existe.")
                return
        self.adjacencias[origem].append((destino, peso))
        print(f"Aresta adicionada: {origem} -> {destino} (Peso: {peso})")
        if not self.direcionado:
            self.adjacencias[destino].append((origem, peso))
            print(f"Aresta adicionada: {destino} -> {origem} (Peso: {peso})")

    def remover_aresta(self, origem, destino):
        if origem in self.adjacencias:
            original_length = len(self.adjacencias[origem])
            self.adjacencias[origem] = [
                (d, p) for (d, p) in self.adjacencias[origem] if d != destino
            ]
            if len(self.adjacencias[origem]) < original_length:
                print(f"Aresta removida: {origem} -> {destino}")
            else:
                print(f"Aresta {origem} -> {destino} não encontrada.")

        if not self.direcionado:
            if destino in self.adjacencias:
                original_length = len(self.adjacencias[destino])
                self.adjacencias[destino] = [
                    (o, p) for (o, p) in self.adjacencias[destino] if o != origem
                ]
                if len(self.adjacencias[destino]) < original_length:
                    print(f"Aresta removida: {destino} -> {origem}")
                else:
                    print(f"Aresta {destino} -> {origem} não encontrada.")

    def remover_vertice(self, vertice):
        if vertice in self.adjacencias:
            del self.adjacencias[vertice]
            print(f"Vértice '{vertice}' removido.")

            # Remover todas as arestas que apontam para este vértice
            for v in self.adjacencias:
                original_length = len(self.adjacencias[v])
                self.adjacencias[v] = [
                    (d, p) for (d, p) in self.adjacencias[v] if d != vertice
                ]
                if len(self.adjacencias[v]) < original_length:
                    print(f"Aresta removida: {v} -> {vertice}")
        else:
            print(f"Vértice '{vertice}' não encontrado.")

    def listar_adjacencias(self):
        for vertice in self.adjacencias:
            adjacentes = ", ".join(
                [
                    f"{destino}(Peso: {peso})"
                    for destino, peso in self.adjacencias[vertice]
                ]
            )
            print(f"{vertice}: {adjacentes}")

    def obter_vertices(self):
        return list(self.adjacencias.keys())

    def obter_arestas(self):
        arestas = []
        for origem in self.adjacencias:
            for destino, peso in self.adjacencias[origem]:
                if self.direcionado or (destino, origem, peso) not in arestas:
                    arestas.append((origem, destino, peso))
        return arestas

    def atualizar_peso(self, origem, destino, novo_peso):
        if origem in self.adjacencias:
            atualizado = False
            for index, (d, p) in enumerate(self.adjacencias[origem]):
                if d == destino:
                    self.adjacencias[origem][index] = (d, novo_peso)
                    print(
                        f"Peso da aresta {origem} -> {destino} atualizado para {novo_peso}."
                    )
                    atualizado = True
                    break
            if not atualizado:
                print(f"Aresta {origem} -> {destino} não encontrada.")
            if not self.direcionado:
                # Atualiza a aresta reversa
                if destino in self.adjacencias:
                    for index, (o, p) in enumerate(self.adjacencias[destino]):
                        if o == origem:
                            self.adjacencias[destino][index] = (o, novo_peso)
                            break
        else:
            print(f"Vértice '{origem}' não encontrado.")

    def obter_peso(self, origem, destino):
        if origem in self.adjacencias:
            for d, p in self.adjacencias[origem]:
                if d == destino:
                    return p
        return None
