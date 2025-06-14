
num_uno, num_dos = 0, 1

while num_dos <= 1597:
    print(num_uno, num_dos, end=" ")
    num_uno = num_uno + num_dos
    num_dos = num_uno + num_dos


x=0

while x<=10:
    print(x)
    x+=1





print("*********************** Práctica condicionales *********************")


edad =int(input("Ingresa tu edad:"))

if edad >=18:
    print ("Eres mayor de edad")
else:
    print("Eres menor de edad")






print("*********************** Práctica condicionales 2 *********************")





num =int (input("Ingrese un numero"))

if num >0:
    print("El número que ingreso es positivo")
elif num <0:
    print("El número es negativo")
else:
    print(" El número es cero.")
