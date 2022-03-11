import re

with open("essay.txt", "r") as f:
    essay = f.read()
    splitter = re.split("\?|!|\.|\n", essay)
    #print(splitter)
    for i in range (len(splitter)):
        k = splitter[i]
        k = k.split()
        #print(k)
        for j in reversed (k):
                print(j, end = " ")
