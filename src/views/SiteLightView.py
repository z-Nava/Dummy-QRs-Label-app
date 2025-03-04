import tkinter as tk
from tkinter import ttk
import os
import qrcode
from PIL import Image, ImageTk

class SiteLightView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Site Light")
        self.root.geometry("500x500")  # Aumentamos tamaño para mostrar QR
        self.root.config(bg="white")

        # Título
        tk.Label(root, text="Configurar Código QR", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

        # Selección de Modelo
        tk.Label(root, text="Selecciona el modelo:", font=("Arial", 12), bg="white").pack()
        self.modelo_var = tk.StringVar()
        ttk.Combobox(root, textvariable=self.modelo_var, values=["SL (Site Light)"]).pack(pady=5)

        # Selección de Corrida
        tk.Label(root, text="Selecciona la corrida:", font=("Arial", 12), bg="white").pack()
        self.corrida_var = tk.StringVar()
        ttk.Combobox(root, textvariable=self.corrida_var, values=["MP"]).pack(pady=5)

        # Selección de Versión
        tk.Label(root, text="Selecciona la versión:", font=("Arial", 12), bg="white").pack()
        self.version_var = tk.StringVar()
        ttk.Combobox(root, textvariable=self.version_var, values=["UL", "GB", "ANZ"]).pack(pady=5)

        # Selección de Año
        tk.Label(root, text="Selecciona el año:", font=("Arial", 12), bg="white").pack()
        self.año_var = tk.IntVar(value=2024)
        ttk.Spinbox(root, from_=2020, to=2030, textvariable=self.año_var, width=5).pack(pady=5)

        # Selección de Semana
        tk.Label(root, text="Selecciona la semana:", font=("Arial", 12), bg="white").pack()
        self.semana_var = tk.IntVar(value=1)
        ttk.Spinbox(root, from_=1, to=52, textvariable=self.semana_var, width=5).pack(pady=5)

        # Selección de Consecutivo
        tk.Label(root, text="Selecciona el consecutivo:", font=("Arial", 12), bg="white").pack()
        self.consecutivo_var = tk.IntVar(value=1)
        ttk.Spinbox(root, from_=1, to=99, textvariable=self.consecutivo_var, width=5).pack(pady=5)

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
        tk.Button(root, text="Regresar", font=("Arial", 12, "bold"), bg="gray", fg="white",
                  command=self.regresar).pack(pady=10)
        
    def generar_codigo(self):
        """Genera el código QR y lo muestra en la interfaz."""
        modelo = self.modelo_var.get().split()[0]
        corrida = self.corrida_var.get()
        version = self.version_var.get()
        año = str(self.año_var.get())[-2:]
        semana = str(self.semana_var.get()).zfill(2)
        consecutivo = str(self.consecutivo_var.get()).zfill(3)

        # Generar código
        codigo = f"MXF_{modelo}{corrida}{version}{año}{semana}{consecutivo}"
       
        self.resultado_label.config(text=f"Código: {codigo}")

        # Generar y guardar QR
        self.guardar_qr(codigo)

    def guardar_qr(self, codigo_qr):
        """Genera el QR y lo guarda en la carpeta qrs_generados/"""
        qr = qrcode.make(codigo_qr)
        
        # Ruta correcta fuera de `src/`
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Obtiene la ruta actual (`src/views/`)
        qr_folder = os.path.abspath(os.path.join(script_dir, "..", "..", "qrs_generados"))  # Sube a `qrs_generados/`

        if not os.path.exists(qr_folder):
            os.makedirs(qr_folder)

        # Ruta del archivo QR
        qr_path = os.path.join(qr_folder, f"{codigo_qr}.png")
        qr.save(qr_path)

        # Mostrar QR en la interfaz
        self.mostrar_qr(qr_path)

    def mostrar_qr(self, qr_path):
        """Carga la imagen QR y la muestra en la interfaz"""
        qr_img = Image.open(qr_path)
        qr_img = qr_img.resize((150, 150))  # Ajustar tamaño
        qr_img = ImageTk.PhotoImage(qr_img)

        self.qr_label.config(image=qr_img)
        self.qr_label.image = qr_img  # Guardar referencia para evitar que se elimine

    def regresar(self):
        """Cierra esta ventana y regresa a la vista principal"""
        self.root.destroy()
        new_root = tk.Tk()
        from views.main_view import MainView
        MainView(new_root, self.controller)
        new_root.mainloop()
