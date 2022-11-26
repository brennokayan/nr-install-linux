from math import *
import sympy as sp
# funcao = ''
# derivada = '' 

count = 0
x0 = 0 
resultadoDerivada = 0
resultadoFuncao = 0
parada = 0 


def EntradaDeDados():
    global funx, parada, xo
    funx = input("Digite a Função de x: \n")
    parada = input("Digite o valor de parada: ")
    xo = input("x = ")


def ValueFuncao():
    x = sp.symbols("x")
    funcao = compile(str(funx), "<string>", "eval")
    x = xo
    x = float(x)
    resultadoFuncao = (eval(funcao))
    return resultadoFuncao


def ValueDerivada():
    x = sp.symbols("x")
    derivada = (sp.diff(funx,x))
    x = xo
    x = float(x)
    derivada = compile(str(derivada), "<string>", "eval")
    resultadoDerivada = (eval(derivada))
    return resultadoDerivada

def MetodoNewthonRaphson():
    global count
    global parada
    count = count + 1
    global xo
    print(90*"#", "\n")
    print(count,"° Interação")
    resultadoFuncao = ValueFuncao()
    resultadoDerivada = ValueDerivada()
    print("Resultado da função: ",resultadoFuncao, "\nResultado da derivada: ",resultadoDerivada)
    xi = eval(str(resultadoFuncao / resultadoDerivada))
    xo = float(xo) - xi
    print(xo)
    print(90*"#", "\n")
    if(abs(xo) >= float(parada) ):
        MetodoNewthonRaphson()
    else:
        print("rola")

EntradaDeDados()
MetodoNewthonRaphson()
input("press enter to exit")

