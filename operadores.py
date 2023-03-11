seconds = 1042
display_minutes = 1042 // 60 # Reoondea el resultado a un numero entero
print(display_minutes)

# Output: 17

seconds = 1042
display_minutes = 1042 // 60
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)

# Output:
# 17
# 22

# Ejercicio

tierra=149597870
jupiter=778547200
distancia_entre_planetas=(jupiter-tierra)
print(distancia_entre_planetas)

distancia_en_millas=distancia_entre_planetas/1.609344
print(distancia_en_millas)

# Ejercicio 2

Distancia_primera=input('Ingresa la distancia del sol al primer planeta')
Distancia_segunda=input('Ingresa la distancia del sol al segundo planeta')

Primero=int(Distancia_primera)
Segundo=int(Distancia_segunda)

Distancia_total=(Segundo-Primero)
print(abs(Distancia_total))