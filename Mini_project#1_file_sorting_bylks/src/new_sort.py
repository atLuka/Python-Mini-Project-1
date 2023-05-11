

import os
import subprocess 
from PyQt5 import *



def new_sort(src_path, tgt_path):
    files = os.listdir(src_path)

    w_ext = []
    wtt_ext = []
    
    for i in files:

        if os.path.isfile(os.path.join(src_path, i)): # condition vérifiant que le fichier n'est pas un dossier 
                if "." in i:
                    w_ext.append(i)
                else:
                    wtt_ext.append(i)

    if w_ext: # parcours des fichiers avec une extension
        for i in w_ext:
            ext = i.rsplit(".", 1)[1] # prend l'extension de chaque fichier

            if ext not in os.listdir(tgt_path):
                subprocess.run(["mkdir", f"{tgt_path}/{ext}"])
                subprocess.run(["mv", f"{src_path}/{i}", f"{tgt_path}/{ext}"])
            else:
                subprocess.run(["mv", f"{src_path}/{i}", f"{tgt_path}/{ext}"])

    if wtt_ext: # parcours des fichiers sans extension 
        for i in wtt_ext:
            if "autres" not in os.listdir(tgt_path):
                subprocess.run(["mkdir", f"{tgt_path}/autres"])
                subprocess.run(["mv", f"{src_path}/{i}", f"{tgt_path}/autres"])
            else:
                subprocess.run(["mv", f"{src_path}/{i}", f"{tgt_path}/autres"])





    



