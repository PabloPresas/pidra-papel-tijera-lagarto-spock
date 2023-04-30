import random
import tkinter as tk

# Creamos la ventana
ventana = tk.Tk()
ventana.title("Juego de piedra, papel o tijera")
ventana.geometry("1024x768")

# Creamos el título
titulo = tk.Label(text="Piedra, Papel, Tijera, Lagarto, Spock", font=("Arial", 24), bg="#74b1ce", fg="white")
titulo.pack(fill="both", expand=True)
by_pablo = tk.Label(ventana, text="By Pablo Presas", font=("Arial", 10), fg="Black")
by_pablo.pack()

opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

def jugar(opcion_jugador):
    resultado.config(text="")
    
    computadora = random.choice(opciones)

    computadora_label.config(text=f"La computadora eligió {computadora}.")
    
    if opcion_jugador == computadora:
        resultado.config(text="Empate!", fg="#f7b840", highlightbackground="#f7b840", highlightthickness=2)
    elif opcion_jugador == "piedra" and (computadora == "tijera" or computadora == "lagarto"):
        resultado.config(text="¡Ganaste!", fg="#74b1ce", highlightbackground="#74b1ce", highlightthickness=2)
    elif opcion_jugador == "papel" and (computadora == "piedra" or computadora == "spock"):
        resultado.config(text="¡Ganaste!", fg="#74b1ce", highlightbackground="#74b1ce", highlightthickness=2)
    elif opcion_jugador == "tijera" and (computadora == "papel" or computadora == "lagarto"):
        resultado.config(text="¡Ganaste!", fg="#74b1ce", highlightbackground="#74b1ce", highlightthickness=2)
    elif opcion_jugador == "lagarto" and (computadora == "papel" or computadora == "spock"):
        resultado.config(text="¡Ganaste!", fg="#74b1ce",  highlightbackground="#74b1ce", highlightthickness=2)
    elif opcion_jugador == "spock" and (computadora == "piedra" or computadora == "tijera"):
        resultado.config(text="¡Ganaste!", fg="#74b1ce",highlightbackground="#74b1ce", highlightthickness=2)
    else:
        resultado.config(text="Perdiste. Lo siento.", fg="#ea3e18", highlightbackground="#ea3e18", highlightthickness=2)

# Creamos los botones
boton_piedra = tk.Button(text="Piedra", command=lambda: jugar("piedra"), font=("Arial", 14), padx=10, pady=20, fg="black", bg="#74b1ce", activebackground="#5cbf88", borderwidth=0, highlightthickness=0, width=10, bd=5)
boton_piedra.pack()

boton_papel = tk.Button(text="papel", command=lambda: jugar("papel"), font=("Arial", 14), padx=10, pady=20, fg="black", bg="#74b1ce", activebackground="#5cbf88", borderwidth=0, highlightthickness=0, width=10, bd=5)
boton_papel.pack()

boton_tijera = tk.Button(ventana, text="Tijera", command=lambda: jugar("tijera"), font=("Arial", 14), padx=10, pady=20, fg="black", bg="#74b1ce", activebackground="#5cbf88", borderwidth=0, highlightthickness=0, width=10, bd=5)
boton_tijera.pack()

boton_lagarto = tk.Button(ventana, text="Lagarto", command=lambda: jugar("lagarto"), font=("Arial", 14), padx=10, pady=20, fg="black", bg="#74b1ce", activebackground="#5cbf88", borderwidth=0, highlightthickness=0, width=10, bd=5)
boton_lagarto.pack()

boton_spock = tk.Button(ventana, text="spock", command=lambda: jugar("spock"), font=("Arial", 14), padx=10, pady=20, fg="black", bg="#74b1ce", activebackground="#5cbf88", borderwidth=0, highlightthickness=0, width=10, bd=5)
boton_spock.pack()

computadora_label = tk.Label(ventana, text="")
computadora_label.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()











