string = "Diana se peina sola"
resultado = 0
starts_with = "Ejemplos con starswith(): "
ends_with = "Ejemplos que terminen con endswith(): "

print(f"\{starts_with.rjust(50, '=')}")

resultado= string.startswith("D")
print(f"\n{string} comienza con la subcadena D: {resultado}")

resultado= string.startswith("d")
print(f"\n{string} comienza con la subcadena d: {resultado}")

resultado= string.startswith("Diana")
print(f"\n{string} comienza con la subcadena Diana: {resultado}")

resultado= string.startswith("se", 6)
print(f"\n{string} comienza con la subcadena se,desde la posición 6 {resultado}")

resultado= string.startswith("se", 6, 7)
print(f"\n{string} comienza con la subcadena se, desde la posición 6 hasta la 7: {resultado}")

resultado= string.startswith("se",6 ,100)
print(f"\n{string} comienza con la subcadena se, hasta la posición 100: {resultado}")

resultado= string.startswith("se",100 ,100)
print(f"\n{string} comienza con la subcadena se,desde la posición 100 hasta la posición 100: {resultado}")

resultado= string.startswith("se",-4,-1)
print(f"\n{string} comienza con la subcadena se, desde la posición -4 hasya la posición -1 : {resultado}")

print(f"\n{ends_with.rjust(50, '=')}")

resultado= string.endswith("A")
print(f"\n{string}termina con la subcadena A:")

resultado= string.endswith("a")
print(f"\n{string}termina con la subcadena a:")

resultado= string.endswith("sola")
print(f"\n{string}termina con la subcadena sola:")

resultado= string.endswith("sola", 10)
print(f"\n{string}termina con la subcadena desde la posición 10:")

resultado= string.startswith("s, 9, 14")
print(f"\n{string}termina con la subcadena s, desde la posición 9 hasta la posición 14:")

resultado= string.startswith("s, 100, 100")
print(f"\n{string}termina con la subcadena s, desde la posición 100 hasta la posición 100:")

resultado= string.startswith("s, -4, -2")
print(f"\n{string}termina con la subcadena s, desde la posición -4 hasta la posición -2:")