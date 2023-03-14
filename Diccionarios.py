# Diccionarios llevan {} y :
planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get('name'))

# Displays Earth

# planet['name'] is identical to using planet.get('name')
print(planet['name'])

# Displays Earth

wibble = planet.get('wibble') # Returns None
wibble = planet['wibble'] # Throws KeyError