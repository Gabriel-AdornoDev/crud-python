na = int(input('Seu número secreto: '))
ne = int(input('Chute o número do seu amigo: '))
if ne == na:
    print("Parabéns! Você acertou o número.")
elif ne < na:
    print('Your number its smaller than your friend one!')
else:
    print('Your number its bigger than your friend one!')

