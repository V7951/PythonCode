frase = input("Escribe una frase:").lower()
vocales ="aeiou"
contador = 0

for letra in frase:
    if letra in vocales:
        contador +=1
print(f"La frase tiene {contador} vocales")