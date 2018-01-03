import os
import sys
import shutil
import uuid

def integrate(folders, root='', target='', name=''):
    print folders

    if not root:
        root = os.path.dirname(folders[0])

    if not target:
        target = os.path.join(root, 'untitled')
        try:
            os.mkdir(target)
        except:
            target = os.path.join(root, 'untitled' + str(uuid.uuid4()))
            os.mkdir(target)
            

    for folder in folders:
        files = os.listdir(folder)
        for f in files:
            f = os.path.join(folder, f)
            shutil.copy(f, target)


if __name__ == '__main__':
    folders = sys.argv
    folders.pop(0)
    integrate(sys.argv)
    