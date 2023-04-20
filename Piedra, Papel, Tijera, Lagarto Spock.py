import random

opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

jugar_de_nuevo = "s"

while jugar_de_nuevo == "s":
    jugador = input("Elige una opción (piedra, papel, tijera, lagarto o spock): ")
    
    # Verificar si la opción del jugador es válida
    while jugador not in opciones:
        jugador = input("Opción inválida. Elige una opción válida (piedra, papel, tijera, lagarto o spock): ")
        
    computadora = random.choice(opciones)

    print(f"La computadora eligió {computadora}.")

    if jugador == computadora:
        print("Empate!")
    elif jugador == "piedra" and (computadora == "tijera" or computadora == "lagarto"):
        print("¡Ganaste!")
    elif jugador == "papel" and (computadora == "piedra" or computadora == "spock"):
        print("¡Ganaste!")
    elif jugador == "tijera" and (computadora == "papel" or computadora == "lagarto"):
        print("¡Ganaste!")
    elif jugador == "lagarto" and (computadora == "papel" or computadora == "spock"):
        print("¡Ganaste!")
    elif jugador == "spock" and (computadora == "piedra" or computadora == "tijera"):
        print("¡Ganaste!")
    else:
        print("Perdiste. Lo siento.")
    
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    
print("Gracias por jugar. ¡Hasta la próxima!")
