import json, io, os
from PIL import Image

print("opening files")
#These are the files that the program will create/use
fileListName = "fileList.txt" #list of files to be indexed
jsonFile = "fileTableAutoRun.json" #json version of the file table
dictFileName = "dictFileAutoRun.txt" #txt file of the dictionary

#if the json file is present, it is loaded as the file table.
try:
	fileTable = json.load(open(jsonFile))
	print("File table found")
except:
	# A new dictionary is used as the file table otherwise.
	fileTable = {}
	print("File table created")


#class for each image UNUSED
#class ImageEntry:
#	def __init__(name,Extention,Width,Height,bAlen,bArray):
#		self.name = name
#		self.Extention = Extention
#		self.Width = Width
#		self.Height = Height
#		self.bAlen = bAlen
#		self.bArray = bArray


# Takes the list of files in the module and idexes them
def fileTableAdd(fileTable):
    #Creates a list of file Names that will be indexed
		fileList = open(fileListName, "r").readline().strip().split(",")
		print(fileList)
		for fileName in fileList:
			print("getting file", fileName)
			try:

				with Image.open(fileName) as im:

			# name
					fileNameBase = fileName.split(".")[0]
			# extention
					fileNameExt = fileName.split(".")[1]
					if fileNameExt == "png":
						print("This software cannot process png files")
						pass
						
			# old method of getting the bytearray
			# gets byteArray
          #buf = io.BytesIO()
          #imRGB = im.convert("RGB")          
          #imRGB.save(buf, format=fileNameExt)
          #imByteFor = buf.getvalue()

			# new method of getting bytearray
					pixel_list = list(im.getdata())
					imByteArr = ""
					imIntArr = []
          
					print(pixel_list)
					# loop that separates the pixel list into rgb values and converts to rgb565 format
					print("separating and converting pixels")
					
					for pix in pixel_list:
						#turns empty/transparent pixels black
						if pix == None:
							r,g,b = 0
						else:
							#separates to rgb values and converts into hex
							r = (pix[0] >> 3) & 0x1F
							g = (pix[1] >> 2) & 0x3F
							b = (pix[2] >> 3) & 0x1F

						#print(r,g,b)
						
						# turns each value into a string and adjusts to 565 format
						rStr = (str(bin(r)).strip('0b'))
						if len(rStr) < 5 :
							rMiss = 5 - len(rStr)
							rStr = ("0" * rMiss) + rStr    

						gStr = (str(bin(g)).strip('0b'))
						if len(gStr) < 6 :
							gMiss = 6 - len(gStr)
							gStr = ("0" * gMiss) + gStr      

						bStr = (str(bin(b)).strip('0b'))
						if len(bStr) < 5 :
							bMiss = 5 - len(bStr)
							bStr = ("0" * bMiss) + bStr   

						#adds the pixel values to the byte array
						imByteArr = imByteArr + (rStr + gStr + bStr)
						imIntArr.append((r,g,b))

						# Image Width
						imWidth = im.size[0]
						# Image Height
						imHeight = im.size[1]

						im.close()

					print("added file to table")
				# Adds / adjusts the elements in the file table
					fileTable[fileName] = {"Name": str(fileNameBase),
														"Extention": str(fileNameExt),
														"Width": imWidth,
														"Height": imHeight,
														"bAlen": len(imByteArr),
														"hexByteArray": pixel_list,
														"ByteArray": imByteArr
														}

			except:
				print("Something went wrong with file, ", fileName,  " check the file name given or the file itself")

    #print(fileTable)
		return



#Creates a json file using the fileTable
def fileTableJSON(fileTable):
    jsonDict = {}
    with open(jsonFile, "w") as outfile:
        jsonDict = fileTable
        json.dump(jsonDict, outfile, indent=4)
    outfile.close()
    return

#Creates a txt file to store dicts in
def createDictFile(exDict):
		print("opening dict file")
		newFile = open(dictFileName, "w")
		newFile.write(str(exDict))
		newFile.close()
		return

#calls each function
fileTableAdd(fileTable)
fileTableJSON(fileTable)
createDictFile(fileTable)
