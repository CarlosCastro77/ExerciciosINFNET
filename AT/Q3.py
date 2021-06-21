def validarGastos(tipo, porcentagem, recomendado, valorIdealMaximo):
  if porcentagem > recomendado:
    print(f"Seus gastos totais com {tipo} comprometem {format(porcentagem, '.1f')}% de sua renda total. O máximo recomendado é de {recomendado}%. Portanto, idealmente, o máximo de sua renda comprometida com {tipo} deveria ser de R$ {format(valorIdealMaximo, '.1f')}.")
  else:
    print(f"Seus gastos totais com educação comprometem {format(porcentagem, '.1f')}% de sua renda total. O máximo recomendado é de {recomendado}%. Seus gastos estão dentro da margem recomendada.")

def calcularPorcentagem(valorTotal, valorCalculo):
  return (valorCalculo / valorTotal) * 100

def calcularValorIdealMaximo(valorTotal, porcentagemIdeal):
  return valorTotal * (porcentagemIdeal / 100)

def checarInputValido(mensagem):
  while True: 
    valorInput = float(input(mensagem))
    if type(valorInput) == float and valorInput > 0.0:
      break
    else:
      print('Valor inválido')
  return valorInput

def adqurirDados():
  rendaMensalTotal = checarInputValido("Renda mensal total: R$ ")
  gastosTotaisMoradia = checarInputValido("Gastos totais com moradia: R$ ")
  gastosTotaisEducacao = checarInputValido("Gastos totais com educação: R$ ")
  gastosTotaisTransporte = checarInputValido("Gastos totais com transporte: R$ ")

  return {'rendaMensalTotal': rendaMensalTotal, 'gastosTotaisMoradia': gastosTotaisMoradia, 'gastosTotaisEducacao': gastosTotaisEducacao, 'gastosTotaisTransporte': gastosTotaisTransporte}

def main():
  dados = adqurirDados();
  validarGastos('moradia', calcularPorcentagem(dados['rendaMensalTotal'], dados['gastosTotaisMoradia']), 30, calcularValorIdealMaximo(dados['rendaMensalTotal'], 30))
  validarGastos('educação', calcularPorcentagem(dados['rendaMensalTotal'], dados['gastosTotaisEducacao']), 20, calcularValorIdealMaximo(dados['rendaMensalTotal'], 20))
  validarGastos('transporte', calcularPorcentagem(dados['rendaMensalTotal'], dados['gastosTotaisTransporte']), 15, calcularValorIdealMaximo(dados['rendaMensalTotal'], 15))
if __name__ == "__main__":
  main()