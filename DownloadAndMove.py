import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/jaidevkaleeswaran/Downloads"              # Add the path of you "Downloads" folder.
to_dir = "/Users/jaidevkaleeswaran/Desktop/Downloaded_Files" #Create "Document_Files" folder in your Desktop and update the path accordingly.


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(event)

        name, extension = os.path.splitext(event.src_path)
        print(name, extension)
       
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name = os.path.basename(event.src_path)
                print("Downloaded" + file_name)
                
                path_1 = from_dir + '/' + file_name 
                path_2 = to_dir + "/" + key
                path_3 = to_dir + "/" + key + "/" + file_name

                time.sleep(1)
                if os.path.exists(path_2):
                    print("Directory Extists!")
                    time.sleep(1)
                    if os.path.exists(path_3):
                        print("File already exists in " + key)
                        print("Renaming file" + file_name + "...")
                        new_file_name = os.path.splitext(file_name)[0] + str(random.randint(1,999))
                    print("Moving" + file_name + "...")

                    shutil.move(path_1, path_3)
                else:
                    os.makedirs(path_2)
                    print("Moving" + file_name + "...")
                    shutil.move(path_1, path_3)
                    
            
# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()

