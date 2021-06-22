import csv

def calcularVariacao(pais, valorInicial, valorFinal):
  variacao = (valorFinal - valorInicial) / valorInicial * 100
  print(f"{pais:30s} Variação de {str(format(variacao, '.2f'))}% entre 2013 e 2020.")

def retornarDadosCsv():
  with open('pib_paises.csv', encoding="utf8") as f:
    reader = csv.DictReader(f)
    for row in reader:
      calcularVariacao(row['País'], float(row['2013']), float(row['2020']))

def main():
  retornarDadosCsv()
  
if __name__ == "__main__":
  main()