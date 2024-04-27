# -- coding: utf-8 --

import os
from PIL import Image, ImageDraw, ImageFont
import csv

os.makedirs("done")
allFiles = os.listdir()
Needed = []
for files in allFiles:
    if files.endswith(".jpg" or ".png"):
        Needed.append(files)
        
x = len(Needed)
for stuff in range(0, x): 
    naming = ""
    pics = Image.open(Needed[stuff])
    watermark = ImageDraw.Draw(pics)
    fonter = ImageFont.truetype("arial.ttf", 50)
    watermark.text((100,100),"water_mark", 100, font=fonter, size=50)
    naming = str(stuff)
    naming = naming + ".jpg"
    pics.save("D:\\project\\vsCourse\\UniLab9\\done\\" + naming)
    
name = []
amount = []
price = []
with open('book.csv', 'r') as f:
    read = csv.reader(f)
    for row in read:
        for index, value in enumerate(row):
            if index % 3 == 0:
                name.append(value)
            if index % 3 == 1:
                amount.append(value)
            if index % 3 == 2:
                price.append(value)

print("Нужно купить : ")
for i in range(0, len(name)):
    print(f'{name[i]} - {amount[i]} шт. за {price[i]}руб.')