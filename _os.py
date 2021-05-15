import os
import shutil

path = "/home/hungnndev/Pictures/Screenshot from 2020-11-23 00-03-57.png"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exists")


source = "folder"
destination = "/home/hungnndev/Desktop/folder"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")


try:
    os.remove("./file/copy.txt")
except FileNotFoundError as e:
    print(e)


try:
    # os.remove(path)   # delete an empty directory
    shutil.rmtree('./rm') # to delete folder with has file
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print("File/folder was deleted")