string=input("Introduce una frase: ")
palabra=input("Introduce la palabra que desees eliminar: ")
substring=""

buscador = string.find(palabra)
substring = string[0 : buscador]+ string[buscador + len(palabra)+ 1 :]


print(f"Cadena resultante: {substring}")