import pandas as pd
import openpyxl
from GrafoMatriz import GrafoMatriz

# Ana Luisa Tsunematsu Ferreira	TIA: 32158521
# Gabriel Ramires	TIA: 42080681
# Lucas Teixeira Soares	TIA: 32124831

def print_menu():
  print("╔═══════════════════════════════════════════╗")
  print("║                 NaveGrafos                ║")
  print("║            Selecione uma opção!           ║")
  print("╠═══════════════════════════════════════════╣")
  print("║ 1.Ler arquivo                             ║")
  print("║                                           ║")
  print("║ 2.Salvar dados                            ║")
  print("║                                           ║")
  print("║ 3.Inserir vértice                         ║")
  print("║                                           ║")
  print("║ 4.Inserir aresta                          ║")
  print("║                                           ║")
  print("║ 5.Remover vértice                         ║")
  print("║                                           ║")
  print("║ 6.Remover aresta                          ║")
  print("║                                           ║")
  print("║ 7.Conteúdo do arquivo                     ║")
  print("║                                           ║")
  print("║ 8.Mostrar grafo                           ║")
  print("║                                           ║")
  print("║ 9.Conexidade                              ║")
  print("║                                           ║")
  print("║ 10.Caminho minimo                         ║")
  print("║                                           ║")
  print("║ 11.Grau                                   ║")
  print("║                                           ║")
  print("║ 12.caminho euleriano                      ║")
  print("║                                           ║")
  print("║ 0.Sair                                    ║")
  print("╚═══════════════════════════════════════════╝")

def escolherOpcao():
  valido = False

  x = 0
  while not valido:
    x = input()
    try:
      x = int(x)
    except ValueError:
      print("Porfavor digite o número de uma das opções!")
      continue
    if x > 12 or x < 0:
      print("Porfavor digite o número de uma das opções!")
      continue
    valido = True

  return x

def lerArquivo():
  with open("grafo.txt") as f:
    line = f.readline()
    line = f.readline()
    g = GrafoMatriz(int(line))

    for i in range(int(line)):
      line = f.readline()
      temp = line.split(" ")
      g.nomes.append(temp[1].replace('\n', ''))
      
    
    line = f.readline()
    
    for i in range(int(line)):
        line = f.readline()
        aresta = line.split(" ")
        g.insereA(int(aresta[0]), int(aresta[1]), int(aresta[2]))

  return g

def salvarDados(g):
  with open("grafo.txt", "w") as f:
    f.write("2\n")
    f.write(f"{g.n}\n")
    for i in range(g.n):
      f.write(f"{i} {g.nomes[i]}\n")
    f.write(f"{g.m}\n")
    for i in range(g.n):
      for j in range(g.n):
        if g.adj[i][j] >= 1 and g.adj[i][j] != float('inf'):
          f.write(f"{i} {j} {g.adj[i][j]}\n")

def printArquivo():
  with open("grafo.txt") as f:
    line = f.readline()
    tipo = int(line)
    match tipo:
      case 0:
        print("\nO grafo é não orientado e sem peso")
      case 1:
        print("\nO grafo é não orientado com peso no vértice")
      case 2:
        print("\nO grafo é não orientado com peso nas arestas")
      case 3:
        print("\nO grafo é não orientado com peso nos vértices e arestas")
      case 4:
        print("\nO grafo é orientado sem peso")
      case 5:
        print("\nO grafo é orientado com peso no vértice")
      case 6:
        print("\nO grafo é orientado com peso na aresta")
      case 7:
        print("\nO grafo é orientado com peso nos vértices e arestas")

    line = f.readline()
    print(f"\nele possui {line[:-1]} vértices:")

    for i in range(int(line)):
      line = f.readline()
      line = line.split(" ")
      if tipo == 1 or tipo == 3 or tipo == 5 or tipo == 7:
        print(f"número:{line[0]}, nome: {line[1]}, peso: {line[2]}")
      else:
        print(f"número:{line[0]}, nome: {line[1]}")

    line = f.readline()
    print(f"\nele possui {line[:-1]} arestas:")

    for i in range(int(line)):
      line = f.readline()
      line = line.split(" ")
      if tipo == 2 or tipo == 3 or tipo == 6 or tipo == 7:
        print(f"de:{line[0]}, para: {line[1]}, peso: {line[2]}")
      else:
        print(f"de:{line[0]}, para: {line[1]}")



def main():
  print("Bem Vindo!")

  rodar = True

  g = None

  while rodar:
    print_menu()
    x = escolherOpcao()

    match x:
      case 1:
        # ler arquivo
        g = lerArquivo()
        print("\nO arquivo grafo.txt foi lido com êxito!\n")
        
      case 2:
        # salvar dados
        if g:
          salvarDados(g)
          print("\nDados salvos com êxito")
        else:
          print("\nNão existe nenhum grafo!\n")

      case 3:
        # inserir vertice
        if g:
          print("\nDigite o nome do novo vértice!")
          nome = input()
          g.insereV(nome)
          print("\nNome vértice inserido com sucesso!\n")
        else:
          print("\nNão existe nenhum grafo!\n")

      case 4:
        # inserir aresta
        if g:
          print("\nQual porto gostaria de conectar? (digite o número dele)\n")
          i = input()
          print(f"\nCom porto gostaria de conectar o vértice {i}? (digite o número dele)\n")
          j = input()
          print("\nQual seria a distancia desses portos?")
          val = input()
          g.insereA(int(i), int(j), int(val))
          g.insereA(int(j), int(i), int(val))
          print("\nNova aresta inserida com sucesso!\n")
        else:
          print("\nNão existe nenhum grafo!\n")

      case 5:
        # remover vertice
        if g:
          print("\nQual vértice gostaria de remover? (digite o número dele)\n")
          i = input()
          g.removeV(int(i))
          print("\nVértice removido com sucesso!\n")
        else:
          print("\nNão existe nenhum grafo!\n")

      case 6:
        # remover aresta
        if g:
          print("\nDe qual vértice começa a aresta? (digite o número dele)\n")
          i = input()
          print("\nEm qual vértice a aresta termina? (digite o número dele)\n")
          j = input()
          g.removeA(int(i), int(j))
          g.removeA(int(j), int(i))
          print("\nAresta removida com sucesso!\n")
        else:
          print("\nNão existe nenhum grafo!\n")

      case 7:
        # conteudo do arquivo
        printArquivo()

      case 8:
        # mostrar grafo
        if g:
          g.show()
        else:
          print("\nNão existe nenhum grafo!\n")

      case 9:
        #conexidade
        if g:
          if g.categoriaConexidade() > 0:
            print("\nO grafo não é conexo!\n")
          else:
            print("\nO grafo é conexo!\n")
        else:
          print("\nNão existe nenhum grafo!\n")

      case 10:
        if g:
          print("Qual seria o porto inicial? (digite seu número conrespondente)")
          inpu = input()
          caminhos_minimos = g.dijkstra(int(inpu))
          print(f"\nCaminhos minimos do porto {g.nomes[int(inpu)]} até outros portos:")
          for i in range(len(caminhos_minimos)):
            if i == int(inpu):
              continue
            print(f"\n{g.nomes[i]} - {caminhos_minimos[i]}")
        else:
          print("\nNão existe nenhum grafo!\n")
          
      case 11:
        if g:
          print("Qual o porto você quer calcular o grau? (digite seu número conrespondente)")
          i = input()
          print(f"\nO grau desse porto é: {g.grau_vertice(int(i))}")
        else:
          print("\nNão existe nenhum grafo!\n")

      case 12:
        if g:
          if g.euleriano():
            print("\nEsse grafo é euleriano!")
          else:
            print("\nEsse grafo não é euleriano!")
        else:
          print("\nNão existe nenhum grafo!\n")
          
      case 0:
        #sair
        rodar = False


if __name__ == "__main__":
    main()
