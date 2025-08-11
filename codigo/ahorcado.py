# Juego del Ahorcado en Python
# Autor: Diego Vega

palabra = "PERA".upper()
intentos = 6
adivinadas = set()
estado = ["_" for _ in palabra]

def mostrar_estado():
    print(" ".join(estado), f" | Intentos: {intentos} | Letras probadas: {', '.join(sorted(adivinadas))}")

while "_" in estado and intentos > 0:
    mostrar_estado()
    letra = input("Ingresa una letra: ").strip().upper()

    if len(letra) != 1 or not letra.isalpha():
        print("Debes ingresar una sola letra.")
        continue
    if letra in adivinadas:
        print("Ya intentaste esa letra.")
        continue

    adivinadas.add(letra)

    if letra in palabra:
        for i, ch in enumerate(palabra):
            if ch == letra:
                estado[i] = letra
        print("¡Correcto!")
    else:
        intentos -= 1
        print("Incorrecto.")

if "_" not in estado:
    print(" ".join(estado))
    print("¡Ganaste!")
else:
    print(f"Perdiste. La palabra era {palabra}.")
