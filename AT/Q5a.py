import csv

def retornarDadosCsv(pais, ano):
  with open('pib_paises.csv', encoding="utf8") as f:
    reader = csv.DictReader(f)
    for row in reader:
      if (pais == row['País']):
        print(f"PIB {pais} em {ano}: US${row[ano]} trilhões.")

def checarInputValidoAnoSelecionado(mensagem):
  while True: 
    valorInput = int(input(mensagem))
    if type(valorInput) == int and valorInput >= 2013 and valorInput <= 2020:
      break
    else:
      print('Valor inválido')
  return valorInput

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
  anoSelecionado = checarInputValidoAnoSelecionado("Informe um ano entre 2013 e 2020: ")

  return {'pais': paisSelecionado, 'ano': str(anoSelecionado)}

def main():
  dados = adqurirDados();
  retornarDadosCsv(dados['pais'], dados['ano'])
  
if __name__ == "__main__":
  main()