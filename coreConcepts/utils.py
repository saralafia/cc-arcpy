from fields import *

def make_field(filepath):
    myField = check_extension(filepath)
    return myField

def check_extension(filepath):
    fileTypes = {
        ".tiff":GeoTiffField,
        ".tif":GeoTiffField,
        ".mp3":TestObject}

    if(filepath.endswith(".tiff") or filepath.endswith(".tif")):
        return fileTypes[".tiff"]
    elif(filepath.endswith(".mp3") or filepath.endswith(".MP3")):
        return fileTypes[".mp3"]
    else:
        print("unknown file extension")