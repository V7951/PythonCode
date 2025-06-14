print("*****************************************\n")
print ("* Sistema de control vacacional *")
print("*****************************************\n")

nombre_empleado = input("Por favor introduce el nombre del empleado")
clave_departamento = int(input("Por favor introduce la clave del departamento"))
antiguedad_empleado= float(input("Por favor introduce los años laborados por el empleado"))

if clave_departamento == 1:

    if antiguedad_empleado >=1 and antiguedad_empleado <2:
        print ("El empleado ", nombre_empleado, "Tiene derecho a 6 días de vacaciones.")
    elif antiguedad_empleado >=2 and antiguedad_empleado <=6:
        print ("El empleado", nombre_empleado, "Tiene derecho a 14 días de vacaciones.")
    elif antiguedad_empleado >=7:
        print ("El empleado", nombre_empleado, "Tiene derecho a 20 días de vacaciones.")
    else:
        print ("El empleado", nombre_empleado, "Aún no tiene derecho a 14 días de vacaciones.")

elif clave_departamento ==2:

    if antiguedad_empleado >=1 and antiguedad_empleado <2:
        print ("El empleado ", nombre_empleado, "Tiene derecho a 7 días de vacaciones.")
    elif antiguedad_empleado >=2 and antiguedad_empleado <=6:
        print ("El empleado", nombre_empleado, "Tiene derecho a 15 días de vacaciones.")
    elif antiguedad_empleado >=7:
        print ("El empleado", nombre_empleado, "Tiene derecho a 22 días de vacaciones.")
    else:
        print ("El empleado", nombre_empleado, "Aún no tiene derecho a 14 días de vacaciones.")


elif clave_departamento == 3:

    if antiguedad_empleado >=1 and antiguedad_empleado <2:
        print ("El empleado ", nombre_empleado, "Tiene derecho a 10 días de vacaciones.")
    elif antiguedad_empleado >=2 and antiguedad_empleado <=6:
        print ("El empleado", nombre_empleado, "Tiene derecho a 20 días de vacaciones.")
    elif antiguedad_empleado >=7:
        print ("El empleado", nombre_empleado, "Tiene derecho a 30 días de vacaciones.")
    else:
        print ("El empleado", nombre_empleado, "Aún no tiene derecho a 14 días de vacaciones.")


else:
    print("La clave del departamento no existe, vuelve a intentarlo")
    
