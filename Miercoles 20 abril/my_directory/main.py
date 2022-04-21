import os
# entries = os.listdir("my_directory")

with os.scandir("my_directory") as entries:
    for entry in entries:
        # print(entry.name)
        pass

from pathlib import Path
entries = Path("my_directory")
for entry in entries.iterdir():
    print(entry.name)

# os.listdir() Retorna una lista de todos los archivos en el directorio
# os.scandir() Retorna un iterador  de todos los objetos en un directorio
# incluyendo informacion del archivo
# pathlib.Path.iterdir() Retorna un iterador de todos los objetos
# en un dricetorio incluynedo informacion del arhcivo