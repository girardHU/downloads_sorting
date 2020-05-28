import sys
import os
import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from monitoring import MyHandler
from menu import MyMenu

# TODO implement image handling
# TODO detect folder arborescence from the parent folder and offer to select in which sub-folders it should be stored
if __name__ == '__main__':


    # menu = MyMenu()
    # menu.display_menu()

    with open('config.json') as config_file:
        config_json = json.load(config_file)

    downloadsObserver = Observer()
    downloadsObserver.schedule(MyHandler(), path=config_json.get('monitored_folder'), recursive=True)

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
