#Diego Andre Solis Vazquez
#3B programacion
#CBTIS89
#programa que pide que escojas una figura geometrica y te la muestre
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk
# Ruta base del archivo actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Diccionario de figuras con rutas de imagen
# Diccionario con rutas completas
figuras = {
    "Cuadrado": os.path.join(BASE_DIR, "cuadro.png"),
    "Rectángulo": os.path.join(BASE_DIR, "rectangulo.png"),
    "Círculo": os.path.join(BASE_DIR, "circulo.png"),
    "Triángulo": os.path.join(BASE_DIR, "triangulo.png")
}

def mostrar_imagen(event):
   seleccion = lista_figuras.get(lista_figuras.curselection())
   ruta = figuras.get(seleccion)
   imagen = Image.open(ruta)
   imagen = imagen.resize((200, 200)) # Redimensionar imagen
   imagen_tk = ImageTk.PhotoImage(imagen)
   etiqueta_imagen.config(image=imagen_tk)
   etiqueta_imagen.image = imagen_tk # Mantener referencia

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Visualizador de Figuras")
ventana.geometry("400x400")

# Título
titulo = tk.Label(ventana, text="Selecciona una figura:", font=("Arial", 14))
titulo.pack(pady=10)

# Listbox de figuras
lista_figuras = tk.Listbox(ventana, font=("Arial", 12), height=4)
for figura in figuras.keys():
   lista_figuras.insert(tk.END, figura)
   lista_figuras.pack()

# Imagen mostrada
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady=20)

# Evento al seleccionar
lista_figuras.bind("<<ListboxSelect>>", mostrar_imagen)

# Ejecutar
ventana.mainloop()

 

 