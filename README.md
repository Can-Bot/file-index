# UGR-file-indexing-system
This is a file indexing system for UGR made by Can Gural Tanova

Required Libraries:
json
Pillow (PIL)


HOW TO MAKE IT WORK:


Have all of the files you want to index in the same folder as the prrogram

If using an existing file table, name it "fileTable" and keep it in the same folder as the program

Once run, the program will prompt you to ask which action you want to take

When providing file names, only provide the name or directory.

In order to add files by list, provide a .txt file of a list of the names or directories of the files meant to be indexed, with the names separated with commas called "fileList.txt"
 
HOW TO MAKE AUTORUN WORK:

The AutoRun programme is meant to be compiled and run in the MCU where the files will already be stored

In order for the program to work, a .txt file of a list of the names or directories of the files meant to be indexed, with the names separated with commas called "fileList.txt" must be made

The program will create two files, "fileTableAutoRun.json" and "dictFileAutoRun.txt" will be created, the .json file will contain all of the information recorded of each file, but will not contain a pointer to the file itself while the .txt file will also contain the pointer (in python)

The names of the files needed and created can be changed in the first few lines of the code 
