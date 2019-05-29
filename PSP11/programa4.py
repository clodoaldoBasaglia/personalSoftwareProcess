'''
 Universidade Tecnológica Federal do Paraná
 Aluno: Clodoaldo A. Basaglia da Fonseca
 RA: 968692
 Engenharia de Software 2
'''
import sys, math
import numpy as np

'''
IN: String com o caminho até o arquivo com valores
Recebe o caminho do arquivo, faz um split na quebra de linha e devolve um vetor
de valores
OUT: Vetor de valores
'''
def abrirArquivo(caminho):
    file = open(caminho, "r")
    conteudo = file.read()
    conteudo = conteudo.split('\n')
    return conteudo

'''

'''
def getNomesValores(conteudo):
    nomes = []
    valores = []
    for i in conteudo:
        aux = i.split(',')
        if(aux!=['']):
            nomes.append(str(aux[0]))
            valores.append(int(aux[1]))
    return nomes,valores

'''
IN: valores
somatorio dos logaritmos de todos os valores
'''
def somatoriaLn(valores):
    som = 0
    for i in valores:
        som = som + np.log(i)
    return som

def media(sumLn,n):
    return sumLn/n

def variancia(valores,n,avg):
    som = 0
    for i in valores:
        som = som +(math.pow(np.log(i)-avg,2))
    var = som /(n-1)
    return var

def mostrarFaixas(desvioPadrao,avg):
    print("PP: "+str(avg-(2*desvioPadrao)))
    print("P: "+str(avg-desvioPadrao))
    print("M: "+str(avg))
    print("G: "+(str(avg+desvioPadrao)))
    print("GG: "+str(avg+2*desvioPadrao))

def main():
    arq = sys.argv[1]
    conteudo = abrirArquivo(arq)
    nomes,valores = getNomesValores(conteudo)
    avg = media(somatoriaLn(valores),len(valores))
    var = variancia(valores,len(valores),avg)
    desvioPadrao = math.sqrt(var)
    mostrarFaixas(desvioPadrao,avg)
main()
