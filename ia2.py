from random import uniform


def criaParticulas():
    particulas = []
    n = int(input("Entre com o numero de particulas:"))
    for i in range(n):
        particulas.append([uniform(min(
            dominio1+dominio2), max(dominio1+dominio2)), uniform(0, max(dominio1+dominio2))])
    print(particulas)
    return(particulas)


# def atribuiVelocidade(particulas):
#     for i in range(3):
#         velocidade[i] = (uniform(min(limiteVelocidade[0]), max(limiteVelocidade[1]))
#         print(velocidade)


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

dominio1 = [-100, 100]
dominio2 = [-100, 100]
limiteVelocidade = [-15, 15]
criaParticulas()
inte = int(input("Entre com o numero de interacoes:"))
for i in range(inte):
    print(limiteVelocidade[0], limiteVelocidade[1])
