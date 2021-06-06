def adquirirDadosParticipantes():
  participantes = []
  for x in range(1,6):
    nome = input(f'Informe nome do {x}º participante: ')
    while True:
      nota = float(input(f'Informe nota do {x}º participante: '))
      if nota >= 0.0 and nota <= 10.0:
        break
      else:
        print('Nota inválida')
    participantes.append({'nome': nome, 'nota': nota})
  return participantes;

def verificarVencedor(participantes):
  maiorNota = 0
  for participante in participantes:
    if participante['nota'] > maiorNota:
      maiorNota = participante['nota']
      vencedor = {'nome': participante['nome'], 'nota': participante['nota']}
  return vencedor

def exibirInformacoes(vencedor):
  print(f"O(a) vencedor(a) foi {vencedor['nome']} com nota {vencedor['nota']}!")

def main():
  participantes = adquirirDadosParticipantes();
  vencedor = verificarVencedor(participantes)
  exibirInformacoes(vencedor)

if __name__ == "__main__":
  main()