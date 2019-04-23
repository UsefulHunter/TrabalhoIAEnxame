from random import uniform
from math import sqrt
from math import sin
from math import pow


class Particle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.velocidade = 0


def criaParticulas():
    # 1.Determina o número de partículas P da população
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
        f[i] = 0.5 + (pow(sin(sqrt(pow(particulas[i].x, 2) + (pow(particulas[i].y, 2))), 2)) -
                  0.5)/pow((1 + 0.001 * (pow(particulas[i].x, 2) + (pow(particulas[i].y, 2))), 2))
        if(f[i] > melhorParticula):
            melhorParticula = f[i]
            print(melhorParticula)
    return melhorParticula


def atribuiVelocidade(particulas, n):
    for i in range(n):  # 3.Atribua uma velocidade inivial (v) igual para todas as particulas
        velocidade[i] = (uniform(min(limiteVelocidade[0]), max(limiteVelocidade[1]))
         particulas[i].velocidade=velocidade[i]
         print(velocidade[i])


# def verificaVelocidade():
#     for particula in particulas
#        if particula.velocidade > limiteVelocidade[1]
#             particula.velocidade = limiteVelocidade[1]
#             particula[0] = 100
#             particula[1] = 100
#             particula.velocidade = 0
#         else if particula.velocidade < limiteVelocidade[0]
#            particula.velocidade = limiteVelocidade[0]
#            particula[0] = -100
#            particula[1] = -100
#            particula.velocidade = 0

dominio1=[-100, 100]
dominio2=[-100, 100]
limiteVelocidade=[-15, 15]
criaParticulas()
atribuiVelocidade(particulas, n)
inte=int(input("Entre com o numero de interacoes:"))
for i in range(inte):
    print(limiteVelocidade[0], limiteVelocidade[1])
