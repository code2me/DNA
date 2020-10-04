import csv
from sys import argv

with open(argv[1]) as database:
    reader = list(csv.reader(database))
    dna_seq = reader[0]
    dna_seq.pop(0)

with open(argv[2],) as seq:
    seq = seq.read()

count = []

for i in dna_seq:
    counter = 0
    pattern = i
    while pattern in seq:
        counter += 1
        pattern += i
    count.append(counter)

new_count = []

for i in count:
    i = str(i)
    new_count.append(i)

flag = True
database = csv.reader(open(argv[1]))
for row in database:
    name = row.pop(0)
    if row == new_count:
        flag = True
        break
    else:
        flag = False

if flag == True:
    print(name)
else:
    print("No match")