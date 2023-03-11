planets=['Mercurio','Venus','Tierra','Marte','Jupiter','Saturno','Urano','Neptuno']
print(planets)
#Mostrar el numero de planetas
print('Hay', len(planets), 'planetas')
#Añadir un planeta a la lista
planets.append('Plutón')
print(planets)
print(planets[-1],'es el último planeta')
##Ingresar el usuario un planeta
planeta_usuario=input('Ingresa un planeta con la primera letra mayúscula: ')
nuevo_planeta=planets.index(planeta_usuario)
print('Los demás planetas aparte de', planeta_usuario,'más cerca del sol son:')
print(planets[0:nuevo_planeta])
print('Los demás planetas aparte de', planeta_usuario,'más lejos del sol son:')
print(planets[nuevo_planeta+1:])
