from os import path, system as c, rename as rn
import os

c('cls')

tag = input('Tag you want to remove from filenames: ')

c('cls')

print('Renaming files...')
for dir, subfolders, filenames in os.walk(path.curdir):
    for file in filenames:
        if '.py' not in file and '.vscode' not in file:
            # old_file_path = path.join(dir, file)
            filename = file.replace(tag, '')
            # new_file_path = path.join(dir, filename)
            try:
                rn(file, filename)
                print(f'>> File renamed: {file} → {filename}')
            except:
                print(f'>> Error renaming file: {file}')

c('pause')