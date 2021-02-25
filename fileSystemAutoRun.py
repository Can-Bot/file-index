import os
import json

#These are the files that the program will create/use
fileListName = "fileList.txt"
jsonFile = "fileTableAutoRun.json"
dictFileName = "dictFileAutoRun.txt"

fileTable = {}

# Takes the list of files in the module and idexes them
def fileTableAdd(fileTable): 
    
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
            fileNameBase = baseName.split(".")[0]
            #extention
            fileNameExt = baseName.split(".")[1]
            file.close()
            
            fileTable[baseName] = {"Name":str(fileNameBase), 
                               "Extention":str(fileNameExt), 
                               "Size": stats, 
                               "Directory" : dirName,
                               "File": file}
            
        except:
            print("Something went wrong with file, ", fileName,  " check the file name given or the file itself")        
        
        
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

#Creates a txt file to store dicts in
def createDictFile(exDict):
    newFile = open(dictFileName, "w")
    newFile.write(str(exDict))
    file.close()
    return


fileTableAdd(fileTable)
fileTableJSON(fileTable)
createDictFile(fileTable)
