import os

path = "/home/ishtiaq/Documents/Python_Files/test.txt"

# file detection

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("The location doesn't exist")

# file read

try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("That file was not found")
finally:
    if file.closed:
        print("The file is closed")
    else:
        file.close()

# file write and append

python = "Python is fun!"
python_append = "\nI love python"

# write

try: 
    with open('python.txt', 'w') as file:
        file.write(python)
    with open('python.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("That file was not found")
finally:
    if file.closed:
        print("The file is closed")
    else:
        file.close()

# append

try: 
    with open('python.txt', 'a') as file:
        file.write(python_append)
    with open('python.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("That file was not found")
finally:
    if file.closed:
        print("The file is closed")
    else:
        file.close()


# copyfile() = copies content of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('test.txt', '/home/ishtiaq/Documents/copy.txt') # src, destination
shutil.copy('test.txt', '/home/ishtiaq/Documents/copy.txt') # src, destination
shutil.copy2('test.txt', 'copy.txt') # src, destination


# move file & folder


# file

source_file = "copy.txt"
destination_file = "/home/ishtiaq/Documents/"


try: 
    if os.path.exists(destination_file):
        print("There is already a file there")
    else:
        os.replace(source_file, destination_file)
        print(source_file + " is moved")
except FileNotFoundError:
    print(source_file + " was not found")


# folder

source_folder = "folder"
destination_folder = "/home/ishtiaq/Documents/folder"

try: 
    if os.path.exists(destination_folder):
        print("There is already a folder there")
    else:
        os.replace(source_folder, destination_folder)
        print(source_folder + " is moved")
except FileNotFoundError:
    print(source_folder + " was not found")


# Delete file & folder

# file

path_delete = 'copy.txt'

try: 
    os.remove(path_delete)
    print(path_delete + " is deleted")
except FileNotFoundError:
    print("That file was not found")
else:
    print(path_delete + " is deleted")

# folder

path_folder_delete = 'python_folder'

try: 
    os.rmdir(path_folder_delete) # empty folder
    # shutil.rmtree(path_folder_delete) # non-empty file
    print(path_folder_delete + " is deleted")
except FileNotFoundError:
    print("Yjay file was not found")
except PermissionError:
    print("YOu do not have permission to delete that")
except OSError:
    print("You cann't delete that using that function")
else:
    print(path_folder_delete + " is deleted")