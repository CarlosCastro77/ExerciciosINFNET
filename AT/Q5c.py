import csv
import matplotlib.pyplot as plt

def exibirGrafico(listaAnos, listaValoresPib):
  plt.plot(listaAnos, listaValoresPib)  
  plt.ylabel('Evolução do PIB ao longo dos anos (em bilhões)')
  plt.xlabel('Anos')
  plt.show()

def retornarDadosCsv(pais):
  listaValoresPib = []
  listaAnos = []
  with open('pib_paises.csv', encoding="utf8") as f:
    reader = csv.DictReader(f)
    for row in reader:
      if (pais == row['País']):
        for key, value in row.items():
          if (value != row['País']):
            listaAnos.append(int(key))
            listaValoresPib.append(float(value))
  exibirGrafico(listaAnos, listaValoresPib)

def checarInputValidoPais(mensagem):
  listaPaises = ['EUA', 'China', 'Japão', 'Alemanha', 'Reino Unido', 'França', 'Brasil', 'Itália', 'Índia', 'Rússia', 'Canadá', 'Coreia do Sul', 'Espanha', 'México', 'Indonésia']
  while True: 
    valorInput = input(mensagem)
    if type(valorInput) == str and len(valorInput) > 2 and valorInput in listaPaises:
      break
    else:
      print("Valor inválido, os valores aceitos são: " + ", ".join(listaPaises))
  return valorInput

def adqurirDados():
  paisSelecionado = checarInputValidoPais("Informe um país: ")

  return {'pais': paisSelecionado}

def main():
  dados = adqurirDados();
  retornarDadosCsv(dados['pais'])
  
if __name__ == "__main__":
  main()