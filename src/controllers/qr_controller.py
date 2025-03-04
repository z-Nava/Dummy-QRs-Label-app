import tkinter as tk
from models.qr_model import generar_qr
from models.nomenclaturas import obtener_modelos
from views.main_view import MainView
from views.BackpackBriefcaseView import BackpackBriefcaseView  
from views.SiteLightView import SiteLightView
from views.ScreedView import ScreedView

class QRController:
    def __init__(self):
        self.root = tk.Tk()
        self.view = MainView(self.root, self)

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
        else:
            print(f"No hay vista implementada aún para {modelo}")  # Mensaje para futuras herramientas

        new_root.mainloop()


    def generar_qrs(self, codigo_qr, cantidad):
        """Llama a la función del modelo para generar QR"""
        return generar_qr(codigo_qr, cantidad)

    def run(self):
        self.root.mainloop()
