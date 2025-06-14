###Strings###

my_strings = "Mi string"
my_other_string ='Mi string'

print(len(my_strings))
print(len(my_other_string))

print (my_strings+ " "+ my_other_string)

my_new_line_string = "Este es un String \n con salto de linea"
print (my_other_string)

my_tab_new_line_string = "\tEste es un String  con tabulación"
print (my_tab_new_line_string)

my_scape_string = "\\tEste es un String \\n con scape "
print (my_scape_string)

# Formateo
name, surname, age = "Valentin", "V", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %s" %(name, surname, age))
