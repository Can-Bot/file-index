# UGR-file-indexing-system
This is a file indexing system for UGR made by Djan Gural Tanova

### Required Libraries:
json,
Pillow (PIL)

### Inputs:

The AutoRun programme is meant to be compiled and run in the MCU where the files will already be stored.

In order for the program to work, a .txt file of a list of the names or directories of the files meant to be indexed, with the names separated with commas called "fileList.txt" must be made

### Outputs:

The program will create two files, "fileTableAutoRun.json" and "dictFileAutoRun.txt"; the .json file will contain all of the information recorded from each file.

**The dictionary created will contain the following data**: 

- "fileName.extention" : the key to the dictionary will be the filename and the extention of the file being indexed

- {"quality" : data} : the value corresponding to the key will be another dictionary containing the different qualities that will be indexed 

**The dictionary related to each file will be structured in the following way:**

- "Name": The name of the file
- "Extention": The extention of the file 
- "Width": The pixel width of the image
- "Height": The pixel height of the image
- "bAlen": Length of the byte array, i.e. the size of the file
- "ByteArray": The converted byte array as a long string of binary digits in rgb 565 format

The names of the files needed and created can be changed in the first few lines of the code 

### Processing:

Using the PIL module, the pixel list is taken from the image file. The pixel list is separated into the rgb values per pixel and these values are converted from hex to binary. The binary rgb values are stitched together in accordance to rgb565 format and added to the byte array list that will be included in the final dictionary.

The other desired qualities are extracted from the file using the PIL module and all of the desired values are added into the dictionary.

The `createDictFile(exDict)` and `fileTableJSON(fileTable)` functions check whether files with file-names stated on the first few lines of the program exist and create or append the newly indexed files onto those files accordingly.