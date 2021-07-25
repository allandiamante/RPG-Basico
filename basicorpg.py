import random
import os
import copy

class monstro():
    def __init__(self, classe, vida, porcentagemres, resistencia):
        self.classe = classe
        self.vida = vida
        self.porcentagemres = porcentagemres
        self.resistencia = resistencia
    
    def atualizar(self, vida):
        self.vida = vida

class classe():
    def __init__(self, nome, dano):
        self.classe = nome
        self.dano = dano

    def ataque(self):
        print(f"POR DEMACIA!")

class Druida(classe):
    def __init__(self):
        super().__init__("Druida", 5)

    def ataque(self, monstros):
        if len(monstros) > 0 and monstros[0].resistencia!= "Veneno":
            print("O "+'{}Druida{}'.format('\033[4;32m', '\033[m')+" ataca o "+ monstros[0].classe +f" inimigo com {self.dano} de dano de "+'{}veneno{}'.format('\033[4;32m', '\033[m'))
            monstros[0].atualizar(monstros[0].vida - self.dano)
        elif len(monstros) > 0:
            print("O "+'{}Druida{}'.format('\033[4;32m', '\033[m')+" ataca o "+ monstros[0].classe +" inimigo com "+ str(self.dano * 0.5) +" de dano de "+'{}veneno{}'.format('\033[4;32m', '\033[m'))
            monstros[0].atualizar(monstros[0].vida - (self.dano * (monstros[0].porcentagemres / 100)))

        if len(monstros) > 1 and monstros[1].resistencia!= "Veneno":
            print("O "+'{}Druida{}'.format('\033[4;32m', '\033[m')+" ataca o "+ monstros[1].classe +f" inimigo com {self.dano} de dano de "+'{}veneno{}'.format('\033[4;32m', '\033[m'))
            monstros[1].atualizar(monstros[1].vida - self.dano)
        elif len(monstros) > 1:
            print("O "+'{}Druida{}'.format('\033[4;32m', '\033[m')+" ataca o "+ monstros[1].classe +" inimigo com "+ str(self.dano * 0.5) +" de dano de "+'{}veneno{}'.format('\033[4;32m', '\033[m'))
            monstros[1].atualizar(monstros[1].vida - (self.dano * (monstros[1].porcentagemres / 100)))

        if len(monstros) > 2 and monstros[2].resistencia!= "Veneno":
            print("O "+'{}Druida{}'.format('\033[4;32m', '\033[m')+" ataca o "+ monstros[2].classe +f" inimigo com {self.dano} de dano de "+'{}veneno{}'.format('\033[4;32m', '\033[m'))
            monstros[2].atualizar(monstros[2].vida - self.dano)
        elif len(monstros) > 2:
            print("O "+'{}Druida{}'.format('\033[4;32m', '\033[m')+" ataca o "+ monstros[2].classe +" inimigo com "+ str(self.dano * 0.5) +" de dano de "+'{}veneno{}'.format('\033[4;32m', '\033[m'))
            monstros[2].atualizar(monstros[2].vida - (self.dano * (monstros[2].porcentagemres / 100)))

    def pintar(self):
        return ("\033[4;32m"+ self.classe+ 's' +"\033[m")

class Mago(classe):
    def __init__(self):
        super().__init__("Mago", 4)

    def ataque(self, monstros):
        if len(monstros) > 0 and monstros[0].resistencia!= "Mágico":
            print("O "+'{}Magos{}'.format('\033[4;31m', '\033[m') + " ataca o "+ monstros[0].classe +f" inimigo com {self.dano} de dano de "+'{}fogo{}'.format('\033[4;31m', '\033[m'))
            monstros[0].atualizar(monstros[0].vida - self.dano)
        elif len(monstros) > 0:
            print("O "+'{}Magos{}'.format('\033[4;31m', '\033[m') + " ataca o "+ monstros[0].classe +f" inimigo com "+str(self.dano * 0.5) +" de dano de "+'{}fogo{}'.format('\033[4;31m', '\033[m'))
            monstros[0].atualizar(monstros[0].vida - (self.dano * (monstros[0].porcentagemres / 100)))

        if len(monstros) > 1 and monstros[1].resistencia!= "Mágico":
            print("O "+'{}Magos{}'.format('\033[4;31m', '\033[m') + " ataca o "+ monstros[1].classe +f" inimigo com {self.dano} de dano de "+'{}fogo{}'.format('\033[4;31m', '\033[m'))
            monstros[1].atualizar(monstros[1].vida - self.dano)
        elif len(monstros) > 1:
            print("O "+'{}Magos{}'.format('\033[4;31m', '\033[m') + " ataca o "+ monstros[1].classe +f" inimigo com "+str(self.dano * 0.5) +" de dano de "+'{}fogo{}'.format('\033[4;31m', '\033[m'))
            monstros[1].atualizar(monstros[1].vida - (self.dano * (monstros[1].porcentagemres / 100)))

        if len(monstros) > 2 and monstros[2].resistencia!= "Mágico":
            print("O "+'{}Magos{}'.format('\033[4;31m', '\033[m') + " ataca o "+ monstros[2].classe +f" inimigo com {self.dano} de dano de "+'{}fogo{}'.format('\033[4;31m', '\033[m'))
            monstros[2].atualizar(monstros[2].vida - self.dano)
        elif len(monstros) > 2:
            print("O "+'{}Magos{}'.format('\033[4;31m', '\033[m') + " ataca o "+ monstros[2].classe +f" inimigo com "+str(self.dano * 0.5) +" de dano de "+'{}fogo{}'.format('\033[4;31m', '\033[m'))
            monstros[2].atualizar(monstros[2].vida - (self.dano * (monstros[2].porcentagemres / 100)))

        if len(monstros) > 3 and monstros[3].resistencia!= "Mágico":
            print("O "+'{}Magos{}'.format('\033[4;31m', '\033[m') + " ataca o "+ monstros[3].classe +f" inimigo com {self.dano} de dano de "+'{}fogo{}'.format('\033[4;31m', '\033[m'))
            monstros[3].atualizar(monstros[3].vida - self.dano)
        elif len(monstros) > 3:
            print("O "+'{}Magos{}'.format('\033[4;31m', '\033[m') + " ataca o "+ monstros[3].classe +f" inimigo com "+str(self.dano * 0.5) +" de dano de "+'{}fogo{}'.format('\033[4;31m', '\033[m'))
            monstros[3].atualizar(monstros[3].vida - (self.dano * (monstros[3].porcentagemres / 100)))

    def pintar(self):
        return ("\033[4;31m"+ self.classe+ 's' +"\033[m")

class Guerreiro(classe):
    def __init__(self):
        super().__init__("Guerreiro", 6)

    def ataque(self, monstros):
        if len(monstros) > 0 and monstros[0].resistencia!= "Físico":
            print(f"O "+ '{}Guerreiro{}'.format('\033[4;34m', '\033[m') +" ataca o "+monstros[0].classe+f" inimigo com {self.dano} de dano "+ '{}físico{}'.format('\033[4;34m', '\033[m'))
            monstros[0].atualizar(monstros[0].vida - self.dano)
        elif len(monstros) > 0:
            print(f"O "+ '{}Guerreiro{}'.format('\033[4;34m', '\033[m') +" ataca o "+monstros[0].classe+" inimigo com "+ str(self.dano * 0.5) +" de dano "+ '{}físico{}'.format('\033[4;34m', '\033[m'))
            monstros[0].atualizar(monstros[0].vida - (self.dano * (monstros[0].porcentagemres / 100)))

        if len(monstros) > 1 and monstros[1].resistencia!= "Físico":
            print(f"O "+ '{}Guerreiro{}'.format('\033[4;34m', '\033[m') +" ataca o "+monstros[1].classe+f" inimigo com {self.dano} de dano "+ '{}físico{}'.format('\033[4;34m', '\033[m'))
            monstros[1].atualizar(monstros[1].vida - self.dano)
        elif len(monstros) > 1:
            print(f"O "+ '{}Guerreiro{}'.format('\033[4;34m', '\033[m') +" ataca o "+monstros[1].classe+" inimigo com "+ str(self.dano * 0.5) +" de dano "+ '{}físico{}'.format('\033[4;34m', '\033[m'))
            monstros[1].atualizar(monstros[1].vida - (self.dano * (monstros[1].porcentagemres / 100)))

    def pintar(self):
        return ("\033[4;34m"+ self.classe+ 's' +"\033[m")

def seleciona_monstro():
    x = random.randrange(0,3)
    if x == 0:
        return monstro("Dragão", 12, 50, "Mágico")
    elif x == 1:
        return monstro("Orc", 6, 50, "Físico")
    else:
        return monstro("Morto_vivo", 8, 50, "Veneno")

def cria_lista_monstro(nivel):
    nivel = nivel + 3
    inimigos = []
    for x in range(nivel):
        inimigos.append(seleciona_monstro())
    return inimigos

def verifica(monstros):
    x = 0
    while x < len(monstros):
        if monstros[x].vida <= 0:
            monstros.pop(x)
        else:
            x = x + 1
    return monstros

def print_monstros(inimigos):
    l = 1
    print("Ordem do   Tipo de      Vida do\n monstro   monstro      monstro")
    for x in inimigos:
        if x.classe == "Dragão":
            print(" ", l, "        " + '{}Dragão{}'.format('\033[4;31m', '\033[m') + "      ", x.vida)
        elif x.classe == "Orc":
            print(" ", l, "        " + '{}Orc{}'.format('\033[4;32m', '\033[m') + "          ", x.vida)
        else:
            print(" ", l, "        " + '{}Morto_Vivo{}'.format('\033[4;35m', '\033[m') + "   ", x.vida)
        l = l +1

def cria_lista_aventureiros():
    avent = []
    avent.append([Druida(), 0])
    avent.append([Mago(), 0])
    avent.append([Guerreiro(), 0])
    return avent

def soma(avent):
    soma = 0
    for x in avent:
        soma = soma + x[1]
    return soma

def dificuldade_esc(dificuldade, x):
    print("----------------------------------")
    avent = cria_lista_aventureiros()
    i = 0
    while i < len(avent):
        print("Você tem " + str(x - soma(avent)) + " aventureiros para escolher!")
        print("Quantos " + avent[i][0].pintar() +" você gostaria na sua party?")
        avent[i][1] = int(input())

        if soma(avent) > x:
            print("------------------------------------------------------------------------")
            print('\033[0;30;41mALERTA--Quantidade de aventureiros excede a dificuldade escolhida!!--ALERTA\033[m')
            print("------------------------------------------------------------------------")
            print("Gostaria de voltar ao menu principal?")
            print("1- Sim!")
            print("2- Não!")
            esc = int(input())
            if esc == 1:
                main()
            else:
                print("--------------")
                print(".........")
                print("--------------")
        else:
            i+=1

    return avent

def masmorra(dificuldade, grupo, nivel):
    print('{}      ____________________      {}'.format('\033[4;33m', '\033[m'))
    print("")
    print("        Masmorra nível: " + str(nivel))
    print('{}      ____________________      {}'.format('\033[4;33m', '\033[m'))
    monstros = cria_lista_monstro(nivel)
    copia = copy.deepcopy(grupo)
    while soma(copia) != 0:
        print_monstros(monstros)
        print("----------------------------------")
        l = 0
        while l < len(copia):
            if copia[l][1] > 0:
                print(str(l+1) + ". Você tem " + str(copia[l][1]) + " " + copia[l][0].pintar())
            l+=1
        print("Quem irá atacar?")
        escolha = input()
        os.system('cls' if os.name == 'nt' else 'clear')
        if int(escolha) == 1 and copia[0][1] > 0:
            print("---------------------Registro de Batalha---------------------")
            copia[0][0].ataque(monstros)
            print("-------------------------------------------------------------")
            copia[0][1]-=1
        elif int(escolha) == 2 and copia[1][1] > 0:
            print("---------------------Registro de Batalha---------------------")
            copia[1][0].ataque(monstros)
            print("-------------------------------------------------------------")
            copia[1][1]-=1
        elif int(escolha) == 3 and copia[2][1] > 0:
            print("---------------------Registro de Batalha---------------------")
            copia[2][0].ataque(monstros)
            print("-------------------------------------------------------------")
            copia[2][1]-=1
        else:
            print("--------------------------------------------------------")
            print('{}    Você não possui aventureiros na classe escolhida!!{}'.format('\033[4;33m', '\033[m'))
            print("--------------------------------------------------------")

        monstros = verifica(monstros)

        if monstros == []:
            os.system('cls' if os.name == 'nt' else 'clear')
            return masmorra(dificuldade, grupo, nivel + 1)

    if dificuldade == 1:
        dificuldade = "Fácil"
    elif dificuldade == 2:
        dificuldade = "Médio"
    else:
        dificuldade = "Difícil"

    os.system('cls' if os.name == 'nt' else 'clear')
    print("--------------------------------------------------")
    print('\033[0;30;41mYOU DIED\033[m')
    print("Nível alcançado: " + str(nivel) + "\nDificuldade escolhida: " + dificuldade)
    print("--------------------------------------------------")



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("BEM VINDO AVENTUREIRO")
    print("Dificuldades:")
    print("----------------------------")
    print("1: Fácil -  30 aventureiros")
    print("2: Médio -  20 aventureiros")
    print("3: Difícil - 10 aventureiros")
    print("4: Sair")
    print("----------------------------")
    print("Entre com a dificuldade:")
    dificuldade = int(input())
    if dificuldade == 1:
        grupo = dificuldade_esc(dificuldade, 30)
    elif dificuldade == 2:
        grupo = dificuldade_esc(dificuldade, 20)
    elif dificuldade == 3:
        grupo = dificuldade_esc(dificuldade, 10)
    elif dificuldade == 4:
        print("-----------------------")
        print("Até mais aventureiro!!")
        return 0
    else:
        print("------------------------------------------------------------------------")
        print('\033[0;30;41mALERTA--Dificuldade escolhida não existente!!--ALERTA\033[m')
        print("Aperte enter para continuar")
        input()
        main()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Boa sorte em sua aventura, que os Deuses o acompanhe!")
    masmorra(dificuldade,grupo,1)


main()
