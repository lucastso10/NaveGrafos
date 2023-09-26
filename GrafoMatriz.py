from tabulate import tabulate

# Ana Luisa Tsunematsu Ferreira	TIA: 32158521
# Gabriel Ramires	TIA: 42080681
# Lucas Teixeira Soares	TIA: 32124831

class GrafoMatriz:
  TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
  # construtor da classe grafo
  def __init__(self, n=TAM_MAX_DEFAULT):
    self.n = n # número de vértices
    self.m = 0 # número de arestas
    # matriz de adjacência
    self.nomes = []
    self.adj = [[0 for i in range(n)] for j in range(n)]
  
  # Insere uma aresta no Grafo tal que
  # v é adjacente a w
  def insereA(self, v, w, val):
    if self.adj[v][w] == 0:
      self.adj[v][w] = val
      self.m+=1 # atualiza qtd arestas
  
  # remove uma aresta v->w do Grafo	
  def removeA(self, v, w):
    # testa se temos a aresta
    if self.adj[v][w] >= 1:
      self.adj[v][w] = 0
      self.m-=1; # atualiza qtd arestas

  def insereV(self, val):
    self.n += 1
    novoV = [0 for i in range(self.n)]
    self.adj.append(novoV)
    for i in range(self.n-1):
      self.adj[i].append(0)

    self.nomes.append(val)
    
  
  def removeV(self, v):
    adjNovo = [[0 for i in range(self.n - 1)] for j in range(self.n - 1)]

    for i in range(self.n):
      self.removeA(i, v)
      self.removeA(v, i)
  
    for i in range(self.n - 1):
      for j in range(self.n - 1):
        if i >= v and j >= v:
          adjNovo[i][j] = self.adj[i+1][j+1]
        elif i >= v and j < v:
          adjNovo[i][j] = self.adj[i+1][j]
        elif i < v and j >= v:
          adjNovo[i][j] = self.adj[i][j+1]
        else:
          adjNovo[i][j] = self.adj[i][j]

    self.n -= 1
    
    self.adj = adjNovo

    self.nomes.pop(v)
  
  # Apresenta o Grafo contendo
  # número de vértices, arestas
  # e a matriz de adjacência obtida	
  def show(self):
    print(f"\n n: {self.n:2d} ", end="")
    print(f"m: {self.m:2d}\n")

    temp_adj = []

    for i in range(4, self.n, 4):
      for j in range(self.n):
        if i < self.n:
          line = self.adj[j][i-4:i]
          line.insert(0, self.nomes[j] + f"({j})")
          temp_adj.append(line)
        else:
          line = self.adj[j][i-4:self.n]
          line.insert(0, self.nomes[j] + f"({j})")
          temp_adj.append(line)

      nomes = self.nomes[i-4:i]
      nomes.insert(0, "")
      print(tabulate(temp_adj, nomes, tablefmt="pretty"))

      temp_adj = []

    if self.n % 4 != 0:
      for j in range(self.n):
        line = self.adj[j][self.n - (self.n % 4):self.n]
        line.insert(0, self.nomes[j] + f"({j})")
        temp_adj.append(line)

      nomes = self.nomes[self.n - (self.n % 4):self.n]
      nomes.insert(0, "")
      print(tabulate(temp_adj, nomes, tablefmt="pretty"))
  
  # Apresenta o Grafo contendo
  # número de vértices, arestas
  # e a matriz de adjacência obtida 
  # Apresentando apenas os valores 0 ou 1	
  def showMin(self):
    print(f"\n n: {self.n:2d} ", end="")
    print(f"m: {self.m:2d}\n")
    for i in range(self.n):
      for w in range(self.n):
        if self.adj[i][w] >= 1:
          print(f" {self.adj[i][w]} ", end="") 
        else:
          print(" 0 ", end="")
      print("\n")
    print("\nfim da impressao do grafo." )

  
  def inDegree(self, v):
    degree = 0
    for i in range(self.n):
      if self.adj[i][v] == 1:
        degree += 1

    return degree
  
  def outDegree(self, v):
    degree = 0
    for i in range(self.n):
      if self.adj[v][i] == 1:
        degree += 1
  
    return degree  
  
  def ehFonte(self, v):
    if self.inDegree(v) == 0 and self.outDegree(v) > 0:
      return 1
    return 0
  
  def ehSorvedouro(self, v):
    if self.inDegree(v) > 0 and self.outDegree(v) == 0:
      return 1
    return 0
  
  def ehSimetrico(self):
    if self.m % 2  != 0:
      return 0
  
    for i in range(self.n):
      for j in range(i, self.n):
        if self.adj[i][j] == 1 and self.adj[j][i] == 0:
          return 0
      
    return 1

  def ehCompleto(self):
    for i in range(self.n):
      for j in range(self.n):
        if self.adj[i][j] == 0 and i != j:
          return 0
    return 1


  def caminhoPossivelIntern(self, x, y, rota):
    if x == y:
      return True
      
    rota.add(x)

    for i in range(self.n):
      if self.adj[x][i] == 1 and i not in rota and self.caminhoPossivelIntern(i, y, rota):
        return True

    return False
  
  # se é possivel chegar no vertice y a partir do vertice x  
  def caminhoPossivel(self, x, y):
    rota = set()
    return self.caminhoPossivelIntern(x, y, rota)
    

  def categoriaConexidade(self):
    conectados = {0}
    novos_conectados = {0}
    antigo = 0
    
    while antigo < len(conectados):
      antigo = len(conectados)

      for x in conectados:
        for i in range(self.n):
          if self.adj[x][i] == 1 or self.adj[i][x] == 1:
            novos_conectados.add(i)

      conectados = conectados.union(novos_conectados)
      novos_conectados.clear()

    if self.n != len(conectados):
      return 0

    for i in range(self.n):
      for j in range(i, self.n):
        if not self.caminhoPossivel(i, j) and not self.caminhoPossivel(j, i):
          return 1

    for i in range(self.n):
      for j in range(self.n):
        if not (self.caminhoPossivel(i, j) and self.caminhoPossivel(i,j)):
          return 2

    return 3


  def grafoReduzido(self):
    RMais = {0}
    RMenos = {0}
    Total = {0}
    S = []
    verticeAtual = 0

    while len(Total) != self.n:

      RMais.add(verticeAtual)
      RMenos.add(verticeAtual)

      # calcula o RMais desse vertice
      for i in range(self.n):
        if i in Total:
          continue
        if self.caminhoPossivel(verticeAtual, i):
          RMais.add(i)

      # calcula o RMenos desse vertice
      for i in range(self.n):
        if i in Total:
          continue
        
        if self.caminhoPossivel(i, verticeAtual):
          RMenos.add(i)

      # pega a intersecção e coloca na lista
      S.append(list(RMais.intersection(RMenos)))
      Total = Total.union(RMais.intersection(RMenos))

      RMais.clear()
      RMenos.clear()

      # pega o maior vertice de todas as intersecções e soma um para
      # decidir o proximo vertice que vai calcular o RMais e RMenos
      verticeAtual = max(Total) + 1

    # cria um grafo com a quantidade de secções do outro
    Gr = GrafoMatriz(len(S))

    # for bem feio para calcular todas as arestas do grafo reduzido
    # ela compara cada vertice de cada secção com cada vertice das outras
    # secções pra determinar se tem uma aresta entre os vertices do novo grafo
    for i in range(len(S)):
      for j in range(len(S[i])):
        for k in range(len(S)):
          for l in range(len(S[k])):
            if i != k and self.caminhoPossivel(S[i][j], S[k][l]):
              Gr.insereA(i,k)

    return Gr
