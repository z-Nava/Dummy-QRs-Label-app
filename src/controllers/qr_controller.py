import tkinter as tk
from models.qr_model import generar_qr, obtener_jobs
from views.main_view import QRView

class QRController:
    def __init__(self):
        self.root = tk.Tk()
        self.view = QRView(self.root, self)

    def obtener_jobs(self):
        """Devuelve una lista de Job IDs disponibles"""
        return obtener_jobs()

    def generar_qrs(self, job_id, cantidad):
        """Llama a la función del modelo para generar QR"""
        return generar_qr(job_id, cantidad)

    def abrir_ventana_secundaria(self):
        """Abre una ventana secundaria"""
        new_window = tk.Toplevel(self.root)
        new_window.title("Ventana secundaria")
        new_window.geometry("500x300")
        new_window.config(bg="blue")

        tk.Label(new_window, text="Hola desde la ventana secundaria", bg="blue", fg="white", font=("Arial", 12)).pack(pady=10)

        btn_cerrar = ttk.Button(new_window, text="Cerrar", command=new_window.destroy)
        btn_cerrar.pack(pady=10)

    def run(self):
        self.root.mainloop()
