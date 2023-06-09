
from PIL import Image, ImageTk
import random
import tkinter as tk
from tkinter import messagebox

contador = 0

def reiniciar_juego():
    global numero_secreto, contador
    contador = 0
    numero_secreto = random.randint(1, 10)

def incrementar_contador():
    global contador
    contador += 1

def verificar_numero():
    intento = int(entry.get())
    entry.delete(0, tk.END)
    
    if intento < numero_secreto:
        messagebox.showinfo("Resultado", "Demasiado bajo. Intenta de nuevo.")
        incrementar_contador()
    elif intento > numero_secreto:
        messagebox.showinfo("Resultado", "Demasiado alto. Intenta de nuevo.")
        incrementar_contador()
    else:
        incrementar_contador()
        messagebox.showinfo("Resultado", f"¡Felicidades! ¡Adivinaste el número en {contador} intentos!")
        reiniciar_juego()

numero_secreto = random.randint(1, 10)

vent = tk.Tk()
vent.geometry("500x800+560+150")
vent.title("Adivina el número")
vent.config(cursor="pirate")
vent.config(bg="black")

entry = tk.Entry(vent, background="red")
entry.pack(pady=20)
entry.config(fg="white")

imagen = Image.open("G:\Escritorio\profe\polimorfismo\mmm.jpg") # Abrir imagen

imagen_tk = ImageTk.PhotoImage(imagen) #  imagen formato compatible con Tkinter

etiqueta = tk.Label(vent, image=imagen_tk) #  widget de imagen y mostrarla
etiqueta.pack()

label = tk.Label(vent, text="Estoy pensando en un número entre 1 y 10.\n¿Puedes adivinar cuál es?")
label.pack(pady=40)
label.config(bg="green")

button = tk.Button(vent, text="Adivinar", command=verificar_numero)
button.pack(pady=5)

vent.mainloop()
