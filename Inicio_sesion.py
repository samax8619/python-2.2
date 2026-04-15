import tkinter as Ventana

class Inicio_sesion:

    def __init__(self, dato_color):
        self.formulario = Ventana.Tk()
        self.formulario.geometry("600x600")
        self.formulario.title("Inicio de sesion")

        self.label_mensaje = ""

    def ejecutar_preguntas(self):
        label_usuario = Ventana.Label(self.formulario, text="Usuario: ")
        label_usuario.pack()

        entry_usuario = Ventana.Entry(self.formulario)
        entry_usuario.pack()

        self.label_mensaje = Ventana.Label(self.formulario, text="mensaje")
        self.label_mensaje.pack()

        boton_inicio = Ventana.Button(
            self.formulario,
            text="Iniciar sesion",
            command=lambda: self.iniciar_sesion()
        )
        boton_inicio.pack()

        return self.formulario

    def iniciar_sesion(self):
        self.label_mensaje.config(text="Usuario inicio sesion....")