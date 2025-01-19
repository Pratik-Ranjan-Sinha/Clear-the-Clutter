'''clearTheClutter'''

from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os

def select_source_folder():
    folder = filedialog.askdirectory(title="Select Source Folder")
    if folder:
        source.set(folder)

def select_destination_folder():
    folder = filedialog.askdirectory(title="Select Destination Folder")
    if folder:
        destination.set(folder)

def on_set():
    if not os.path.isdir(source.get()) or not os.path.isdir(destination.get()):
        messagebox.showerror("Error", "Invalid source or destination path!")
    else:
        print("Source Path:", source.get())
        print("Destination Path:", destination.get())
        print("File Prefix:", prefix.get())
        messagebox.showinfo("Success", "Paths and prefix set successfully!")

def run_core_logic():
    source_path = source.get()
    destination_path = destination.get()
    file_prefix = prefix.get()
    
    if not os.path.isdir(source_path) or not os.path.isdir(destination_path):
        messagebox.showerror("Error", "Please provide valid paths.")
        return

    if not file_prefix:
        messagebox.showerror("Error", "Please provide a file prefix.")
        return
    
    all_files = getLocationOfImages(source_path)
    
    if not all_files:
        messagebox.showwarning("Warning", "No files found in the source folder!")
        return
    
    fileNamesInSeries(all_files, destination_path, file_prefix)
    messagebox.showinfo("Success", "Files have been renamed and moved successfully!")

def getLocationOfImages(folderPath):
    files = []
    for root, _, filenames in os.walk(folderPath):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def fileNamesInSeries(allFiles, renamePath, file_prefix):
    counter = 1
    for i in allFiles:
        try:
            ext = os.path.splitext(i)[1]
            new_name = os.path.join(renamePath, f"{file_prefix}_{counter}{ext}")
            
            while os.path.exists(new_name):  # Ensure no overwriting
                counter += 1
                new_name = os.path.join(renamePath, f"{file_prefix}_{counter}{ext}")
            
            os.rename(i, new_name)
            counter += 1
        except Exception as e:
            print(f"Error renaming file {i}: {e}")

root = Tk()
root.title("File Organizer")

mainframe = ttk.Frame(root, padding="10 10 15 15")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

source = StringVar()
destination = StringVar()
prefix = StringVar()

# Entry fields
sourcePath_entry = ttk.Entry(mainframe, width=50, textvariable=source)
destinationPath_entry = ttk.Entry(mainframe, width=50, textvariable=destination)
prefix_entry = ttk.Entry(mainframe, width=20, textvariable=prefix)

# Layout for entry fields
sourcePath_entry.grid(column=2, row=1, sticky=(W, E))
destinationPath_entry.grid(column=2, row=2, sticky=(W, E))
prefix_entry.grid(column=2, row=3, sticky=(W, E))

# Folder selection buttons
ttk.Button(mainframe, text="Select Source", command=select_source_folder).grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="Select Destination", command=select_destination_folder).grid(column=3, row=2, sticky=W)

# Control buttons
ttk.Button(mainframe, text="Set", command=on_set).grid(column=3, row=4, sticky=W)
ttk.Button(mainframe, text="Run", command=run_core_logic).grid(column=3, row=5, sticky=W)

# Labels
ttk.Label(mainframe, text="Source folder path").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Destination folder path").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="File rename prefix").grid(column=1, row=3, sticky=W)

# Padding for widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

sourcePath_entry.focus()
root.mainloop()
