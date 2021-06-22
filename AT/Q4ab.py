import matplotlib.pyplot as plt

def exibirGrafico(listaValores, totalPeriodos):
  plt.plot(totalPeriodos, listaValores)  
  plt.ylabel('Evolução do valor acumulado')
  plt.xlabel('Período (em meses)')
  plt.show()

def calcularJurosCompostos(valorInicial, rendimentoPeriodo, aportePeriodo, totalPeriodos):
  valorAtual = valorInicial
  listaValores = []
  for i in range(1, int(totalPeriodos) + 1):
    valorAtual = (valorAtual + (valorAtual * (rendimentoPeriodo / 100))) + aportePeriodo
    listaValores.append(valorAtual)
    print(f"Após {i} períodos(s), o montante será de R${format(valorAtual, '.2f')}.")
  exibirGrafico(listaValores, range(1, int(totalPeriodos) + 1))

def checarInputValido(mensagem):
  while True: 
    valorInput = float(input(mensagem))
    if type(valorInput) == float and valorInput > 0.0:
      break
    else:
      print('Valor inválido')
  return valorInput

def adquirirDados():
  valorInicial = checarInputValido("Valor inicial: R$ ")
  rendimentoPeriodo = checarInputValido("Rendimento por período (%): ")
  aportePeriodo = checarInputValido("Aporte a cada período: R$ ")
  totalPeriodos = checarInputValido("Total de períodos: ")

  calcularJurosCompostos(valorInicial, rendimentoPeriodo, aportePeriodo, totalPeriodos)

def main():
  adquirirDados();

if __name__ == "__main__":
  main()