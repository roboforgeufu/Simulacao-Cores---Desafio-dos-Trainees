cores = ["R", "G", "B"]
direcoes_cor = []
#Associa uma direcao(com relacao a original do robo) a um numero
direcoes = {
    0 : "a direita" ,
    1 : "em frente" ,
    2 : "a esquerda" ,
    }

#Entrada da configuracao do circuito
print("Entrada da configuracao do circuito")
#   Entrada das cores, em ordem
cores_circuito = []
for n in range(4):
    print("Insira a cor na posicao %d:" %(n+1))
    x = input().upper()
    cores_circuito.append(x)
print(cores_circuito)

#Entrada da direcao certa de cada cor
print("\n\nEntrada da direcao certa de cada cor(0 Direita, 1 Em frente, 2 Esquerda)")
for n in range(3):
    print("Insira a direcao correta da cor", cores[n])
    x = int(input())
    direcoes_cor.append(x)
    print(cores[n], direcoes[x])
print(direcoes_cor)
print("\n\n\tINICIO\n\n")

"""SIMULAÇÃO DO ROBÔ"""

print("Robo no inicio.")
dir_disponiveis = [0, 1, 2]
cores_direcoes_aprendidas = {}
for cor in cores_circuito:
    cor_atual = "-"
    print("O robo se move p/frente ate encontrar uma cor")
    cor_atual = cor
    print("Encontra a cor", cor_atual)
    if cor_atual in cores_direcoes_aprendidas.keys():
        print("Ja aprendeu que [", cor_atual, direcoes[cores_direcoes_aprendidas[cor_atual]], "]")
        print("Segue", direcoes[cores_direcoes_aprendidas[cor_atual]])
    elif len(dir_disponiveis) == 1:
        print("Apenas uma direcao disponivel")
        cores_direcoes_aprendidas[cor_atual] = dir_disponiveis[0]
        print("Por eliminacao, aprende que [", cor_atual, ":", direcoes[dir_disponiveis[0]], "]")
        print("Aprende que a direcao [", dir_disponiveis[0], direcoes[dir_disponiveis[0]], "] nao esta mais disponivel")
        dir_disponiveis.pop(0)
        print("Segue", direcoes[cores_direcoes_aprendidas[cor_atual]])
    else:
        print("Aprendera a nova cor")
        for e in dir_disponiveis:
            print("Tenta seguir", direcoes[e])
            if e == direcoes_cor[cores.index(cor_atual)]:
                print("Acerta")
                cores_direcoes_aprendidas[cor_atual] = e
                print("Aprende que", cor_atual, ':', direcoes[cores_direcoes_aprendidas[cor_atual]])
                print("Aprende que a direcao [", e, direcoes[e], "] nao estara mais disponivel p/ outras cores")
                dir_disponiveis.pop(dir_disponiveis.index(e))
                print("Direcoes disponiveis = ", dir_disponiveis)
                break
            else:
                print("Encontra preto")
                print("Volta")
print("Chega no final.")
print("\n\n\tFIM\n\n")
