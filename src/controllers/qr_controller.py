import tkinter as tk
from models.nomenclaturas import obtener_modelos
from views.main_view import MainView
from views.BackpackBriefcaseView import BackpackBriefcaseView  
from views.SiteLightView import SiteLightView
from views.ScreedView import ScreedView
from views.EarlyEntrySawView import EarlyEntrySawView
from views.LSMView import LSMView
from views.PowerTrowelView import PowerTrowelView
from views.ThreaderView import ThreaderView
from views.PlateCompactorView import PlateCompactorView
from PIL import Image, ImageTk

class QRController:
    def __init__(self):
        self.root = tk.Tk()
        self.view = MainView(self.root, self)
        self.root.mainloop()

    def mostrar_vista_principal(self):
        self.root = tk.Tk()  # Crea una nueva instancia solo si no existe
        self.main_view = MainView(self.root, self)
        self.root.mainloop()

    def obtener_modelos(self):
        """Devuelve una lista de modelos de herramientas disponibles"""
        return obtener_modelos()

    def abrir_seleccion_herramienta(self, modelo):
        """Abre la ventana de configuración de la herramienta seleccionada"""
        
        # Verifica si la ventana principal 'root' existe antes de intentar destruirla
        if hasattr(self, 'root') and self.root.winfo_exists():
            self.root.destroy()  # Cierra la ventana principal
        
        new_root = tk.Tk()  # Crea una nueva ventana

        if modelo == "BACKPACK / BRIEFCASE":
            BackpackBriefcaseView(new_root, self)  # Abre la vista específica
        elif modelo == "SITE LIGHT":
            SiteLightView(new_root, self)
        elif modelo == "SCREED":
            ScreedView(new_root, self)
        elif modelo == "EARLY ENTRY SAW":
            EarlyEntrySawView(new_root, self)
        elif modelo == "LSM":
            LSMView(new_root, self)
        elif modelo == "POWER TROWEL":
            PowerTrowelView(new_root, self)
        elif modelo == "THREADER":
            ThreaderView(new_root, self)
        elif modelo == "PLATE COMPACTOR":
            PlateCompactorView(new_root, self)
        else:
            print(f"No hay vista implementada aún para {modelo}")  # Mensaje para futuras herramientas

        new_root.mainloop()
        
    def regresar(self, ventana=None):
        """Cierra la ventana actual y regresa a la vista principal."""
        if ventana:
            ventana.destroy()
        self.mostrar_vista_principal()


    def mostrar_qr(self, qr_path):
        """Carga la imagen QR y la muestra en la interfaz"""
        qr_img = Image.open(qr_path)
        qr_img = qr_img.resize((150, 150))
        qr_img = ImageTk.PhotoImage(qr_img)

        self.qr_label.config(image=qr_img)
        self.qr_label.image = qr_img  # Guardar referencia para evitar que se elimine

    def run(self):
        self.root.mainloop()
