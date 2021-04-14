#Author: SpiderhamPorker(Carlos)
#Made while listening to Circulation. Link: https://www.youtube.com/watch?v=uKxyLmbOc0Q
from tkinter import Tk, Label, Entry, Button, messagebox
import time
import subprocess
limit=input("At what RAM usage do you want to be warned? (In GB): ")
true_limit=float(limit)
while True:
    FreeMemory=subprocess.check_output('wmic os get freephysicalmemory /format:value', shell=True, text=True)
    AllMemory=subprocess.check_output('wmic ComputerSystem get TotalPhysicalMemory', shell=True, text=True)
    FreeMemoryWithoutText=FreeMemory.replace('FreePhysicalMemory=', '')
    AllMemoryWithoutText=AllMemory.replace('TotalPhysicalMemory  ', '')
    FreeMemoryWithoutNewlines=FreeMemoryWithoutText.replace('\n', '')
    AllMemoryWithoutNewlines=AllMemoryWithoutText.replace('\n', '')
    hey=int(FreeMemoryWithoutNewlines)
    hey2=int(AllMemoryWithoutNewlines)
    IntTotal=(hey/1024)/1024
    IntAll=((hey2/1024)/1024)/1024
    if IntTotal>true_limit:
        messagebox.showinfo(title="Warning!", message="Quick! Close something!")
    DefinitiveAll=str(IntAll)
    DefinitiveTotal=str(IntTotal)
    print("Used memory: "+DefinitiveTotal+"\n"+'All memory: '+DefinitiveAll+'\n'+'---------------------------------------------------------------------')#Fun fact: I counted all of this lines. I hate my life. Kill me.
    time.sleep(2)