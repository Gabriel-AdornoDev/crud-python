def par_ou_impar(a):
    return a % 2
a = int(input('Selecione um numero: '))

if par_ou_impar(a) == 0:
    print('Seu numero eh par!')
else:
    print('Seu numero eh impar!')

