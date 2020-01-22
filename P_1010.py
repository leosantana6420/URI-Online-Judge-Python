cod_peca1 = int(input())
num_peca1 = int(input())
val_peca1 = float(input())

cod_peca2 = int(input())
num_peca2 = int(input())
val_peca2 = float(input())

total_peca1 = (num_peca1 * val_peca1)
total_peca2 = (num_peca2 * val_peca2)

total_final = total_peca1 + total_peca2

print('VALOR A PAGAR: R$ {:.2f}'.format(total_final))