import os
import time
from datetime import datetime
from utils.config import URL, SAVE_DIRECTORY, INTERVAL
from screenshot import take_screenshot

if __name__ == "__main__":
    print("=" * 50)
    print("  SISTEMA DE CAPTURAS DE PANTALLA AUTOMÁTICAS")
    print("=" * 50)
    print(f"URL: {URL}")
    print(f"Directorio de guardado: {SAVE_DIRECTORY}")
    print(f"Intervalo: {INTERVAL} segundos ({INTERVAL/60} minutos)")
    print("\nEl programa está ejecutándose. Presiona Ctrl+C para detener.")
    print("-" * 50)
    
    # Crear directorio si no existe
    os.makedirs(SAVE_DIRECTORY, exist_ok=True)
    
    try:
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"\n[{current_time}] Tomando captura de pantalla...")
            take_screenshot(URL, SAVE_DIRECTORY)
            print(f"Esperando {INTERVAL/60} minutos para la próxima captura...")
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("\n\nPrograma detenido por el usuario.")
        print("Gracias por usar el sistema de capturas automáticas.")