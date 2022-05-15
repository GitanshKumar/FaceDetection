from PIL import Image
import random
import os

directory = os.fsencode(r"C:\Users\gitan\OneDrive\Desktop\⠀\Python\Face Recognition\Images")
filenames = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    filenames.append(filename)


for i in filenames:
    img = Image.open("Images/{}".format(i))
    bw_img = img.convert("L")
    resized_img = bw_img.resize((25,25))
    l = list(resized_img.getdata())


    data_s = ""
    for j in l:
        data_s += str(j) + ","
    data_s =  data_s[:len(data_s)-1]


    f = open("im_val.csv", "a")
    if "0_" in i:
        f.write("0,")
    else:
        f.write("1,")
    
    f.write("{}{}".format(data_s, "\n"))
    f.close()
