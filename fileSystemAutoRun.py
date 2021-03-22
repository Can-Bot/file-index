import os
import json
from PIL import *


#These are the files that the program will create/use
fileListName = "fileList.txt"
jsonFile = "fileTableAutoRun.json"
dictFileName = "dictFileAutoRun.txt"

fileTable = {}

#class for each image
class ImageEntry:
	def __init__(name,Extention,Width,Height,bAlen,bArray):
		self.name = name
		self.Extention = Extention
		self.Width = Width
		self.Height = Height
		self.bAlen = bAlen
		self.bArray = bArray


# Takes the list of files in the module and idexes them
def fileTableAdd(fileTable):

    #   Creates a list of file Names that will be indexed
    fileList = open(fileListName, "r").readline().strip().split(",")

    for fileName in fileList:
        try:

                im = Image.open(fileName, "rb")

                # gets byteArray
                f = im.read()
                bArray = bytearray(f)

                # Image Width
                imWidth = im.size()[0]

                # Image Height
                imHeight = im.size()[1]

                # base name
                baseName = os.path.basename(file)
                # name
                fileNameBase = fileName.split(".")[0]
                # extention
                fileNameExt = fileName.split(".")[1]

                im.close()

                fileTable[baseName] = {"Name": str(fileNameBase),
                                    "Extention": str(fileNameExt),
                                    "Width": imWidth,
                                    "Height": imHeight,
                                    "bAlen": len(bArray),
                                    "ByteArray": str(bArray)}

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
