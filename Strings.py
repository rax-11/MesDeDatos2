"Moon" in "This text will describe facts and challenges with space travel"
print("Moon" in "This text will describe facts and challenges with space travel")

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has: -28 Celsius."""
print(temperatures.find("Moon"))
print(temperatures.find("Mars")) # Da el numero de elemento donde está el string
print(temperatures.count("Mars")) # Cuenta cuantos Mars hay
print(temperatures.count("Moon")) # Cuenta cuantos Moon hay
print(temperatures.split()) # Separa en elementos en cada espacio que exista
print(temperatures.title()) # Pone mayusculas y minusculas
print(temperatures.lower()) # Pone todas en minusculas
print(temperatures.upper()) # Pone todas en mayusculas
print(temperatures.split(':')) # Separa en dos elementos luego de que asome el símbolo

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():                            # Separa el string en elementos segun el espacio, luego hace un loop en cada elemento y si es numerico lo imprime
        print(item)

print("-60".startswith('-'))                        # Imprime true si empieza con el argumento

if "30 C".endswith("C"):                            # Imprime true si termina con el argumento
    print("This temperature is in Celsius")

text="Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."
print(text.replace("Celsius", "C"))                 # Reemplaza el primer elemento del argumento con el segundo

tex = "Temperatures on the Moon can vary wildly."
print("temperatures" in tex)
print("temperatures" in tex.lower())

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
print('\n'.join(moon_facts))

#Para introducir información a las strings, no es el mas recomendado
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage)

print("""Both sides of the %s get the same amount of sunlight,
... but only one side is seen from %s because
... the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

#Método format()
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))

print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))

print("""You are lighter on the {moon}, because on the {moon} 
... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))

#F strings
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")

subject = "interesting facts about the moon"
print(f"{subject.title()}")
