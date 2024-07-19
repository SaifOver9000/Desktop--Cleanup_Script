import os

#TODO: Build a Script that checks if there are files in the Directory
def file_exist(path):
    files = os.listdir(path)
    #filters out only the files.
    files = [f for f in files if os.path.isfile(path+'/'+f)]
    if len(files) != 0:
        return True
    else:
        return False
#TODO: Build a Script that Moves files from One directory to another,
# I need to build a list of the potential file types and create a folder based on them if they exist in the directory.
#divide the file into "." and organize them into it
common_file_extensions = [
    # Document files
    '.doc', '.docx', '.pdf', '.txt', '.odt', '.rtf',
    # Spreadsheet files
    '.xls', '.xlsx', '.csv', '.ods',
    # Presentation files
    '.ppt', '.pptx', '.odp',
    # Image files
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg',
    # Audio files
    '.mp3', '.wav', '.aac', '.flac', '.ogg',
    # Video files
    '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm',
    # Compressed files
    '.zip', '.rar', '.tar', '.gz', '.7z',
    # Code files
    '.py', '.java', '.cpp', '.c', '.js', '.html', '.css', '.php', '.rb',
    # Executable files
    '.exe', '.bat', '.sh',
    # System files
    '.dll', '.sys', '.ini', '.log',
    # Database files
    '.db', '.sql', '.mdb', '.accdb'
]
#TODO: Create a folder for each file type
#TODO: Move File into Associated folder, DONT touch folders.

#TODO: Find a way to run the code ccontinously in the background


