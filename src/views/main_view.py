import tkinter as tk
from PIL import Image, ImageTk
import os

class MainView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Selecciona un tipo de herramienta")
        self.root.geometry("1020x800")
        self.root.config(bg="red")

        # Ruta del logo
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.logo_path = os.path.join(base_dir, "..", "assets", "MW-Black-Logo.png")

        # Cargar imagen del logo
        self.logo = Image.open(self.logo_path)
        self.logo = self.logo.resize((150, 75))
        self.logo = ImageTk.PhotoImage(self.logo)

        # Mostrar logo
        self.logo_label = tk.Label(root, image=self.logo, bg="red")
        self.logo_label.pack(pady=10)

        # Título
        tk.Label(root, text="Seleccione el tipo de herramienta:", font=("Arial", 14, "bold"), bg="red", fg="white").pack(pady=5)

        # Contenedor de botones (marco)
        self.frame = tk.Frame(root, bg="red")
        self.frame.pack()

        # Crear botones dinámicamente en formato de cuadrícula
        modelos = self.controller.obtener_modelos()
        columnas = 4
        self.imagenes = {}

        for i, modelo in enumerate(modelos):
            fila = i // columnas
            columna = i % columnas

            # Crear botón con imagen si existe, sino solo texto
            btn = tk.Button(self.frame, text=modelo, font=("Arial", 12), width=25, height=10,
                            command=lambda m=modelo: self.controller.abrir_seleccion_herramienta(m))
            btn.grid(row=fila, column=columna, padx=10, pady=10)
