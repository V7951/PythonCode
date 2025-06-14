

print("*******************Ejercicio para comparar números*************")
#ingresa números de manera aleatoria
numero1 =int(input("Ingresa el primer número:"))
numero2 =int(input("Ingresa el segundo número:"))
numero3 =int(input("Ingresa el tercer número:"))

#compara los tres números y determina cuál es el numero grande, más pequeño o si son iguales
if numero1 > numero2 and numero1 > numero3:
    print ("El numero 1 es el mayor")
if numero2 > numero1 and numero2 > numero3:
    print ("El numero 2 es el mayor")
if numero3 > numero1 and numero3 > numero2:
    print ("El numero 3 es el mayor")
else:
    print ("Los 3 números son iguales")
