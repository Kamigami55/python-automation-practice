import os

def findLargeFiles(path):
    path = os.path.abspath(path)
    for foldername, subfolder, filenames in os.walk(path):
        for filename in filenames:
            if os.path.getsize(os.path.join(foldername, filename)) > 100000000: # larger than 100MB
                print('%s ... %s' % (str(os.path.getsize(os.path.join(foldername, filename))).rjust(15), os.path.join(foldername, filename)))

findLargeFiles('.')
