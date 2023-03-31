import numpy as np
import pyttsx3
import speech_recognition as sr

audio = sr.Recognizer()
machine = pyttsx3.init()


def cerebro():
    machine.say('O que precisa?')
    machine.runAndWait()
    try:
        with sr.Microphone() as source:
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'padrão' in comando:
                machine.say('Boa sorte em suas atividades, usuário')
                machine.runAndWait()

            return comando
    except sr.UnknownValueError:
        machine.say('Não entendi o que você disse. Pode repetir, por favor?')
        machine.runAndWait()
        return cerebro()
    except sr.RequestError:
        machine.say('Não foi possível se comunicar com o microfone. Por favor, verifique se está conectado corretamente.')
        machine.runAndWait()
        return cerebro()


def corpo():
    comando = cerebro()
    if 'criar' in comando:
        machine.say('Criando Matriz')
        Matriz_Inversa()
        machine.runAndWait()

    elif 'explique' in comando:
        machine.say('O projeto minerva é um projeto ambicioso, que tem como intuito a criação de uma calculadora de Matriz Inversa, ela está acoplada com uma assistente virtual')
        machine.runAndWait()
        machine.say(',eu mesma a Minerva, e uma interface gráfica para melhor visualização do usuário')
        machine.runAndWait()
        machine.say('Infelizmente não tivemos tempo de melhorar o projeto no ponto que queríamos, mas ele foi feito com muito carinho, e determinação de todos os membros!')
        machine.runAndWait()
        return corpo()

    elif 'professora' in comando:
        machine.say('Acho que a professora Marcela é incrível e deveria dar 10 aos alunos ')
        machine.runAndWait()
        return corpo()

    elif 'adjunta' in comando:
        machine.say('uma matriz adjunta, é a transposta, de sua matriz dos cofatores.')
        machine.runAndWait()


    elif 'inversa' in comando:
        machine.say('A matriz inversa, ocorre quando o produto de duas matrizes resulta numa matriz identidade de mesma ordem')
        machine.runAndWait()


####################    INTELIGENCÊNCIA DA CALCULADORA  #########################

class MatrizInversa:

    def __init__(self):
        self.ordem = None
        self.linha = None
        self.coluna = None
        self.matriz = []

    def criaMatriz(self, valorOrdem, aux=[]):
        self.ordem = valorOrdem
        for i in range(0, self.ordem):
            aux = []
            for y in range(0, self.ordem):
                aux.append(0)
            self.matriz.append(aux)
        return self.matriz

    def exibeMatriz(self, valorMatriz):
        self.matriz = valorMatriz
        machine.say('Exibindo a Matriz')
        machine.runAndWait()
        for l in range(0, self.ordem):
            for c in range(0, self.ordem):
                print(f'{self.matriz[l][c]}', end=' ')
            print()
        print()

    def calculaDeterminante(self):
        # Calcula a Determinante
        detMatriz = np.linalg.det(self.matriz)
        machine.say('Resultado, da Determinante')
        machine.runAndWait()
        print(f'-->(Determinante): {round(detMatriz)}')
        print()

        if detMatriz == 0:
            machine.say('Como o resultado da determinante é 0, é Impossível de calcular a Matriz Inversa!')
            machine.runAndWait()
            return detMatriz
        else:
            return detMatriz

    def calculaCofator(self, determinante):
        # Calcula a Transposta
        matrizTransposta = np.linalg.inv(self.matriz).T

        # Calculamos a Matriz dos Cofatores
        cofatorMatriz = matrizTransposta * determinante
        machine.say('Resultado, da Matriz dos Cofatores')
        machine.runAndWait()
        print(f'-->(Matriz dos cofatores)\n {cofatorMatriz.round(2)}')
        print()
        return cofatorMatriz

    def calculaAdjunta(self, cofator):
        # Calcula a Matriz Adjunta
        adjuntaMatriz = cofator.T
        machine.say('Resultado, da Matriz Adjunta')
        machine.runAndWait()
        print(f'-->(Matriz Adjunta)\n {adjuntaMatriz.round(2)}')
        print()
        return adjuntaMatriz

    def calculaInversa(self, determinante, adjunta):
        # A-¹ = 1/det * adj
        matrizInversa = (1 / determinante) * adjunta
        machine.say('Resultado, da Matriz Inversa ')
        machine.runAndWait()
        print(f'-->(Matriz Inversa)\n {matrizInversa.round(2)} ')
        print()
        return matrizInversa

    def verificaResultado(self, inversa, matriz):
        testeMesa = np.dot(inversa, matriz)
        machine.say('Resultado, do teste de mesa')
        machine.runAndWait()
        print(f'-->(teste de mesa)\n {np.around(testeMesa)} ')
        print()
        return testeMesa


#########################################################       ENTRADA DE DADOS POR MEIO DO USUARIO         ########################################################

def Matriz_Inversa():
    m = MatrizInversa()
    machine.say('Digite o valor para a matriz quadrada na seta abaixo ')
    machine.runAndWait()
    valorOrdem = int(input(' --> '))
    valorMatriz = m.criaMatriz(valorOrdem)

    for l in range(0, valorOrdem):
        for c in range(0, valorOrdem):
            valorMatriz[l][c] = float(input(f'Digite um número para a posição {l + 1}x{c + 1}: '))

    print()
    m.exibeMatriz(valorMatriz)
    det = m.calculaDeterminante()

    if det != 0:
        cof = m.calculaCofator(det)
        adj = m.calculaAdjunta(cof)
        inv = m.calculaInversa(det, adj)
        teste = m.verificaResultado(inv, valorMatriz)

corpo()