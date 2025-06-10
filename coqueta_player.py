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

# Lista de tuplas: (línea, tiempo en segundos desde el inicio)
sync_letra = [
    ("Pensando y viendo las estrellas, pregunté", 0),
    ("Si, en algún lugar, esto se estaría repitiendo", 4),
    ("Si es que, en otro mundo, tal vez nos ganó el deseo", 7),
    ("O si solo fuimos un error del universo", 11),
    ("", 13),
    ("Baby, bésame", 14),
    ("Quiero que vuelvas a mis brazos pa' sentirnos eternos como la última vez", 15),
    ("Quiero confesarte, te extraño, como un loco, te pienso, yo sé que tú también", 20),
    ("Porfa, ma, ya vuelve conmigo, pero no como amigos como la última vez", 28),
    ("Quiero confesarte, te extraño, como un loco, te pienso, yo sé que tú también", 34),
    ("", 36),
    ("Coqueta", 38),
    ("Si me quieres, solo di la neta", 40),
    ("Que se entere todito el planeta", 44),
    ("Chula, ya decide qué onda, nena", 47),
    ("Qué onda, nena", 48),
    ("", 50),
    ("Coqueta", 51),
    ("Si me quieres, solo di la neta", 53),
    ("Que se entere todito el planeta", 56),
    ("Chula, ya decide qué onda, nena", 58),
    ("Qué onda, nena", 60),
    ("", 63),
    ("Dame, dame un besito, mami", 64),
    ("Dale, ¿cómo no quieres que me clave?", 67)
]

def mostrar_karaoke(letra, delay=4):
    import time
    colores = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    for i, linea in enumerate(letra):
        color = colores[i % len(colores)]
        print(color + linea + Style.RESET_ALL)
        # Delay personalizado
        if i == 19:
            time.sleep(5)
        elif i >= 30:
            time.sleep(4)
        else:
            time.sleep(delay)


def mostrar_karaoke_sincronizado(sync_letra):
    import time
    colores = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    start = time.time()
    for i, (linea, t_obj) in enumerate(sync_letra):
        color = colores[i % len(colores)]
        now = time.time()
        wait = t_obj - (now - start)
        if wait > 0:
            time.sleep(wait)
        print(color + linea + Style.RESET_ALL)


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
        # Lanzar karaoke sincronizado y detener música a los 70 segundos
        karaoke_thread = threading.Thread(target=mostrar_karaoke_sincronizado, args=(sync_letra,))
        karaoke_thread.start()
        time.sleep(70)
        pygame.mixer.music.stop()
        karaoke_thread.join()
        print("\nMúsica detenida tras 1 minuto y 10 segundos.\n")
    except Exception as e:
        print(f"Error al reproducir la canción: {e}")

# NOTA: Para sincronizar la letra con la música, debes ajustar el parámetro 'delay' en mostrar_karaoke(letra, delay=SEGUNDOS) para que coincida con el ritmo de la canción. Si quieres una sincronización exacta, se requiere un archivo de tiempos (timestamps) para cada línea, lo cual se puede agregar si lo deseas.
