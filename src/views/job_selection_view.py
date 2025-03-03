import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class JobSelectionView:
    def __init__(self, root, controller, modelo):
        self.controller = controller
        self.root = tk.Toplevel(root)  # Crear una nueva ventana
        self.root.title(f"Seleccionar Job ID - {modelo}")
        self.root.geometry("400x400")
        self.root.config(bg="lightgray")

        self.modelo = modelo

        # Etiqueta y selección de Job ID
        tk.Label(self.root, text=f"Modelo: {modelo}", font=("Arial", 14, "bold"), bg="lightgray").pack(pady=10)
        tk.Label(self.root, text="Seleccione un Job ID:", font=("Arial", 12), bg="lightgray").pack(pady=5)
        
        self.entry_job = ttk.Combobox(self.root, values=self.controller.obtener_jobs_por_modelo(modelo))
        self.entry_job.pack(pady=5)
        
        # Entrada de cantidad
        tk.Label(self.root, text="Cantidad de QRs:", font=("Arial", 12), bg="lightgray").pack(pady=5)
        self.entry_cantidad = tk.Entry(self.root)
        self.entry_cantidad.pack(pady=5)

        # Botón para generar QR
        self.btn_generar = tk.Button(self.root, text="Generar QRs", command=self.generar_qr, bg="black", fg="white", font=("Arial", 10))
        self.btn_generar.pack(pady=10)

        # Espacio para mostrar el QR generado
        self.qr_label = tk.Label(self.root)
        self.qr_label.pack(pady=10)

    def generar_qr(self):
        """Genera y muestra los códigos QR"""
        job_id = self.entry_job.get()
        cantidad = self.entry_cantidad.get()

        if not job_id or not cantidad:
            messagebox.showerror("Error", "Seleccione un Job ID y especifique la cantidad")
            return

        qr_files = self.controller.generar_qrs(job_id, cantidad)

        if qr_files is None:
            messagebox.showerror("Error", "Job ID inválido o cantidad incorrecta")
            return

        self.mostrar_qr(qr_files[0])  # Mostrar el primer QR generado
        messagebox.showinfo("QRs generados", f"Se han generado {len(qr_files)} códigos QR")

    def mostrar_qr(self, filename):
        """Muestra un QR en la interfaz"""
        img = Image.open(filename)
        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)
        self.qr_label.config(image=img)
        self.qr_label.image = img
