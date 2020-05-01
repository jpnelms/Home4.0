# This program Parses JSON Data and converts it to a csv
# JPNELMS - MAY 1ST, 2020

import json

s = open("Data.txt","rt") #source
d = open("Data.csv","wt") #destination
i = 1 #toggle for first time

#Heading Create Function
def create_heading(jbuff):
        heading = "" #Starts blank Heading
        for y in jbuff:
            heading = heading + y + ","
        heading = heading + ";"
        return heading

for x in s:
    buffer0 = s.readline()
    buffer1 = str(buffer0)
    jbuff = json.loads(buffer0)
    #print(jbuff)
    if (i ==1):
        heading = create_heading(jbuff)
        headers = heading.split(',')
        del headers[len(headers)-1] #Removes the ; from header array
        #print(headers)
        heading = heading.replace(',;','\n')
        #print(heading)
        d.write(heading)
        i = 0
    line = ''
    for j in headers:
        line =  line + str(jbuff[j]) + ','
    line = line + '\n'
    d.write(line)
s.close()
d.close()
