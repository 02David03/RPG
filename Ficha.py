from Nivel import Nivel
class Ficha:

    def __init__(self,nomep,nomej,raca,classe,vida =60, mana = 60, nivel = 1, dinheiro = 400):
        self.__nomeP = nomep
        self.__nomeJ = nomej
        self.__raca = raca
        self.__classe = classe
        self.__vida = vida
        self.__mana = mana
        self.__nivel = nivel
        self.__dinheiro = dinheiro
    def getNomep(self):
        return  self.__nomeP

    def getNomeJ(self):
        return  self.__nomeJ

    def getRaca(self):
        return  self.__raca

    def getClasse(self):
        return  self.__classe

    def getNivel(self):
        return self.__nivel

    def getDinheiro(self):
        return  self.__dinheiro

    def getVida(self):
        return self.__vida

    def getMana(self):
        return  self.__mana







