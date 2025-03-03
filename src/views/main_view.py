import tkinter as tk
from tkinter import ttk

class MainView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Selecciona un tipo de herramienta")
        self.root.geometry("500x300")
        self.root.config(bg="white")

        tk.Label(root, text="Seleccione el tipo de herramienta:", font=("Arial", 14, "bold")).pack(pady=10)

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
