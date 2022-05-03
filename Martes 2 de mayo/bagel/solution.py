import random

NUM_DIGIT = 3
MAX_GUESSES = 10

def get_secret_number():
    numbers = [str(i) for i in range(10)]
    random.shuffle(numbers)
    secret_number = ""
    for i in range(NUM_DIGIT):
        secret_number += numbers[i]
    return secret_number

def get_clues(secret_number, guess):
    if guess == secret_number:
        return "Fermi"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append("Fermi")
        elif guess[i] in secret_number:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"

    else:
        clues.sort()
        return " ".join(clues)

def main():
    """
    # Bagle

    Es un juego de logica deductiva, dodne tu deberas
    adivinar un numero secreto de tres digitos basasdo
    en pistas
    El juego te dara las siguientes pistas
    - Pico: Cuando tu intento tiene un numero pero en la 
    posicion incorrecta

    - Fermi: Cuando tu intento tiene un numero en la posicion
    correcta

    - Bagels: Cuando el intento no tienen ningun numero

    Tienes 10 intentos para adivinar el problema

    por ejemplo si el numero secreto es 248 y tu intento fue 843
    las pistas serian: fermi, pico

    """

    while True:
        secret_number = get_secret_number()
        print("Bienvenido al juego de Bagle")
        print("Ya he pensado un numero secreto")
        print(f"Tienes {MAX_GUESSES} intentos para adivinarlo")
        
        num_guess = 1
        while num_guess <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGIT or not guess.isdecimal():
                print(f"Inteto {num_guess} de {MAX_GUESSES}")
                guess = input("Ingresa tu intento: ")

            clues = get_clues(secret_number, guess)
            print(clues)
            num_guess += 1

            if guess == secret_number:
                print("Felicidades, has ganado")
                break

            if num_guess > MAX_GUESSES:
                print("Lo siento, has perdido")
                print("La respuesta correcta era: ", secret_number)
                break

        print("Deseas jugar de nuevo? (s/n)")
        if not input().lower().startswith("s"):
            break
    print("Gracias por jugar")

main()