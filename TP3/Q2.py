def adquirirDados():
  while True:
    idade = int(input('Informe a idade: '))
    if idade > 0:
      break
    else:
      print('Idade inválida')
  return {'idade': idade}

def validarIdade(idade):
  if idade >= 18 and idade < 70:
    return 'Tem a obrigação de votar.'
  elif (idade >= 16 and idade < 18) or idade >= 70:
    return 'Não tem a obrigação de votar.'
  else: return 'Não tem direito a voto.'


def exibirInformacoes(validacaoIdade):
  print(validacaoIdade)

def main():
  dados = adquirirDados();
  validacaoIdade = validarIdade(dados['idade'])
  exibirInformacoes(validacaoIdade)

if __name__ == "__main__":
  main()