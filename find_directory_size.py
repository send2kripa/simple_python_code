import os, win32api

total_size = 0
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\x00')[:-1]
for drive in drives:
    os.chdir(drive)
    for dir in os.listdir(drive):
        for path, dirs, files in os.walk('.'):
            for f in files:
                fp = os.path.join(path, f)
                total_size += os.path.getsize(fp)
        print(f'Directory {dir} size MB:{str(round(total_size/(1024*1024), 3))}')


