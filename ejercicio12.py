#Ezer Santa Cruz
#Prueba corta 1
#Ejercicio 12

nombreEmpleado=input("Ingrese el nombre del empleado: ")
tipoEmpleado=int(input("Ingrese el tipo de empleado (1, 2, 3 o 4): "))
horasTrabajadas=int(input("Ingrese las horas trabajadas: "))
cuotaPorHora=int(input("Ingrese la couta por hora: "))

#determinar horas regulares y extras
if horasTrabajadas>0 and horasTrabajadas<=40:
    horasRegulares=horasTrabajadas
    horasExtras=0
elif horasTrabajadas>40:
    horasRegulares=40
    horasExtras=horasTrabajadas-40

#calcular horas regulares
sueldoAPagar=horasRegulares*cuotaPorHora

#calcular horas extras
if tipoEmpleado==1:
    cuotaExtra=horasExtras*cuotaPorHora*1.5
    print("El empleado ",nombreEmpleado,"es un tipo de empleado: ",tipoEmpleado)
    print("El sueldo a pagar regular es de: ",sueldoAPagar,"y las horas extras a pagar es de: ",cuotaExtra)
elif tipoEmpleado==2:
    cuotaExtra=horasExtras*cuotaPorHora*2
    print("El empleado ",nombreEmpleado,"es un tipo de empleado: ",tipoEmpleado)
    print("El sueldo a pagar regular es de: ",sueldoAPagar,"y las horas extras a pagar es de: ",cuotaExtra)    
elif tipoEmpleado==3:
    cuotaExtra=horasExtras*cuotaPorHora*2.5
    print("El empleado ",nombreEmpleado,"es un tipo de empleado: ",tipoEmpleado)
    print("El sueldo a pagar regular es de: ",sueldoAPagar,"y las horas extras a pagar es de: ",cuotaExtra)
elif tipoEmpleado==4:
    cuotaExtra=horasExtras*cuotaPorHora*3
    print("El empleado ",nombreEmpleado,"es un tipo de empleado: ",tipoEmpleado)
    print("El sueldo a pagar regular es de: ",sueldoAPagar,"y las horas extras a pagar es de: ",cuotaExtra)
else:
    print("Por favor ingresar in tipo de empleado correcto")