import tkinter as tk
from tkinter import ttk

class AppAutenticacion:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Autenticación")
        self.ventana.geometry("700x600")

        self.crear_tabs()

   
    def crear_tabs(self):
        pestañas = ttk.Notebook(self.ventana)

        self.tab_login = tk.Frame(pestañas)
        self.tab_registro = tk.Frame(pestañas)

        pestañas.add(self.tab_login, text="Inicio de Sesión")
        pestañas.add(self.tab_registro, text="Registro Cliente")

        pestañas.pack(expand=True, fill="both")

        self.interfaz_login()
        self.interfaz_registro()

   
    def interfaz_login(self):

        tk.Label(self.tab_login, text="Usuario o correo:").pack()
        self.entry_usuario = tk.Entry(self.tab_login)
        self.entry_usuario.pack()

        tk.Label(self.tab_login, text="Contraseña:").pack()
        self.entry_password = tk.Entry(self.tab_login, show="*")
        self.entry_password.pack()

        self.recordar = tk.BooleanVar()
        tk.Checkbutton(self.tab_login, text="Recordar sesión", variable=self.recordar).pack()

        tk.Button(self.tab_login, text="Ingresar", command=self.iniciar_sesion).pack(pady=5)
        tk.Button(self.tab_login, text="Limpiar", command=self.limpiar_login).pack(pady=5)

        self.label_login = tk.Label(self.tab_login, text="")
        self.label_login.pack()

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        self.label_login.config(text=f"Bienvenido {usuario} ✅")

    def limpiar_login(self):
        self.entry_usuario.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.label_login.config(text="")

    
    def interfaz_registro(self):

        frame = tk.LabelFrame(self.tab_registro, text="Datos del Cliente")
        frame.pack(padx=10, pady=10, fill="both")

        # Nombre
        tk.Label(frame, text="Nombre completo:").pack()
        self.entry_nombre = tk.Entry(frame)
        self.entry_nombre.pack()

        # Tipo documento
        tk.Label(frame, text="Tipo de documento:").pack()
        self.combo_doc = ttk.Combobox(frame, values=["CC", "TI", "Pasaporte"])
        self.combo_doc.pack()

        # Número documento
        tk.Label(frame, text="Número de documento:").pack()
        self.entry_doc = tk.Entry(frame)
        self.entry_doc.pack()

        # Fecha nacimiento
        tk.Label(frame, text="Fecha de nacimiento:").pack()
        self.entry_fecha = tk.Entry(frame)
        self.entry_fecha.pack()

        # Género
        tk.Label(frame, text="Género:").pack()
        self.genero = tk.StringVar()
        tk.Radiobutton(frame, text="Masculino", variable=self.genero, value="M").pack()
        tk.Radiobutton(frame, text="Femenino", variable=self.genero, value="F").pack()

        # Intereses
        tk.Label(frame, text="Intereses:").pack()
        self.int1 = tk.BooleanVar()
        self.int2 = tk.BooleanVar()
        tk.Checkbutton(frame, text="Ropa", variable=self.int1).pack()
        tk.Checkbutton(frame, text="Tecnología", variable=self.int2).pack()

        # Ciudad
        tk.Label(frame, text="Ciudad:").pack()
        self.combo_ciudad = ttk.Combobox(frame, values=["Cúcuta", "Bogotá", "Medellín"])
        self.combo_ciudad.pack()

        # Dirección
        tk.Label(frame, text="Dirección:").pack()
        self.entry_direccion = tk.Entry(frame)
        self.entry_direccion.pack()

        # Observaciones
        tk.Label(frame, text="Observaciones:").pack()
        self.text_obs = tk.Text(frame, height=3)
        self.text_obs.pack()

        # Satisfacción
        tk.Label(frame, text="Nivel de satisfacción:").pack()
        self.scale = tk.Scale(frame, from_=0, to=10, orient="horizontal")
        self.scale.pack()

        # Botones
        tk.Button(frame, text="Registrar", command=self.registrar_cliente).pack(pady=5)
        tk.Button(frame, text="Limpiar", command=self.limpiar_registro).pack(pady=5)

        self.label_registro = tk.Label(frame, text="")
        self.label_registro.pack()

    def registrar_cliente(self):
        nombre = self.entry_nombre.get()
        self.label_registro.config(text=f"Cliente {nombre} registrado ✅")

    def limpiar_registro(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_doc.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
        self.entry_direccion.delete(0, tk.END)
        self.text_obs.delete("1.0", tk.END)
        self.label_registro.config(text="")

    
    def ejecutar(self):
        self.ventana.mainloop()



if __name__ == "__main__":
    app = AppAutenticacion()
    app.ejecutar()