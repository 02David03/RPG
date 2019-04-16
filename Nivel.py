class Nivel:
    def __init__(self,adicionar):
        self.__nivel = 1
        self.__adicionar = -adicionar
        self.__limite = -10
        self.__valor = 0
        self.__restante = 0
        self.__oldNivel = 0

    def getNivel(self):
        return  self.__nivel

    def setNivel(self,nivel):
        self.__nivel = nivel

    def getLimite(self):
        return  self.__limite

    def setLimete(self,limite):
        self.__limite = limite

    def getValor(self):
        return self.__valor

    def setValor(self,valor):
        self.__valor = valor

    def getAdicionar(self):
        return self.__adicionar

    def setAdicionar(self,adicionar):
        self.__adicionar = -adicionar
        self.contadorLimite()

    def contadorLimite(self):
        self.__oldNivel = self.__nivel
        self.__valor = self.__valor - abs(self.__adicionar)
        self.__restante = 0

        print('Você Ganhou {} XPs'.format(abs(self.__adicionar)))

        if self.__valor <= (self.__limite) and self.__nivel < 5:
            print('Parabéns, você subiu de Nível!!')

            self.__restante = self.__valor - (self.__limite)
            self.__nivel +=1
            self.__valor = self.__restante

            self.limitandoLimite()

        if self.__nivel == 5:
            print('Você está no nível máximo, com {} XPs'.format(abs( self.__valor)))

        if self.__nivel < 5:
            print('Você tem {}/{} XP, e você está no Nível {}'.format(abs(self.__valor), abs(self.__limite), self.__nivel))

    def limitandoLimite(self):

        if self.__oldNivel + 1 == (self.__nivel) and self.__nivel < 5:
            self.__limite -= 2

        if self.__nivel == 5:
            self.__limite = 0


