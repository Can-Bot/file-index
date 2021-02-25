import os  
import json

fileListName = "fileList.txt"
jsonFile = "fileTable.json"
dictFileName = "dictFile.txt"

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
        fileNameBase = baseName.split(".")[0]
        #extention
        fileNameExt = baseName.split(".")[1]
        
        file.close()
    except:
        print("Something went wrong with file, ", fileName,  " check the file name given or the file itself")
        return
    
    fileTable[baseName] = {"Name":str(fileNameBase), 
                           "Extention":str(fileNameExt), 
                           "Size": stats, 
                           "Directory" : dirName,
                           "File": file}
    print("closed file")
    return

# Takes the list of files in the module and idexes them
def fileTableAddByList(fileTable): 
    #Creates a list of file Names that will be indexed
    fileList = open(fileListName, "r").readline().strip().split(",")
    
    for fileName in fileList:
        try:
            file = open(fileName, "r")
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
            file.close()
            
            fileTable[fileName] = {"Name":str(fileNameBase), 
                               "Extention":str(fileNameExt), 
                               "Size": stats, 
                               "Directory" : dirName,
                               "File": file}
            
        except:
            print("Something went wrong with file, ", fileName,  " check the file name given or the file itself")             
    return

#Grabs dict from .json file
def addByJson():
    with open(jsonFile, "r") as outfile:
        newDict = json.load(outfile)       
        for key in newDict.keys():
            fileTable[key] = newDict[key]
            fileTable[key]["File"] = open(key, "r")
    outfile.close()
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
    with open(dictFileName, "w") as newFile:
        newFile.write(str(fileTable))
        newFile.close() 
    return

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
    fileTable = open(dictFileName, "w")
    while cont == True:        
        userIn = input("Would you like to (C)lear the file table, (A)dd a new file, Add files by (L)ist, Add (B)y json file, (R)emove a file, (S)tore the table, (J)SONify the table or (Q)uit the program?  ")
        
        if userIn == "A" or userIn == "a": 
            fileTableAdd(fileTable)
        elif userIn == "C" or userIn == "c":
            clearTable(fileTable)
        elif userIn == "R" or userIn == "r":
            fileTableRem(fileTable)
        elif userIn == "S" or userIn == "s":
            storeTable(fileTable)
        elif userIn == "Q" or userIn == "q":
            cont = False
        elif userIn == "J" or userIn == "j":
            fileTableJSON(fileTable)
        elif userIn == "L" or userIn == "l":
            fileTableAddByList(fileTable)
        elif userIn == "B" or userIn == "b":
            addByJson()
        else:
            default()
    return

main()
