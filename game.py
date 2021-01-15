from code import *
import sys,os
import time as t

def limpar():
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('win32'):
        os.system('cls')

def sair():
    if sys.platform.startswith('linux'):
        os.system('exit')
    elif sys.platform.startswith('win32'):
        os.system('exit')

def delay(time):
    t.sleep(time) 

# Inicialização
pl = Palavra()
limpar()
print('Bem vindo ao game de adivinhação!')
delay(3)
limpar()
valido = False

# loop principal
while not valido:
    print(pl.palavra)
    print(pl.imprime())
    escolha = input('Digite sair,dica ou uma letra: ')

    if escolha in pl.palavra:
        pl.mostraLetra(escolha)
    elif escolha == 'dica':
        print(f'Essa plavra possui algum {pl.dica()}')
        delay(3)
    elif escolha == 'sair':
        print(f'Já vai? Que pena a palavra escondida era "{pl.palavra}"')
        delay(5)
        sair()
    else:
        print(f'Que pena parece que não há nenhuma "{escolha}" nessa palavra')
        delay(5)
    if not '_' in pl.palavraOculta:
        valido = True
    limpar()

print(f"""Parabrens você acertou a palavra e como bonus fique com a descrição dela:

{pl.descrissaoPalavra()}
""")