#!/usr/bin/python3

import sys
import re
import json
import csv

reg = re.compile('[\d\d\d]')

nums = []
vals = []
d = dict()
d1 = dict()
d2 = dict()
d3 = dict()
level = 0
d = { 1: d1, 2: d2, 3: d3 }

line = sys.stdin.readline()
while line:
    line = line.rstrip()

    if line == 'Main Classes':
        level = 1
    elif line == 'Hundred Divisions':
        level = 2
    elif line == 'Thousand Sections':
        level = 3
    elif reg.match(line) and level > 0:
        nums.append(line)
        #print("Added " + line + " to nums...")
    elif not line or ord(line[0]) == 0x13:
        if nums and vals:
            if level > 0:
                d[level].update(dict(zip(nums, vals)))
                del nums[:]
                del vals[:]
    else:
        if nums:
            vals.append(line)
            #print("Added " + line + " to vals...")
    line = sys.stdin.readline()

with open('results.csv', 'w') as f:
    writer = csv.writer(f, delimiter = ',', quotechar='"')
    for i in range(3):
        for k in d[i+1].keys():
            writer.writerow([k, d[i+1][k], str(i+1)])
for i in range(3):
    with open('results_' + str(i+1) + '.json', 'w') as f:
        json.dump(d[i+1], f, sort_keys = True, indent = 4, separators = (',', ': '))
