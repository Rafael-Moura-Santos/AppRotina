inicio = []
termino = []
tarefa = []
cont = '0'
a = 0

print( 60 * "=" )
print( "Organizador de Tarefas" )
print("Crie sua rotina da semanal")
print( 60 * "=" )

print("SEGUNDA")

while cont != '2':
    segunda_inicio = (input("Determine o horário de inicio: "))
    segunda_fim = input("Determine o horário de término: ")
    segunda = input("Determine a tarefa: ")
    inicio.append(segunda_inicio)
    termino.append(segunda_fim)
    tarefa.append(segunda)
    print('[1]-Nova Tarefa')
    print('[2]-Encerrar tarefa')
    while True:
        cont = input('Digite o número da opção desejada: ')
        if cont == '2':
            break
        elif cont == '1':
            print('Proxima tarefa')
            break
        else:
            print('Valor invalido')
cont = '0'

"""print("TERÇA")

while cont != '2':
    terca_inicio = input("Determine o horário de inicio: ")
    terca_fim = input("Determine o horário de término: ")
    terca=input("Determine a tarefa: ")
    inicio.append(terca_inicio)
    termino.append(terca_fim)
    tarefa.append(terca)
    print('[1]-Nova Tarefa')
    print('[2]-Encerrar tarefa')
    while True:
        cont = input('Digite o número da opção desejada: ')
        if cont == '2':
            break
        elif cont == '1':
            print('Proxima tarefa')
            break
        else:
            print('Valor invalido')

cont = '0'

print("QUARTA")

while cont != '2':
    quarta_inicio = input("Determine o horário de inicio: ")
    quarta_fim = input("Determine o horário de término: ")
    quarta=input("Determine a tarefa: ")
    inicio.append(quarta_inicio)
    termino.append(quarta_fim)
    tarefa.append(quarta)
    print('[1]-Nova Tarefa')
    print('[2]-Encerrar tarefa')
    while True:
        cont = input('Digite o número da opção desejada: ')
        if cont == '2':
            break
        elif cont == '1':
            print('Proxima tarefa')
            break
        else:
            print('Valor invalido')

cont = '0'

print("QUINTA")

while cont != '2':
    quinta_inicio = input("Determine o horário de inicio: ")
    quinta_fim = input("Determine o horário de término: ")
    quinta=input("Determine a tarefa: ")
    inicio.append(quinta_inicio)
    termino.append(quinta_fim)
    tarefa.append(quinta)
    print('[1]-Nova Tarefa')
    print('[2]-Encerrar tarefa')
    while True:
        cont = input('Digite o número da opção desejada: ')
        if cont == '2':
            break
        elif cont == '1':
            print('Proxima tarefa')
            break
        else:
            print('Valor invalido')

cont = '0'

print("SEXTA")

while cont != '2':
        sexta_inicio = input("Determine o horário de inicio: ")
        sexta_fim = input("Determine o horário de término: ")
        sexta=input("Determine a tarefa: ")
        inicio.append(sexta_inicio)
        termino.append(sexta_fim)
        tarefa.append(sexta)
        print('[1]-Nova Tarefa')
        print('[2]-Encerrar tarefa')
        while True:
            cont = input('Digite o número da opção desejada: ')
            if cont == '2':
                break
            elif cont == '1':
                print('Proxima tarefa')
                break
            else:
                print('Valor invalido')

cont = '0'

print("SABADO")

while cont != '2':
    sabado_inicio = input("Determine o horário de inicio: ")
    sabado_fim = input("Determine o horário de término: ")
    sabado=input("Determine a tarefa: ")
    inicio.append(sabado_inicio)
    termino.append(sabado_fim)
    tarefa.append(sabado)
    print('[1]-Nova Tarefa')
    print('[2]-Encerrar tarefa')
    while True:
        cont = input('Digite o número da opção desejada: ')
        if cont == '2':
            break
        elif cont == '1':
            print('Proxima tarefa')
            break
        else:
            print('Valor invalido')

cont = '0'

print("DOMINGO")

while cont != '2':
    domingo_inicio = input("Determine o horário de inicio: ")
    domingo_fim = input("Determine o horário de término: ")
    domingo=input("Determine a tarefa: ")
    inicio.append(domingo_inicio)
    termino.append(domingo_fim)
    tarefa.append(domingo)
    print('[1]-Nova Tarefa')
    print('[2]-Encerrar tarefa')
    while True:
        cont = input('Digite o número da opção desejada: ')
        if cont == '2':
            break
        elif cont == '1':
            print('Proxima tarefa')
            break
        else:
            print('Valor invalido')

print('Lista de Tarefas')"""

x = (len(inicio))
print(x)
z = (len(termino))
t = (len(tarefa))

while a != x:
    for y in range(x):
        print(inicio[0:x], end='')
        break
    for w in range(z):
        print(termino[w], end='')
        break
    for b in range(t):
        print(tarefa[b])
        break
    a = a + 1