print("*********************** comparación de números *********************")



numero_1= float(input("Ingrese el primer número:"))
numero_2= float(input("Ingrese el segundo número:"))



if numero_1 > numero_2:
    print (f"El primer número ({numero_1}) es mayor que el segundo número ({numero_2}).")
    
elif numero_1 < numero_2:
    print (f"El segundo número ({numero_2}) es menor que el primer número ({numero_1}).")
else:
    print (f"El: ({numero_1}) es igual que: ({numero_2}).")
    

# Pide al usuario que ingrese dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Verifica cuál número es mayor o si son iguales
if numero1 > numero2:
    print(f"El primer número ({numero1}) es mayor que el segundo número ({numero2}).")
elif numero1 < numero2:
    print(f"El segundo número ({numero2}) es mayor que el primer número ({numero1}).")
else:
    print("Ambos números son iguales.")
