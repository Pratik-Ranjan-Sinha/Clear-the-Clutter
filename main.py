import os
import shutil

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
            newName = f"File_{counter}.png"
            os.rename(i, newName)
            newFileLocation = findFileLocation(newName)
            sourceFile = f"{newFileLocation}"
            destinationFolder = f"{renamePath}"
            destinationFile = os.path.join(destinationFolder, os.path.basename(sourceFile))
            shutil.move(sourceFile, destinationFile)
            counter = counter + 1
        except OSError as e:
            print(f"Error Renaming File: {e}")
        
folderPath = "C:/Users/prati/OneDrive/Desktop/Data/Pratik Git Uploads/Clear the Clutter/Pictures"              # Give the file location
renamePath = "C:/Users/prati/OneDrive/Desktop/Data/Pratik Git Uploads/Clear the Clutter/renamedFiles"          # Give the Location where you want to put your file after renaming
allFiles = getLocationOfImages(folderPath)
fileNamesInSeries(allFiles, renamePath)