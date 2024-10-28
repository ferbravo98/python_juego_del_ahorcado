import random


def obtener_palabra_secreta() -> str:
    palabras = ["python", "javascript", "java", "angular", "django"]
    return random.choice(palabras)

def mostrar_avance(palabra_secreta, letras_adivinadas):
    adivinado = ''

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "-"
    return adivinado

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 5
    final_juego = False
    print("|--------------------------------------------------|")
    print("| Estas por comenzar a jugar el juego del ahorcado |")
    print("|--------------------------------------------------|")

    print(f"\n--> Tienes {intentos} intentos para poder adivinar la palabra\n")
    print(mostrar_avance(palabra_secreta, letras_adivinadas),"La cantidad de letras de la palabra es:",len(palabra_secreta))

    while not final_juego and intentos >0:
        adivinanza = input("\nIntroduce una letra ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("\nPor favor ingrese una letra valida")
        elif adivinanza in letras_adivinadas:
            print("\nYa ha utilizado la letra que acaba de ingresar")
        else:
            letras_adivinadas.append(adivinanza)
            if adivinanza in palabra_secreta:
                print(
                    f"\nExcelente, la letra [{adivinanza}] esta en la palabra a buscar. ¡SIGAMOS! \n")
            else:
                intentos -= 1
                print(f"\nLo siento, la letra {adivinanza} no corresponde a la palabra secreta\n")
                print(f"XXX Te quedan {intentos} intentos XXX\n")
    
        progreso_actual = mostrar_avance(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "-" not in progreso_actual:
            final_juego = True
            palabra_secreta= palabra_secreta.upper()
            print(f"Felicitaciones Has ganado. La palabra secreta era [{palabra_secreta}]")
    if intentos == 0:
        palabra_secreta= palabra_secreta.upper()
        print(f"Lo siento has perdido, la palabra secreta era [{palabra_secreta}]")
        return
juego_ahorcado()
