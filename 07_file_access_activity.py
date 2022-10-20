
from asyncore import write


devices=[]
file=open("devices.txt","a")
while True:
    newItem= input("ingrese un nuevo item: ")
    if newItem == "exit":
        print("All done!")
        newItem=newItem.strip()
        break
    else:
        file.write(newItem +"\n")
    
file.close()
