import sys
import time
import logging
import os
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

origin_dir = "C:\\Users\\Saif\\OneDrive\\Desktop"

class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(origin_dir) as enteries:
            for entry in enteries:
                name = entry.name
                #dest = 
    
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = origin_dir
    event_handler = MoveHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()