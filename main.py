import os
import shutil

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
        
folderPath = "C:/Users/prati/OneDrive/Desktop/Python/Day 68 - Exercise 7 - Clear the Clutter/Pictures"              # Give the file location
renamePath = "C:/Users/prati/OneDrive/Desktop/Python/Day 68 - Exercise 7 - Clear the Clutter/renamedFiles"          # Give the Location where you want to put your file after renaming
allFiles = getLocationOfImages(folderPath)
fileNamesInSeries(allFiles, renamePath)