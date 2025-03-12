import tkinter as tk
from tkinter import ttk
import os
import qrcode
from PIL import Image, ImageTk
from models.nomenclaturas import herramientas_data

class SiteLightView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Site Light")
        self.root.geometry("500x500")  # Aumentamos tamaño para mostrar QR
        self.root.config(bg="white")

        self.data = herramientas_data["SITE LIGHT"]

        # Título
        tk.Label(root, text="Site Light QR", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

        # Selección de Versión
        tk.Label(root, text="Selecciona la versión:", font=("Arial", 12), bg="white").pack()
        self.version_var = tk.StringVar()
        ttk.Combobox(root, textvariable=self.version_var, values=self.data["version"], state="readonly").pack(pady=5)

        # Selección de Año
        tk.Label(root, text="Selecciona el año:", font=("Arial", 12), bg="white").pack()
        self.año_var = tk.IntVar(value=2024)
        ttk.Spinbox(root, from_=min(self.data["años"]), to=max(self.data["años"]), textvariable=self.año_var, width=5).pack(pady=5)

        # Selección de Semana
        tk.Label(root, text="Selecciona la semana:", font=("Arial", 12), bg="white").pack()
        self.semana_var = tk.IntVar(value=1)
        ttk.Spinbox(root, from_=min(self.data["semanas"]), to=max(self.data["semanas"]), textvariable=self.semana_var, width=5).pack(pady=5)

        # Selección de Consecutivo
        tk.Label(root, text="Selecciona el consecutivo:", font=("Arial", 12), bg="white").pack()
        self.consecutivo_var = tk.IntVar(value=1)
        ttk.Spinbox(root, from_=min(self.data["consecutivo"]), to=max(self.data["consecutivo"]), textvariable=self.consecutivo_var, width=5).pack(pady=5)

        # Botón para generar código QR
        tk.Button(root, text="Generar Código QR", font=("Arial", 12, "bold"), bg="green", fg="white",
                  command=self.generar_codigo).pack(pady=15)
        
        # Espacio para mostrar el código generado
        self.resultado_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="white", fg="blue")
        self.resultado_label.pack()

        # Espacio para mostrar la imagen del QR
        self.qr_label = tk.Label(root, bg="white")
        self.qr_label.pack()

        # Botón para regresar a la vista principal
        tk.Button(self.root, text="Regresar", font=("Arial", 12, "bold"), bg="gray", fg="white",
          command=lambda: self.controller.regresar(self.root)).pack(pady=10)
    
    def generar_codigo(self):
        """Genera y muestra el código QR usando el controlador."""
        codigo_qr = self.controller.generar_codigo(
        "SL",
        self.version_var.get(),
        self.año_var.get(),
        self.semana_var.get(),
        self.consecutivo_var.get()
    )

        self.resultado_label.config(text=f"Código: {codigo_qr}")

        qr_path = self.controller.guardar_qr(
            codigo_qr, "SITE_LIGHT", self.año_var.get(), self.semana_var.get()
    )

        self.controller.mostrar_qr(qr_path, self.qr_label)



    def mostrar_qr(self, qr_path):
        """Carga la imagen QR y la muestra en la interfaz"""
        qr_img = Image.open(qr_path)
        qr_img = qr_img.resize((150, 150))  # Ajustar tamaño
        qr_img = ImageTk.PhotoImage(qr_img)

        self.qr_label.config(image=qr_img)
        self.qr_label.image = qr_img  # Guardar referencia para evitar que se elimine

