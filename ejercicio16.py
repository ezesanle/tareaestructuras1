#Ezer Santa Cruz
#Prueba corta 1
#Ejercicio 16

#lista de temperaturas
print("""De la siguiente lista:
1. Farenheit
2. Celsius
3. Kelvin
4. Rankine""")
temperatura=int(input("Seleccione la temperatura que desea convertir: "))
convertirGrado=int(input("Ingrese los grados a convertir: "))

#control de la seleccion y calculo de temperaturas
if temperatura!=1 and temperatura!=2 and temperatura!=3 and temperatura!=4:
    print("Por favor seleccione nuevamente la temperatura")
elif temperatura==1:
    celsius=(convertirGrado-32)*5/9
    rankine=convertirGrado+460
    kelvin=celsius+273
    print("Los ",temperatura,"grados Farenheit se convierten en las siguientes temperaturas:")
    print("Celsius: ",celsius)
    print("Kelvin: ",kelvin)
    print("Rankine: ",rankine)
elif temperatura==2:
    kelvin=convertirGrado+273
    farenheit=(convertirGrado*9/5)+32
    rankine=farenheit+460
    print("Los ",temperatura,"grados Celsius se convierten en las siguientes temperaturas:")
    print("Farenheit: ",farenheit)
    print("Kelvin: ",kelvin)
    print("Rankine: ",rankine)
elif temperatura==3:
    celsius=convertirGrado-273
    farenheit=(celsius*9/5)+32
    rankine=farenheit+460
    print("Los ",temperatura,"grados Kelvin se convierten en las siguientes temperaturas:")
    print("Celsius: ",celsius)
    print("Farenheit: ",farenheit)
    print("Rankine: ",rankine)
elif temperatura==4:
    farenheit=convertirGrado-460
    celsius=(farenheit-32)*5/9
    kelvin=celsius+273
    print("Los ",temperatura,"grados Rankine se convierten en las siguientes temperaturas:")
    print("Celsius: ",celsius)
    print("Kelvin: ",kelvin)
    print("Farenheit: ",farenheit)