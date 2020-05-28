import os
from watchdog.events import FileSystemEventHandler
class MyHandler(FileSystemEventHandler):

    # TODO implementer attributs pour tous les dossiers
    def on_modified(self, event):
        print(event.src_path)
        for filename in os.listdir(event.src_path):
        #     src = folder_to_track + '/' + filename
        #     new_destination = folder_destination + '/' + filename
        #     os.rename(src, new_destination)
        #     print("Ah, le fichier %s a été deplace" % filename)