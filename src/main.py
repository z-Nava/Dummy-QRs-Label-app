import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import Image, ImageTk
import os

#Datos simulados de "Jobs"
jobs_data = {
    "MXF_BPMPUL2434061": {"modelo": "BACKPACK", "corrida": "MXF371-2XC", "version": "24", "año": "2025", "semana": "34", "consecutivo": "061"},
    "MXF_BPMPUL2434062": {"modelo": "BACKPACK", "corrida": "MXF371-2XC", "version": "24", "año": "2025", "semana": "34", "consecutivo": "062"},
}

def generar_qr():
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
    
    info_job = jobs_data[job_id]
    modelo = info_job["modelo"]
    corrida = info_job["corrida"]
    version = info_job["version"]
    año = info_job["año"]
    semana = info_job["semana"]
    consecutivo = info_job["consecutivo"]

    #Carpeta para guardar los QR
    output_dir = "qrs_generados"
    os.makedirs(output_dir, exist_ok=True)

    for i in range(cantidad):
        data_qr = f"MXF_{modelo[:2].upper()}MP{corrida}UL{version}{año[-2:]}{semana}{consecutivo}"
        qr = qrcode.make(data_qr)
        filename = f"{output_dir}/{data_qr}_{i+1}.png"
        qr.save(filename)

        if i == 0:
            mostrar_qr(filename)

    messagebox.showinfo("QRs generados", f"Se han generado {cantidad} QRs")

def mostrar_qr(filename):
    img = Image.open(filename)
    #QR TAMAÑO 1 PULGADAS POR .5 PULGADAS
    img = img.resize((400, 400))
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img

#Ventana principal
root = tk.Tk()
root.title("Generador de QRs")
root.resizable(False, False)
root.config(bg="red")
root.geometry("400x400")

#Widgets
tk.Label(root, text="Job ID:", bg="red").pack(pady=5)
entry_job = tk.Entry(root)
entry_job.pack(pady=5)

#Drop down
entry_job = ttk.Combobox(root)
entry_job['values'] = list(jobs_data.keys())
entry_job.pack(pady=5)

tk.Label(root, text="Cantidad:", bg="red").pack(pady=5)
entry_cantidad = tk.Entry(root)
entry_cantidad.pack(pady=5)

btn_generar = tk.Button(root, text="Generar QRs", command=generar_qr)
btn_generar.pack(pady=5)

qr_label = tk.Label(root)
qr_label.pack(pady=5)

root.mainloop()