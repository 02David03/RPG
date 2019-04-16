class Contador:

    def __init__(self,pontuacao,limite = 60):
        self.__limite = limite
        self.__pontuacao = pontuacao

    def perca(self,quantidade):
        self.__pontuacao = self.__pontuacao - quantidade

    def ganho(self,quantidade):
        self.__pontuacao = self.__pontuacao + quantidade
        self.limitar()

    def mudarLimite(self,limite):
        self.__limite = limite

    def limitar(self):
        if self.__pontuacao > self.__limite:
            self.__pontuacao = self.__limite


