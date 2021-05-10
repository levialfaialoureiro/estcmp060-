import turtle

#Angulo das ramificações
ang = 30

#Cria a caneta
caneta = turtle.Turtle()

#Altera a velocidade da caneta.
caneta.speed('fastest')

#Muda a direção da caneta para cima.
caneta.right(-90)

def arvoreY(size,level):

    if level > 0:
        turtle.colormode(255)
        #Altera a cor de acordo com nivel(altura)atual
        caneta.pencolor(0,255//level,0)

        #Faz a base
        caneta.forward(size)
        caneta.right(ang)

        #Cria os "galhos" da "arvore" e muda a cor
        arvoreY(0.8 * size, level-1)
        caneta.pencolor(0,255//level,0)

        caneta.left(2 * ang)
        arvoreY(0.8 * size,level-1)

        caneta.pencolor(0,255//level, 0)
        caneta.right(ang)
        caneta.forward(-size)



#Executa o processo.
arvoreY(80,7)