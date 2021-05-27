#importamos la libreria para poder graficar
import matplotlib.pyplot as plt
#Preguntamos por medio de un mensaje porque metodo se va a resolver
#1 Algoritmo DDA
#2 Algoritmo Bresenhams
respuesta = int( input("Coloca 1 Si deceas ocupar el ALgoritmo DDA O 2 de Bresenhams para construir el Triangulo") )
if respuesta == 1:
    print("Algoritmo ADD")
    x1=1
    y1=2
    x2=6
    y2=7
    #calculamos la primera parte
    #calculamos la diferencia
    dx = x2-x1
    dy = y2-y1
    #calculamos la pendiente
    if dx !=0 :
        m = dy / dx
    else:
        print("No se puede realizar una operacion entre cero")
    #calculamos el valor de steps
    if(dx > dy):
        steps = dx
    else:
        steps = dy
    #Calculamos el incremento
    xinc = dx / steps
    yinc = dy / steps
    print(x1,y1)
    plt.scatter(x1,y1)
    #calculamos los nuevos valores de x y y
    i=1
    while(i<=steps):
        x1 = x1 + xinc
        y1 = y1 + yinc
        #Redondeamos los valores con el metodo round 
        x=round(x1)
        y=round(y1)
        i+=1
        print(x,y)
        plt.scatter(x,y)

    #calculamos la segunda parte
    x1=1
    y1=2
    x3=11
    y3=2
    #calculamos la diferencia
    dx = x3-x1
    dy = y3-y1
    #calculamos la pendiente
    if dx !=0 :
        m = dy / dx
    else:
        print("No se puede realizar una operacion entre cero")
    #calculamos el valor de steps
    if(dx > dy):
        steps = dx
    else:
        steps = dy
    #Calculamos el incremento
    xinc = dx / steps
    yinc = dy / steps

    if yinc !=0 :
         print("Se puede")
    else:
        print("No se puede realizar una operacion entre cero")
    
    print(x1,y1)
    plt.scatter(x1,y1)
    #calculamos los nuevos valores de x y y
    i=1
    while(i<=steps):
        x1 = x1 + xinc
        y1 = y1 + yinc
        #Redondeamos los valores con el metodo round 
        x=round(x1)
        y=round(y1)
        i+=1
        print(x,y)
        plt.scatter(x,y)
    #calculamos la tercera parte
    x3=11
    y3=2
    x2=6
    y2=7
    #calculamos la diferencia
    dx = x2-x3
    dy = y2-y3
    #calculamos la pendiente
    if dx !=0 :
        m = dy / dx
    else:
        print("No se puede realizar una operacion entre cero")
    #calculamos el valor de steps
    if(dx > dy):
        steps = dx
    else:
        steps = dy
    #Calculamos el incremento
    xinc = dx / steps
    yinc = dy / steps
    
    if xinc !=0 :
         print("Se puede")
    else:
        print("No se puede realizar una operacion entre cero")
    if yinc !=0 :
         print("Se puede")
    else:
        print("No se puede realizar una operacion entre cero")
    print(x1,y1)
    plt.scatter(x1,y1)
    #calculamos los nuevos valores de x y y
    i=1
    while(i<=steps):
        x1 = x1 + xinc
        y1 = y1 + yinc
        #Redondeamos los valores con el metodo round 
        x=round(x1)
        y=round(y1)
        i+=1
        print(x,y)
        plt.scatter(x,y)
    plt.show()
if respuesta == 2:
    print("Algoritmo Bresenhams")
    #Primera parte
    #Declaramos las variables que recibiran los valores
    x1 = 1
    y1 = 2
    x2 = 6
    y2 = 7
    #calculamos la diferencia
    dx = x2-x1
    dy = y2-y1
    #calculamos a p
    p = 2*dy - dx
    plt.scatter(x1,y1)
    print(x1,y1)
    #calculamos los nuevos valores de x y y
    while(x1<x2):
        plt.scatter(x1,y1)
        x1=x1+1
        if p<0:
            p=p+2*dy
        else:
            p=p + (2*dy)-(2*dx)
            y1=y1+1
        print(x1,y1)

    #Segunda parte
    #Declaramos las variables que recibiran los valores
    x1 = 1
    y1 = 2
    x2 = 11
    y2 = 2
    #calculamos la diferencia
    dx = x2-x1
    dy = y2-y1
    #calculamos a p
    p = 2*dy - dx
    plt.scatter(x1,y1)
    print(x1,y1)
    #calculamos los nuevos valores de x y y
    while(x1<x2):
        plt.scatter(x1,y1)
        x1=x1+1
        if p<0:
            p=p+2*dy
        else:
            p=p + (2*dy)-(2*dx)
            y1=y1+1
        print(x1,y1)

    #tercera parte
    #Declaramos las variables que recibiran los valores
    x1=6
    y1=7
    x2=11
    y2=2
    #calculamos la diferencia
    dx = x2-x1
    dy = y2-y1
    #calculamos a p
    p = 2*dy - dx
    plt.scatter(x2,y2)
    #calculamos los nuevos valores de x y y
    while(x1<x2):
        plt.scatter(x1,y1)
        x1=x1+1
        if dy<0:
            if p<0:
                p=p+2*dy
                y1=y1-1
            else:
                p=p + (2*dy)-(2*dx)
        else:
            if p<0:
                p=p+2*dy
            else:
                p = p + (2*dy)-(2*dx)
                y1=y1+1
        print(x1,y1)
    plt.show()