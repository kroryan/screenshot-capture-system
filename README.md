# Sistema de Capturas de Pantalla Automáticas

Este sistema permite realizar capturas de pantalla automáticas de una URL específica a intervalos regulares. Utiliza Selenium y Chrome en modo headless para capturar imágenes de alta calidad sin necesidad de interfaz gráfica.

## Características

- Capturas de pantalla automáticas de cualquier sitio web o aplicación web
- Modo headless (sin interfaz gráfica) para funcionamiento en segundo plano
- Intervalos configurables entre capturas (por defecto cada 5 minutos)
- Nombres de archivo con timestamp para fácil organización (formato: screenshot_YYYYMMDD_HHMMSS.png)
- Resolución de captura configurable (por defecto 1920x1080)
- Manejo de errores y recuperación automática
- Interfaz de línea de comandos simple y clara
- Creación automática del directorio de destino si no existe
- Posibilidad de detener el proceso con Ctrl+C

## Requisitos

- Python 3.7 o superior
- Google Chrome instalado
- Conexión a internet (para la primera ejecución, cuando se descarga el WebDriver)
- Sistema operativo: Windows, macOS o Linux

## Dependencias

El sistema utiliza las siguientes bibliotecas de Python:
- `selenium`: Para la automatización del navegador
- `webdriver-manager`: Para gestionar automáticamente la instalación del controlador de Chrome
- `requests`: Para operaciones HTTP (opcional)
- `pillow`: Para procesamiento de imágenes (opcional)

## Instalación

1. Clona o descarga este repositorio:
```bash
git clone <URL-del-repositorio>
cd screenshot-capture-system
```

2. Navega hasta la carpeta del proyecto:
```bash
cd c:\Users\adryl\Pictures\screenshot\screenshot-capture-system
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Configuración

Puedes modificar la configuración en el archivo `src/utils/config.py`:

- `URL`: La dirección web de la que quieres tomar capturas
  - Default: "http://localhost:8080/game/details?host=unknown&port=6302"
  - Ejemplo: "https://www.ejemplo.com"

- `SAVE_DIRECTORY`: La carpeta donde se guardarán las imágenes
  - Default: "C:\Users\adryl\Pictures\screenshot\capturas"
  - Asegúrate de que la ruta exista o el programa la creará automáticamente

- `INTERVAL`: El tiempo en segundos entre cada captura
  - Default: 300 (5 minutos)
  - Puedes reducirlo para capturas más frecuentes o aumentarlo para capturas más espaciadas

- `WINDOW_SIZE`: La resolución de las capturas en formato "ancho,alto"
  - Default: "1920,1080"
  - Formatos comunes: "1366,768", "1280,720", "3840,2160" (4K)

## Uso

### Ejecución básica

Para ejecutar el programa:

```bash
cd c:\Users\adryl\Pictures\screenshot\screenshot-capture-system\src
python main.py
```

El programa mostrará información sobre su configuración y comenzará a tomar capturas automáticamente.

### Información mostrada durante la ejecución

Al iniciar el programa verás la siguiente información:
- URL que se está capturando
- Directorio donde se guardan las capturas
- Intervalo entre capturas
- Instrucciones para detener el programa

Por cada captura tomada, el programa mostrará:
- Timestamp de la captura
- Ruta completa donde se guardó la imagen
- Tiempo de espera hasta la próxima captura

### Detener el programa

Para detener el programa, simplemente presiona `Ctrl+C` en la terminal. El programa mostrará un mensaje de despedida y se cerrará correctamente.

## Estructura del proyecto

```
screenshot-capture-system/
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Este archivo de documentación
└── src/                  # Código fuente
    ├── main.py           # Punto de entrada del programa
    ├── screenshot.py     # Funciones para tomar capturas
    └── utils/            # Utilidades y configuración
        └── config.py     # Configuración del sistema
```

## Funcionamiento interno

1. **Inicialización**:
   - El programa carga la configuración desde `config.py`
   - Verifica y crea el directorio de guardado si no existe
   - Muestra información sobre la configuración actual

2. **Captura de pantalla**:
   - Inicializa Chrome en modo headless (sin interfaz gráfica)
   - Navega a la URL especificada
   - Espera a que la página cargue completamente (3 segundos por defecto)
   - Toma la captura de pantalla
   - Guarda la imagen con un nombre basado en la fecha y hora actual
   - Cierra el navegador para liberar recursos

3. **Ciclo principal**:
   - Después de cada captura, el programa espera el tiempo especificado
   - El ciclo continúa hasta que el usuario detiene el programa con Ctrl+C

## Solución de problemas

### El programa no inicia o muestra errores

- Verifica que Chrome esté instalado correctamente
- Asegúrate de tener todas las dependencias instaladas con `pip install -r requirements.txt`
- Verifica que la URL sea accesible desde tu navegador normal

### Las capturas no muestran el contenido esperado

- Aumenta el tiempo de espera en `screenshot.py` (busca `time.sleep(3)` y aumenta el valor)
- Verifica que la URL sea correcta y que no requiera autenticación
- Comprueba que la página cargue correctamente en un navegador normal

### Errores con el WebDriver

Si ves errores relacionados con el WebDriver:
- Borra la carpeta `.wdm` en tu directorio de usuario y deja que el programa descargue de nuevo el controlador
- Actualiza Chrome a la última versión

## Personalización avanzada

### Cambiar el formato de la imagen

Actualmente el sistema guarda las imágenes en formato PNG. Si deseas cambiar el formato, modifica el nombre del archivo en la función `take_screenshot` en `screenshot.py`.

### Añadir autenticación

Si necesitas capturar páginas que requieren autenticación, puedes modificar la función `take_screenshot` para añadir cookies o completar formularios de inicio de sesión.

### Capturar diferentes secciones de la página

Puedes modificar el código en `screenshot.py` para capturar elementos específicos de la página en lugar de la página completa.

## Notas finales

- La primera ejecución puede tardar un poco mientras se descarga el driver adecuado para Chrome
- Asegúrate de que el sitio web o servidor esté funcionando antes de iniciar el programa
- El sistema está diseñado para ser ligero y consumir pocos recursos
- Las capturas de pantalla se guardan con alta resolución y sin compresión
- Si necesitas ejecutar el programa en segundo plano por largos períodos, considera usar un administrador de procesos como `nohup` en Linux o crear un servicio en Windows
│   └── utils
│       └── config.py    # Configuration settings for the application
├── requirements.txt      # Lists the project dependencies
├── README.md             # Documentation for the project
└── .gitignore            # Specifies files to ignore in Git
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd screenshot-capture-system
   ```

2. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Configure the application:**
   - Open `src/utils/config.py` to set the desired URL and save directory for screenshots.

4. **Run the application:**
   ```
   python src/main.py
   ```

## Usage

The application will take a screenshot of the specified URL every 5 minutes and save it in the designated directory with a timestamped filename. To stop the application, press `Ctrl+C` in the terminal.

## Dependencies

- `selenium`: For browser automation.
- `webdriver-manager`: To manage the Chrome WebDriver automatically.

## Notes

- Ensure that Google Chrome is installed on your system.
- Make sure the local server hosting the specified URL is running before starting the application.