#Count the number of Duplicates
#Write a function that will return the count of distinct case-insensitive alphabetic 
#characters and numeric digits that occur more than once in the input string. 
#The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.#


from collections import Counter

def encontrar_repetidos(cadena):
    """Función que encuentra los caracteres repetidos en una cadena, sin distinguir mayúsculas y minúsculas."""
    contador = Counter(cadena.lower())  # Convertimos a minúsculas
    repetidos = {caracter: cantidad for caracter, cantidad in contador.items() if cantidad > 1}
    return repetidos

# Solicitar entrada al usuario
cadena = input("Introduce una cadena de texto: ")

# Llamar a la función y mostrar el resultado
resultado = encontrar_repetidos(cadena)
print(f"Caracteres repetidos: {resultado}")