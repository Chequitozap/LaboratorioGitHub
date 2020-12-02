#Interfaz grafica para el usuario 

import tkinter 

ventana = tkinter.Tk()
ventana.geometry ("400x300")

def saludo():
    print("Te amo mi amor eres la mejor de todas")

boton1 = tkinter.Button(ventana, text = "Presionalo mi amor" , padx = 20 , pady =20 , command = saludo)
boton1.pack()

etiqueta = tkinter.Label(ventana, text = "Interfaz creada para decirte lo mucho que te amo  ",bg = "red")
etiqueta.pack(fill = tkinter.BOTH, expand = True)

ventana.mainloop()
