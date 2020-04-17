import random


def adivinar(chosenNumber):
    number = random.randint(0, 100)

    print('{0}.'.format(number))
    count = 0
    while True:

        if chosenNumber > 100 or chosenNumber < 1:
            chosenNumber = int(input('La cantidad de aciertos debe ser mayor a 0 y menor a 100: '))
        else:
            break

    guess = int(input('Ingrese un entero entre 0 y 100: '))

    while True:
        count = count + 1
        if guess == number:
            print('Felicidades, adivinaste en el intento numero: {0}.'.format(count))
            break
        elif chosenNumber == count:
            print('Lo lamento a superado la cantidad maxima de intentos({0}) el numero era {1}'.format(chosenNumber, number))
            break
        else:
            guess = int(input('No haz adivinado por favor ingrese otro numero: '))

            while True:

                if guess > 100 or guess < 0:
                    guess = int(input('El numero debe ir de 0 a 100: '))
                else:
                    break


attempt = int(input('Ingrese la cantidad de intentos que desea poseer: '))
adivinar(attempt)
