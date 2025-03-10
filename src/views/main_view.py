import tkinter as tk
from PIL import Image, ImageTk
import os

class MainView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Dummy QR Generator - MXFUEL")
        self.root.geometry("1020x800")
        self.root.config(bg="#DC1F26")

        # Ruta base de la carpeta assets (corrige la ruta para apuntar a src/assets/)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Sube un nivel a `src/`
        assets_path = os.path.join(base_dir, "assets")  # Ahora apunta correctamente a `src/assets/`

        # Cargar imagen del logo
        logo_path = os.path.join(assets_path, "MW-Black-Logo.png")
        if os.path.exists(logo_path):
            logo_img = Image.open(logo_path).resize((150, 75))
            self.logo = ImageTk.PhotoImage(logo_img)  # Guardar referencia para evitar que se borre
        else:
            print(f"⚠️ Imagen del logo no encontrada: {logo_path}")
            self.logo = None  # Evitar errores

        # Mostrar logo
        if self.logo:
            self.logo_label = tk.Label(root, image=self.logo, bg="#DC1F26")
            self.logo_label.pack(pady=10)

        # Título
        tk.Label(root, text="Seleccione el tipo de herramienta:", font=("Arial", 14, "bold"), bg="#DC1F26", fg="white").pack(pady=5)

        # Contenedor de botones (marco)
        self.frame = tk.Frame(root, bg="#DC1F26")
        self.frame.pack()

        # Modelos con imágenes disponibles
        modelos_con_imagen = {
            "SITE LIGHT": "sitelight.png",
            "SCREED": "screed.png",
            "EARLY ENTRY SAW": "earlyentrysaw.png",
            "BACKPACK / BRIEFCASE": "backpack.png",

            "POWER TROWEL": "powertrowel.png",
            "THREADER": "threader.png",
            "PLATE COMPACTOR": "platecompactor.png",
            "HIGH CICLE" : "highcIcle.png",
            
            "SUB PUMP": "subpump.png",
            "RAMER": "rammer.png",
        }

        # Obtener lista de herramientas desde el controlador
        modelos = self.controller.obtener_modelos()
        columnas = 4
        self.imagenes = {}  # Diccionario para almacenar imágenes y evitar que desaparezcan

        for i, modelo in enumerate(modelos):
            fila = i // columnas
            columna = i % columnas

            # Verificar si la herramienta tiene imagen asignada
            img_filename = modelos_con_imagen.get(modelo, None)  # Verifica si hay imagen asignada
            img_path = os.path.join(assets_path, img_filename) if img_filename else None

            if img_path and os.path.exists(img_path):
                imagen = Image.open(img_path).resize((80, 80))  # Ajustar tamaño sin deformar
                self.imagenes[modelo] = ImageTk.PhotoImage(imagen)  # Guardar en memoria

                # Crear botón con imagen
                btn = tk.Button(self.frame, text=modelo, font=("Arial", 12), width=150, height=120,
                                image=self.imagenes[modelo], compound="top",
                                command=lambda m=modelo: self.controller.abrir_seleccion_herramienta(m))
            else:
                if img_path:
                    print(f"⚠️ Imagen no encontrada: {img_path}")  # Mensaje para depuración

                # Crear botón solo con texto si no hay imagen
                btn = tk.Button(self.frame, text=modelo, font=("Arial", 12), width=20, height=2,
                                command=lambda m=modelo: self.controller.abrir_seleccion_herramienta(m))

            btn.grid(row=fila, column=columna, padx=10, pady=10)
