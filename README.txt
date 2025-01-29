README - Configurador de Entorno de Trabajo / Workspace Setup

Descripción / Description

Este script de Python automatiza la configuración de un entorno de trabajo abriendo automáticamente Google Chrome con pestañas esenciales (YouTube, Google Calendar, Gmail y X) y Visual Studio Code.

This Python script automates the setup of a workspace by automatically opening Google Chrome with essential tabs (YouTube, Google Calendar, Gmail, and X) and Visual Studio Code.

Requisitos / Requirements

Python 3 instalado / Python 3 installed

Google Chrome instalado en la ubicación predeterminada del sistema operativo / Google Chrome installed in the default system location

Visual Studio Code instalado y accesible desde la línea de comandos / Visual Studio Code installed and accessible from the command line

Instalación y Uso / Installation and Usage

Clonar o descargar el script en tu máquina local. / Clone or download the script to your local machine.

Ejecutar el script desde la terminal o línea de comandos: / Run the script from the terminal or command line:

python script.py

Verificación manual: / Manual verification:

Si Google Chrome no se abre correctamente, revisa su ruta en el código. / If Google Chrome does not open correctly, check its path in the code.

Si Visual Studio Code no se inicia, asegúrate de que está instalado y accesible desde la terminal. / If Visual Studio Code does not start, ensure it is installed and accessible from the terminal.

Compatibilidad / Compatibility

El script es compatible con los siguientes sistemas operativos: / The script is compatible with the following operating systems:

Windows

macOS

Linux

Funcionalidades / Features

open_browser_tabs(): Abre Chrome con pestañas en YouTube, Google Calendar, Gmail y X. / Opens Chrome with tabs for YouTube, Google Calendar, Gmail, and X.

open_visual_studio_code(): Inicia Visual Studio Code. / Launches Visual Studio Code.

setup_workspace(): Ejecuta ambas funciones para preparar el entorno de trabajo. / Runs both functions to set up the workspace.

Posibles Errores y Soluciones / Possible Errors and Solutions

Google Chrome no abre: Verifica que la ruta en chrome_path sea correcta para tu sistema operativo. / Google Chrome does not open: Check that the path in chrome_path is correct for your operating system.

Visual Studio Code no se inicia: Asegúrate de que code está en el PATH del sistema. / Visual Studio Code does not start: Ensure that code is in the system PATH.

Autor / Author

Creado por Francisco Villahermosa. / Created by Francisco Villahermosa.

