#!/usr/bin/python
# coding: utf-8 -*-

import cv2,time
import os

#Remove LHS border using imagemagick
os.system('convert screenshot.png -fuzz 20% -trim s.png')
#Remove RHS border using imagemagick
os.system('convert s.png -crop -270 ss.png')

#Slicing ss.png into 3 

img = cv2.imread('ss.png')
img2 = img

height, width, channels = img.shape
# Number of pieces Horizontally 
CROP_W_SIZE  = 3
# Number of pieces Vertically to each Horizontal  
CROP_H_SIZE = 1 

for ih in range(CROP_H_SIZE ):
    for x,iw in enumerate(range(CROP_W_SIZE )):

        x = width/CROP_W_SIZE * iw 
        y = height/CROP_H_SIZE * ih
        h = (height / CROP_H_SIZE)
        w = (width / CROP_W_SIZE )
        print(x,y,h,w)
        img = img[y:y+h, x:x+w]
        NAME = str(time.time()) 		
        #cv2.imwrite("CROP\\" + str(time.time()) +  ".png",img)
        cv2.imwrite("CROP\\" + str(x) +  ".png",img)
        img = img2
		
#using Tesseract program to extract text in text file
tes_cmd = chr(34) + "C:\Program Files (x86)\Tesseract-OCR" + "\\tesseract.exe" + chr(34)
os.system(tes_cmd + ' CROP\\0.png 1')
os.system(tes_cmd + ' CROP\\468.png 2')
os.system(tes_cmd + ' CROP\\936.png 3')

os.remove('s.png')
os.remove('ss.png')