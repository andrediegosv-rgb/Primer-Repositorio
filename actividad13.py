#Diego Andre Solis Vazquez
#3B programacion
#CBTIS89
#programa que pide que escojas una carrera y te muestre cual seleccionaste
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("lista despelgable ComboBox")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana,text="Seleciona una carrera:")  
etiqueta.pack(pady=18)

opciones = ["ARH","arquitectura","comercio electronico","comercio internacional","construcccion","contabilidad","mecatronica","programacion"]
ComboColores = ttk.Combobox(ventana,values=opciones, state="readonly")
ComboColores.pack(pady=5)

def mostrar_seleccion(event):
    seleccion = ComboColores.get()
    etiqueta_resultado.config(text=f"seleccionaste:{seleccion}")

ComboColores.bind("<<ComboboxSelected>>",mostrar_seleccion)

etiqueta_resultado = tk.Label(ventana, text="No has seleccionado nada")
etiqueta_resultado.pack(pady=20)

ventana.mainloop()