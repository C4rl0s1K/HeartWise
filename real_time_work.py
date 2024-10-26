import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class RestartOnChange(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"Zmieniono plik: {event.src_path}. Restartuję aplikację...")
            os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == "__main__":

    process = subprocess.Popen([sys.executable, "main.py"])

    path = "."
    event_handler = RestartOnChange()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        process.terminate()

    observer.join()
