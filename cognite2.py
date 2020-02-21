# The Code takes input a file 'data.csv' and then add a column on the data and 
# output file in another file 'output.csv'

import csv 

name = []
description = []

with open('data.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=';')
    for row in csvReader:
        name.append(row[0])
        description.append(row[1])


name = name[1:]
description = description[1:]

l = len(name)
parent = [0]*l

for i in range(0,l):
    if name[i].find('.') != -1:
        temp = name[i].split('.')
        temp = temp[:-1]
        temp2 = '.'.join(temp)
        parent[i] = temp2
    elif name[i].find('.') == -1:
        if len(name[i]) == 1:
            parent[i] = ''
        else:
            parent[i] = name[i][:-1]   

result = []
outp = [' ']*l
for i in range(0,l):
    outp[i] = str(name[i]) + ';'+ str(parent[i]) + ';' + str(description[i])
    result.append(outp[i])

with open('output.csv','w') as csvfile:
    fieldnames = ['name;parent;description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for line in result:
        writer.writerow({'name;parent;description': line})


