#Your spaceship has three tanks: Main, External and Hydrogen. You want to create an app to display the amount of fuel in each tank, and the average amount of fuel between the three tanks. Because you wish to reuse this code in other projects, you want to create a function with the logic.
#Create a function named generate_report. The function will take three parameters named main_tank, external_tank and hydrogen_tank. When run, the function will display output which resembles the following:
def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """
    print(output)

generate_report(80, 70, 75)

#La misión Apolo 11 tardó unas 51 horas en llegar a la Luna. Vamos a crear una función que devuelva la hora estimada de llegada usando el mismo valor que la misión Apolo 11 como valor predeterminado:
from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

arrival_time()
'Arrival: Saturday 16:42'

arrival_time(hours=0)
'Arrival: Thursday 13:42'