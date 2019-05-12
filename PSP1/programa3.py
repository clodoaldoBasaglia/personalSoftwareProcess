import sys, math

def valoresDeXeY(conteudo):
    x=[]
    y=[]
    for i in conteudo:
        aux=i.split(",")
        if(aux!=['']):
            x.append(int(aux[0]))
            y.append(int(aux[1]))
    return x,y

def media(var):
    sum = 0
    for i in var:
        sum = sum + int(i)
    return sum/len(var)

def somatoriaQuadrado(var):
    somatoria = 0
    for i in var:
        somatoria = somatoria + (i**2)
    return somatoria

def somatoriaProduto(varX,varY):
    somatoriaProduto = 0
    for i in range(0,len(varX)):
        somatoriaProduto = somatoriaProduto + (varX[i]*varY[i])
    return somatoriaProduto

def abrirArquivo(caminho):
    file = open(caminho, "r")
    conteudo = file.read()
    conteudo = conteudo.split('\n')
    return conteudo

def somatorio(varX,varY):
    somaX,somaY=0,0
    for i in range(0,len(varX)):
        somaX = somaX + int(varX[i])
        somaY = somaY + int(varY[i])
    return somaX,somaY

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
