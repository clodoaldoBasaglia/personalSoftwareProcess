import math, sys

def abrirArquivo(caminho):
    file = open(caminho, "r")
    conteudo = file.read()
    conteudo = conteudo.split('\n')
    return conteudo

def contaLinhasDeCodigo(conteudo):
    cont = 0
    for i in conteudo:
        if(not i.split()==[]):
            cont = cont+1
        else:
            continue
    return cont

def contaFuncoes(conteudo):
    cont = 0
    for i in conteudo:
        if("def" in i):
            cont = cont + 1
        else:
            continue
    return cont

def nomesFuncoes(conteudo):
    nomeFuncoes = []
    for i in conteudo:
        if("def" in i):
            inicio = i.index("def")
            fim = i.index(":")
            nomeFuncoes.append(i[inicio+3:fim])
    return nomeFuncoes

def linhasComentadas(conteudo):
    cont = 0
    for i in conteudo:
        if("#" in i):
            cont = cont+1
    return cont


def main():
    arq = sys.argv[1]
    conteudo = abrirArquivo(arq)
    nLinhas = contaLinhasDeCodigo(conteudo)
    nFuncoes = contaFuncoes(conteudo)
    listaNomes = nomesFuncoes(conteudo)
    nLinhasComentadas = linhasComentadas(conteudo)
    print("Linhas do código: "+str(nLinhas))
    print("Número de funções: "+str(nFuncoes))
    print("Número de funções: "+str(listaNomes))
    print("Número de linhas comentadas: "+str(nLinhasComentadas))
main()
