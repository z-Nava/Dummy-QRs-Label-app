import tkinter as tk
from tkinter import ttk
import os
import qrcode
from PIL import Image, ImageTk
from models.nomenclaturas import herramientas_data  # Importa el diccionario


class ThreaderView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Threader")
        self.root.geometry("500x500")
        self.root.config(bg="white")

        # Obtener datos del diccionario
        datos = herramientas_data["THREADER"]
        self.modelo = datos["modelo"][0]  # Siempre "TH"
        self.corrida = datos["corrida"][0]  # Siempre "MP"
        self.versiones = datos["version"]
        self.tipos = datos["tipo"]  # Funcional (1) o Bomba (2)
        self.años = datos["años"]
        self.semanas = datos["semanas"]
        self.consecutivos = datos["consecutivo"]

        # Título
        tk.Label(root, text="Configurar Código QR - THREADER", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

        # Selección de versión (UL, EMEA, ANZ)
        tk.Label(root, text="Selecciona la versión:", font=("Arial", 12), bg="white").pack()
        self.version_var = tk.StringVar(value=self.versiones[0])  # Primera versión por defecto
        ttk.Combobox(root, textvariable=self.version_var, values=self.versiones).pack(pady=5)

        # Selección de tipo (1 = Funcional, 2 = Bomba)
        tk.Label(root, text="Selecciona el tipo:", font=("Arial", 12), bg="white").pack()
        self.tipo_var = tk.StringVar(value=self.tipos[0])  # Primer tipo por defecto
        ttk.Combobox(root, textvariable=self.tipo_var, values=self.tipos).pack(pady=5)

        # Selección de Año
        tk.Label(root, text="Selecciona el año:", font=("Arial", 12), bg="white").pack()
        self.año_var = tk.StringVar(value=self.años[0])  # Primer año disponible
        ttk.Combobox(root, textvariable=self.año_var, values=self.años).pack(pady=5)

        # Selección de Semana
        tk.Label(root, text="Selecciona la semana:", font=("Arial", 12), bg="white").pack()
        self.semana_var = tk.StringVar(value=self.semanas[0])  # Primera semana
        ttk.Combobox(root, textvariable=self.semana_var, values=self.semanas).pack(pady=5)

        # Selección de Consecutivo
        tk.Label(root, text="Selecciona el consecutivo:", font=("Arial", 12), bg="white").pack()
        self.consecutivo_var = tk.StringVar(value=self.consecutivos[0])  # Primer consecutivo
        ttk.Combobox(root, textvariable=self.consecutivo_var, values=self.consecutivos).pack(pady=5)

        # Botón para generar código QR
        tk.Button(
            root,
            text="Generar Código QR",
            font=("Arial", 12, "bold"),
            bg="green",
            fg="white",
            command=self.generar_codigo,
        ).pack(pady=15)

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
        modelo = self.modelo  # Siempre "TH"
        corrida = self.corrida  # Siempre "MP"
        version = self.version_var.get()  # Obtener la versión seleccionada
        tipo = self.tipo_var.get()  # Tipo de accesorio (1 o 2)
        año = self.año_var.get()[-2:]  # Últimos 2 dígitos del año
        semana = self.semana_var.get()
        consecutivo = int(self.consecutivo_var.get())  # Convertimos a entero

        # Ajustar el consecutivo según la versión para que siempre sean 21 caracteres
        if version == "UL":
            consecutivo_str = str(consecutivo).zfill(6)  # 6 dígitos
        elif version == "ANZ":
            consecutivo_str = str(consecutivo).zfill(5)  # 5 dígitos
        else:  # EMEA
            consecutivo_str = str(consecutivo).zfill(4)  # 4 dígitos

        # Generar código QR con la nomenclatura correcta
        codigo_qr = f"MXF_{modelo}{corrida}{version}{tipo}{año}{semana}{consecutivo_str}"
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

    
