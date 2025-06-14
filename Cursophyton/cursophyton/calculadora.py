print ("******************************************** \n")
print ("*********Calculadora en Phyton************** \n")

print ("*********Menu de opciones************** \n")
print ("Opción 1: Suma.")
print ("Opción 2: Resta.")
print ("Opción 3: Multiplicación.")
print ("Opción 4: División.")
print ("Opción 5: División entera.")
print ("Opción 6: Exponente.")
print ("Opción 7: Resto.")


print ("Selecciona una opción del menu de operaciones: \n")
opcion= int (input("Selecciona una opción del menu de opciones: \n"))

if opcion == 1:
    print("Ha seleccionado la Suma, favor de introducir los valores. \n")
    numero= int(input("Introduce el primer número:"))
    numero+= int(input("introduce el segundo número:"))
    print("El resultado de la suma es:", numero, "\n")

elif opcion == 2:
    print("Ha seleccionado la Resta, favor de introducir los valores. \n")
    numero= int(input("Introduce el primer número:"))
    numero-= int(input("introduce el segundo número:"))
    print("El resultado de la resta es:", numero, "\n")
    
    
elif opcion == 3:
    print("Ha seleccionado la Multiplicación, favor de introducir los valores. \n")
    numero= int(input("Introduce el primer número:"))
    numero*= int(input("introduce el segundo número:"))
    print("El resultado de la multiplicación es:", numero, "\n")
    
elif opcion == 4:
    print("Ha seleccionado la División, favor de introducir los valores. \n")
    numero= float(input("Introduce el primer número:"))
    numero/= float(input("introduce el segundo número:"))
    print("El resultado de la división es:", numero,"\n")
    
elif opcion == 5:
    print("Ha seleccionado la Division entera, favor de introducir los valores. \n")
    numero= int(input("Introduce el primer número:"))
    numero//= int(input("introduce el segundo número:"))
    print("El resultado de la división entera es:", numero, "\n")

elif opcion == 6:
    print("Ha seleccionado el Exponente, favor de introducir los valores. \n")
    numero= int(input("Introduce el primer número:"))
    numero**= int(input("introduce el segundo número:"))
    print("El resultado del exponente es:", numero, "\n")

elif opcion == 7:
    print("Ha seleccionado el Resto, favor de introducir los valores. \n")
    numero= int(input("Introduce el primer número:"))
    numero%= int(input("introduce el segundo número:"))
    print("El resultado del resto es:", numero, "\n")

else:
    print("La opción no existe")

    
