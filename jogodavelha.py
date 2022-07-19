import random
contO = 0
contX = 0
print('''
       _________________________________________________
      /                                                / 
     |                                                |
     |          Esse é um jogo da velha               |
     |                author=TGN                      |
     |                                                |
     /________________________________________________/
      ''')
while True:
    while True:
        opçao = str(input("Você que ser X ou O?? "))[0].lower()
        if opçao not in 'xo':
            print('Voce digitou uma letra que nao aceitamos')

        else:
            break
    lista = [[' ',' ',' '],
                 [' ',' ',' '],
                 [' ',' ',' ']]

    while True:
        
        if lista[0][0] == lista[0][1] == lista[0][2] != ' ':
            if lista[0][0] == 'x':
                print(f'o {lista[0][0]} venceu')
                contX +=1
            else:
                print(f'a letra o venceu')
                contO +=1
        
        if lista[1][0] == lista[1][1] == lista[1][2] != ' ':
            if lista[1][0] == 'x':
                print(f'o {lista[1][0]} venceu')
                contX +=1
            else:
                print(f'a letra o venceu')
                contO +=1
        
        if lista[2][0] == lista[2][1] == lista[2][2] != ' ':
            if lista[2][0] == 'x':
                print(f'o {lista[2][0]} venceu')
                contX +=1
            else:
                print(f'a letra o venceu')
                contO +=1
        
        if lista[0][0] == lista[1][0] == lista[2][0] != ' ':
            if lista[0][0] == 'x':
                print(f'o {lista[2][0]} venceu')
                contX +=1
            else:
                print(f'a letra o venceu')
                contO +=1
       
        if lista[0][1] == lista[1][1] == lista[2][1] != ' ':
            if lista[0][1] == 'x':
                print(f'o {lista[1][1]} venceu')
                contX +=1
            else:
                print(f'a letra o venceu')
                contO +=1
       
        if lista[0][2] == lista[1][2] == lista[2][2] != ' ':
            if lista[0][2] == 'x':
                print(f'o {lista[2][2]} venceu')
                contX +=1
            else:
                print(f'a letra o venceu')
                contO +=1
       
        if lista[0][0] == lista[1][1] == lista[2][2] != ' ':
            if lista[0][0] == 'x':
                print(f'o {lista[2][2]} venceu')
                contX +=1
            else:
                print(f'a letra o venceu')
                contO +=1
            
        if lista[2][0] == lista[1][1] == lista[0][2] != ' ':
            if lista[2][0] == 'x':
                print(f'o {lista[2][0]} venceu')
                contX +=1
            else:
                print(f'a letra o venceu')
                contO +=1
        if contO >0 or contX>0:
            continuar = str(input("quer continuar com o  jogo da velha[s/n]: "))[0].lower()
            if continuar in "n":
                break
            
        

        linhadopc=random.randint(0, 2)
        colunadopc =random.randint(0, 2)

        lugarlinha = int(input("Digite qual a linha: ")) - 1
        lugarcoluna = int(input("Digite a coluna agora: ")) - 1
        if opçao == 'x':
            opçaopc = 'o'
        else:
            opçaopc = 'x'


        while True:
            if lista[lugarlinha][lugarcoluna] == ' ':
                lista[lugarlinha][lugarcoluna] = opçao
                break
            else:
                lugarlinha = int(input(" digite qual linha: ")) - 1
                lugarcoluna = int(input("digite a coluna agora: ")) - 1

        print(f'''
        {lista[0][0]}| {lista[0][1]}| {lista[0][2]}
        -------------
        {lista[1][0]}| {lista[1][1]}| {lista[1][2]}
        -------------
        {lista[2][0]}| {lista[2][1]}| {lista[2][2]}    
                    ''')

        print("-------------------------------")
        while True:
            if lista[linhadopc][colunadopc] == ' ':
                lista[linhadopc][colunadopc] = opçaopc
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
        
        
        
