

print("******************************************************************")
print("*Sistema de discriminación de números pares o impares en una división*")
print("******************************************************************")


numero_uno = int(input("Introduce el primer número:\n"))
numero_dos = int(input("Introduce el segundo numero:\n"))
resultado = numero_uno % numero_dos


if resultado == 0:
    print("El número es par")
else:
    print ("El número es impar")





