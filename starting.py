import webbrowser
import os
import platform
import subprocess

def open_browser_tabs():
    """Abre las ventanas de YouTube, Google Calendar, Gmail y X en Google Chrome."""
    chrome_path = None
    if platform.system() == "Windows":
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    elif platform.system() == "Darwin":  # macOS
        chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    elif platform.system() == "Linux":
        chrome_path = "/usr/bin/google-chrome"

    if chrome_path and os.path.exists(chrome_path):
        youtube_url = "https://www.youtube.com"
        calendar_url = "https://calendar.google.com"
        gmail_url = "https://mail.google.com"
        x_url = "https://x.com/Franbucho"

        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(youtube_url)
        webbrowser.get('chrome').open_new_tab(calendar_url)
        webbrowser.get('chrome').open_new_tab(gmail_url)
        webbrowser.get('chrome').open_new_tab(x_url)
    else:
        print("Google Chrome no está instalado o no se encuentra en la ubicación predeterminada.")

def open_visual_studio_code():
    """Abre Visual Studio Code."""
    try:
        if platform.system() == "Windows":
            subprocess.Popen("code")
        elif platform.system() == "Darwin":  # macOS
            subprocess.Popen(["open", "-a", "Visual Studio Code"])
        elif platform.system() == "Linux":
            subprocess.Popen(["code"])
        else:
            print("Sistema operativo no reconocido. No se pudo abrir Visual Studio Code.")
    except Exception as e:
        print(f"Error al abrir Visual Studio Code: {e}")

def setup_workspace():
    """Configura el entorno de trabajo abriendo las herramientas necesarias."""
    print("Configurando tu área de trabajo...")
    open_browser_tabs()
    open_visual_studio_code()
    print("¡Todo listo para empezar a trabajar!")

if __name__ == "__main__":
    setup_workspace()