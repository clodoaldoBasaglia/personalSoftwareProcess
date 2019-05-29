'''
 Universidade Tecnológica Federal do Paraná
 Aluno: Clodoaldo A. Basaglia da Fonseca
 RA: 968692
 Engenharia de Software 2
'''
import sys, math

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
IN: VetorX, VetorY
Faz uma somatoria de todos os valores dos vetores multiplicados entre si
'''
def somatoriaProduto(varX,varY):
    somatoriaProduto = 0
    for i in range(0,len(varX)):
        somatoriaProduto = somatoriaProduto + (varX[i]*varY[i])
    return somatoriaProduto

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

'''IN: produtoXeY - multiplicação de X e Y
    n - número de entradas
    xAvarage - valores medios de X
    yAvarage - valores medios de y
    xQuadrado - valores de x ao quadrado
'''
def calcBeta1(produtoXeY,n,xAvarage,yAvarage,xQuadrado):
    beta1 = 0
    beta1 = (produtoXeY-(n*xAvarage*yAvarage))/(xQuadrado-(n*xAvarage**2))
    return beta1

def calcBeta0(yAvarage,beta1,xAvarage):
    return (yAvarage-(beta1*xAvarage))

def main():
    xKa = 386
    arq = sys.argv[1]
    conteudo = abrirArquivo(arq)
    varX,varY = valoresDeXeY(conteudo)
    xAvarage = media(varX)
    somatorioX,somatorioY = somatorio(varX,varY)
    yAvarage = media(varY)
    xQuadrado = somatoriaQuadrado(varX)
    yQuadrado = somatoriaQuadrado(varY)
    produtoXeY = somatoriaProduto(varX,varY)
    beta1 = calcBeta1(produtoXeY,len(varX),xAvarage,yAvarage,xQuadrado)
    beta0 = calcBeta0(yAvarage,beta1,xAvarage)
    rQuadrado = calcR(len(varX),somatorioX,somatorioY,xQuadrado,yQuadrado,produtoXeY)**2
    yKa = beta0 - beta1*xKa
    print("Resultado: "+str(yKa))
main()
