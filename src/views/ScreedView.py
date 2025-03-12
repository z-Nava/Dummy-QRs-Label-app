import tkinter as tk
from tkinter import ttk
import os
import qrcode
from PIL import Image, ImageTk
from models.nomenclaturas import herramientas_data  # Importa el diccionario

class ScreedView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Screed")
        self.root.geometry("500x500")
        self.root.config(bg="white")

        # Obtener datos del diccionario
        self.data = herramientas_data["SCREED"]
        

        # Título
        tk.Label(root, text="Screed QR", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
    
        # Selección de Año
        tk.Label(root, text="Selecciona el año:", font=("Arial", 12), bg="white").pack()
        self.año_var = tk.StringVar(value=2024)  # Primer año disponible
        ttk.Spinbox(root, from_=min(self.data["años"]), to=max(self.data["años"]), textvariable=self.año_var, width=5).pack(pady=5)

        # Selección de Semana
        tk.Label(root, text="Selecciona la semana:", font=("Arial", 12), bg="white").pack()
        self.semana_var = tk.StringVar(value=1)  # Primera semana
        ttk.Spinbox(root, from_=min(self.data["semanas"]), to=max(self.data["semanas"]), textvariable=self.semana_var, width=5).pack(pady=5)

        # Selección de Consecutivo
        tk.Label(root, text="Selecciona el consecutivo:", font=("Arial", 12), bg="white").pack()
        self.consecutivo_var = tk.IntVar(value=1)  # Primer consecutivo
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
        """Genera el código QR y lo muestra en la interfaz."""
        año = self.año_var.get()[-2:]  # Últimos 2 dígitos
        semana = self.semana_var.get()
        consecutivo = str(self.consecutivo_var.get()).zfill(7) 

        codigo_qr = f"MXF_CSMPUL{año}{semana}{consecutivo}"
        self.resultado_label.config(text=f"Código: {codigo_qr}")

        # Generar y guardar QR en carpeta `qrs_generados/`
        self.guardar_qr(codigo_qr)

    def guardar_qr(self, codigo_qr):
        """Genera el QR y lo guarda en la carpeta qrs_generados/"""
        qr = qrcode.make(codigo_qr)

        # Ruta correcta fuera de `src/`
        script_dir = os.path.dirname(os.path.abspath(__file__))
        qr_folder = os.path.abspath(os.path.join(script_dir, "..", "..", "qrs_generados"))

        if not os.path.exists(qr_folder):
            os.makedirs(qr_folder)

        qr_path = os.path.join(qr_folder, f"{codigo_qr}.png")
        qr.save(qr_path)

        self.mostrar_qr(qr_path)

    def mostrar_qr(self, qr_path):
        """Carga la imagen QR y la muestra en la interfaz"""
        qr_img = Image.open(qr_path)
        qr_img = qr_img.resize((150, 150))
        qr_img = ImageTk.PhotoImage(qr_img)

        self.qr_label.config(image=qr_img)
        self.qr_label.image = qr_img  # Guardar referencia para evitar que se elimine

