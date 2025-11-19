#Diego Andre Solis Vazquez
#3B programacion
#CBTIS89
#programa para calcular una compra
import tkinter as tk
from tkinter import messagebox

# Variables globales para almacenar cálculos
subtotal = 0.0
iva = 0.0
total = 0.0

def calcular_subtotal():
    global subtotal
    try:
        cantidad = int(entry_cantidad.get())
        precio = float(entry_precio.get())
        subtotal = cantidad * precio
        label_resultado.config(text=f"Subtotal: ${subtotal:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

def calcular_iva():
    global iva
    if subtotal == 0:
        messagebox.showwarning("Atención", "Primero calcula el subtotal.")
        return
    iva = subtotal * 0.16
    label_resultado.config(text=f"IVA (16%): ${iva:.2f}")

def calcular_total():
    global total
    if subtotal == 0:
        messagebox.showwarning("Atención", "Primero calcula el subtotal.")
        return
    iva = subtotal * 0.16
    total = subtotal + iva
    label_resultado.config(text=f"Total de compra: ${total:.2f}")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Compra")
ventana.geometry("320x350")

# Etiquetas y entradas
tk.Label(ventana, text="Cantidad de artículos:").pack(pady=5)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

tk.Label(ventana, text="Precio por artículo ($):").pack(pady=5)
entry_precio = tk.Entry(ventana)
entry_precio.pack()

# Botones para cada cálculo
tk.Button(ventana, text="Calcular Subtotal", command=calcular_subtotal).pack(pady=10)
tk.Button(ventana, text="Calcular IVA", command=calcular_iva).pack(pady=10)
tk.Button(ventana, text="Calcular Total", command=calcular_total).pack(pady=10)

# Etiqueta para mostrar resultados
label_resultado = tk.Label(ventana, text="", font=("Arial", 12), justify="left")
label_resultado.pack(pady=20)

# Iniciar ventana
ventana.mainloop()