import os
import random
while True:
    while True:
        opçao = str(input("voce que ser X ou O??"))[0].lower()
        if opçao not in 'xo':
            print('Voce digitou uma letra que nao aceitamos')

        else:
            break
    lista = [[' ',' ',' '],
                 [' ',' ',' '],
                 [' ',' ',' ']]

    while True:
        if lista[0][0] == lista[0][1] == lista[0][2] == 'x':
            print('o x venceu')
        if lista[1][0] == lista[1][1] == lista[1][2] =='x':
            print('o x venceu')
        if lista[2][0] == lista[2][1] == lista[2][2] == 'x':
            print('o x venceu')
        if lista[0][0] == lista[1][0] == lista[2][0] == 'x':
            print('o x venceu')
        if lista[0][1] == lista[1][1] == lista[2][1] == 'x':
            print('o x venceu')
        if lista[0][2] == lista[1][2] == lista[2][2] == 'x':
            print('o x venceu')
        if lista[0][0] == lista[1][1] == lista[2][2] == 'x':
            print('o x venceu')
        if lista[2][0] == lista[1][1] == lista[0][2] == 'x':
            print('o x venceu')
        else:
            print('a letra o venceu')

        linhadopc=random.randint(0, 2)
        colunadopc =random.randint(0, 2)

        lugarlinha = int(input("qual o lugar que voce quer,\n digite a linha: ")) - 1
        lugarcoluna = int(input("digite a coluna agora: ")) - 1
        if opçao == 'x':
            opçaopc = 'o'
        else:
            opçaopc = 'x'


        while True:
            if lista[lugarlinha][lugarcoluna] == ' ':
                lista[lugarlinha][lugarcoluna] = opçao
                print(1)
                break
            else:
                lugarlinha = int(input("qual o lugar que voce quer,\n digite a linha: ")) - 1
                lugarcoluna = int(input("digite a coluna agora: ")) - 1

        print(f'''
                {lista[0][0]}| {lista[0][1]}| {lista[0][2]}
                ----------------
                {lista[1][0]}| {lista[1][1]}| {lista[1][2]}
                ----------------
                {lista[2][0]}| {lista[2][1]}| {lista[2][2]}    
                    ''')

        os.system("cls")
        while True:
            if lista[linhadopc][colunadopc] == ' ':
                lista[linhadopc][colunadopc] = opçaopc
                print(2)
                break
            else:
                linhadopc = random.randint(0, 2)
                colunadopc = random.randint(0, 2)


        print(f'''
        {lista[0][0]}| {lista[0][1]}| {lista[0][2]}
        -------------
        {lista[1][0]}| {lista[1][1]}| {lista[1][2]}
        -------------
        {lista[2][0]}| {lista[2][1]}| {lista[2][2]}    
            ''')






