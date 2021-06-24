import glob, os
import subprocess
import random
import csv
import datetime
#print(str(datetime.datetime.now().time()))

#Critical nodes extracted from the golden code.
parameter = ['N1', 'N13', 'N20', 'N33', 'N41', 'N45', 'N50', 'N58', 'N68', 'N77', 'N87', 'N97', 'N107', 'N116', 'N124', 'N125', 'N128', 'N132', 'N137', 'N143', 'N150', 'N159', 'N169', 'N179', 'N190', 'N200', 'N213', 'N222', 'N223', 'N226', 'N232', 'N238', 'N244', 'N250', 'N257', 'N264', 'N270', 'N274', 'N283', 'N294', 'N303', 'N311', 'N317', 'N322', 'N326', 'N329', 'N330', 'N343', 'N349', 'N350']
lookup = 'en = 0'
linenumber = []
rows = []
#add clk, inputs, en, outputs
toAdd = ["Clk", "N1", "N13", "N20", "N33", "N41", "N45", "N50", "N58", "N68", "N77", "N87", "N97", "N107", "N116", "N124", "N125", "N128", "N132", "N137", "N143", "N150", "N159", "N169", "N179", "N190", "N200", "N213", "N222", "N223", "N226", "N232", "N238", "N244", "N250", "N257", "N264", "N270", "N274", "N283", "N294", "N303", "N311", "N317", "N322", "N326", "N329", "N330", "N343", "N349", "N350", "en", "N1713", "N1947", "N3195", "N3833", "N3987", "N4028", "N4145", "N4589", "N4667", "N4815", "N4944", "N5002", "N5045", "N5047", "N5078", "N5102", "N5120", "N5121", "N5192", "N5231", "N5360", "N5361"]

# Generating a random number, to randomly select one of the parameters
randpara = random.randint(0, len(parameter)-1)
#print ("Random number = ",randpara)

para = parameter[randpara]
#print("Random Parameter = ", para);
#print(str(datetime.datetime.now().time()))

# Generating a random number, to randomly select one of the clock cycle to inject fault
# After generating random number, print the index
#randrange ([start,] stop [,step])
randcycle = random.randrange(2, 998, 2)
randcycle  = randcycle + 0.8
#print ("Random clock cycle = ",randcycle)
randomize = repr(randcycle) + "_" + para
print(randomize)
#print(str(datetime.datetime.now().time()) + "test 2")
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
#print(str(datetime.datetime.now().time()) + "test 3")
# creating csv file to store the output of this faulty file
#for para in parameter:
with open('fault{}.v'.format(randomize), "r") as f:
	cmd1 = 'iverilog -o fault' + randomize + " " + 'fault' + randomize + '.v'
	#print(cmd1)
	#print(str(datetime.datetime.now().time()) + "test 4")
	cmd2 = 'vvp fault' + randomize + " " + '> fault' + randomize + '.csv'
	os.system(cmd1)
	#print(str(datetime.datetime.now().time()) + "test 4.1")
	os.system(cmd2)
#print(str(datetime.datetime.now().time()) + "test 5")
with open('fault{}.csv'.format(randomize), "r") as infile:
	reader = list(csv.reader(infile))
	reader.insert(0, toAdd)
#print(str(datetime.datetime.now().time()) + "test 5")
with open('fault{}.csv'.format(randomize), "w", newline = '') as outfile:
	writer = csv.writer(outfile)
	for line in reader:
		writer.writerow(line)

#print(str(datetime.datetime.now().time()) + "test 3")