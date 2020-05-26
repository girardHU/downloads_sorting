class Handler(FileSystemEventHandler):

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + '/' + filename
            new_destination = folder_destination + '/' + filename
            os.rename(src, new_destination)
            print("Ah, le fichier %s a été deplace" % filename)