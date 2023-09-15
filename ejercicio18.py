#Ezer Santa Cruz
#Prueba corta 1
#Ejercicio 18

#menu con variables
marcaAuto=input("Digite la marca del automovil: ")
print("""De la siguiente lista:
1. Alemania
2. Japon
3. Italia
4. USA""")
origenAuto=int(input("Seleccione el origen del automovil: "))
costoAuto=int(input("Ingrese el costo del automovil: "))

#calcular costo e impuestos
if origenAuto!=1 and origenAuto!=2 and origenAuto!=3 and origenAuto!=4:
    print("Por favor seleccione nuevamente el origen del automovil")
elif origenAuto==1:
    impuesto=costoAuto*0.20
    costoFinal=costoAuto+impuesto
    print("El automovil marca: ",marcaAuto,"tiene el siguiente costo e impuesto: ")
    print("Costo sin impuesto: ",costoAuto)
    print("Impuesto: ",impuesto)
    print("Costo final: ",costoFinal)
elif origenAuto==2:
    impuesto=costoAuto*0.30
    costoFinal=costoAuto+impuesto
    print("El automovil marca: ",marcaAuto,"tiene el siguiente costo e impuesto: ")
    print("Costo sin impuesto: ",costoAuto)
    print("Impuesto: ",impuesto)
    print("Costo final: ",costoFinal)
elif origenAuto==3:
    impuesto=costoAuto*0.15
    costoFinal=costoAuto+impuesto
    print("El automovil marca: ",marcaAuto,"tiene el siguiente costo e impuesto: ")
    print("Costo sin impuesto: ",costoAuto)
    print("Impuesto: ",impuesto)
    print("Costo final: ",costoFinal)
elif origenAuto==4:
    impuesto=costoAuto*0.08
    costoFinal=costoAuto+impuesto
    print("El automovil marca: ",marcaAuto,"tiene el siguiente costo e impuesto: ")
    print("Costo sin impuesto: ",costoAuto)
    print("Impuesto: ",impuesto)
    print("Costo final: ",costoFinal)