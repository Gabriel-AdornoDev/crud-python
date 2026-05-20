tarefas = []

#Função para criar uma tarefa.
def criar():
    titulo = str(input('Título da tarefa: '))
    tarefas.append({'titulo': titulo, 'Concluído': False})
 
#Função para mostrar as tarefas.
def listar():
    concluidas = 0
    pendentes = 0
    for indice, tarefa in enumerate(tarefas):
        if tarefa['Concluído']:
            status = '[✓]'
        else:
            status = '[✗]'
        print(indice, tarefa['titulo'], status)
    for tarefa in tarefas:
        if tarefa['Concluído']:
          concluidas += 1
        else:
             pendentes += 1
    
    print(f'{concluidas} tarefas concluídas \n {pendentes} tarefas pendentes')

#Função para deletar uma tarefa.           
def deletar():
    if not tarefas:
        print('Nenhuma tarefa cadastrada!')
        return
    try:
        indice = int(input('Qual tarefa deseja deletar? '))
    except ValueError:
        print('Erro, digite um número válido!')
        deletar()
        return
    if indice < 0 or indice > len(tarefas) - 1:
        print('Erro, essa tarefa não existe!')
        deletar()
    else:
        tarefas.pop(indice)
        print("Tarefa deletada!")

#Função para editar uma tarefa
def editar():
    if not tarefas:
        print('Nenhuma tarefa cadastrada!')
        return
    listar()
    try:
        indice = int(input('Qual tarefa deseja editar?  '))
    except ValueError:
        print('Erro, digite um número válido!')
        editar()
        return
    if indice < 0 or indice > len(tarefas) - 1:
        print('Erro, essa tarefa não existe!')
        editar()
        return
    novo_titulo = input('Novo título: ')
    tarefas[indice]['titulo'] = novo_titulo

#Função para concluir uma tarefa.
def check():
    listar()
    indice = int(input('Qual tarefa deseja dar como concluida?  '))
    tarefas[indice]['Concluído'] = not tarefas[indice]['Concluído']
    print('Tarefa concluida')
    listar()

#Manter o código aberto
while True:
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Deletar tarefa")
    print("4 - Editar tarefa")
    print("5 - Concluir tarefa")
    print("0 - Sair")
    escolha = input('Escolha a ação: ')
    if escolha == "1":
        criar()
    elif escolha == '2':
        listar()
    elif escolha == '3':
        deletar()
    elif escolha == '4':
        editar()
    elif escolha == '5':
        check()
    elif escolha == '0':
        print('Fim do programa.')
        break
    else:
        print('Escolha um número válido.')