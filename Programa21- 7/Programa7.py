'''
 Universidade Tecnológica Federal do Paraná
 Aluno: Clodoaldo A. Basaglia da Fonseca
 RA: 968692
 Engenharia de Software 2
'''
import sys, math
from Simpson import Simpson
from Simpson_Inv import SimpsonInv
import numpy as np

'''
IN: vetor de valores
Split em virgulas para separar os valores de X e Y
OUT: tupla com valores de X e Y
'''
def valoresDeXeY(conteudo):
    x=[]
    y=[]
    for i in conteudo:
        aux=i.split(",")
        if(aux!=['']):
            x.append(int(aux[0]))
            y.append(int(aux[1]))
    return x,y

'''
IN: vetor de valores
Calcula o valor da média
OUT: media
'''
def media(var):
    sum = 0
    for i in var:
        sum = sum + int(i)
    return sum/len(var)

'''
IN: Vetor
Faz uma somatoria de todos os valores do vetor elevados ao quadrado
'''
def somatoriaQuadrado(var):
    somatoria = 0
    for i in var:
        somatoria = somatoria + (i**2)
    return somatoria
'''
IN: Vetor
Faz uma somatoria de todos os valores do vetor multiplicados um pelo outro
'''
def somatoriaProduto(varX,varY):
    somatoriaProduto = 0
    for i in range(0,len(varX)):
        somatoriaProduto = somatoriaProduto + (varX[i]*varY[i])
    return somatoriaProduto

'''
IN: VetorX, VetorY
Faz um somatorio dos valores dos vetor de X e Y separadamente
'''
def somatorio(varX,varY):
    somaX,somaY=0,0
    for i in range(0,len(varX)):
        somaX = somaX + int(varX[i])
        somaY = somaY + int(varY[i])
    return somaX,somaY

'''
IN: N - numero de entradas, somatorioX - somatorio dos valores X, somatorioY - somatorio dos valores Y
    xQuadrado - soma dos valores de X elevados ao quadrado
    yQuadrado - soma dos valores de y elevados ao quadrado
    produtoXeY - valores de X multiplicados por Y
Retorna o R calculado
'''
def calcR(n,somatorioX,somatorioY,xQuadrado,yQuadrado,produtoXeY):
    ptBaixo=1
    ptCima = ((n*produtoXeY)-(somatorioX*somatorioY))
    ptBaixo = (((n*xQuadrado)-(somatorioX**2))-((n*yQuadrado)-(somatorioY**2)))
    return ptCima/ptBaixo


def calcBeta1(produtoXeY,n,xAvarage,yAvarage,xQuadrado):
    beta1 = 0
    beta1 = (produtoXeY-(n*xAvarage*yAvarage))/(xQuadrado-(n*xAvarage**2))
    return beta1

def calcBeta0(yAvarage,beta1,xAvarage):
    return (yAvarage-(beta1*xAvarage))

def somatoriaLn(valores):
    som = 0
    for i in valores:
        som = som + np.log(i)
    return som

def mediaLn(sumLn,n):
    return sumLn/n

def variancia(valores,n,avg):
    som = 0
    for i in valores:
        som = som +(math.pow(np.log(i)-avg,2))
    var = som /(n-1)
    return var
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


def valorX(n,rxy):
    ptCima = math.fabs(rxy)*math.sqrt(n-2)
    ptBaixo = math.sqrt(1-(rxy**2))
    return ptCima/ptBaixo

def somatorioSimples(x):
    somatorio = 0
    for i in x:
        somatorio += i
    return somatorio
def somatorioValAvg(x,avg):
    som = 0
    for i in x:
        som = som + ((i-avg)**2)
    return som
def funcaoEstranha(n,x,xk,avg):
    sva = somatorioValAvg(x,avg)
    ptcima = (xk-avg)**2
    saida = math.sqrt(1+(1/n)+(ptcima/sva))
    return saida


def main():
    xk= 386
    arq = sys.argv[1]
    conteudo = abrirArquivo(arq)
    x,y=valoresDeXeY(conteudo)
    rxy = calcR(len(x),somatorioSimples(x),somatorioSimples(y),somatoriaQuadrado(x),somatoriaQuadrado(y),somatoriaProduto(x,y))
    xCalc = valorX(len(x),rxy)
    simpson  = Simpson(0,xCalc,len(x),1000).calc();
    simpsonInv = SimpsonInv(xCalc,len(x),0.35, eRR=0.0001, num_seg=2).find_P()
    funcE = funcaoEstranha(len(x),x,xk,media(x))
    range = simpsonInv[0]*math.sqrt(variancia(x,len(x),media(x)))*funcE
    print("Resultado é: "+str(range))

main()
