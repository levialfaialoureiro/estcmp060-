import turtle
import math

def FibonacciPloting(t):
    a = 0
    b = 1
    quadrado_a = a
    quadrado_b = b

    #Alterando a cor da caneta para verde
    caneta.pencolor("green")

    #Desenhando o primeiro quadrado
    caneta.forward(b * factor)
    caneta.left(90)
    caneta.forward(b * factor)
    caneta.left(90)
    caneta.forward(b * factor)
    caneta.left(90)
    caneta.forward(b * factor)

    #Executando a sequência de Fibonacci
    temp = quadrado_b
    quadrado_b  += quadrado_a
    quadrado_a = temp

    #Desenhando os outros quadrados
    for i in range(1,t):
        caneta.backward(quadrado_a * factor)
        caneta.right(90)
        caneta.forward(quadrado_b * factor)
        caneta.left(90)
        caneta.forward(quadrado_a * factor)
        caneta.left(90)
        caneta.forward(quadrado_b * factor)

        #Atualiza Fibonacci
        temp = quadrado_b
        quadrado_b += quadrado_a
        quadrado_a = temp

    #Traz a caneta para o ponto inicial da espiral
    caneta.penup()
    caneta.setposition(factor, 0)
    caneta.seth(0)
    caneta.pendown()

    #Trocando a cor da caneta para azul
    caneta.pencolor("blue")

    #roteiro da espiral de fibonacci
    caneta.left(90)
    for i in range(t):
        print(b)
        fdwd = pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            caneta.forward(fdwd)
            caneta.left(1)
        temp = a
        a = b
        b += temp

#Valor do pi matemático
pi = math.pi

#Aqui o fator significa o fator multiplicativo que
# expande ou encolhe a escala do plot
# por um certo fator.
factor = 1

#Interação com Usuário
t = int(input("Digite um número de iterações(tem que ser maior que 1: "))

#Guia da espiral e faz aparecer na tela o número de Fibonacci correspondente
if t > 0:
    print("Série de Fibonacci por", t,"elementos:")
    caneta = turtle.Turtle()
    caneta.speed(100)
    FibonacciPloting(t)
    turtle.done()
else:
    print("Numero de iterações tem que ser maior que 0.")