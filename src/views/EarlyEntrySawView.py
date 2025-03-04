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
