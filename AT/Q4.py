def calcularJurosCompostos(valorInicial, rendimentoPeriodo, aportePeriodo, totalPeriodos):
  valorAtual = valorInicial 
  for i in range(1, int(totalPeriodos) + 1):
    valorAtual = (valorAtual + (valorAtual * (rendimentoPeriodo / 100))) + aportePeriodo
    print(f"Após {i} períodos(s), o montante será de R${format(valorAtual, '.2f')}.")


def checarInputValido(mensagem):
  while True: 
    valorInput = float(input(mensagem))
    if type(valorInput) == float and valorInput > 0.0:
      break
    else:
      print('Valor inválido')
  return valorInput

def adqurirDados():
  valorInicial = checarInputValido("Valor inicial: R$ ")
  rendimentoPeriodo = checarInputValido("Rendimento por período (%): ")
  aportePeriodo = checarInputValido("Aporte a cada período: R$ ")
  totalPeriodos = checarInputValido("Total de períodos: ")

  calcularJurosCompostos(valorInicial, rendimentoPeriodo, aportePeriodo, totalPeriodos)

def main():
  adqurirDados();

if __name__ == "__main__":
  main()