
import os

upath = input("Введите полный путь до директории: ")
if not os.path.exists(upath):
    print("Такой директории не существует")
    exit()

for dir_path, dirs, files in os.walk(upath):
    dir_lst = list(map(lambda x: "dir: "+str(x), dirs))
    file_lst = list(map(lambda x: "file: "+str(x), files))
    print('\n'.join(dir_lst+file_lst))
    break
