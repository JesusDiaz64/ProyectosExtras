
# sudo apt install network-manager
# python3 "Nombre Aplicacion".py

import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

def get_wifi_profiles_linux():
    try:
        # Ejecutar el comando `nmcli` para listar perfiles de Wi-Fi guardados
        data = subprocess.check_output(['nmcli', '-t', '-f', 'NAME', 'connection', 'show'], 
                                       stderr=subprocess.STDOUT).decode('utf-8')
        # Dividir los resultados por líneas para obtener los nombres de las conexiones
        profiles = data.strip().split('\n')
        return profiles
    except subprocess.CalledProcessError:
        return []

def get_wifi_password_linux(profile):
    try:
        # Ejecutar el comando `nmcli` para obtener los detalles de la conexión
        data = subprocess.check_output(['nmcli', '-s', '-g', '802-11-wireless-security.psk', 
                                        'connection', 'show', profile], 
                                       stderr=subprocess.STDOUT).decode('utf-8').strip()
        return data if data else "None"
    except subprocess.CalledProcessError:
        return "Error al obtener la contraseña."

def fetch_wifi_data():
    profiles = get_wifi_profiles_linux()
    if not profiles:
        messagebox.showerror("Error", "No se encontraron perfiles de red o falta de permisos.")
        return
    
    # Limpiar los datos existentes en la tabla
    for row in tree.get_children():
        tree.delete(row)
    
    # Agregar perfiles y contraseñas a la tabla
    for profile in profiles:
        password = get_wifi_password_linux(profile)
        tree.insert("", tk.END, values=(profile, password))

# Crear la ventana principal
app = tk.Tk()
app.title("Gestor de Redes Wi-Fi")
app.geometry("600x400")

# Etiqueta
label = tk.Label(app, text="Lista de redes Wi-Fi guardadas:", font=("Arial", 14))
label.pack(pady=10)

# Crear una tabla para mostrar los datos
columns = ("Red Wi-Fi", "Contraseña")
tree = ttk.Treeview(app, columns=columns, show="headings", height=15)
tree.heading("Red Wi-Fi", text="Red Wi-Fi")
tree.heading("Contraseña", text="Contraseña")
tree.pack(pady=10, fill=tk.BOTH, expand=True)

# Botón para actualizar los datos
fetch_button = tk.Button(app, text="Actualizar", command=fetch_wifi_data, font=("Arial", 12))
fetch_button.pack(pady=10)

# Ejecutar el bucle de la aplicación
app.mainloop()
