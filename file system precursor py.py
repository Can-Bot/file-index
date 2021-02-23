import os  

def fileTableAdd(fileTable):
    try:
        fileName = input("Input the name of the file you would like to add")
        file = open(fileName, "r")
        print("opened file")
        # get file stats
        stats = os.stat(fileName)
    except:
        print("Something went wrong with the file, check the file name given or the file itself")
        return
    
    fileTable[fileName] = {"Size": stats, "File": file}
    file.close()
    print("closed file")
    return
    
def fileTableRem(fileTable):
    try:
        fileName = input("Input the name of the file you would like to remove")
        file = open(fileName, "r")
        print("opened file")
    
    except:
        print("Something went wrong, check the file name given or the file itself")
        return
    
    if fileName in fileTable:
        del fileTable[fileName]
    else:
        print("That file doesnt exist in the file table")
        
    file.close()
    print("closed file")
    return
        
        
def clearTable(fileTable):
    fileTable = {}
    return

def storeTable(fileTable):
    newFile = open("fileTable", "w")

def quitProg(fileTable):
    fileTable.close()
    cont = False
    return

def default():
    print("Invalid input")
    return

def main():
    cont = True
    fileTable = open("fileTable", "w")
    while cont == True:        
        userIn = input("Would you like to (C)lear the file table, (A)dd a new file, (R)emove a file, (S)tore the table or (Q)uit the program")

        #Failed case switch :(
        
#        options = {
 #       "C":clearTable(fileTable),
  #      "A":fileTableAdd(fileTable),
   #     "R":fileTableRem(fileTable),
    #    "S":storeTable(fileTable),
     #   "Q":quitProg(fileTable),

#        "c":clearTable(fileTable),
 #       "a":fileTableAdd(fileTable),
  #      "r":fileTableRem(fileTable),
   #     "s":storeTable(fileTable),
    #    "q":quitProg(fileTable)
     #   }
        
        if userIn == "A" or userIn == "a": 
            fileTableAdd(fileTable)
        elif userIn == "C" or userIn == "c":
            clearTable(fileTable)
        elif userIn == "R" or userIn == "r":
            fileTableRem(fileTable)
        elif userIn == "S" or userIn == "s":
            storeTable(fileTable)
        elif userIn == "Q" or userIn == "q":
            fileTable.close()
            cont = False
        else:
            default()
    return

main()
