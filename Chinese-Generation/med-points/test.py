#coding:utf-8
from PIL import Image, ImageDraw, ImageFont
import random
import os
import codecs
import numpy as np
import cv2
from matplotlib import pyplot as plt
import scipy.misc

#This file is used to mimic the characters printed by wire printer
#This is only a demo
#There are two steps
#1. Add spaces 
#2. Gauss blur
#The output 1.png and 3.png is in the current directory

w = 64
h = 64
im = Image.new('RGB', (w, h), (255,255,255))
draw = ImageDraw.Draw(im)
font_size = 55
ttfont = ImageFont.truetype("/alter/fonts/微软vista仿宋.ttf", font_size)
string = '实'
draw.text((0, 0), string.decode('utf-8'), fill=(105,105,105), font=ttfont)
pixmap = im.load()

for i in range(w):
    for j in range(h):
        if (i % 5 == 0 or j % 10 == 0):
            # N = random.uniform(0, 1)
            N = 0
            current = pixmap[i, j]
            # a = int(current[0] * N)
            # b = int(current[1] * N)
            # c = int(current[2] * N)
            # d = int(current[3] * N)
            # pixmap[i,j] = (a,b,c,d)
            pixmap[i,j] = (255, 255, 255)
        print pixmap[i,j]

im.save('1.png')


img = cv2.imread('1.png')

kernel = np.ones((2, 2), np.float32) / 4
dst = cv2.filter2D(img, -1, kernel)

scipy.misc.imsave('3.png', dst)
