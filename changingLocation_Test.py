'''IGNORE... This is just a Testing Program'''

import shutil
import os

def move_files(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print(f"File Moved successfully from {source_path} to {destination_path}")
    except Exception as e:
        print(f"Error Moving file: {e}")

source_file = "C:/Users/prati/OneDrive/Desktop/Python/Day 68 - Exercise 7 - Clear the Clutter/readMe.txt"
destination_folder = "C:/Users/prati/OneDrive/Desktop/Python/Day 68 - Exercise 7 - Clear the Clutter/Pictures"
destination_file = os.path.join(destination_folder, os.path.basename(source_file))

move_files(source_file, destination_file)