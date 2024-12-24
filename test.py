'''IGNORE... this is just a testing Program '''

import os


# filename = os.path.basename(file_path)
# print(filename)

def get_files_in_folder(folder_path):
    files = []
    for root, dirs, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            files.append(file_path)
    return files

# def get_files_in_folder(folder_path):
#     filenames = []
#     for root, dirs, files in os.walk(folder_path):
#         filenames.extend(files)
#     return filenames

folder_path = "C:/Users/prati/OneDrive/Desktop/Python/Day 68 - Exercise 7 - Clear the Clutter/Pictures"
all_files = get_files_in_folder(folder_path)
counter = 1
for i in all_files:
    try:
        new_name = f"{counter}.png"
        os.rename(i, new_name)
        counter = counter + 1
    except OSError as e:
        print(f"Error Renaming File: {e}")





# counter = 1
# try:
#     for i in all_files:
#         new_name = f"{counter}.png"
#         os.rename(all_files, new_name)
#         print(f"File '{all_files}' renamed to '{new_name}' Successfully")
#         counter += 1
# except OSError as e:
#     print(f"Error renaming file : {e}")




# counter = 1
# old_name = "abhishek.png"
# new_name = f"{counter}.png"

# try: 
#     os.rename(old_name,new_name)
#     print(f"File '{old_name}' renamed to '{new_name}' SuccessFully")
# except OSError as e:
#     print(f"Error renameing file : {e}")