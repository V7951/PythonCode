invitados = ["Carolina", "Juan", "Gerardo"]
amigos = ["Luis", "Ana"]
print(f"Lista de invitados: {invitados} \nLista de amigos: {amigos}")
invitados.extend(amigos)
print(f"Lista invitados: {invitados}")

numeros = [10, 20]
print(f"\nLista números: {numeros}")
numeros.extend(range(30, 100, 10))
print(f"Lista números: {numeros}")

