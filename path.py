import os 

def Path(path_name):
    if os.path.exists(path_name):
        return path_name
    else:
        print("[INFO] Path not found")