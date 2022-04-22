import os

# entries = os.listdir("my_directory")

with os.scandir("my_directory") as entries:
    for entry in entries:
        # print(entry.name)
        pass

from pathlib import Path

entries = Path("my_directory")
# for entry in entries.iterdir():
#     print(entry.name)

# os.listdir() Retorna una lista de todos los archivos en el directorio
# os.scandir() Retorna un iterador  de todos los objetos en un directorio
# incluyendo informacion del archivo
# pathlib.Path.iterdir() Retorna un iterador de todos los objetos
# en un dricetorio incluynedo informacion del arhcivo

base_path = "my_directory"
# for entry in os.listdir(base_path):
#     if os.path.isfile(os.path.join(base_path,entry)):
#         print(entry)


base_path = "my_directory"
with os.scandir(base_path) as entries:
    for entry in entries:
        if entry.is_file():
            # print(entry.name)
            pass

base_path = "my_directory"
for entry in os.listdir(base_path):
    if os.path.isdir(os.path.join(base_path, entry)):
        new_path = os.path.join(base_path, entry)
        for entry in os.listdir(new_path):
            # print(entry)
            pass
        pass

with os.scandir(base_path) as entries:
    for entry in entries:
        if entry.is_dir():
            # print(entry.name)
            pass

basepath = Path("my_directory")
for entry in basepath.iterdir():
    if entry.is_dir():
        # print(entry.name)
        pass

with os.scandir("my_directory") as dir_contents:
    for entry in dir_contents:
        info = entry.stat()
        # print(info.st_mtime)

current_dir = Path("my_directory")
for path in current_dir.iterdir():
    info = path.stat()
    # print(info.st_mtime)

from datetime import datetime


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def get_files(route_path):
    dir_entries = os.scandir(route_path)
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            print(f"{entry.name}\t Last modified: {convert_date(info.st_mtime)}  ")

get_files("my_directory")