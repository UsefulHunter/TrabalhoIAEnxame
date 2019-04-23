from random import uniform
from math import sqrt
from math import sin
from math import pow


class Particle:
    def __init__(self, x, y, velocidade, pb):
        self.x = 0
        self.y = 0
        self.velocidadex = 0
        self.velocidadey = 0
        self.pb = [-100, 100]


def criaParticulas():
    n = int(input("Entre com o numero de particulas:"))
    particulas = []
    velocidadex = (uniform(min(limiteVelocidade), max(limiteVelocidade)))
    velocidadey = (uniform(min(limiteVelocidade), max(limiteVelocidade)))
    for i in range(n):
        particulas[i] = Particle(uniform(dominio1[0], dominio1[1]), uniform(
            dominio2[0], dominio2[1]), velocidadex, velocidadey)
    print(particulas)
    return(particulas)


def rodaFuncao(particulas):
    aptidao = []
    melhorAptidao = 0
    for i in range(len(particulas)):
        aptidao.append(0.5 + (pow(sin(sqrt(pow(particulas[i].x, 2) + (pow(particulas[i].y, 2))), 2)) -
                              0.5)/pow((1 + 0.001 * (pow(particulas[i].x, 2) + (pow(particulas[i].y, 2))), 2)))
        if(aptidao[i] > melhorAptidao):
            melhorAptidao = aptidao[i]
            print(melhorAptidao)
    return melhorAptidao


def atribuiVelocidade(particulas):
    velocidade = []
    for i in range(len(particulas)):
        velocidade.append(
            uniform(min(limiteVelocidade[0]), max(limiteVelocidade[1]))))
        particulas[i].velocidade=velocidade[i]
        print(velocidade[i])
    return particulas


def atualizaVelocidade(particulas):
    novaVelocidade=0
    for i in range(len(particulas)):
        novaVelocidade=particulas[i].velocidade + (particulas[i].x * rand(0, 1) * (
            particulas[i].pb[0] - particulas[i].x)) + particulas[i].y * rand(0, 1)*(gb - particulas[i].y)
        particulas[i].velocidade=novaVelocidade
        verificaVelocidade(particulas)
        print(novaVelocidade)


def atualizaPosicao(particulas):
    novaPosicaox=-100
    novaPosicaoy=100
    for i in range(len(particulas)):
        novaPosicaox=particulas[i].x + particulas[i].velocidade
        novaPosicaoy=particulas[i].y + particulas[i].velocidade


def aplicaPesoInercial(particulas):
    for i in range(len(particulas)):
        particulas[i].velocidade=rand(0.4, 0.9) * particulas[i].velocidade

def calculoPonderacao(particulas):
    for i in range(len(particulas)):
        w=0.9 - inte*((0.9 - 0.4)/inte)

dominio1=[-100, 100]
dominio2=[-100, 100]
limiteVelocidade=[-15, 15]
gB=[-100, 100]
criaParticulas()
atribuiVelocidade(particulas, n)
inte=int(input("Entre com o numero de interacoes:"))
for i in range(inte):
    print(limiteVelocidade[0], limiteVelocidade[1])
