#importamos la libreria para poder graficar
import matplotlib.pyplot as plt
#Preguntamos por medio de un mensaje porque metodo se va a resolver
#1 Algoritmo DDA
#2 Algoritmo Bresenhams
respuesta = int( input("Coloca 1 Si deceas ocupar el ALgoritmo DDA O 2 de Bresenhams para construir el cuadrado") )
if respuesta == 1:
    print("Algoritmo ADD")
    #Declaramos nuestras coordenadas
    x1=4
    y1=3
    x2=4
    y2=7
    x3=11
    y3=7
    #calculamos la primera parte del resctangulo
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

    #Calculamos la segunda parte del rectangulo
    #calculamos la diferencia
    dx = x3-x2
    dy = y3-y2
    #calculamos la pendiente
    if dx !=0 :
        m1 = dy / dx
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
    print(x2,y2)
    plt.scatter(x2,y2)
    #calculamos los nuevos valores de x y y
    i=1
    while(i<=steps):
        x2 = x2 + xinc
        y2 = y2 + yinc
        #Redondeamos los valores con el metodo round 
        x=round(x2)
        y=round(y2)
        i+=1
        print(x,y)
        plt.scatter(x,y)

    #Calculamos la tercera parte rectangulo
    xx1=4
    yy1=3
    x4=11
    y4=3
    #calculamos la diferencia
    dx = x4-xx1
    dy = y4-yy1
    #calculamos la pendiente
    if dx !=0 :
        m1 = dy / dx
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
    print(xx1,yy1)
    plt.scatter(xx1,yy1)
    #calculamos los nuevos valores de x y y
    i=1
    while(i<=steps):
        xx1 = xx1 + xinc
        yy1 = yy1 + yinc
        #Redondeamos los valores con el metodo round 
        x=round(xx1)
        y=round(yy1)
        i+=1
        print(x,y)
        plt.scatter(x,y)
    #Calculamos la cuarta parte del rectangulo
    x3=11
    y3=7
    x4=11
    y4=3
    #calculamos la diferencia
    dx = x3-x4
    dy = y3-y4
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
    print(x4,y4)
    plt.scatter(x4,y4)
    #calculamos los nuevos valores de x y y
    i=1
    while(i<=steps):
        x4 = x4 + xinc
        y4 = y4 + yinc
        #Redondeamos los valores con el metodo round 
        x=round(x4)
        y=round(y4)
        i+=1
        print(x,y)
        plt.scatter(x,y)
    plt.show()

if respuesta == 2:
    print("Algoritmo Bresenhams")
    #Declaramos las coordenadas 
    x1 = 4
    y1 = 3
    x2 = 4
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
    #Segunda parte del reactangulo
    #Declaramos las coordenadas 
    x1 = 4
    y1 = 7
    x2 = 11
    y2 = 7
    #calculamos la diferencia
    dx = x2-x1
    dy = y2-y1
    #calculamos a p
    p = 2*dy - dx
    plt.scatter(x2,y2)
    print(x2,y2)
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
    #tercera parte del reactangulo
    #Declaramos las coordenadas
    x1 = 4
    y1 = 3
    x2 = 11
    y2 = 3
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
    #cuarta parte del rectangulo
    #Declaramos las coordenadas
    x1 = 11
    y1 = 7
    x2 = 11
    y2 = 3
    #calculamos la diferencia
    dx = x2-x1
    dy = y2-y1
    #calculamos a p
    p = 2*dy - dx
    plt.scatter(x2,y2)
    print(x2,y2)
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
    plt.show()