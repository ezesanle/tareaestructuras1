#Ezer Santa Cruz
#Prueba corta 1
#Ejercicio 6

cantidadHojas=int(input("Ingrese la cantidad de hojas de hielo seco a comprar: "))
precioHojas=int(input("Ingrese el precio unitario de las hojas de hielo seco: "))
cantidadViguetas=int(input("Ingrese la cantidad de viguetas a comprar: "))
precioViguetas=int(input("Ingrese el precio unitario de las viguetas: "))
cantidadArmazones=int(input("Ingrese la cantidad armazones a comprar: "))
precioArmazones=int(input("Ingrese el precio unitario de los armazones: "))

if cantidadHojas<0 or cantidadViguetas<0 or cantidadArmazones<0:
    print("Ingrese la cantidad correcta a comprar")
else:
    #calculo del valor final de hojas de hielo seco
    if cantidadHojas>50 and cantidadHojas<=100:
        valorHojas=cantidadHojas*precioHojas
        descuentoHojas=valorHojas*0.25
        totalHojas=valorHojas-descuentoHojas
    elif cantidadHojas>100:
        valorHojas=cantidadHojas*precioHojas
        descuentoHojas=valorHojas*0.30
        totalHojas=valorHojas-descuentoHojas
    else:
        valorHojas=cantidadHojas*precioHojas
        descuentoHojas=valorHojas*0.20
        totalHojas=valorHojas-descuentoHojas
    
    #calculo del valor final de las viguetas
    valorViguetas=cantidadViguetas*precioViguetas
    descuentoViguetas=valorViguetas*0.15
    totalViguetas=valorViguetas-descuentoViguetas

    #calculo del valor final de los armazones
    totalArmazones=cantidadArmazones*precioArmazones

    subTotal=totalHojas+totalViguetas+totalArmazones

    #calculo del total de contado
    descuentoContado=subTotal*0.07
    totalcontado=subTotal-descuentoContado

    valorCredito=subTotal

    print("Si el pago es de contado, el total a pagar es de: ",totalcontado,"y si el pago es de contado, el total a pagar es de: ",valorCredito,)