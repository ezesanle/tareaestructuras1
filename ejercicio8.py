#Ezer Santa Cruz
#Prueba corta 1
#Ejercicio 8

anguloA=int(input("Ingrese el tamano del angulo A: "))
anguloB=int(input("Ingrese el tamano del angulo B: "))
anguloC=int(input("Ingrese el tamano del angulo C: "))

if anguloA+anguloB+anguloC==180:
    if anguloA==90 or anguloB==90 or anguloC==90:
        print("El triangulo es rectangulo")
    elif anguloA<90 and anguloB<90 and anguloC<90:
        print("El triangulo es Acutangulo")
    else:
        print("Es un triangulo obtusangulo")
else:
    print("Por favor ingresar nuevamente el valor de los angulos del trangulo, los angulos deben sumar en total 180 para ser un triangulo")