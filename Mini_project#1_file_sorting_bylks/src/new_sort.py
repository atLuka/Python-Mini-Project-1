

from os import *
from PyQt5 import *







#path="/home/lks/Documents/GIT/fic_cible"


def new_sort(src_path,tgt_path):


    files=listdir(src_path)
    
    
    w_ext=[]
    wtt_ext=[]

    for i in files: 
        if "." in i :
            w_ext.append(i)

        else:
            wtt_ext.append(i)
    
    
    if w_ext != []:

        for i in w_ext:
            ext=i.rsplit(".",1)[1]
            
            if ext not in listdir(tgt_path):

                system(f"mkdir {tgt_path}/{ext};mv {src_path}/{i} {tgt_path}/{ext}")
        
            else:
                system(f"mv {src_path}/{i} {tgt_path}/{ext}")

    if wtt_ext != [] : 

        for i in wtt_ext:

            if "autres" not in listdir(tgt_path):
                system(f"mkdir {tgt_path}/autres ; mv {src_path}/{i} {tgt_path}/autres")
            else:
                system(f"mv {src_path}/{i} {tgt_path}/autres")
            



        



    



