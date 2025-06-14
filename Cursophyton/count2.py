string ="Mi Mamá me mima"
contador = 0

print(string.center(40, "*"))
contador = string.count("M")
print(f"\nLa letra M aparece  {contador}veces en la cadena: {string}")

contador = string.count("m")
print(f"\nLa letra m se encontro {contador}veces en la cadena: {string}")


contador = string.count("mamá")
print(f"\nLa palaba mamá aparece  {contador}veces en la cadena: {string}")

contador = string.count("me mima")
print(f"\nLa palabra me mima  {contador}veces en la cadena: {string}") 

contador = string.count("m, 13")
print(f"\nLa letra m aparece  {contador}veces desde la posición número 13 en la cadena: {string}")


contador = string.count("m, 100")
print(f"\nLa letra m aparece  {contador}veces desde la posición número 100 en la cadena: {string}")

contador = string.count("m, -3")
print(f"\nLa letra m aparece  {contador}veces desde la posición número -3 en la cadena: {string}")


contador = string.count("m, 3, 7")
print(f"\nLa letra m aparece  {contador}veces desde la posición número 3 y  7 en la cadena: {string}")


contador = string.count("m, 100, 100")
print(f"\nLa letra m aparece  {contador}veces desde la posición número 100 y  7 en la cadena: {string}")

contador = string.count("m, -4, -1")
print(f"\nLa letra m aparece  {contador}veces desde la posición número -4 y -1 en la cadena: {string}")




