string="012345689"
substring=""

print(f"Cadena princiapal{string}")

substring=string[0]
print(f"\nSubcadena con el indice en la posición [0] es {substring}")

substring=string[5]
print(f"\nSubcadena con el indice en la posición [5 ]es {substring}")

substring=string[-4]
print(f"\nSubcadena con el indice en la posición [-4] es {substring}")

substring= string[:3]
print(f"\nSubcadena con el indice en la posición [:3] es {substring}")

substring=string[5:]
print(f"\nSubcadena con el indice en la posición [5:] es {substring}")


substring=string[-4:-1]
print(f"\nSubcadena con el indice en la posición [-4:-1] es {substring}")

substring=string[:]
print(f"\nSubcadena con el indice en la posición [:] es {substring}")


substring=string[1:6:2]
print(f"\nSubcadena con el indice en la posición y salto  [1:6:2] es {substring}")

substring=string[::3]
print(f"\nSubcadena con el indice en la posición y salto  [::3] es {substring}")

