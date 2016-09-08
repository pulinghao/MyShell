# ! /usr/bin/python
#coding=utf-8
# This is a script for change png file to @2x file
# for example, aaa.png =>  aaa@2x.png

import os

currentFilePath = os.getcwd()

filelist = os.listdir(currentFilePath)

for files in filelist:
	Olddir = os.path.join(currentFilePath,files)
	if os.path.isdir(Olddir):
		continue
	filename = os.path.splitext(files)[0]
	filetype = os.path.splitext(files)[1]

	if filetype == ".png":
		Newdir = os.path.join(currentFilePath,filename+"@2x"+filetype)
		os.rename(Olddir,Newdir)
		print filename+filetype+ "finished change!"

print "all Clear!"

