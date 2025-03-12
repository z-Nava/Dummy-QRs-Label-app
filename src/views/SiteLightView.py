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
        """Genera el código QR y lo muestra en la interfaz."""
        version = self.version_var.get()
        año = str(self.año_var.get())[-2:]  # Últimos 2 dígitos del año
        semana = str(self.semana_var.get()).zfill(2)  # Formato de dos dígitos
        consecutivo = str(self.consecutivo_var.get()).zfill(3)  # Siempre 3 dígitos

        # Generar código con la nomenclatura correcta
        codigo = f"MXF_SLMP{version}{año}{semana}{consecutivo}"

        # Actualizar etiqueta de resultado
        self.resultado_label.config(text=f"Código: {codigo}")

        # Obtener datos completos para guardar en la estructura de carpetas
        herramienta_nombre = "SITE_LIGHT"  # Carpeta principal
        año_completo = int(self.año_var.get())  # Año completo (ej. 2024)
        semana_num = int(self.semana_var.get())  # Convertir semana a entero

        # Llamar a `guardar_qr()` con la estructura organizada
        self.guardar_qr(codigo, herramienta_nombre, año_completo, semana_num)


    def guardar_qr(self, codigo_qr, herramienta, año, semana):
        """Genera el QR y lo guarda en una estructura organizada"""
        qr = qrcode.make(codigo_qr)

        # Obtener la ruta base `qrs_generados/`
        script_dir = os.path.dirname(os.path.abspath(__file__))  # `src/views/`
        qr_base_folder = os.path.abspath(os.path.join(script_dir, "..", "..", "qrs_generados"))

        # Construir la estructura de carpetas: qrs_generados/{herramienta}/{año}/Semana_{semana}/
        herramienta_folder = os.path.join(qr_base_folder, herramienta)
        año_folder = os.path.join(herramienta_folder, str(año))
        semana_folder = os.path.join(año_folder, f"Semana_{semana}")

        # Crear las carpetas si no existen
        os.makedirs(semana_folder, exist_ok=True)

        # Ruta del archivo QR
        qr_path = os.path.join(semana_folder, f"{codigo_qr}.png")
        qr.save(qr_path)

        # Mostrar QR en la interfaz
        self.mostrar_qr(qr_path)

        print(f"✅ QR guardado en: {qr_path}")  # Para depuración

    def mostrar_qr(self, qr_path):
        """Carga la imagen QR y la muestra en la interfaz"""
        qr_img = Image.open(qr_path)
        qr_img = qr_img.resize((150, 150))  # Ajustar tamaño
        qr_img = ImageTk.PhotoImage(qr_img)

        self.qr_label.config(image=qr_img)
        self.qr_label.image = qr_img  # Guardar referencia para evitar que se elimine

