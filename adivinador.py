import random

def dificultades(): #Permite elegir una dificultad validando que sea correcta y devuelve el rango maximo de cada dificultad
    print("Dificultades: ")
    print("1: 1-10")
    print("2: 1-50")
    print("3: 1-100")

    dificultad1 = 10
    dificultad2 = 50
    dificultad3 = 100

    dificultad = int( input("Elige una dificultad (1,2,3): ") )
    
    while(dificultad != 1 and dificultad != 2 and dificultad != 3):
        print("-------------------------------------------------")
        print("La dificultad que has escogido no existe, tiene que ser 1 2 o 3")
        dificultad = int( input("Elige una dificultad (1,2,3): ") )

    print("-------------------------------------------------")

    if(dificultad == 1):
        print("Has elegido la dificultad 1, tienes que adivinar un número del 1 al", dificultad1)
        return dificultad1
    elif(dificultad == 2):
        print("Has elegido la dificultad 2, tienes que adivinar un número del 1 al", dificultad2)
        return dificultad2
    elif(dificultad == 3):
        print("Has elegido la dificultad 3, tienes que adivinar un número del 1 al", dificultad3)
        return dificultad3


def adivinador(dificultad): #Se le pasa por parametro el rango máximo de la dificultad, se genera el numero correcto aleatoriamente y empiezas a probar números hasta acertar
    historial = [] #Historial de intentos
    numero_max = dificultad
    numero_correcto = random.randint(1, numero_max)

    numero = int( input("Elige un numero para adivinar: ") )

    historial.append(numero) #Se le añaden los números probados al historial

    while(numero != numero_correcto):
        if(numero_correcto > numero):
            print("El numero que tienes que adivinar es mayor")
            print("-------------------------------------------------")
            numero = int( input("Elige otro numero para adivinar: ") )
            historial.append(numero) #Se le añaden los números probados al historial
        else:
           print("El numero que tienes que adivinar es menor") 
           print("-------------------------------------------------")
           numero = int( input("Elige otro numero para adivinar: ") )
           historial.append(numero) #Se le añaden los números probados al historial
    
    print("Has acertado el número!")
    print("El numero era", numero_correcto)

    print("-------------------------------------------------")

    ver_historial = input("Quieres ver el historial de intentos? s/n: ") #Pregunta al usuario si quiere ver el historial
    if(ver_historial == "s"):
        print(historial)


#Aquí se llaman las funciones
print("Bienvenido al juego de Adivinar Números")
dificultad_elegida = dificultades()
adivinador(dificultad_elegida)



