import sys
import os
import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from monitoring import Handler
from menu import Menu

if __name__ == '__main__':


    menu = Menu()
    menu.display_menu()
    
    downloadsObserver = Observer()
    downloadsObserver.schedule(Handler(), path=folder_to_track, recursive=True)

    downloadsObserver.start()

    # L'observer travaille dans un thread séparé donc on fait une 
    # boucle infinie pour maintenir le thread principal
    # actif dans cette démo mais dans un vrai programme,
    # vous mettez votre taff ici.
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Ctrl + C arrête tout
        downloadsObserver.stop()
    # on attend que tous les threads se terminent proprement
    downloadsObserver.join()
