import sys, math
import numpy as np

def abrirArquivo(caminho):
    file = open(caminho, "r")
    conteudo = file.read()
    conteudo = conteudo.split('\n')
    return conteudo

def intervalo(conteudo):
    intervalo=[]
    aux = conteudo.split(',')
    intervalo = aux[0].split(' ')
    return float(intervalo[0]),float(intervalo[len(intervalo)-1])

def degreesOfFreedom(conteudo):
    aux = conteudo.split(',')
    return int(aux[1])

def pEsperado(conteudo):
    aux = conteudo.split(',')
    return float(aux[2])

def funcGammaInt(valor):
    if valor == 1:
        return valor
    else:
        return (valor * funcGammaInt(valor - 1))

def funcGamma(valor):
    if not float(valor).is_integer():
        if math.isclose(valor, (1 / 2)):
            return ((math.pi ** 0.5))
        else:
            return((valor - 1) * funcGamma((valor - 1)))
    else:
        return funcGammaInt(valor - 1)

def funcaoFx(valor):
    fxp1 = funcGamma((degreesOfFreedom+1.0)/2)
    fxp2 = (
    ((degreesOfFreedom*math.pi)**0.5)*funcGamma(degreesOfFreedom/2.0)
    )
    fxp3 = (
    ((1.0+((valor**2.0)/degreesOfFreedom))**-((degreesOfFreedom+1.0)/2.0))
    )
    fResultado = (fxp1/fxp2)*fxp3
    return fResultado

def  Simpson(xInicio,xFinal,dof,pResp,erro,nSegmentos):
    w = xFinal/nSegmentos
    part1 = funcaoFx(0.0)
    part2= 0.0
    part3=0.0
    part4 = funcaoFx(xFinal)
    for i in range(1,nSegmentos-1,2):
        part2+=(4.0*funcaoFx(i*w))
    for i in range(2, nSegmentos-2,2):
        part3+=(2.0*funcaoFx(i*w))

    pResultado = (
        (w/3)*
        (part1+part2+part3+part4)
        )
    return pResultado

def calcSimpson(xInicio,xFinal,dof,pResp,erro,nSegmentos):
    anterior = Simpson(xInicio,xFinal,dof,pResp,erro,nSegmentos)
    nSegmentos *=2
    atual = Simpson(xInicio,xFinal,dof,pResp,erro,nSegmentos)
    while((anterior - atual)>erro):
        nSegmentos *= 2
        anterior = atual
        atual = Simpson(xInicio,xFinal,dof,pResp,erro,nSegmentos)
    return atual


def main():
    erro =  0.00001
    nSegmentos =  100
    arq = sys.argv[1]
    conteudo = abrirArquivo(arq)
    for i in range(0,len(conteudo)):
        if(conteudo[i]!=''):
            xInicio,xFinal = intervalo(conteudo[i])
            dof = degreesOfFreedom(conteudo[i])
            pResp = pEsperado(conteudo[i])
            resultado = calcSimpson(xInicio,xFinal,dof,pResp,erro,nSegmentos)
            print(resultado)
main()
