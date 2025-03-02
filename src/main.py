import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import Image, ImageTk
import os

# Datos simulados de "Jobs"
jobs_data = {
    "MXF_BPMPUL2434061": {"modelo": "BACKPACK", "corrida": "MP", "version": "UL", "año": "2024", "semana": "34", "consecutivo": "001"},
    "MXF_BCMPUL2434062": {"modelo": "BRIEFCASE", "corrida": "MP", "version": "UL", "año": "2024", "semana": "34", "consecutivo": "001"},
}

def generar_qr():
    """Genera códigos QR según la cantidad ingresada, manteniendo la nomenclatura original."""
    job_id = entry_job.get()
    cantidad = entry_cantidad.get()

    if job_id not in jobs_data:
        messagebox.showwarning("Error", "El trabajo no existe")
        return
    
    try:
        cantidad = int(cantidad)
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Cantidad no válida")
        return

    # Extraer datos según la nomenclatura definida
    info_job = jobs_data[job_id]
    modelo = info_job["modelo"]
    corrida = info_job["corrida"]
    version = info_job["version"]
    año = info_job["año"]
    semana = info_job["semana"]
    consecutivo = info_job["consecutivo"]

    # Carpeta para guardar los QR
    output_dir = "qrs_generados"
    os.makedirs(output_dir, exist_ok=True)

    for i in range(cantidad):
        # Generar nomenclatura correcta sin modificar estructura
        data_qr = f"MXF_{modelo[0].upper()}{modelo[4].upper()}{corrida}{version}{año[2]}{año[3]}{semana}{consecutivo}"

        # Configurar QR con mejor calidad
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data_qr)
        qr.make(fit=True)

        img_qr = qr.make_image(fill="black", back_color="white")
        filename = f"{output_dir}/{data_qr}_{i+1}.png"
        img_qr.save(filename)

        # Mostrar solo el primer QR generado
        if i == 0:
            mostrar_qr(filename)

    messagebox.showinfo("QRs generados", f"Se han generado {cantidad} códigos QR")

def mostrar_qr(filename):
    """Muestra la imagen del código QR generado"""
    img = Image.open(filename)
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img

def new_window():
    """Crea una ventana secundaria"""
    ventana = tk.Toplevel(root)
    ventana.title("Ventana secundaria")
    ventana.geometry("500x300")
    ventana.config(bg="blue")

    tk.Label(ventana, text="Hola desde la ventana secundaria", bg="blue", fg="white", font=("Arial", 12)).pack(pady=10)

    btn_cerrar = ttk.Button(ventana, text="Cerrar", command=ventana.destroy)
    btn_cerrar.pack(pady=10)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Generador de QRs")
root.resizable(False, False)
root.config(bg="red")
root.geometry("400x400")

# Widgets
tk.Label(root, text="Job ID:", bg="red", fg="white", font=("Arial", 12)).pack(pady=5)
entry_job = ttk.Combobox(root, values=list(jobs_data.keys()))
entry_job.pack(pady=5)

tk.Label(root, text="Cantidad:", bg="red", fg="white", font=("Arial", 12)).pack(pady=5)
entry_cantidad = tk.Entry(root)
entry_cantidad.pack(pady=5)

btn_generar = tk.Button(root, text="Generar QRs", command=generar_qr, bg="black", fg="white", font=("Arial", 10))
btn_generar.pack(pady=5)

btn_ventana = tk.Button(root, text="Ventana secundaria", command=new_window, bg="black", fg="white", font=("Arial", 10))
btn_ventana.pack(pady=5)

qr_label = tk.Label(root)
qr_label.pack(pady=5)

root.mainloop()
