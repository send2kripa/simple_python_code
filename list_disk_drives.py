import win32api

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\x00')[:-1]
print(f'List of Windows drives: {drives}')