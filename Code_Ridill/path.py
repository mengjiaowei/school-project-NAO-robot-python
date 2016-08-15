import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():

    # duplicera
    if path.exists("ny.txt"):
        # få fram path 
        src = path.realpath("ny.txt");

        # separera filnamn från dir
        head, tail = path.split(src)
        print ("path: " + head)
        print ("file: " + tail)
            
        # skapa kopia
#        dst = src + ".bak"
        # use shell to make copy
#        shutil.copy(src, dst)

        # kopiera permissions, modifications etc.
#        shutil.copystat(src, dst)

        # byt namn på original
#        os.rename("ny.txt", "nyare.txt")

        # skapa zip fil
#        root_dir, tail = path.split(src)
#        shutil.make_archive("archive", "zip", root_dir)

        # snyggare zip sätt
#        with ZipFile ("testzip.zip", "w") as newzip:
#            newzip.write("ny.txt")
#            newzip.write("ny.txt.bak")



if __name__ == "__main__":
    main()
