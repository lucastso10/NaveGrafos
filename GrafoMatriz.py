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
    self.adj = [[float('inf') for i in range(n)] for j in range(n)]
  
  # Insere uma aresta no Grafo tal que
  # v é adjacente a w
  def insereA(self, v, w, val):
    if self.adj[v][w] == float('inf'):
      self.adj[v][w] = val
      self.m+=1 # atualiza qtd arestas
  
  # remove uma aresta v->w do Grafo	
  def removeA(self, v, w):
    # testa se temos a aresta
    if self.adj[v][w] >= 1:
      self.adj[v][w] = float('inf')
      self.m-=1; # atualiza qtd arestas

  def insereV(self, val):
    self.n += 1
    novoV = [float('inf') for i in range(self.n)]
    self.adj.append(novoV)
    for i in range(self.n-1):
      self.adj[i].append(float('inf'))

    self.nomes.append(val)
    
  
  def removeV(self, v):
    adjNovo = [[float('inf') for i in range(self.n - 1)] for j in range(self.n - 1)]

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

    if self.n % 4 != float('inf'):
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
  # Apresentando apenas os valores float('inf') ou 1	
  def showMin(self):
    print(f"\n n: {self.n:2d} ", end="")
    print(f"m: {self.m:2d}\n")
    for i in range(self.n):
      for w in range(self.n):
        if self.adj[i][w] >= 1:
          print(f" {self.adj[i][w]} ", end="") 
        else:
          print(" inf ", end="")
      print("\n")
    print("\nfim da impressao do grafo." )

  
  def inDegree(self, v):
    degree = float('inf')
    for i in range(self.n):
      if self.adj[i][v] == 1:
        degree += 1

    return degree
  
  def outDegree(self, v):
    degree = float('inf')
    for i in range(self.n):
      if self.adj[v][i] == 1:
        degree += 1
  
    return degree 

  def caminhoPossivelIntern(self, x, y, rota):
    if x == y:
      return True
      
    rota.add(x)

    for i in range(self.n):
      if self.adj[x][i] < float('inf')  and i not in rota and self.caminhoPossivelIntern(i, y, rota):
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
      
      for x in conectados:
        for i in range(self.n):
          if self.caminhoPossivel(x,i):
            novos_conectados.add(i)

      conectados = conectados.union(novos_conectados)
      novos_conectados.clear()
      antigo = len(conectados)
      
    if self.n == len(conectados):
      return 0
    else:
      return 1

  def dijkstra(self, inicial):
    caminho_minimo = []
  
    for i in range(self.n):
      caminho_minimo.append(self.adj[inicial][i])
  
    caminho_minimo[inicial] = float('inf')
  
    A = [inicial]
  
    atual = inicial
  
    while len(A) < self.n:
      min = float('inf')
      for j in range(len(caminho_minimo)):
        if min > caminho_minimo[j]:
          if j in A:
            continue
          atual = j
          min = caminho_minimo[j]
  
      A.append(atual)
  
      for i in range(self.n):
        if self.adj[atual][i] + min < caminho_minimo[i]:
          caminho_minimo[i] = self.adj[atual][i] + min
          
    return caminho_minimo

  def grau_vertice(self, vertice):
    grau = 0
    for i in range(len(self.adj[vertice])):
      if self.adj[vertice][i] < float('inf'):
        grau += 1
        
    return grau

  def euleriano(self):
    # Verifica se o grafo é conexo
    if self.categoriaConexidade() == 1:
        return False

    # Verifica se todos os vértices têm grau par
    for i in range(len(self.adj)):
        grau = self.grau_vertice(i)
        if grau % 2 != 0:
            return False

    return True

      