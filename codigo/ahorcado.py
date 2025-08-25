# Juego del Ahorcado en Python
# Autor: Jared Vega
# Versión final con pistas (letra inicial y final visibles)

import random

# Lista de palabras
PALABRAS = ["PERA", "MANZANA", "KIWI", "MANGO", "PLATANO", "FRESA", "TOMATE", "DURAZNO", "PIÑA"]

def elegir_palabra():
    return random.choice(PALABRAS).upper()

def mostrar_estado(estado, intentos, adivinadas):
    print("\n" + " ".join(estado))
    print(f"Intentos restantes: {intentos}")
    print(f"Letras probadas: {', '.join(sorted(adivinadas))}\n")

def actualizar_estado(palabra, estado, letra):
    return [letra if ch == letra else estado[i] for i, ch in enumerate(palabra)]

def jugar():
    palabra = elegir_palabra()
    intentos = 6
    adivinadas = set()

    # Revelar automáticamente la primera y la última letra
    estado = [
        ch if i == 0 or i == len(palabra) - 1 else "_"
        for i, ch in enumerate(palabra)
    ]
    adivinadas.update([palabra[0], palabra[-1]])

    print("🎮 Bienvenido al Juego del Ahorcado 🎮\n")
    print(f"La palabra tiene {len(palabra)} letras.")
    print("🕵️ Pista: ¡Ya tienes la primera y la última letra reveladas!\n")

    while "_" in estado and intentos > 0:
        mostrar_estado(estado, intentos, adivinadas)
        letra = input("👉 Ingresa una letra: ").strip().upper()

        if len(letra) != 1 or not letra.isalpha():
            print("⚠️ Ingresa solo una letra válida.\n")
            continue
        if letra in adivinadas:
            print("⚠️ Ya intentaste esa letra.\n")
            continue

        adivinadas.add(letra)

        if letra in palabra:
            estado = actualizar_estado(palabra, estado, letra)
            print("✅ ¡Correcto!\n")
        else:
            intentos -= 1
            print("❌ Incorrecto.\n")

    if "_" not in estado:
        print("🎉 ¡Ganaste! La palabra era:", palabra)
    else:
        print(f"😢 Perdiste. La palabra era: {palabra}")

if __name__ == "__main__":
    jugar()
