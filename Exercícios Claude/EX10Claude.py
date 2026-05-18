contato = {
    'Gabriel': 123,
    'Ana': 456,
    'Mateus': 789
}
procura = input('Digite o número de telefone da pessoa: ')

if procura in contato:
    print(contato[procura])
else:
    print('Esse nome não tem um número de telefone')