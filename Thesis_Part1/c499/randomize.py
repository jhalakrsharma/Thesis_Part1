import glob, os
import subprocess
import random
import csv

#Critical nodes extracted from the golden code.
parameter =  ['N1', 'N5', 'N9', 'N13', 'N17', 'N21', 'N25', 'N29', 'N33', 'N37', 'N41', 'N45', 'N49', 'N53', 'N57', 'N61', 'N65', 'N69', 'N73', 'N77', 'N81', 'N85', 'N89', 'N93', 'N97', 'N101', 'N105', 'N109', 'N113', 'N117', 'N121', 'N125', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N724', 'N725', 'N726', 'N727', 'N728', 'N729', 'N730', 'N731', 'N732', 'N733', 'N734', 'N735', 'N736', 'N737', 'N738', 'N739', 'N740', 'N741', 'N742', 'N743', 'N744', 'N745', 'N746', 'N747', 'N748', 'N749', 'N750', 'N751', 'N752', 'N753', 'N754', 'N755', 'error', 'N250', 'N251', 'N252', 'N253', 'N254', 'N255', 'N256', 'N257', 'N258', 'N259', 'N260', 'N261', 'N262', 'N263', 'N264', 'N265', 'N266', 'N267', 'N268', 'N269', 'N270', 'N271', 'N272', 'N273', 'N274', 'N275', 'N276', 'N277', 'N278', 'N279', 'N280', 'N281', 'N282', 'N283', 'N284', 'N285', 'N286', 'N287', 'N288', 'N289', 'N290', 'N293', 'N296', 'N299', 'N302', 'N305', 'N308', 'N311', 'N314', 'N315', 'N316', 'N317', 'N318', 'N319', 'N320', 'N321', 'N338', 'N339', 'N340', 'N341', 'N342', 'N343', 'N344', 'N345', 'N346', 'N347', 'N348', 'N349', 'N350', 'N351', 'N352', 'N353', 'N354', 'N367', 'N380', 'N393', 'N406', 'N419', 'N432', 'N445', 'N554', 'N555', 'N556', 'N557', 'N558', 'N559', 'N560', 'N561', 'N562', 'N563', 'N564', 'N565', 'N566', 'N567', 'N568', 'N569', 'N570', 'N571', 'N572', 'N573', 'N574', 'N575', 'N576', 'N577', 'N578', 'N579', 'N580', 'N581', 'N582', 'N583', 'N584', 'N585', 'N586', 'N587', 'N588', 'N589', 'N590', 'N591', 'N592', 'N593', 'N594', 'N595', 'N596', 'N597', 'N598', 'N599', 'N600', 'N601', 'N602', 'N607', 'N620', 'N625', 'N630', 'N635', 'N640', 'N645', 'N650', 'N655', 'N692', 'N693', 'N694', 'N695', 'N696', 'N697', 'N698', 'N699', 'N700', 'N701', 'N702', 'N703', 'N704', 'N705', 'N706', 'N707', 'N708', 'N709', 'N710', 'N711', 'N712', 'N713', 'N714', 'N715', 'N716', 'N717', 'N718', 'N719', 'N720', 'N721', 'N722', 'N723', 'd1', 'd5', 'd9', 'd13', 'd17', 'd21', 'd25', 'd29', 'd33', 'd37', 'd41', 'd45', 'd49', 'd53', 'd57', 'd61', 'd65', 'd69', 'd73', 'd77', 'd81', 'd85', 'd89', 'd93', 'd97', 'd101', 'd105', 'd109', 'd113', 'd117', 'd121', 'd125', 'd129', 'd130', 'd131', 'd132', 'd133', 'd134', 'd135', 'd136', 'd137', 'd724', 'd725', 'd726', 'd727', 'd728', 'd729', 'd730', 'd731', 'd732', 'd733', 'd734', 'd735', 'd736', 'd737', 'd738', 'd739', 'd740', 'd741', 'd742', 'd743', 'd744', 'd745', 'd746', 'd747', 'd748', 'd749', 'd750', 'd751', 'd752', 'd753', 'd754', 'd755', 'N724', 'N725', 'N726', 'N727', 'N728', 'N729', 'N730', 'N731', 'N732', 'N733', 'N734', 'N735', 'N736', 'N737', 'N738', 'N739', 'N740', 'N741', 'N742', 'N743']
lookup = 'en = 0'
linenumber = []
rows = []
toAdd = ["Clk", "N1", "N5", "N9", "N13", "N17", "N21", "N25", "N29", "N33", "N37", "N41", "N45", "N49", "N53", "N57", "N61", "N65", "N69", "N73", "N77", "N81", "N85", "N89", "N93", "N97", "N101", "N105", "N109", "N113", "N117", "N121", "N125", "N129", "N130", "N131", "N132", "N133", "N134", "N135", "N136", "N137", "en", "N724", "N725", "N726", "N727", "N728", "N729", "N730", "N731", "N732", "N733", "N734", "N735", "N736", "N737", "N738", "N739", "N740", "N741", "N742", "N743", "N744", "N745", "N746", "N747", "N748", "N749", "N750", "N751", "N752", "N753", "N754", "N755"]
                
# Generating a random number, to randomly select one of the parameters
randpara = random.randint(0, 336)
#print ("Random number = ",randpara)
para = parameter[randpara];
#print("Random Parameter = ", para);

# Generating a random number, to randomly select one of the clock cycle to inject fault
# After generating random number, print the index
#randrange ([start,] stop [,step])
randcycle = random.randrange(2, 1023, 2)
randcycle  = randcycle + 0.8;
#print ("Random clock cycle = ",randcycle)
randomize = repr(randcycle) + "_" + para;
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