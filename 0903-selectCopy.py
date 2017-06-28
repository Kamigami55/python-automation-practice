import os, shutil

for foldername, subfolders, filenames in os.walk('.'):
    if foldername.endswith('0903-files'):
        continue
    for filename in filenames:
        if filename.endswith('.py'):
            shutil.copy(os.path.join(foldername, filename), os.path.join('./0903-files/', filename))
            

