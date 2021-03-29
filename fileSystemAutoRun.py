import os
import io
import json
from PIL import Image


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

        with Image.open(fileName) as im:

			# name
          fileNameBase = fileName.split(".")[0]
			# extention
          fileNameExt = fileName.split(".")[1]

			# gets byteArray
          buf = io.BytesIO()
          im.save(buf, format=fileNameExt)
          imByteArr = buf.getvalue()

			# Image Width
          imWidth = im.size[0]
			# Image Height
          imHeight = im.size[1]



          im.close()

          fileTable[fileName] = {"Name": str(fileNameBase),
															"Extention": str(fileNameExt),
															"Width": imWidth,
															"Height": imHeight,
															"bAlen": len(imByteArr),
															"ByteArray": str(imByteArr)
														}
      except:
        print("Something went wrong with file, ", fileName,  " check the file name given or the file itself")

    print(fileTable)
    return



#Creates a json file using the fileTable
def fileTableJSON(fileTable):
    jsonDict = {}
    with open(jsonFile, "w") as outfile:
        jsonDict = fileTable
#        for fileKey in jsonDict.keys():
#            fileTable[fileKey].pop("File")
        json.dump(jsonDict, outfile, indent=4)
    outfile.close()
    return

#Creates a txt file to store dicts in
def createDictFile(exDict):
    newFile = open(dictFileName, "w")
    newFile.write(str(exDict))
    newFile.close()
    return


fileTableAdd(fileTable)
fileTableJSON(fileTable)
createDictFile(fileTable)
