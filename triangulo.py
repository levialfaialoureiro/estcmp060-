import turtle

#Cria a Caneta e a Tela
caneta_tartaruga = turtle.Turtle()
tela = turtle.Screen()

def triangulo(posiçaox,posiçaoy):
    # "Abre" a caneta e move ela para a posição do mouse
    # e depois "fecha a caneta"
    caneta_tartaruga.penup()
    caneta_tartaruga.goto(posiçaox,posiçaoy)
    caneta_tartaruga.pendown()
    for i in range(3):

        # Faz com que a caneta se movimente na tela,
        # para frente,100 posições
        caneta_tartaruga.forward(100)
        # Gira o ponteiro em 120 graus para a esquerda.
        caneta_tartaruga.left(120)
        #Novamente a caneta se movimenta para a frente.
        caneta_tartaruga.forward(100)

#Envia a posição atual do click do mouse
# para que faça o triangulo.
turtle.onscreenclick(triangulo,1)
turtle.listen()

#Pausar o programa
turtle.done()