class Grafo:
    def __init__(self, direcionado=False):
        self.direcionado = direcionado
        self.adjacencias = {}

    def adiciona_vertice(self, vertice):
        if vertice not in self.adjacencias:
            self.adjacencias[vertice] = []
        else:
            pass

    def adiciona_aresta(self, origem, destino, peso=1):
        if origem not in self.adjacencias:
            self.adiciona_vertice(origem)
        if destino not in self.adjacencias:
            self.adiciona_vertice(destino)

        for d, p in self.adjacencias[origem]:
            if d == destino:
                return
        self.adjacencias[origem].append((destino, peso))
        if not self.direcionado:
            self.adjacencias[destino].append((origem, peso))

    def remover_aresta(self, origem, destino):
        if origem in self.adjacencias:
            self.adjacencias[origem] = [
                (d, p) for (d, p) in self.adjacencias[origem] if d != destino
            ]
        if not self.direcionado:
            if destino in self.adjacencias:
                self.adjacencias[destino] = [
                    (o, p) for (o, p) in self.adjacencias[destino] if o != origem
                ]

    def remover_vertice(self, vertice):
        if vertice in self.adjacencias:
            del self.adjacencias[vertice]
            for v in self.adjacencias:
                self.adjacencias[v] = [
                    (d, p) for (d, p) in self.adjacencias[v] if d != vertice
                ]

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
                    atualizado = True
                    break
            if not atualizado:
                pass
            if not self.direcionado:
                if destino in self.adjacencias:
                    for index, (o, p) in enumerate(self.adjacencias[destino]):
                        if o == origem:
                            self.adjacencias[destino][index] = (o, novo_peso)
                            break
        else:
            pass

    def obter_peso(self, origem, destino):
        if origem in self.adjacencias:
            for d, p in self.adjacencias[origem]:
                if d == destino:
                    return p
        return None
