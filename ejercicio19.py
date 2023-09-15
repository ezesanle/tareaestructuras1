#Ezer Santa Cruz
#Prueba corta 1
#Ejercicio 19

#ingreso de valores de variables
variableA=int(input("Digite el numero de la variable a: "))
variableB=int(input("Digite el numero de la variable b: "))
variableC=int(input("Digite el numero de la variable c: "))
variableD=int(input("Digite el numero de la variable d: "))
variableE=int(input("Digite el numero de la variable e: "))
variableF=int(input("Digite el numero de la variable f: "))

#verificador si tiene solucion o no
if (variableA*variableE - variableB*variableD)!=0:
    x=(variableC*variableE - variableB*variableF)/(variableA*variableE - variableB*variableD)
    y=(variableA*variableF - variableC*variableD)/(variableA*variableE - variableB*variableD)
    print("El valor de X es: ",x)
    print("El valor de Y es: ",y)
else:
    print("La ecuacion no tiene solucion debido a que (ae-bd) es igual a 0")
    