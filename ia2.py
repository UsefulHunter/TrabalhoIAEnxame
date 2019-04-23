from random import uniform
from math import sqrt
from math import sin
from math import pow


class Particle:
    def __init__(self):
        self.x1 = 0
        self.y2 = 0
        self.pb = [-100, 100]
        self.velocidade = 0


def criaParticulas():  # 1.Determina o número de partículas P da população
    n = int(input("Entre com o numero de particulas:"))
    particulas[n] = []
    for i in range(n):  # 2.Inicializa aleatoriamente a posição inicial(x) de cada partícula p de P
        particulas[i] = Particle(
            uniform(dominio1[0], dominio1[1]), uniform(dominio2[0], dominio2[1]))
    print(particulas)
    return(particulas, n)


def rodaFuncao(particulas, n):
    melhorParticula = 0
    for i in range(n):  # 4.(a). Calcula Aptidão fp = f(p)
        f[i] = 0.5 + (pow(sin(sqrt(pow(particulas[i].x1, 2) + (pow(particulas[i].x2, 2))), 2)) -
                  0.5)/pow((1 + 0.001 * (pow(particulas[i].x1, 2) + (pow(particulas[i].x2, 2))), 2))
        if(f[i] > melhorParticula):
            melhorParticula = f[i]
            print(melhorParticula)
    return melhorParticula


def atribuiVelocidade(particulas, n):
    for i in range(n):  # 3.Atribua uma velocidade inivial (v) igual para todas as particulas
        velocidade[i] = (uniform(min(limiteVelocidade[0]), max(limiteVelocidade[1]))
         particulas[i].velocidade=velocidade[i]
         print(velocidade[i])
    return particulas

def atualizaVelocidade(particulas, n):
    novaVelocidade=0
    for i in range(n):
        novaVelocidade=particulas[i].velocidade + (particulas[i].x1 * rand(0, 1) * (
            particulas[i].pb[0] - particulas[i].x1)) + particulas[i].x2 * rand(0, 1)*(gb - particulas[i].x2)
        particulas[i].velocidade=novaVelocidade
        verificaVelocidade(particulas)
        print(novaVelocidade)

# def verificaVelocidade():
#     for particula in particulas:
#        if particula.velocidade > limiteVelocidade[1]
#             particula.velocidade = limiteVelocidade[1]
#             particula.x1 = 100
#             particula.x2 = 100
#             particula.velocidade = 0
#         else if particula.velocidade < limiteVelocidade[0]:
#            particula.velocidade = limiteVelocidade[0]
#            particula.x1 = -100
#            particula.x2 = -100
#            particula.velocidade = 0

dominio1=[-100, 100]
dominio2=[-100, 100]
limiteVelocidade=[-15, 15]
gB=[-100, 100]
criaParticulas()
atribuiVelocidade(particulas, n)
inte=int(input("Entre com o numero de interacoes:"))
for i in range(inte):
    print(limiteVelocidade[0], limiteVelocidade[1])
