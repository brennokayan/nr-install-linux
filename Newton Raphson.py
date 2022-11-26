#Importação
from math import *
import sympy as sp
#Fim da importação

#Inicio de declaração de de váriaveis
count = 0
x0 = 0 
resultadoDerivada = 0
resultadoFuncao = 0
parada = 0 
#Fim de declaração de de váriaveis

#Função de entrada de dados 
def EntradaDeDados():
    global funx, parada, xo #Chamada de váriaveis global
    funx = input("Digite a Função de x: \n") #Entrada da Função de x
    parada = input("Digite o valor de parada: ") #Entrada do eplison valor de parada
    xo = input("x = ") #Entrada do valor de xk-1 que vai ser utilizado como xk 

#Função para resolver a função de x 
def ValueFuncao():
    x = sp.symbols("x") #Chamada da biblioteca sympy chamando a função symbols para que x fique como símbole
    funcao = compile(str(funx), "<string>", "eval") #Váriavel funcao com compile para deixar a string pronta para eval
    x = xo #Variavel x recebe o xk
    x = float(x) #Variavel x transformação em float
    resultadoFuncao = (eval(funcao)) #Váriavel local result que é o retorno dessa função
    return resultadoFuncao #Returno da função em float ou int

#Função para resolver a função de x 
def ValueDerivada():
    x = sp.symbols("x") #Chamada da biblioteca sympy chamando a função symbols para que x fique como símbole
    derivada = (sp.diff(funx,x)) #Função local que chama biblioteca sympy chamando a função diff para fazer a derivada da função de x entrada no começo do código
    x = xo #Variavel x recebe o xk
    x = float(x) #Variavel x transformação em float
    derivada = compile(str(derivada), "<string>", "eval") #Váriavel funcao com compile para deixar a string pronta para eval
    resultadoDerivada = (eval(derivada)) #Váriavel local result que é o retorno dessa função
    return resultadoDerivada #Retorno da função em float ou int

#Função para resolver a derivada da função de x 
def MetodoNewthonRaphson():
    global count, parada, xo #Chamada de váriaveis global
    count = count + 1 #Somar mais 1 em números de interações
    print(90*"#", "\n") #imprimir 90 * #
    print(count,"° Interação") #Imprimir o Numero de Interações
    resultadoFuncao = ValueFuncao() #Var local chamando a função de calculo da função de x
    resultadoDerivada = ValueDerivada() #Var local chamando a função de calculo da derivada função de x
    print("Resultado da função: ",resultadoFuncao, "\nResultado da derivada: ",resultadoDerivada) # Imprimir o resultado
    xi = eval(str(resultadoFuncao / resultadoDerivada)) #váriavel local auxiliar para pegar o calculo da função divida pela derivada
    xo = float(xo) - xi #Variavel global que representa xk recebendo novo xk
    print(xo) #Imprimir novo xk 
    print(90*"#", "\n")#Imprimir 90 * #

    #Inicio do if para verificar se ainda deu parada 
    if(abs(ValueFuncao()) >= float(parada) ):
        MetodoNewthonRaphson()
    ##Fim do if de verificação de para

    #Inicio do else para quando verificação de parada está satisfeita
    else:
        print("rola")
    ##Fim do else de verificação de parada
    
EntradaDeDados() #Chamando a função de entrada de dados
MetodoNewthonRaphson() #Chamando a função de calculo do calculo em método de newthon Raphson
input("press enter to exit") #Para que o exe do código não pare quando executado

