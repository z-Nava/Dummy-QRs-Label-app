import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class QRView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Generador de QRs")
        self.root.geometry("400x400")
        self.root.config(bg="red")

        # Widgets
        tk.Label(root, text="Job ID:", bg="red", fg="white", font=("Arial", 12)).pack(pady=5)
        self.entry_job = ttk.Combobox(root, values=self.controller.obtener_jobs())
        self.entry_job.pack(pady=5)

        tk.Label(root, text="Cantidad:", bg="red", fg="white", font=("Arial", 12)).pack(pady=5)
        self.entry_cantidad = tk.Entry(root)
        self.entry_cantidad.pack(pady=5)

        self.btn_generar = tk.Button(root, text="Generar QRs", command=self.generar_qr, bg="black", fg="white", font=("Arial", 10))
        self.btn_generar.pack(pady=5)

        self.btn_ventana = tk.Button(root, text="Ventana secundaria", command=self.abrir_ventana_secundaria, bg="black", fg="white", font=("Arial", 10))
        self.btn_ventana.pack(pady=5)

        self.qr_label = tk.Label(root)
        self.qr_label.pack(pady=5)

    def generar_qr(self):
        """Genera y muestra los códigos QR"""
        job_id = self.entry_job.get()
        cantidad = self.entry_cantidad.get()
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

    def abrir_ventana_secundaria(self):
        """Abre una nueva ventana secundaria"""
        self.controller.abrir_ventana_secundaria()
