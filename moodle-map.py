# Tom Postler, 2015-03-27
# Convert the moodle gradebook to the moodle-map

import csv

ifilename = input("Input filename: ")

# Read
lines = []
with open(ifilename, newline='') as ifile:
    reader = csv.reader(ifile)
    for line in reader:
        lines.append([line[0], line[2]])

# Header row
del lines[0]

# Participants
for line in lines:
    line[0] = line[0].split(' ')[1]

ofilename = input("Output filename: ")

with open(ofilename, 'w', newline='') as ofile:
    writer = csv.writer(ofile)
    writer.writerow(['moodle-id','user_id'])
    writer.writerows(lines)

