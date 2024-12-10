from pathlib import Path
import os
import shutil


#Maybe a hashmap would be better for this
folder_names = {
    # Document files
    '.doc': "Documents",
    '.docx': "Documents",
    '.pdf': "Documents",
    '.txt': "Documents",
    '.odt': "Documents",
    '.rtf': "Documents",
    # Spreadsheet files
    '.xls': "Spreadsheets",
    '.xlsx': "Spreadsheets",
    '.csv': "Spreadsheets",
    '.ods': "Spreadsheets",
    # Presentation files
    '.ppt': "Presentations",
    '.pptx': "Presentations",
    '.odp': "Presentations",
    # Image files
    '.jpg': "Images",
    '.jpeg': "Images",
    '.png': "Images",
    '.gif': "Images",
    '.bmp': "Images",
    '.tiff': "Images",
    '.svg': "Images",
    # Audio files
    '.mp3': "Audio Files",
    '.wav': "Audio Files",
    '.aac': "Audio Files",
    '.flac': "Audio Files",
    '.ogg': "Audio Files",
    # Video files
    '.mp4': "Video Files",
    '.avi': "Video Files",
    '.mkv': "Video Files",
    '.mov': "Video Files",
    '.wmv': "Video Files",
    '.flv': "Video Files",
    '.webm': "Video Files",
    # Compressed files
    '.zip': "Compressed Files",
    '.rar': "Compressed Files",
    '.tar': "Compressed Files",
    '.gz': "Compressed Files",
    '.7z': "Compressed Files",
    # Code files
    '.py': "Code Files",
    '.java': "Code Files",
    '.cpp': "Code Files",
    '.c': "Code Files",
    '.js': "Code Files",
    '.html': "Code Files",
    '.css': "Code Files",
    '.php': "Code Files",
    '.rb': "Code Files",
    # Executable files
    '.exe': "Executables",
    '.bat': "Executables",
    '.sh': "Executables",
    # System files
    '.dll': "System",
    '.sys': "System",
    '.ini': "System",
    '.log': "System",
    # Database files
    '.db': "Database",
    '.sql': "Database",
    '.mdb': "Database",
    '.accdb': "Database"
    }

#TODO: Build a function that checks if there are files in a directory, Returns True if files are present

#TODO: Create a function that detects the types of files in the directory

def file_TypeCheck():
    p = Path('C:\\Users\\Saif\\OneDrive\\Desktop')
    
    #files = [x for x in p.iterdir() if x.suffix == f".{filetype}" ] #Here it prints out the specific file type you want to see
    files = [x for x in p.iterdir()]
    for file in files:
        print(file.suffix)

#TODO: Buid a function that moves files from one directory to another.

def move_files(user_dict_path):
    p = Path(user_dict_path)
    
    for file in p.iterdir():
        if file.is_file():
            file_ext = file.suffix
            foldertype = folder_names[file_ext]
            destinationpath = p / foldertype
            if (destinationpath.exists()):
                shutil.move(file, destinationpath)
            else:
                destinationpath.mkdir(parents=True, exist_ok= True)
                shutil.move(file, destinationpath)
            
        #We want to check if the folder exists in the directory, if so we will just moves the file there,
        #if not we would then create the folder, based on the foldertype assigned 
        
        
    
    

#TODO: Dont touch the folders in the current directory.

#TODO: Make the Program run in the background --- Automation

#TODO: Upload this to the repo

user_dict_path = input("Please enter the  path of the directory you want to organise: ")

#print(folder_names[0])
move_files(user_dict_path)
    
