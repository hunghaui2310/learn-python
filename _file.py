try:
    with open('./file/test.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
except Exception:
    print("Some went wrong!")


# write to  file

text = "Yooooooooooooooooo\nI hacked this file"
try:
    with open('./file/test.txt', 'a') as file: # w to override, a to append
        file.write(text)
except Exception as e:
    print(e)

# copying file

import shutil

shutil.copyfile("./file/test.txt", "./file/copy.txt")