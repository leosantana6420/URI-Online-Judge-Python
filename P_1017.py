tempo_viagem = int(input())
velocidade = int(input())

quantidade_litros = ((tempo_viagem * velocidade) / 12.0)

print('{:.3f}'.format(quantidade_litros))