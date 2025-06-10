import os
import sys
from colorama import init, Fore, Style
import pygame

init(autoreset=True)

print("\nReproduciendo: 'Coqueta' - Grupo Frontera\n")

mp3_file = os.path.join(os.path.dirname(__file__), 'coqueta.mp3')

# Letra de la canción (fragmento representativo)
letra = [
    "Pensando y viendo las estrellas, pregunté",
    "Si, en algún lugar, esto se estaría repitiendo",
    "Si es que, en otro mundo, tal vez nos ganó el deseo",
    "O si solo fuimos un error del universo",
    "",
    "Baby, bésame",
    "Quiero que vuelvas a mis brazos pa' sentirnos eternos como la última vez",
    "Quiero confesarte, te extraño, como un loco, te pienso, yo sé que tú también",
    "Porfa, ma, ya vuelve conmigo, pero no como amigos como la última vez",
    "Quiero confesarte, te extraño, como un loco, te pienso, yo sé que tú también",
    "",
    "Coqueta",
    "Si me quieres, solo di la neta",
    "Que se entere todito el planeta",
    "Chula, ya decide qué onda, nena",
    "Qué onda, nena",
    "",
    "Coqueta",
    "Si me quieres, solo di la neta",
    "Que se entere todito el planeta",
    "Chula, ya decide qué onda, nena",
    "Qué onda, nena",
    "",
    "Dame, dame un besito, mami",
    "Dale, ¿cómo no quieres que me clave?"
]

def mostrar_karaoke(letra, delay=4):
    import time
    import threading
    try:
        import msvcrt
        usar_msvcrt = True
    except ImportError:
        usar_msvcrt = False
    print("\nPresiona 'q' y luego ENTER para salir del karaoke...\n")
    stop_event = threading.Event()
    def check_quit():
        if usar_msvcrt:
            while not stop_event.is_set():
                if msvcrt.kbhit() and msvcrt.getch().lower() == b'q':
                    stop_event.set()
                    break
        else:
            while not stop_event.is_set():
                if input().strip().lower() == 'q':
                    stop_event.set()
                    break
    t_quit = threading.Thread(target=check_quit, daemon=True)
    t_quit.start()
    colores = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    for i, linea in enumerate(letra):
        if stop_event.is_set():
            print("\nKaraoke detenido por el usuario.\n")
            break
        color = colores[i % len(colores)]
        print(color + linea + Style.RESET_ALL)
        # Delay personalizado
        if i == 19:
            time.sleep(5)
        elif i >= 30:
            time.sleep(4)
        else:
            time.sleep(delay)
    stop_event.set()

if not os.path.exists(mp3_file):
    print("No se encontró el archivo 'coqueta.mp3'. Por favor, colócalo en la misma carpeta que este script.")
else:
    try:
        import threading
        import time
        # Inicializar pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.load(mp3_file)
        pygame.mixer.music.play()
        # Lanzar karaoke y detener música a los 45 segundos
        karaoke_thread = threading.Thread(target=mostrar_karaoke, args=(letra,))
        karaoke_thread.start()
        time.sleep(45)
        pygame.mixer.music.stop()
        karaoke_thread.join()
        print("\nMúsica detenida tras 45 segundos.\n")
    except Exception as e:
        print(f"Error al reproducir la canción: {e}")

# NOTA: Para sincronizar la letra con la música, debes ajustar el parámetro 'delay' en mostrar_karaoke(letra, delay=SEGUNDOS) para que coincida con el ritmo de la canción. Si quieres una sincronización exacta, se requiere un archivo de tiempos (timestamps) para cada línea, lo cual se puede agregar si lo deseas.
