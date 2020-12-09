#<c>Sharkbyteprojects
from ctypes import *#cdll
import os
import time
mypath="dia"
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
path=".\\"+"setdesktopbg lib.dll"
dlllib=cdll.LoadLibrary(os.path.abspath(path))#load dll
while(1):
 for curr in onlyfiles:
   pcc=mypath+"\\"+curr
   print(os.path.abspath(pcc))
   dlllib.setdeskbg(os.path.abspath(pcc))
   time.sleep(10)
