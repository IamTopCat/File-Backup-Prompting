import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter as tk
from tkinter import simpledialog

class FileHandler(FileSystemEventHandler):
    def on_closed(self, event):
        if event.src_path.endswith(".odt"):  # Check if it's an OpenOffice file
            backup_location = "/path/to/backup"  # Suggested storage destination
            user_destination = simpledialog.askstring("Backup Destination", "Enter backup destination:", initialvalue=backup_location)
            if user_destination:
                # Copy the file to the chosen destination
                shutil.copy(event.src_path, user_destination)

if __name__ == "__main":
    path_to_monitor = "/path/to/OpenOffice/files"
    
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_monitor, recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
