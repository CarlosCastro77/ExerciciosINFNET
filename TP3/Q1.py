def calcularDivisaoConta(valorTotalComTaxaServico, numeroPessoas):
  return valorTotalComTaxaServico / numeroPessoas

def calcularValorComTaxaServico(valorTotal, taxaServico):
  return valorTotal + (valorTotal * (taxaServico / 100))

def adqurirDados():
  valorTotal = float(input("Informe o valor total do consumo: R$ ").replace(',', '.'))

  while True: 
    numeroPessoas = int(float(input("Informe o total de pessoas: ")))
    if type(numeroPessoas) == int and numeroPessoas > 0:
      break
    else: 
      print('Valor inválido')

  while True:
    taxaServico = float(input("Informe o percentual da taxa do serviço, entre 0 e 100: "))
    if type(taxaServico) == float and (taxaServico >= 0 and taxaServico <= 100):
      break
    else:
      print('Valor inválido')
  
  return {'valorTotal': valorTotal, 'numeroPessoas': numeroPessoas, 'taxaServico': taxaServico}

def exibirInformacoes(valorComTaxaServico, numeroPessoas, valorPorPessoa):
  print("O valor total da conta, com a taxa de serviço, será de R$ " + format(valorComTaxaServico, '.2f').replace('.', ','))
  print(f"Dividindo a conta por {numeroPessoas} pessoa(s), cada pessoa deverá pagar R$ {valorPorPessoa.replace('.', ',')}")

def main():
  dados = adqurirDados();
  valorComTaxaServico = calcularValorComTaxaServico(dados['valorTotal'], dados['taxaServico'])
  valorPorPessoa = format(calcularDivisaoConta(valorComTaxaServico, dados['numeroPessoas']), '.2f')
  exibirInformacoes(valorComTaxaServico, dados['numeroPessoas'], valorPorPessoa)

if __name__ == "__main__":
  main()