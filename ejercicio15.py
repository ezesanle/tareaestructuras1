#Ezer Santa Cruz
#Prueba corta 1
#Ejercicio 15

hospedajeDias=int(input("Ingrese la cantidad de dias de hospedaje: "))
precioDiario=int(input("Ingrese el precio diario de la habitacion: "))

#calcular costo del hospedaje
if hospedajeDias>0:
    if hospedajeDias>0 and hospedajeDias<=5:
        totalPagar=hospedajeDias*precioDiario
        print("El total a pagar por el hospedaje es: ",totalPagar)
    elif hospedajeDias>=5 and hospedajeDias<10:
        descuento=hospedajeDias*precioDiario*0.1
        subTotal=(hospedajeDias*precioDiario)
        totalPagar=subTotal-descuento
        print("El subtotal del hospedaje es: ",subTotal)
        print("El descuento del hospedaje es: ",descuento)
        print("El total a pagar por el hospedaje es: ",totalPagar)
    elif hospedajeDias>=10 and hospedajeDias<15:
        descuento=hospedajeDias*precioDiario*0.15
        subTotal=(hospedajeDias*precioDiario)
        totalPagar=subTotal-descuento
        print("El subtotal del hospedaje es: ",subTotal)
        print("El descuento del hospedaje es: ",descuento)
        print("El total a pagar por el hospedaje es: ",totalPagar)
    else:
        descuento=hospedajeDias*precioDiario*0.2
        subTotal=(hospedajeDias*precioDiario)
        totalPagar=subTotal-descuento
        print("El subtotal del hospedaje es: ",subTotal)
        print("El descuento del hospedaje es: ",descuento)
        print("El total a pagar por el hospedaje es: ",totalPagar)
else:
    print("Por favor ingresar la cantidad de dias de hospedaje correcta")