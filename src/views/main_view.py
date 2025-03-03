import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class MainView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Selecciona un tipo de herramienta")
        self.root.geometry("500x400")
        self.root.config(bg="red")

        # Ruta del logo
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Obtiene el directorio actual
        self.logo_path = os.path.join(base_dir, "..", "assets", "MW-Black-Logo.png")  # Ruta absoluta


        # Cargar imagen del logo
        self.logo = Image.open(self.logo_path)
        self.logo = self.logo.resize((150, 75))  # Ajustar tamaño
        self.logo = ImageTk.PhotoImage(self.logo)

        # Mostrar logo
        self.logo_label = tk.Label(root, image=self.logo, bg="red")
        self.logo_label.pack(pady=10)

        # Título
        tk.Label(root, text="Seleccione el tipo de herramienta:", font=("Arial", 14, "bold"), bg="white").pack(pady=5)

        # Contenedor de botones
        self.frame = tk.Frame(root, bg="white")
        self.frame.pack()

        # Crear botones dinámicamente para cada modelo de herramienta
        modelos = self.controller.obtener_modelos()
        for modelo in modelos:
            btn = tk.Button(self.frame, text=modelo, font=("Arial", 12), width=15, height=2, 
                            command=lambda m=modelo: self.abrir_seleccion_job(m))
            btn.pack(pady=5)

    def abrir_seleccion_job(self, modelo):
        """Abre la ventana de selección de Job ID"""
        self.controller.abrir_seleccion_job(modelo)
