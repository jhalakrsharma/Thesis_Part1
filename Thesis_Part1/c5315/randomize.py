import glob, os
import subprocess
import random
import csv
import datetime
#print(str(datetime.datetime.now().time()))

#Critical nodes extracted from the golden code.
parameter = ['N1', 'N4', 'N11', 'N14', 'N17', 'N20', 'N23', 'N24', 'N25', 'N26', 'N27', 'N31', 'N34', 'N37', 'N40', 'N43', 'N46', 'N49', 'N52', 'N53', 'N54', 'N61', 'N64', 'N67', 'N70', 'N73', 'N76', 'N79', 'N80', 'N81', 'N82', 'N83', 'N86', 'N87', 'N88', 'N91', 'N94', 'N97', 'N100', 'N103', 'N106', 'N109', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N135', 'N136', 'N137', 'N140', 'N141', 'N145', 'N146', 'N149', 'N152', 'N155', 'N158', 'N161', 'N164', 'N167', 'N170', 'N173', 'N176', 'N179', 'N182', 'N185', 'N188', 'N191', 'N194', 'N197', 'N200', 'N203', 'N206', 'N209', 'N210', 'N217', 'N218', 'N225', 'N226', 'N233', 'N234', 'N241', 'N242', 'N245', 'N248', 'N251', 'N254', 'N257', 'N264', 'N265', 'N272', 'N273', 'N280', 'N281', 'N288', 'N289', 'N292', 'N293', 'N299', 'N302', 'N307', 'N308', 'N315', 'N316', 'N323', 'N324', 'N331', 'N332', 'N335', 'N338', 'N341', 'N348', 'N351', 'N358', 'N361', 'N366', 'N369', 'N372', 'N373', 'N374', 'N386', 'N389', 'N400', 'N411', 'N422', 'N435', 'N446', 'N457', 'N468', 'N479', 'N490', 'N503', 'N514', 'N523', 'N534', 'N545', 'N549', 'N552', 'N556', 'N559', 'N562', 'N566', 'N571', 'N574', 'N577', 'N580', 'N583', 'N588', 'N591', 'N592', 'N595', 'N596', 'N597', 'N598', 'N599', 'N603', 'N607', 'N610', 'N613', 'N616', 'N619', 'N625', 'N631']
lookup = 'en = 0'
linenumber = []
rows = []
#inputs, en , outputs
toAdd = ["Clk", "N1", "N4", "N11", "N14", "N17", "N20", "N23", "N24", "N25", "N26", "N27", "N31", "N34", "N37", "N40", "N43", "N46", "N49", "N52", "N53", "N54", "N61", "N64", "N67", "N70", "N73", "N76", "N79", "N80", "N81", "N82", "N83", "N86", "N87", "N88", "N91", "N94", "N97", "N100", "N103", "N106", "N109", "N112", "N113", "N114", "N115", "N116", "N117", "N118", "N119", "N120", "N121", "N122", "N123", "N126", "N127", "N128", "N129", "N130", "N131", "N132", "N135", "N136", "N137", "N140", "N141", "N145", "N146", "N149", "N152", "N155", "N158", "N161", "N164", "N167", "N170", "N173", "N176", "N179", "N182", "N185", "N188", "N191", "N194", "N197", "N200", "N203", "N206", "N209", "N210", "N217", "N218", "N225", "N226", "N233", "N234", "N241", "N242", "N245", "N248", "N251", "N254", "N257", "N264", "N265", "N272", "N273", "N280", "N281", "N288", "N289", "N292", "N293", "N299", "N302", "N307", "N308", "N315", "N316", "N323", "N324", "N331", "N332", "N335", "N338", "N341", "N348", "N351", "N358", "N361", "N366", "N369", "N372", "N373", "N374", "N386", "N389", "N400", "N411", "N422", "N435", "N446", "N457", "N468", "N479", "N490", "N503", "N514", "N523", "N534", "N545", "N549", "N552", "N556", "N559", "N562", "N566", "N571", "N574", "N577", "N580", "N583", "N588", "N591", "N592", "N595", "N596", "N597", "N598", "N599", "N603", "N607", "N610", "N613", "N616", "N619", "N625", "N631", "en", "N709", "N816", "N1066", "N1137", "N1138", "N1139", "N1140", "N1141", "N1142", "N1143", "N1144", "N1145", "N1147", "N1152", "N1153", "N1154", "N1155", "N1972", "N2054", "N2060", "N2061", "N2139", "N2142", "N2309", "N2387", "N2527", "N2584", "N2590", "N2623", "N3357", "N3358", "N3359", "N3360", "N3604", "N3613", "N4272", "N4275", "N4278", "N4279", "N4737", "N4738", "N4739", "N4740", "N5240", "N5388", "N6641", "N6643", "N6646", "N6648", "N6716", "N6877", "N6924", "N6925", "N6926", "N6927", "N7015", "N7363", "N7365", "N7432", "N7449", "N7465", "N7466", "N7467", "N7469", "N7470", "N7471", "N7472", "N7473", "N7474", "N7476", "N7503", "N7504", "N7506", "N7511", "N7515", "N7516", "N7517", "N7518", "N7519", "N7520", "N7521", "N7522", "N7600", "N7601", "N7602", "N7603", "N7604", "N7605", "N7606", "N7607", "N7626", "N7698", "N7699", "N7700", "N7701", "N7702", "N7703", "N7704", "N7705", "N7706", "N7707", "N7735", "N7736", "N7737", "N7738", "N7739", "N7740", "N7741", "N7742", "N7754", "N7755", "N7756", "N7757", "N7758", "N7759", "N7760", "N7761", "N8075", "N8076", "N8123", "N8124", "N8127", "N8128"]

# Generating a random number, to randomly select one of the parameters
randpara = random.randint(0, 177)
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