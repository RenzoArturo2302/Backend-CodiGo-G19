numero1 = 20
numero2 = 50
numero3 = 40

# condicionales se pueden dar con resultado boolean
if numero1 > numero2 : 
    print("El número 1 es mayor que el número 2")
# Si no cumple la primera condición entonces trataremos con esta nueva y si no cumple entonces continuará al else o a otro elif si hubiese
elif numero1 > numero3:
    print("El número 1 es mayor que el número 3")
else: 
    print('El número 2 es mayor que el número 1')


# Si tengo el sueldo entre 500 soles y 800 soles entonces puedo ir a la playa
# Si tengo más de 800 soles 



def calcular_actividades_vacacionales(sueldo: int):
    if sueldo >= 500 and sueldo <= 800:
        print("Puedo ir a la playa")
    elif sueldo > 800:
        print("Puedo ir al Inti Raymi")
    else:
        print("No me alcanza")

calcular_actividades_vacacionales(5)


# Queremos saber si un alumno esta reprobado o necesita ir a vacacional o esta reprobado

# 13 - 18 aprobado, 19 - 20 aprobado con felicitaciones. 11 - 20 vacacional, si tiene menos de 11 esta reprobado

def calcular_estado_alumno(nombre: str, nota: int):

    anuncio = "El alumno" + nombre

    if nota < 0:
              print("valor invalido")
    elif nota <=10:
        print(anuncio + " esta reprobado")
    elif nota <= 12:
        print(anuncio + " necesita ir a vacacional")
    elif nota <= 18:
        print(anuncio + " esta aprobado")
    elif nota <= 20:
        print(anuncio + " esta aprobado con felicitaciones")
    
        


calcular_estado_alumno('Renzo',-2)







