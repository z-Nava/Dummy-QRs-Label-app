import tkinter as tk
from models.qr_model import generar_qr
from models.nomenclaturas import obtener_modelos, obtener_jobs_por_modelo
from views.main_view import MainView
from views.job_selection_view import JobSelectionView

class QRController:
    def __init__(self):
        self.root = tk.Tk()
        self.view = MainView(self.root, self)

    def obtener_modelos(self):
        """Devuelve una lista de modelos de herramientas disponibles"""
        return obtener_modelos()

    def obtener_jobs_por_modelo(self, modelo):
        """Devuelve los Job IDs disponibles según el modelo de herramienta"""
        return obtener_jobs_por_modelo(modelo)

    def abrir_seleccion_job(self, modelo):
        """Abre la ventana de selección de Job ID"""
        JobSelectionView(self.root, self, modelo)

    def generar_qrs(self, job_id, cantidad):
        """Llama a la función del modelo para generar QR"""
        return generar_qr(job_id, cantidad)

    def run(self):
        self.root.mainloop()
