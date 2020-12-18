import os, win32api

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\x00')[:-1]
for drive in drives:
    print(f'\nList of directories in the dirve: {drive}')
    os.chdir(drive)
    for dir in os.listdir(drive):
        if os.path.isdir(dir):
            print(dir)



