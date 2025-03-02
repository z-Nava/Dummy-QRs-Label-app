import qrcode
import os

# Datos simulados de "Jobs"
jobs_data = {
    "MXF_BPMPUL2434061": {"modelo": "BACKPACK", "corrida": "MP", "version": "UL", "año": "2024", "semana": "34", "consecutivo": "001"},
    "MXF_BCMPUL2434062": {"modelo": "BRIEFCASE", "corrida": "MP", "version": "UL", "año": "2024", "semana": "34", "consecutivo": "001"},
}

def generar_qr(job_id, cantidad):
    """Genera códigos QR y los guarda en la carpeta qrs_generados/"""
    if job_id not in jobs_data:
        return None

    try:
        cantidad = int(cantidad)
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        return None

    info_job = jobs_data[job_id]
    modelo = info_job["modelo"]
    corrida = info_job["corrida"]
    version = info_job["version"]
    año = info_job["año"]
    semana = info_job["semana"]
    consecutivo = info_job["consecutivo"]

    output_dir = "qrs_generados"
    os.makedirs(output_dir, exist_ok=True)

    qr_files = []
    for i in range(cantidad):
        data_qr = f"MXF_{modelo[0].upper()}{modelo[4].upper()}{corrida}{version}{año[2]}{año[3]}{semana}{consecutivo}"
        
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(data_qr)
        qr.make(fit=True)

        img_qr = qr.make_image(fill="black", back_color="white")
        filename = f"{output_dir}/{data_qr}_{i+1}.png"
        img_qr.save(filename)
        qr_files.append(filename)

    return qr_files  # Retorna la lista de archivos generados

def obtener_jobs():
    """Devuelve los job IDs disponibles"""
    return list(jobs_data.keys())
