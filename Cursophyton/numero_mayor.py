print("**************************************************** \n")
print("* Programa para determinar ¿Cúal es el número más grande de tres números?*")
print("**************************************************** \n")

numero_uno = int(input("Introduce el primer número: \n"))
numero_dos = int(input("Introduce el segundo número: \n"))
numero_tres = int(input("Introduce el tercer número: \n"))

if numero_uno > numero_dos and numero_uno > numero_tres:
         print( "El número", numero_uno, "es el mayor")
elif numero_dos > numero_tres:
         print( "El número", numero_dos, "el el mayor")
else:
         print("El número", numero_tres, "es el mayor")



   
