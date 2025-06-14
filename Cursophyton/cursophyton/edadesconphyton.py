
print("**********************Programa de clasificación de edades con phyton********")
#Ingresa la edad de la persona 
edad = int(input("Ingresa la edad:"))

if edad >=0 and edad<=12:
    print ("La persona es un niño")

elif edad >= 13 and edad<=17:
    print ("La persona es un adolecente")

elif edad >= 17 and edad <=64:
    print ("La persona es un adulto")

else:
    print ("la persona es un anciano")
