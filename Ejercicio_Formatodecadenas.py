#Crear tres variables
name="Ganymede"
planet= "Mars"
gravity="1.43"

#Crear la plantilla para mostrar la información

template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

# Llenar la plantilla
print(template.format(name=name, planet=planet, gravity=gravity))
