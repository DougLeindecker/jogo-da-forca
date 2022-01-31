"""Jogo da forca"""
class Forca:
    tentativa = 10
    nao = []
    sim = []
    frase = 'cabeça'
    def __init__(self, chute):
        self.__chute = chute

    def Checar(self):
        certo = []
        soma =''
        if self.__chute in Forca.frase:
            print(f'({self.__chute}) está na palavra')
            Forca.sim.append(self.__chute)
            certo.append(self.__chute)
            """Condição para ganhar"""
            for i in sorted(Forca.frase):
                for x in sorted(certo):
                    if x == i and len(Forca.sim) == len(Forca.frase):
                        print('Ganhou')
        else:
            print(f'({self.__chute}) não está na palavra')
            Forca.tentativa -= 1
            resto = 10 - Forca.tentativa
            print(f'Perdeu um(a) {resto}/10 tentativa')
            if resto == 10:
                print("Acabou as tentativas, você perdeu")

while True:
    jogo = Forca(input('Chute uma letra:\t'))
    jogo.Checar()
    if Forca.tentativa == 0 or len(Forca.sim) == len(Forca.frase):
        break
