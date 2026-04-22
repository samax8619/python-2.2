import tkinter as Ventana

class Inicio_sesion:

    def __init__(self, dato_color):
        self.formulario = Ventana.Tk()
        self.formulario.geometry("600x600")
        self.formulario.title("Inicio de sesion")

        self.label_mensaje = ""

    def ejecutar_preguntas(self):
        label_usuario = Ventana.Label(self.formulario, text="Digite el nombre:")
        label_usuario.pack()

       
        self.entry_usuario = Ventana.Entry(self.formulario)
        self.entry_usuario.pack()

        self.label_mensaje = Ventana.Label(self.formulario, text="")
        self.label_mensaje.pack()

        boton_guardar = Ventana.Button(
            self.formulario,
            text="Guardar Cliente",
            command=lambda: self.iniciar_sesion()
        )
        boton_guardar.pack()

       
        boton_limpiar = Ventana.Button(
            self.formulario,
            text="Limpiar",
            command=lambda: self.limpiar()
        )
        boton_limpiar.pack()

        return self.formulario

    def iniciar_sesion(self):
        
        usuario = self.entry_usuario.get()
        self.label_mensaje.config(text=f"Cliente guardado: {usuario}")

    def limpiar(self):
        self.entry_usuario.delete(0, Ventana.END)
        self.label_mensaje.config(text="")
