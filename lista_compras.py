import os

# Pede o nome do usuário
nome_usuario = input('Digite seu nome: ')

# Cria a lista de compras
lista_compras = []

# Função para incluir item na lista
def incluir_item():
    # Limpa a tela
    os.system('cls')
    # Solicita a descrição do novo item ao usuário
    novo_elemento = input('Insira a descrição do novo item: ')
    # Adiciona o novo item à lista de compras
    lista_compras.append(novo_elemento)
    # Exibe mensagem de confirmação
    print(f'{nome_usuario} o item {novo_elemento} foi inserido na lista!\n')

# Função para listar os itens e seus índices
def listar_itens():
    # Limpa a tela
    os.system('cls')
    print('listando os objetos de uma lista: ')

    # Verifica se a lista está vazia
    if len(lista_compras) == 0:
        print(f'{nome_usuario} sua lista esta vazia :( ')
    else:
        # Exibe cabeçalho da lista
        print("\nIncio da Lista\n")
        print("ID", "Descrição", sep=" --- ")
        # Itera sobre a lista, exibindo o índice e a descrição de cada item
        for indice, produtos in enumerate(lista_compras):
            print(indice, produtos, sep="  --- ")

    print("\nFim da Lista\n")

# Função para apagar um item pelo índice ou pelo nome
def apagar_item():
    # Limpa a tela
    os.system('cls')
    # Solicita ao usuário que escolha o método de exclusão
    print(f'Olá {nome_usuario}! Selecione o que quer apagar : \n')
    opcao_apagar = input('[i]ndice ou [n]ome do item? ')

    if 'i' in opcao_apagar:
        # Solicita o índice do item a ser removido
        indice = int(input("Qual indice você deseja remover: "))
        # Valida o índice informado
        if indice > (len(lista_compras)-1) or indice < 0:
            print(f"{nome_usuario} este indice não existe na sua lista ou sua lista esta vazia. Tente listar ou buscar o pelo nome do item.")
        else:
            # Remove o item pelo índice e exibe mensagem de confirmação
            item_removido = lista_compras[indice]
            lista_compras.pop(indice)
            print(f"{nome_usuario} você removeu com sucesso o item {item_removido}")
    
    if 'n' in opcao_apagar:
        # Solicita o nome do item a ser removido
        nome_do_item = input("Qual nome você deseja remover: ")
        # Verifica se o item existe na lista
        if nome_do_item in lista_compras:
            # Remove o item pelo nome
            lista_compras.remove(nome_do_item)
        else:
            # Exibe mensagem caso o item não seja encontrado
            print(f'{nome_usuario} este item não existe na lista')

# Laço principal do programa
while True:
    # Exibe o menu de opções para o usuário
    print(f'Olá {nome_usuario}! Selecione uma opção: \n')
    resposta = input("[i]nserir, [a]pagar, [l]istar ou [s]air? ").lower()

    # Processa a opção escolhida pelo usuário
    if 'i' in resposta:
        incluir_item()
    elif 'a' in resposta:
        apagar_item()
    elif 'l' in resposta:
        listar_itens()
    elif 's' in resposta:
        # Encerra o laço e o programa
        break
    else:
        # Caso a opção seja inválida, solicita novamente
        continue

# Limpa a tela e exibe a lista final de compras
os.system('cls')
print(f'Até mais {nome_usuario} Sua lista de itens esta logo abaixo :P')
listar_itens()