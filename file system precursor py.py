import os  
import json

def fileTableAdd(fileTable):
    try:
        fileName = input("Input the name of the file you would like to add")
        file = open(fileName, "r")
        print("opened file")
        # get file stats
        # size
        stats = os.stat(file)
        # directory
        dirName = os.path.dirname(file)
        # base name
        baseName = os.path.basename(file)
        #name
        fileNameBase = baseName[0]
        #extention
        fileNameExt = baseName[1]
        
    except:
        print("Something went wrong with the file, check the file name given or the file itself")
        return
    
    fileTable[fileName] = {"Name":str(fileNameBase), 
                           "Extention":str(fileNameExt), 
                           "Size": stats, 
                           "Directory" : dirName,
                           "File": file}
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

#Creates a json file using the fileTable
def fileTableJSON(fileTable):
    jsonDict = {}
    with open(jsonFile, "w") as outfile: 
        jsonDict = fileTable
        for fileKey in jsonDict.keys():
            fileTable[fileKey].pop("File")         
        json.dump(jsonDict, outfile, indent=4)         
    file.close()
    return

def default():
    print("Invalid input")
    return

def main():
    cont = True
    fileTable = open("fileTable", "w")
    while cont == True:        
        userIn = input("Would you like to (C)lear the file table, (A)dd a new file, (R)emove a file, (S)tore the table, (J)SONify the table or (Q)uit the program?  ")
        
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
        elif userIn == "J" or userIn == "j":
            fileTableJSON(fileTable)
        else:
            default()
    return

main()
