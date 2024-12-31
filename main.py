from tkinter import *
from tkinter import ttk
import os

def on_set():
    print("Source Path:", source.get())
    print("Destination Path:", destination.get())

def run_core_logic():
    source_path = source.get()
    destination_path = destination.get()
    
    # Call your core logic functions here
    all_files = getLocationOfImages(source_path)
    fileNamesInSeries(all_files, destination_path)

def getLocationOfImages(folderPath):
    files = []
    for root, dirs, filenames in os.walk(folderPath):
        for filename in filenames:
            filePath = os.path.join(root, filename)
            files.append(filePath)
    return files

def findFileLocation(fileName):
    for root, dir, files in os.walk("."):
        if fileName in files:
            return os.path.join(root, fileName)
    return None

def fileNamesInSeries(allFiles, renamePath):
    counter = 1
    for i in allFiles:
        try:
            newName = os.path.join(renamePath, f"File_{counter}.png")
            os.rename(i, newName)
            counter += 1
        except Exception as e:
            print(f"Error renaming file {i}: {e}")

root = Tk()
root.title("Clear The Clutter")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

source = StringVar()
destination = StringVar()
sourcePath_entry = ttk.Entry(mainframe, width=50, textvariable=source) # this is the entry box for the source path
destinationPath_entry = ttk.Entry(mainframe, width=50, textvariable=destination) # this is the entry box for the destination path
sourcePath_entry.grid(column=2, row=1, sticky=(W, E))
destinationPath_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Set", command=on_set).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="Run", command=run_core_logic).grid(column=3, row=4, sticky=W)

ttk.Label(mainframe, text="Source folder path").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Destination folder Path").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

sourcePath_entry.focus()
root.bind("<Return>", lambda event: on_set())

root.mainloop()