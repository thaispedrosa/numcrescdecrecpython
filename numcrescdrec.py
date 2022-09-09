from time import sleep

def numero_crescente(numeros:list):
    for c in range(1,len(numeros)):
        atual=numeros[c]
        posanterior=c-1
        while posanterior>=0 and atual<numeros[posanterior]:
            numeros[posanterior+1]=numeros[posanterior]
            posanterior-=1
        numeros[posanterior+1] = atual

def numero_decrescente(numeros:list):
    for c in range(1,len(numeros)):
        atual=numeros[c]
        posanterior=c-1
        while posanterior>=0 and atual>numeros[posanterior]:
            numeros[posanterior+1]=numeros[posanterior]
            posanterior-=1
        numeros[posanterior+1] = atual

def escolha():
    numeros=[]
    for n in range (1,6):
        n=int(input('\n Digite o {}* número:'.format(n)))
        numeros.append(n)
    
    escolha=str(input('''
        Digite a opção de lista ordenada: 
        [1]crescente 
        [2]decrescente 
        [3] finalizar 
        Qual a sua escolha?\n'''))
    while (escolha not in ['1','2','3']):
        print('Número inválido! Digite novamente!\n')
        escolha=str(input('''
        Digite a opção de lista ordenada: 
        [1]crescente 
        [2]decrescente 
        [3] finalizar 
        Qual a sua escolha?\n'''))
        
    if escolha=='1':
        print(f'\nLista desordenada {numeros}')
        numero_crescente(numeros)
        print(f'\nLista ordenada {numeros}')    
        
    elif escolha=='2':
        print(f'\nLista desordenada {numeros}')
        numero_decrescente(numeros)
        print(f'\nLista ordenada {numeros}')     
        
    elif escolha == '3':
        print('\n Programa finalizado!')

sleep(1)
escolha()
