idade_dias = int(input())

anos = idade_dias / 365
meses = ((idade_dias % 365) / 30)
dias = ((idade_dias % 365) / 30)

print('{:.0f} ano(s)'.format(anos))
print('{:.0f} mes(es)'.format(meses))
print('{:.0f} dia(s)'.format(dias))