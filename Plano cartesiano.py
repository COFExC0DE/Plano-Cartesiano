import turtle
import math

def dibujar_plano():

    turtle.reset()
    i=0
    j=0
    cambio =10
    
    while i<=39:
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(5)
        turtle.back(10)
        turtle.forward(5)
        turtle.left(90)

        i+=1
        
        if(i == cambio):
                cambio  += 10
                turtle.back(250)
                turtle.left(90)

def raiz(numero):
    error = 0.0000001
    i=0
    aproximado = 1

    while(abs(numero-aproximado**2)  > error):
        
        aproximado = 0.5*(aproximado+(numero/aproximado))

    return aproximado


def graficar(vector):
    

    i = 0
    suma1 = vector[0]*25
    suma2 = vector[1]*25
    cal_angulo = math.degrees(math.atan2(vector[0],vector[1]))    
    distancia = raiz((suma1**2 + suma2**2))
    
    turtle.penup()    
    turtle.forward((suma1))
    turtle.left(90)
    turtle.pendown()
    
    turtle.pencolor(0.0, 0.6, 0.0)
    turtle.forward((suma2))
    turtle.left(90)
    turtle.forward((suma1))
    turtle.left(90)
    turtle.penup()
    turtle.pencolor(0.0, 0.0, 0.0)
    turtle.forward((suma2))
    turtle.left(90)
    turtle.left(90 - cal_angulo)
    turtle.pendown()
    turtle.forward(distancia)
    turtle.left(180)
        
    turtle.left(20)
    turtle.forward(25)
    turtle.backward(25)
    turtle.right(40)
    turtle.forward(25)
    turtle.backward(25)
    turtle.left(20)
    turtle.right(180 + (90 - cal_angulo))
    
    
    
    return cal_angulo
    
def suma_vectores(vector1, vector2):

    if(len(vector1)==len(vector2)):

        i=0
        nuevo_vector = []
        
        while(i < len(vector1)):
            nuevo_vector.append(vector1[i]+vector2[i])
            i+=1

        turtle.reset()    
        dibujar_plano()
        turtle.home()        
        graficar(vector1)
        graficar(vector2)
        turtle.home()
        graficar(nuevo_vector)
        

    else:
        nuevo_vector = None

    return nuevo_vector    

def resta_vectores(vector1, vector2):

    if(len(vector1)==len(vector2)):

        i=0
        nuevo_vector = []
        while(i < len(vector1)):
            nuevo_vector.append(vector1[i]-vector2[i])
            i+=1

        turtle.reset()
        dibujar_plano()
        turtle.home()
        graficar(vector1)
        turtle.penup()
        turtle.home()
        turtle.pendown()
        graficar(nuevo_vector)
        graficar(vector2)
        
    else:
        nuevo_vector = None

    return nuevo_vector

def magnitud(vector1):

    i = 0
    acumulador = 0

    while(i < len(vector1)):
        acumulador = (vector1[i]**2)
        i += 1

    return math.sqrt(acumulador)

def producto_escalar(vector1, escalar):
    if(len(vector1) > 0):
        i = 0
        regresar = []
        while(i < len(vector1)):
            
            regresar.append(vector1[i] * escalar)
            i += 1
            
        dibujar_plano()
        turtle.penup()
        turtle.home
        turtle.pendown()
        graficar(vector1)
        turtle.home()
        turtle.pendown()
        graficar(regresar)
            
    else:

         regresar = None

    return regresar        
        

    
def angulo_dos_vectores(vector1, vector2):    

    cal_angulo1 = math.atan2(vector1[1],vector1[0])
    p_angulo1 = math.degrees(cal_angulo1)
    cal_angulo2 = math.atan2(vector2[1],vector2[0])
    p_angulo2 = math.degrees(cal_angulo2)
    angulo = abs(p_angulo1 - p_angulo2)


    dibujar_plano()
    graficar(vector1)
    turtle.home()
    graficar(vector2)
    turtle.home()
    turtle.left(p_angulo1)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(40,angulo)
    turtle.home()
   
