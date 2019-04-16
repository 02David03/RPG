from contadorPTs import  *
class Vida(Contador):
    def __init__(self):
        Contador.__init__(self, pontuacao = 60,limite = 60)

    def mensagemMorte(self):
        if self.__pontuacao <= 0:
            print('Você Morreu, e você perdeu todos os seus pertences ')


