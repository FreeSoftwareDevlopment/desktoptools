#<c>Sharkbyteprojects
from ctypes import *#cdll
import os
path=".\\"+"setdesktopbg lib.dll"
dlllib=cdll.LoadLibrary(os.path.abspath(path))#load dll
dlllib.printcopy()
cllinp=input("Filepath for BG: ")
returnvalue=dlllib.setdeskbg(cllinp)
if(returnvalue==1):
    print("Complete Changed")
else:
    print("Error!!")
