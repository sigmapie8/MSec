import platform
import os
import shutil
import time

def makeDir():
	scriptPath = os.getcwd()
	try:
		os.mkdir(scriptPath+"/.Copied Files")
	except:
		return

def findFile(fileType, path):
	pd_path = "/usr/"
	for dirpath, directories, dirfiles in os.walk(path):
		for files in dirfiles:
			if(files.split('.')[-1] == fileType):
				yield (dirpath,files)


def copyFile_Linux(fileType, path = os.path.expanduser('/')):
	dest = os.getcwd()+"/.Copied Files/"
	for dirpath, files in findFile(fileType, path):
		filePath = dirpath+"/"+files
		try:
			shutil.copy2(filePath, dest+files)
		except shutil.SameFileError:
			pass
		print("copied ", files)

		
fileType = input("Enter file type : ")
path = input("Enter path (leave blank if root) : ")


operatingSys = platform.system()
if(operatingSys == "Linux"):
	makeDir()
	copyFile_Linux(fileType, path)


