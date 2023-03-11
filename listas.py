## Ejemplo de lista
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
                #0      #1
## Acceder a elementos de la lista
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

# Output
# The first planet is Mercury
# The second planet is Venus
# The third planet is Earth

## Se puede utilizar un elemento como variable
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

# Output
# Mars is also known as Red Planet

## len() se usa para obtener el numero de elementos de una lista

number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

# Output:
# There are 8 planets in the solar system

## Con Nombredelista.append('elemento') se añade elementos

planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

# Output:
# There are actually 9 planets in the solar system.

## Con Nombredelista.pop(elemento) se elimina un elemento de la lista

planets.pop()  # Se elimina el ultimo elemento de la lista
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

## Índices negativos
## Un indice de -1 devuelve el ultimo elemento de una lista, -2 el penultimo, sucesivamente

print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# Output
# The last planet is Neptune
# The penultimate planet is Uranus

## Nombre de lista.index(elemento) muestra el numero de elemento de la lista
## Se debe agregar +1 porque la lista empieza por 0

jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

# Output
# Jupiter is the 5 planet from the sun

##############################

## float permite numeros decimales
gravity_on_earth = 1.0
gravity_on_the_moon = 0.166

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

bus_weight = 12650 # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "kg")

# Output
# On Earth, a double-decker bus weighs 12650 kg
# On Mercury, a double-decker bus weighs 4781.7 kg

## max(Nombre de la lista) devuelve el numero mas grande y min(Nombrelista) devuelve el numero pequeño

bus_weight = 12650 # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")

# Output
# On Earth, a double-decker bus weighs 12650 kg
# The lightest a bus would be in the solar system is 4769.05 kg
# The heaviest a bus would be in the solar system is 29854 kg

### Se puede segmentar listas con :, va a incluir el elemento del numero incial y explusar el elemento del numero final

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)

# Output: ['Mercury', 'Venus']

planets_after_earth = planets[3:8]
print(planets_after_earth) 

# Output
# ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planets_after_earth = planets[3:]  # Si no se coloca valor final, se incluye hasta el final de la lista
print(planets_after_earth)

# Output
# ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

### Para combinar listas se pueden unir con el simbolo +

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Metis', 'Adrastea', 'Amalthea', 'Thebe', 'Io', 'Europa', 'Ganymede', 'Callisto']

### Se puede ordenar una lista con Nombredelista.sort() se ordenara en orden alfabetico

regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Adrastea', 'Amalthea', 'Callisto', 'Europa', 'Ganymede', 'Io', 'Metis', 'Thebe']

### Para ordenar inversamente se utiliza Nombredelista.sort(reverse=True)
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Thebe', 'Metis', 'Io', 'Ganymede', 'Europa', 'Callisto', 'Amalthea', 'Adrastea']
