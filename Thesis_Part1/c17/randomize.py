import glob, os
import subprocess
import random
import csv

#Critical nodes extracted from the golden code.
parameter =  ['N1', 'N2', 'N3', 'N6', 'N7', 'N10', 'N11', 'N16', 'N19', 'd1', 'd2', 'd3', 'd6', 'd7', 'N22', 'N23', 'd22', 'd23']
lookup = 'en = 0'
linenumber = []
rows = []
toAdd = ["J", "N1", "N2", "N3", "N6", "N7", "en", "N22", "N23"]

# Generating a random number, to randomly select one of the parameters
randpara = random.randint(0, 17)
#print ("Random number = ",randpara)
para = parameter[randpara]
#print("Random Parameter = ", para);

# Generating a random number, to randomly select one of the clock cycle to inject fault
# After generating random number, print the index
#randrange ([start,] stop [,step])
randcycle = random.randrange(2, 499, 2)
randcycle  = randcycle + 0.8
#print ("Random clock cycle = ",randcycle)
randomize = repr(randcycle) + "_" + para
print(randomize)

for param in parameter:
    with open('fault{}.v'.format(randomize), "w") as f:
        with open('fault{}.v'.format(para), 'r') as h:
            for num, line in enumerate(h, 1):
                if lookup in line:
                    linenumber.append(num)

        change = "\t\t#" + repr(randcycle) + " " + "en = 1;\n"

        with open('fault{}.v'.format(para), 'r') as k:
            lines = k.readlines()

        with open('fault{}.v'.format(randomize), "w") as m:
            for i, line in enumerate(lines):
                if i == linenumber[1]-1:
                    m.write(change)
                m.write(line)

# creating csv file to store the output of this faulty file
for para in parameter:
    with open('fault{}.v'.format(randomize), "r") as f:
        cmd1 = 'iverilog -o fault' + randomize + " " + 'fault' + randomize + '.v'
        #print(cmd1)
        cmd2 = 'vvp fault' + randomize + " " + '> fault' + randomize + '.csv'
        os.system(cmd1)
        os.system(cmd2)

    with open('fault{}.csv'.format(randomize), "r") as infile:
        reader = list(csv.reader(infile))
        reader.insert(0, toAdd)

    with open('fault{}.csv'.format(randomize), "w", newline = '') as outfile:
        writer = csv.writer(outfile)
        for line in reader:
            writer.writerow(line)
