import wikipedia as wiki
import random

class Palavra():

    def __init__(self):
        self.__palavra = self.wikiPalavra()
        self.__palavraOculta = self.ocultaPalavra(self.__palavra)

# Getters & Setters
    @property
    def palavra(self):
        return self.__palavra
    
    @palavra.setter
    def palavra(self,palavra):
        self.__palavra = palavra
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    @property
    def palavraOculta(self):
        return self.__palavraOculta
    
    @palavraOculta.setter
    def palavraOculta(self,palavraOculta):
        self.__palavraOculta = palavraOculta
    
# Methods

    @tamanho.setter
    def tamanho(self,tamanho):
        self.__tamanho = tamanho

    def wikiPalavra(self):
        wiki.set_lang('pt')  
        palavra = str(wiki.random(pages=1))
        return palavra.casefold()
        
    def dica(self):
        valido = False
        while not valido:
            dica = random.choice(self.palavra)
            if dica not in self.palavraOculta:
                valido = True

        return dica

    def imprime(self):
        molde = ''
        for item in self.__palavraOculta:
            molde += f'{item} '
        return molde

    def ocultaPalavra(self,palavra):
        palavraOculta = []
        listaPalavras = palavra.split()

        for item in listaPalavras:
            for letra in range(len(item)):
                palavraOculta.append('_')
            palavraOculta.append(' ')     

        return palavraOculta
            
    def mostraLetra(self,letra):
        for j in range(len(self.__palavra)):
            if self.__palavra[j] == letra:
                self.__palavraOculta[j] = letra

    def descrissaoPalavra(self):
        return wiki.summary(self.palavra)