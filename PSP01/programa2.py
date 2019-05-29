'''
 Universidade Tecnológica Federal do Paraná
 Aluno: Clodoaldo A. Basaglia da Fonseca
 RA: 968692
 Engenharia de Software 2
'''
import math, sys

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
IN: Vetor de valores
Conta as linhas com código, linhas em branco são ignoradas
OUT: cont
'''
def contaLinhasDeCodigo(conteudo):
    cont = 0
    for i in conteudo:
        if(not i.split()==[]):
            cont = cont+1
        else:
            continue
    return cont

'''
IN: vetor com as linhas de código
Conta as funções presentes
OUT: cont
'''
def contaFuncoes(conteudo):
    cont = 0
    for i in conteudo:
        if("def" in i):
            cont = cont + 1
        else:
            continue
    return cont
'''
IN: vetor de valores
Salva os nomes das funções em um vetor
OUT: vetor com os nomes
'''
def nomesFuncoes(conteudo):
    nomeFuncoes = []
    for i in conteudo:
        if("def" in i):
            inicio = i.index("def")
            fim = i.index(":")
            nomeFuncoes.append(i[inicio+3:fim])
    return nomeFuncoes

'''
IN: vetor de valores
Conta as linhas comentadas utilziando o #
OUT: cont
'''
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
