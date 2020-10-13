#!/usr/bin/python3
"""
Usage:
zip-tools <command> <extras>

Commands:
-c <filename || filenames> - compress a file
-cd <directory> - compress a directory
-d <zip filename> - decompress a zip file
-de <zip filename> <file> - decompress a especific file from a zip
-a <zip filename> - analize a zip file
"""

import zipfile,sys,os

if(len(sys.argv)<=2):
	print(__doc__.strip())
else:
	if(sys.argv[1]=="-c"):
		if(len(sys.argv)>3):
			out=zipfile.ZipFile("compress"+".zip",mode="w")
			for i in range(len(sys.argv)-2):
				out.write(sys.argv[i+2])
			out.close()
		else:
			out=zipfile.ZipFile(sys.argv[2]+".zip",mode="w")
			out.write(sys.argv[2])
			out.close()
	elif(sys.argv[1]=="-d"):
		with zipfile.ZipFile(sys.argv[2],"r") as zfile:
			os.mkdir("decompress")
			zfile.extractall("decompress")
	elif(sys.argv[1]=="-cd"):
		files=os.listdir(sys.argv[2])
		name="compress"
		out=zipfile.ZipFile(name+".zip",mode="w",compression=0)
		for i in range(len(files)):
			out.write(sys.argv[2]+files[i])
	elif(sys.argv[1]=="-a"):
		with zipfile.ZipFile(sys.argv[2],"r") as zfile:
			zfile.printdir()
	elif(sys.argv[1]=="-de"):
		with zipfile.ZipFile(sys.argv[2],"r") as zfile:
			zfile.extract(sys.argv[3])