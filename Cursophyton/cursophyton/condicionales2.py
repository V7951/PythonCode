
print("*********************** Práctica condicionales 2 *********************")





num =float (input("Ingrese un numero:"))

if num >0:
    print("El número que ingreso es positivo")
elif num <0:
    print("El número es negativo")
else:
    print(" El número es cero.")





print("*********************** Práctica condicionales con resto *********************")


numero= int(input("ingrese un numero:"))


resto =  numero % 2

if resto == 0:
         print(f"El numero es par")
else:
    print(f"El numero es impar")


a= 10

b=3

resultado = a % b
print (f"el resultado de es:{resultado}")



print("*********************** comparación de números *********************")



numero_1= float(input("Ingrese el primer número:"))
numero_2= float(input("Ingrese el segundo número:"))



if numero_1 > numero_2:
    print (f"El: ({numero_1}) es mayor que: ({numero_dos})")
elif numero_1 < numero_2:
    print (f"El: ({numero_1}) es menor que: ({numero_dos})")
else:
    print ("El: ({numero_1}) es igual que: ({numero_dos})")
    
