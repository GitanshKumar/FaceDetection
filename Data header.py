head_s = ""

for j in range(625):
    head_s += "pix" + str(j) + ","

head_s =  head_s[:len(head_s)-1]

f = open("im_val.csv", "a")

f.write("{}{}".format(head_s, "\n"))

f.close()