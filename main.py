# ONLY TESTED ON WINDOWS
# For Personal Use

# This python script is used to organize the files (excluding folders) in the Downloads folder.

# Make sure the user running the program has "Read" permissions.

import os               # To access the file system
from shutil import move # To move the file to the respective folder


# The heirarchy of folders is as follows:
folders = {
    "Images": {
        "Photos":       ["png", "jpg", "jpeg", "bmp", "svg", "webp", "tiff", "tif"],
        "Gifs":         ["gif"],
        "Icons":        ["ico"]
    },
    "Documents": {
        "PDFs":         ["pdf"],
        "Word":         ["docx", "doc", "odt"],
        "Excel":        ["xlsx", "xls", "ods"],
        "Powerpoint":   ["pptx", "ppt", "ppsx", "odp"],
        "Texts & CSV":  ["txt", "csv", "rtf", "md"]
    },
    "Programming": {
        "Python":       ["py"],
        "Java":         ["java"],
        "C Family":     ["c", "cs", "cpp", "h"],
        "SQL":          ["sql"],
        "Web":          ["html", "css", "js", "ts", "php", "xml"],
        "Json":         ["json"],
        "Ruby":         ["rb"]
    },
    "Audio":            ["mp3", "wav", "flac", "aac", "wma", "m4a", "ogg", "oga", "opus", "weba", "webm", "midi", "mid"],
    "Compressed":       ["zip", "rar", "sitx", "7z", "gz", "bz2", "xz", "tgz", "tbz2", "z", "jar", "war", "ear", "iso", "dmg", "img"],
    "Videos":           ["mp4", "mkv", "webm", "flv", "avi", "mov", "wmv", "mpg", "mpeg", "3gp"],
    "Executable": {
        "Executable":   ["exe", "msi", "apk", "app", "gadget"],
        "Scripts":      ["bat", "com", "wsf", "sh", "cmd", "ps1", "vbs"]
    }
}

# function for creating specific folders depending on the file type
def create_folder(path, extension):

    others = True
    # 1
    for folder, subfolders in folders.items():
        # 2
        folder_path = os.path.join(path, folder)
        # 3
        if isinstance(subfolders, dict):

            # 3.1
            for subfolder, extensions in subfolders.items():
                # 3.2
                subfolder_path = os.path.join(folder_path, subfolder)
                # 4
                if extension in extensions:
                    # 5
                    if not os.path.exists(folder_path):
                        os.mkdir(folder_path)
                        
                        print(f"- Folder {folder} created.")
            
                    if not os.path.exists(subfolder_path):
                        os.mkdir(subfolder_path)
                        print(f"- Folder {subfolder} created.")
                    others = False
                    break
                
        else:
            # 4
            if extension in subfolders:
                # 5
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)
                    print(f"- Folder {folder} created.")
                others = False
                break
        
    # 6
    if others == True:
        others_path = os.path.join(path, "Others")
        if not os.path.exists(others_path):
            os.mkdir(others_path)
            print(f"- Folder Others created.")

    return 0


# function for moving the files on designated folders
def move_file(path, file, extension):
    
    others = True
    # 1
    for folder, subfolders in folders.items():
        # 2
        if isinstance(subfolders, dict):
            for subfolder, extensions in subfolders.items():
                source = os.path.join(path, file)
                destination = os.path.join(path, folder, subfolder, file)

                if extension in extensions:
                    # 3
                    move(source, destination)
                    others = False
                    print(f"----- Moved {file} to {subfolder}")
                    break
        else:
            if extension in subfolders:
                source = os.path.join(path, file)
                destination = os.path.join(path, folder, file)
                # 3
                move(source, destination)
                others = False
                print(f"----- Moved {file} to {folder}")
                break
        
    if others == True:
        source = os.path.join(path, file)
        destination = os.path.join(path, "Others", file)
        # 4
        move(source, destination)
        print(f"----- Moved {file} to Others")

    return 0



# to access the specific downloads folder, 
# right click the Downloads folder, go to properties, go to location and copy the path.
if __name__ == '__main__':

    # type here the path of the folder you want to organize (if you want to change directory)
    path = 'F:\\Users\\Lyrick'

    if (os.path.exists(path)):
        with os.scandir(path) as entries:
            for entry in entries:
                # only modify the files
                if entry.is_file():
                    # skip the desktop.ini file
                    if entry.name == "desktop.ini": continue

                    # get the file extension to identify which folder it belongs to 
                    file_extension = os.path.splitext(entry.name)[1]
                    file_extension = file_extension[1:]
                    
                    create_folder(path, file_extension)
                    move_file(path, entry.name, file_extension) 
                    
    else:
        print("The path does not exist.")
    print("End of the program.")



# Create Folder Function
'''
1.  Loop through the folder dictionary
2.  Create folder path (e.g Path/Images)
3.  Check if the extension needs a subfolder or not
3.1 If subfolder needed, loop through the extensions in the subfolder
3.2 Create subfolder path (e.g Path/Images/Gifs)
4.  Check if the extension is in the extensions list
5.  Create folder if it does not exist (and subfolder if needed)
6.  Create Others folder if the file does not belong to any folder
'''
# Move File Function
'''
1.  Loop through the folder dictionary
2.  Check if the extension is in the extensions list
3.  Move the file to the respective folder
4.  Move the file to Others if it's not in any folder
'''