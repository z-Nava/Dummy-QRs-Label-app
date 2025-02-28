import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import Image, ImageTk
import os

#Datos simulados de "Jobs"
jobs_data = {
    "123456" : {"modelo": "taladro", "fecha":"2021-10-10"},
    "654321" : {"modelo": "sierra", "fecha":"2021-10-11"},
    "334623" : {"LINEA": "MXF007", "ITEM_DESCRIPTION": "SPRING, DIA1.32XOD14.3XL56.4MM \MX FUEL BAT INTERFACE", "COMPONENT": "696570001", "FECHA": "02/04/2025 15:44:00"},
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
    fecha = info_job["fecha"]

    #Carpeta para guardar los QR
    output_dir = "qrs_generados"
    os.makedirs(output_dir, exist_ok=True)

    for i in range(cantidad):
        data_qr = f"Job ID: {job_id}\nModelo: {modelo}\nFecha: {fecha}\nQR: {i+1} de {cantidad}"
        qr = qrcode.make(data_qr)
        filename = f"{output_dir}/{job_id}_{i+1}.png"
        qr.save(filename)

        if i == 0:
            mostrar_qr(filename)

    messagebox.showinfo("QRs generados", f"Se han generado {cantidad} QRs")

def mostrar_qr(filename):
    img = Image.open(filename)
    img = img.resize((200, 200))
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