def rocket_parts():
    print("payload, propellant, structure")

#Con el return se puede devolver los valores de la funcion para agregarlos a una variable

def rocket_parts():
    return "payload, propellant, structure"

output = rocket_parts()
print(output)

#La función any devuelve true si un elemento de la lista es true y si no hay elementos true devuelve False
#>>> any([True, False, False])
#True
#>>> any([False, False, False])
#False
#>>> any() LLAMAR ANY SIN ARGUMENTO DA ERROR
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: any() takes exactly one argument (0 given)

# STR() CREA UNA CADENA A PARTIR DE UN ARGUMENTO
#>>> str()
#''
#>>> str(15)
#'15'

# PARA EXIGIR UN ARGUMENTO
def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    
distance_from_earth("Moon")