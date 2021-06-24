import glob, os
import subprocess
import random
import csv

#all possible nodes extracted from the golden code.
parameter =  ['N1', 'N8', 'N13', 'N17', 'N26', 'N29', 'N36', 'N42', 'N51', 'N55', 'N59', 'N68', 'N72', 'N73', 'N74', 'N75', 'N80', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N96', 'N101', 'N106', 'N111', 'N116', 'N121', 'N126', 'N130', 'N135', 'N138', 'N143', 'N146', 'N149', 'N152', 'N153', 'N156', 'N159', 'N165', 'N171', 'N177', 'N183', 'N189', 'N195', 'N201', 'N207', 'N210', 'N219', 'N228', 'N237', 'N246', 'N255', 'N259', 'N260', 'N261', 'N267', 'N268']
lookup = 'en = 0'
linenumber = []
rows = []
toAdd = ["Clk", "N1", "N8", "N13", "N17", "N26", "N29", "N36", "N42", "N51", "N55", "N59", "N68", "N72", "N73", "N74", "N75", "N80", "N85", "N86", "N87", "N88", "N89", "N90", "N91", "N96", "N101", "N106", "N111", "N116", "N121", "N126", "N130", "N135", "N138", "N143", "N146", "N149", "N152", "N153", "N156", "N159", "N165", "N171", "N177", "N183", "N189", "N195", "N201", "N207", "N210", "N219", "N228", "N237", "N246", "N255", "N259", "N260", "N261", "N267", "N268", "en", "N388", "N389", "N390", "N391", "N418", "N419", "N420", "N421", "N422", "N423", "N446", "N447", "N448", "N449", "N450", "N767", "N768", "N850", "N863", "N864", "N865", "N866", "N874", "N878", "N879", "N880"]
                
# Generating a random number, to randomly select one of the parameters
randpara = random.randint(0, 59)
#print ("Random number = ",randpara)
para = parameter[randpara]
#print("Random Parameter = ", para);

# Generating a random number, to randomly select one of the clock cycle to inject fault
# After generating random number, print the index
#randrange ([start,] stop [,step])
randcycle = random.randrange(2, 998, 2)
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
                    # print(linenumber)

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