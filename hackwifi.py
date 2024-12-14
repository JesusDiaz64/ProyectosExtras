
#WINDOWS
import subprocess

def get_wifi_profiles():
    try:
        # Ejecuta el comando para obtener los perfiles de red
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], 
                                       stderr=subprocess.STDOUT, 
                                       shell=True).decode('utf-8', errors="backslashreplace")
        
        # Extrae los nombres de los perfiles
        profiles = [line.split(":")[1][1:-1] for line in data.split('\n') if "All User Profile" in line]
        return profiles
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el comando de red. Asegúrate de tener permisos de administrador.")
        return []

def get_wifi_password(profile):
    try:
        # Ejecuta el comando para obtener la clave del perfil
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', profile, 'key=clear'], 
                                       stderr=subprocess.STDOUT, 
                                       shell=True).decode('utf-8', errors="backslashreplace")
        
        # Extrae la contraseña si está disponible
        password_lines = [line.split(":")[1][1:-1] for line in data.split('\n') if "Key Content" in line]
        return password_lines[0] if password_lines else "None"
    except subprocess.CalledProcessError:
        return "Error al obtener la contraseña. Puede que no tengas permisos."

def main():
    profiles = get_wifi_profiles()
    
    if not profiles:
        print("No se encontraron perfiles de red.")
        return
    
    print("{:<30} | {:<}".format("Red Wi-Fi", "Contraseña"))
    print("-" * 50)
    
    for profile in profiles:
        password = get_wifi_password(profile)
        print("{:<30} | {:<}".format(profile, password))
    
    input("\nPresiona Enter para salir...")

if __name__ == "__main__":
    main()
