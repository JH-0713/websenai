import random
from time import sleep

print("                                                                      Jogo:")
print("                                                               Pedra Papel Tesoura")
print("")
print("")
print("")
print("")
print("")
print("")
print("Clique em Qualquer Tecla:")
input("-")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Regras:")
print("1º o Player tem 3 Opções Pedra✊ Papel✋ e Tesoura✌")
print("2º Com a ordem:")
print("            Pedra ganha de Tesoura")
print("            Papel ganha de Pedra")
print("            Tesoura ganha de Pepel")
print("                      OU")
print("(...) → PEDRA → TESOURA → PAPEL → PEDRA → (...)")
print("")
print("3º Comforme a ordem, tente ganhar o Jogo")
print("")
print("")
print("Clique em Qualquer Tecla:")
input("-")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
x2 = 0
pj1 = [0]
pcp1 = [0]


# Player:",pj1,"Cpu:",pcpu1)
def vitoria_p1():
    pri1 = pj1[0]
    calc1 = pri1 + 1
    pj1 = [calc1]
    return pj1


def vitoria_cpu1():
    pri2 = pcp1[0]
    calc1 = pri2 + 1
    pcp1 = [calc1]
    return pcp1


def msg():
    while True:
        print("")
        print("Continuar(s/n)")
        print("")
        nome = input("")
        if nome == "s" or nome == "S" or nome == "sim" or nome == "Sim" or nome == "SIM":
            print("")
            print("OK")
            break
        elif nome == "n" or nome == "N" or nome == "nao" or nome == "não" or nome == "Nao" or nome == "Não" or nome == "NAO" or nome == "NÃO":
            print("")
            break


def ppt(x2):
    while True:
        x2 += 1
        if x2 == 1:
            print("")
            print("Preparar")
            sleep(0.6)
            print("")
            print("Apontar")
            sleep(0.6)
            print("")
            print("Já!")
            sleep(0.5)
            print("")
            print("Pedra")
            sleep(0.3)
            print("")
            print("Papel")
            sleep(0.3)
            print("")
            print("Tesoura")
            sleep(0.3)
            print("")
            break


while True:
    num1 = random.randint(1, 3)
    print("")
    print("Escolha:")
    print("")
    print("[1] Pedra")
    print("[2] Papel")
    print("[3] Tesoura")
    print("[4] Placar[OFF]:")
    print("")
    jogo = ["Pedra", "Papel", "Tesoura"]
    esc1 = input("-")
    print("")
    if esc1 == "1":
        ppt(x2)
        print("Player: Pedra")
        sleep(0.4)
        if num1 == 1:
            print("CPU: Pedra")
            sleep(0.4)
            print("Empate")
            sleep(1)
            print("")
            msg()

        elif num1 == 2:
            print("CPU: Papel")
            sleep(0.4)
            print("CPU Wins")
            sleep(1)
            print("")
            vitoria_p1()
            msg()


        elif num1 == 3:
            print("CPU: Tesoura")
            sleep(0.4)
            print("Player Wins")
            sleep(1)
            print("")
            vitoria_cpu1()
            msg()




    elif esc1 == "2":
        ppt(x2)
        print("Player: Papel")
        sleep(0.4)
        if num1 == 1:
            print("CPU: Pedra")
            sleep(0.4)
            print("Player Wins")
            sleep(1)
            print("")
            vitoria_p1()
            msg()

        elif num1 == 2:
            print("CPU: Papel")
            sleep(0.4)
            print("Empate")
            sleep(1)
            print("")
            msg()

        elif num1 == 3:
            print("CPU: Tesoura")
            sleep(0.4)
            print("CPU Wins")
            sleep(1)
            print("")
            vitoria_cpu1()
            msg()

    elif esc1 == "3":
        ppt(x2)
        print("Player: Tesoura")
        sleep(0.4)
        if num1 == 1:
            print("CPU: Pedra")
            sleep(0.4)
            print("CPU Wins")
            sleep(1)
            print("")
            vitoria_cpu1()
            msg()

        elif num1 == 2:
            print("CPU: Papel")
            sleep(0.4)
            print("Player Wins")
            sleep(1)
            print("")
            vitoria_p1()
            msg()

        elif num1 == 3:
            print("CPU: Tesoura")
            sleep(0.4)
            print("Empate")
            sleep(1)
            print("")
            msg()

    elif esc1 == "4":
        num1 = random.randint(1, 3)
        print("")
        print("Escolha:")
        print("")
        print("[1] Pedra")
        print("[2] Papel")
        print("[3] Tesoura")
        print(f"[4] Placar[ON]: Player:{pj1} Cpu:{pcp1}")
        print("")
        jogo = ["Pedra", "Papel", "Tesoura"]
        esc1 = input("-")
        print("")
        if esc1 == "1":
            ppt(x2)
            print("Player: Pedra")
            sleep(0.4)
            if num1 == 1:
                print("CPU: Pedra")
                sleep(0.4)
                print("Empate")
                sleep(1)
                print("")
                msg()

            elif num1 == 2:
                print("CPU: Papel")
                sleep(0.4)
                print("CPU Wins")
                sleep(1)
                print("")
                vitoria_cpu1()
                msg()

            elif num1 == 3:
                print("CPU: Tesoura")
                sleep(0.4)
                print("Player Wins")
                sleep(1)
                print("")
                vitoria_p1()
                msg()


        elif esc1 == "2":
            ppt(x2)
            print("Player: Papel")
            sleep(0.4)
            if num1 == 1:
                print("CPU: Pedra")
                sleep(0.4)
                print("Player Wins")
                sleep(1)
                print("")
                vitoria_p1()
                msg()

            elif num1 == 2:
                print("CPU: Papel")
                sleep(0.4)
                print("Empate")
                sleep(1)
                print("")
                msg()

            elif num1 == 3:
                print("CPU: Tesoura")
                sleep(0.4)
                print("CPU Wins")
                sleep(1)
                print("")
                vitoria_cpu1()
                msg()

        elif esc1 == "3":
            ppt(x2)
            print("Player: Tesoura")
            sleep(0.4)
            if num1 == 1:
                print("CPU: Pedra")
                sleep(0.4)
                print("CPU Wins")
                sleep(1)
                print("")
                vitoria_cpu1()
                msg()

            elif num1 == 2:
                print("CPU: Papel")
                sleep(0.4)
                print("Player Wins")
                sleep(1)
                print("")
                vitoria_p1()
                msg()

            elif num1 == 3:
                print("CPU: Tesoura")
                sleep(0.4)
                print("Empate")
                sleep(1)
                print("")
                msg()