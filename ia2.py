from random import uniform


def criaParticulas():
    particulas = []
    n = int(input("Entre com o numero de particulas:"))
    for i in range(n):
        particulas.append([uniform(min(
            dominio1+dominio2), max(dominio1+dominio2)), uniform(0, max(dominio1+dominio2))])
    print(particulas)


def achaPeso(direcao):
    if(direcao == 'cima'):
        if(matriz[pontoAtual[0]-1][pontoAtual[1]] == 0):
            return([1+heuristica([pontoAtual[0]-1, pontoAtual[1]]), 'cima'])
        else:
            return([10+heuristica([pontoAtual[0]-1, pontoAtual[1]]), 'cima'])
    if(direcao == 'baixo'):
        if(matriz[pontoAtual[0]+1][pontoAtual[1]] == 0):
            return([1+heuristica([pontoAtual[0]+1, pontoAtual[1]]), 'baixo'])
        else:
            return([10+heuristica([pontoAtual[0]+1, pontoAtual[1]]), 'baixo'])
    if(direcao == 'esquerda'):
        if(matriz[pontoAtual[0]][pontoAtual[1]-1] == 0):
            return([1+heuristica([pontoAtual[0], pontoAtual[1]-1]), 'esquerda'])
        else:
            return([10+heuristica([pontoAtual[0], pontoAtual[1]-1]), 'esquerda'])
    if(direcao == 'direita'):
        if(matriz[pontoAtual[0]][pontoAtual[1]+1] == 0):
            return([1+heuristica([pontoAtual[0], pontoAtual[1]+1]), 'direita'])
        else:
            return([10+heuristica([pontoAtual[0], pontoAtual[1]+1]), 'direita'])


def mover(lado):
    if(lado == 'esquerda'):
        return(esquerda())
    if(lado == 'direita'):
        return(direita())
    if(lado == 'cima'):
        return(cima())
    else:
        return(baixo())


def ordena(matriz):
    aux = matriz[0]
    for i in matriz:
        if(aux[0] > i[0]):
            aux = i
    return(aux[1])


def imprimeMatriz(data):
    for linha in data:
        for numero in linha:
            print(f'{numero:>5}', end=" ")
        print()


def calculaCaminho(ultimaMovimentacao):
    caminhos = []
    if(pontoAtual[0] != 0 and ultimaMovimentacao != 'baixo'):
        caminhos.append(achaPeso('cima'))
    if(pontoAtual[0] != len(matriz)-1 and ultimaMovimentacao != 'cima'):
        caminhos.append(achaPeso('baixo'))
    if(pontoAtual[1] != len(matriz[0])-1 and ultimaMovimentacao != 'esquerda'):
        caminhos.append(achaPeso('direita'))
    if(pontoAtual[1] != 0 and ultimaMovimentacao != 'direita'):
        caminhos.append(achaPeso('esquerda'))
    a = ordena(caminhos)
    return(a)


def esquerda():
    if(pontoAtual[1] == 0):
        return
    else:
        pontoAtual[1] = pontoAtual[1]-1
        return('esquerda')


def direita():
    if(pontoAtual[1] == len(matriz[0])):
        return
    else:
        pontoAtual[1] = pontoAtual[1]+1
        return('direita')


def cima():
    if(pontoAtual[0] == 0):
        return
    else:
        pontoAtual[0] = pontoAtual[0]-1
        return('cima')


def baixo():
    if(pontoAtual[0] == len(matriz)):
        return
    else:
        pontoAtual[0] = pontoAtual[0]+1
        return('baixo')


def desenhaMatriz():
    matrizNova[pontoInicial[0]][pontoInicial[1]] = 'X'
    matrizNova[pontoFinal[0]][pontoFinal[1]] = 'O'
    for i in range(len(matrizNova)):
        for j in range(len(matrizNova[0])):
            if(matrizNova[i][j] == 1):
                matrizNova[i][j] = 'I'
            if(matrizNova[i][j] == 0):
                matrizNova[i][j] = 'O'
            if(matrizNova[i][j] == 2):
                matrizNova[i][j] = 'D'
            if(matrizNova[i][j] == 4):
                matrizNova[i][j] = 'L'
            if(matrizNova[i][j] == 8):
                matrizNova[i][j] = 'U'
            if(matrizNova[i][j] == 6):
                matrizNova[i][j] = 'R'


def copiaMatriz():
    matrizNova = []
    for i in matriz:
        matrizNova.append(i[:])
    return matrizNova


def atualizaMatriz():
    if(ultimaMovimentacao == 'baixo'):
        matrizNova[pontoAtual[0]][pontoAtual[1]] = 2
    if(ultimaMovimentacao == 'cima'):
        matrizNova[pontoAtual[0]][pontoAtual[1]] = 8
    if(ultimaMovimentacao == 'esquerda'):
        matrizNova[pontoAtual[0]][pontoAtual[1]] = 4
    if(ultimaMovimentacao == 'direita'):
        matrizNova[pontoAtual[0]][pontoAtual[1]] = 6


dominio1 = [-100, 100]
dominio2 = [-100, 100]
criaParticulas()
inte = int(input("Entre com o numero de interacoes:"))
for i in range(inte):
