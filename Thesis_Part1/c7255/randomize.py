import glob, os
import subprocess
import random
import csv
import datetime
#print(str(datetime.datetime.now().time()))

#Critical nodes extracted from the golden code.
parameter = ['N1', 'N5', 'N9', 'N12', 'N15', 'N18', 'N23', 'N26', 'N29', 'N32', 'N35', 'N38', 'N41', 'N44', 'N47', 'N50', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N69', 'N70', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N94', 'N97', 'N100', 'N103', 'N106', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N118', 'N121', 'N124', 'N127', 'N130', 'N133', 'N134', 'N135', 'N138', 'N141', 'N144', 'N147', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156', 'N157', 'N158', 'N159', 'N160', 'N161', 'N162', 'N163', 'N164', 'N165', 'N166', 'N167', 'N168', 'N169', 'N170', 'N171', 'N172', 'N173', 'N174', 'N175', 'N176', 'N177', 'N178', 'N179', 'N180', 'N181', 'N182', 'N183', 'N184', 'N185', 'N186', 'N187', 'N188', 'N189', 'N190', 'N191', 'N192', 'N193', 'N194', 'N195', 'N196', 'N197', 'N198', 'N199', 'N200', 'N201', 'N202', 'N203', 'N204', 'N205', 'N206', 'N207', 'N208', 'N209', 'N210', 'N211', 'N212', 'N213', 'N214', 'N215', 'N216', 'N217', 'N218', 'N219', 'N220', 'N221', 'N222', 'N223', 'N224', 'N225', 'N226', 'N227', 'N228', 'N229', 'N230', 'N231', 'N232', 'N233', 'N234', 'N235', 'N236', 'N237', 'N238', 'N239', 'N240', 'N242', 'N245', 'N248', 'N251', 'N254', 'N257', 'N260', 'N263', 'N267', 'N271', 'N274', 'N277', 'N280', 'N283', 'N286', 'N289', 'N293', 'N296', 'N299', 'N303', 'N307', 'N310', 'N313', 'N316', 'N319', 'N322', 'N325', 'N328', 'N331', 'N334', 'N337', 'N340', 'N343', 'N346', 'N349', 'N352', 'N355', 'N358', 'N361', 'N364', 'N367', 'N382', 'N241_I']
lookup = 'en = 0'
linenumber = []
rows = []

#toAdd = ["J", "N1", "N2", "N3", "N6", "N7", "en", "N22", "N23"];
toAdd = ["Clk", "N1", "N5", "N9", "N12", "N15", "N18", "N23", "N26", "N29", "N32", "N35", "N38", "N41", "N44", "N47", "N50", "N53", "N54", "N55", "N56", "N57", "N58", "N59", "N60", "N61", "N62", "N63", "N64", "N65", "N66", "N69", "N70", "N73", "N74", "N75", "N76", "N77", "N78", "N79", "N80", "N81", "N82", "N83", "N84", "N85", "N86", "N87", "N88", "N89", "N94", "N97", "N100", "N103", "N106", "N109", "N110", "N111", "N112", "N113", "N114", "N115", "N118", "N121", "N124", "N127", "N130", "N133", "N134", "N135", "N138", "N141", "N144", "N147", "N150", "N151", "N152", "N153", "N154", "N155", "N156", "N157", "N158", "N159", "N160", "N161", "N162", "N163", "N164", "N165", "N166", "N167", "N168", "N169", "N170", "N171", "N172", "N173", "N174", "N175", "N176", "N177", "N178", "N179", "N180", "N181", "N182", "N183", "N184", "N185", "N186", "N187", "N188", "N189", "N190", "N191", "N192", "N193", "N194", "N195", "N196", "N197", "N198", "N199", "N200", "N201", "N202", "N203", "N204", "N205", "N206", "N207", "N208", "N209", "N210", "N211", "N212", "N213", "N214", "N215", "N216", "N217", "N218", "N219", "N220", "N221", "N222", "N223", "N224", "N225", "N226", "N227", "N228", "N229", "N230", "N231", "N232", "N233", "N234", "N235", "N236", "N237", "N238", "N239", "N240", "N242", "N245", "N248", "N251", "N254", "N257", "N260", "N263", "N267", "N271", "N274", "N277", "N280", "N283", "N286", "N289", "N293", "N296", "N299", "N303", "N307", "N310", "N313", "N316", "N319", "N322", "N325", "N328", "N331", "N334", "N337", "N340", "N343", "N346", "N349", "N352", "N355", "N358", "N361", "N364", "N367", "N382", "N241_I", "en", "N387", "N388", "N478", "N482", "N484", "N486", "N489", "N492", "N501", "N505", "N507", "N509", "N511", "N513", "N515", "N517", "N519", "N535", "N537", "N539", "N541", "N543", "N545", "N547", "N549", "N551", "N553", "N556", "N559", "N561", "N563", "N565", "N567", "N569", "N571", "N573", "N582", "N643", "N707", "N813", "N881", "N882", "N883", "N884", "N885", "N889", "N945", "N1110", "N1111", "N1112", "N1113", "N1114", "N1489", "N1490", "N1781", "N10025", "N10101", "N10102", "N10103", "N10104", "N10109", "N10110", "N10111", "N10112", "N10350", "N10351", "N10352", "N10353", "N10574", "N10575", "N10576", "N10628", "N10632", "N10641", "N10704", "N10706", "N10711", "N10712", "N10713", "N10714", "N10715", "N10716", "N10717", "N10718", "N10729", "N10759", "N10760", "N10761", "N10762", "N10763", "N10827", "N10837", "N10838", "N10839", "N10840", "N10868", "N10869", "N10870", "N10871", "N10905", "N10906", "N10907", "N10908", "N11333", "N11334", "N11340", "N11342", "N241_O"]

# Generating a random number, to randomly select one of the parameters
randpara = random.randint(0, 206)

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