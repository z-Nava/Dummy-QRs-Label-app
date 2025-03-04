import tkinter as tk
from tkinter import ttk
import os
import qrcode
from PIL import Image, ImageTk

class EarlyEntrySawView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Site Light")
        self.root.geometry("500x500")  # Aumentamos tamaño para mostrar QR
        self.root.config(bg="white")

        # Título
        tk.Label(root, text="Configurar Código QR", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

        # Selección de Modelo
        tk.Label(root, text="Selecciona el modelo:", font=("Arial", 12), bg="white").pack()
        self.modelo_var = tk.StringVar()
        ttk.Combobox(root, textvariable=self.modelo_var, values=["EES (Early Entry Saw)"]).pack(pady=5)

        # Selección de Corrida
        tk.Label(root, text="Selecciona la corrida:", font=("Arial", 12), bg="white").pack()
        self.corrida_var = tk.StringVar()
        ttk.Combobox(root, textvariable=self.corrida_var, values=["MP"]).pack(pady=5)
        