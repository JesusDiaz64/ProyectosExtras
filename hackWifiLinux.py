
# Linux

import subprocess

def get_wifi_profiles_linux():
    try:
        # Ejecutar el comando `nmcli` para listar perfiles de Wi-Fi guardados
        data = subprocess.check_output(['nmcli', '-t', '-f', 'NAME', 'connection', 'show'], 
                                       stderr=subprocess.STDOUT).decode('utf-8')
        # Dividir los resultados por líneas para obtener los nombres de las conexiones
        profiles = data.strip().split('\n')
        return profiles
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el comando nmcli. Asegúrate de tener permisos adecuados.")
        return []

def get_wifi_password_linux(profile):
    try:
        # Ejecutar el comando `nmcli` para obtener los detalles de la conexión
        data = subprocess.check_output(['nmcli', '-s', '-g', '802-11-wireless-security.psk', 
                                        'connection', 'show', profile], 
                                       stderr=subprocess.STDOUT).decode('utf-8').strip()
        return data if data else "None"
    except subprocess.CalledProcessError:
        return "Error al obtener la contraseña. Puede que no tengas permisos."

def main():
    profiles = get_wifi_profiles_linux()
    
    if not profiles:
        print("No se encontraron perfiles de red.")
        return
    
    print("{:<30} | {:<}".format("Red Wi-Fi", "Contraseña"))
    print("-" * 50)
    
    for profile in profiles:
        password = get_wifi_password_linux(profile)
        print("{:<30} | {:<}".format(profile, password))
    
    input("\nPresiona Enter para salir...")

if __name__ == "__main__":
    main()
