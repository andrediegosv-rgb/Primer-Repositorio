#Diego Andre Solis Vazquez
#3B programacion
#CBTIS89
#programa que pida que escojas un descuento y te lo muestre
import tkinter as tk

ventana = tk.Tk()
ventana.title("calcular descuentos")
ventana. geometry("400x300")
ventana.resizable(False,True )


etiqueta_cantidad = tk.Label(ventana,text="ingresa")
etiqueta_cantidad.pack(pady=10)

entrada_cantidad = tk.Entry(ventana,justify="center")
entrada_cantidad.pack()

def ejecutar_radio():
    opcion = seleccion.get()

    if opcion == 1:
        cantidad = float(entrada_cantidad.get())
        descuento = cantidad * 0.05
        etiqueta_resultado.config(text=f"Hola estimado cliente usted obtuvo un descuento del 5%,el cual va ah pagar:{descuento:.2f}")

    elif opcion == 2:
        cantidad = float(entrada_cantidad.get())
        descuento = cantidad * 0.10
        etiqueta_resultado.config(text=f"Hola estimado cliente usted obtuvo un descuento del 10%,el cual va ah pagar:{descuento:.2f}")

    
    elif opcion == 3:
        cantidad = float(entrada_cantidad.get())
        descuento = cantidad * 0.15
        etiqueta_resultado.config(text=f"Hola estimado cliente usted obtuvo un descuento del 15%,el cual va ah pagar:{descuento:.2f}")

seleccion = tk.IntVar()

radioB1 = tk.Radiobutton(ventana,text="descuento del 5%",variable=seleccion,value=1, command=ejecutar_radio)
radioB2 = tk.Radiobutton(ventana,text="descuento del 10%",variable=seleccion,value=2, command=ejecutar_radio)
radioB3 = tk.Radiobutton(ventana,text="descuento del 15%",variable=seleccion,value=3, command=ejecutar_radio)

radioB1.pack(pady=10)
radioB2.pack(pady=10)
radioB3.pack(pady=10)

etiqueta_resultado = tk.Label(ventana,text="",wraplength=200, justify="left")
etiqueta_resultado.pack(pady=20)

ventana.mainloop()