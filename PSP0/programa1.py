'''
 Universidade Tecnológica Federal do Paraná
 Aluno: Clodoaldo A. Basaglia da Fonseca
 RA: 968692
 Engenharia de Software 2
'''
import sys,math

'''
IN: vetor de valores
Calcula o valor da média
OUT: media
'''
def calcMedia(valores):
    n = len(valores)
    soma = 0
    for i in valores:
        soma = soma + i
    return soma/n

'''
IN: vetor de valores, media
Calcula o desvio padrão
OUT: saida
'''
def desvioPadrao(valores,media):
    saida = 0
    for i in valores:
        saida = saida + ((i-media)**2)
    saida = saida/len(valores)
    return math.sqrt(saida)

'''
IN: String com o caminho até o arquivo com valores
Recebe o caminho do arquivo, faz um split na quebra de linha e devolve um vetor
de valores
OUT: Vetor de valores
'''
def abrirArquivo(caminho):
    file = open(caminho, "r")
    conteudo = file.read()
    conteudo = conteudo.split(',')
    return conteudo

def main():
    arq = sys.argv[1]
    conteudo = abrirArquivo(arq)
    valores = []
    for i in conteudo:
        valores.append(int(i))
    print("Calculando média: ")
    media = calcMedia(valores)
    print("Média: "+str(media))
    print("Calculando Desvio Padrão...")
    desvio = desvioPadrao(valores,media)
    print("Desvio Padrão: "+str(desvio))
main()
