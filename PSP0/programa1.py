import sys,math

def calcMedia(valores):
    n = len(valores)
    soma = 0
    for i in valores:
        soma = soma + i
    return soma/n

def desvioPadrao(valores,media):
    saida = 0
    for i in valores:
        saida = saida + ((i-media)**2)
    saida = saida/len(valores)
    return math.sqrt(saida)

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