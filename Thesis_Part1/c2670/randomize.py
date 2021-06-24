import glob, os
import subprocess
import random
import csv
import datetime
#print(str(datetime.datetime.now().time()))

#Critical nodes extracted from the golden code.
parameter = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N11', 'N14', 'N15', 'N16', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N40', 'N43', 'N44', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N219', 'N224', 'N227', 'N230', 'N231', 'N234', 'N237', 'N241', 'N246', 'N253', 'N256', 'N259', 'N262', 'N263', 'N266', 'N269', 'N272', 'N275', 'N278', 'N281', 'N284', 'N287', 'N290', 'N294', 'N297', 'N301', 'N305', 'N309', 'N313', 'N316', 'N319', 'N322', 'N325', 'N328', 'N331', 'N334', 'N337', 'N340', 'N343', 'N346', 'N349', 'N352', 'N355', 'N143_I', 'N144_I', 'N145_I', 'N146_I', 'N147_I', 'N148_I', 'N149_I', 'N150_I', 'N151_I', 'N152_I', 'N153_I', 'N154_I', 'N155_I', 'N156_I', 'N157_I', 'N158_I', 'N159_I', 'N160_I', 'N161_I', 'N162_I', 'N163_I', 'N164_I', 'N165_I', 'N166_I', 'N167_I', 'N168_I', 'N169_I', 'N170_I', 'N171_I', 'N172_I', 'N173_I', 'N174_I', 'N175_I', 'N176_I', 'N177_I', 'N178_I', 'N179_I', 'N180_I', 'N181_I', 'N182_I', 'N183_I', 'N184_I', 'N185_I', 'N186_I', 'N187_I', 'N188_I', 'N189_I', 'N190_I', 'N191_I', 'N192_I', 'N193_I', 'N194_I', 'N195_I', 'N196_I', 'N197_I', 'N198_I', 'N199_I', 'N200_I', 'N201_I', 'N202_I', 'N203_I', 'N204_I', 'N205_I', 'N206_I', 'N207_I', 'N208_I', 'N209_I', 'N210_I', 'N211_I', 'N212_I', 'N213_I', 'N214_I', 'N215_I', 'N216_I', 'N217_I', 'N218_I']
lookup = 'en = 0'
linenumber = []
rows = []

#toAdd = ["J", "N1", "N2", "N3", "N6", "N7", "en", "N22", "N23"];
toAdd = ["Clk", "N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8", "N11", "N14", "N15", "N16", "N19", "N20", "N21", "N22", "N23", "N24", "N25", "N26", "N27", "N28", "N29", "N32", "N33", "N34", "N35", "N36", "N37", "N40", "N43", "N44", "N47", "N48", "N49", "N50", "N51", "N52", "N53", "N54", "N55", "N56", "N57", "N60", "N61", "N62", "N63", "N64", "N65", "N66", "N67", "N68", "N69", "N72", "N73", "N74", "N75", "N76", "N77", "N78", "N79", "N80", "N81", "N82", "N85", "N86", "N87", "N88", "N89", "N90", "N91", "N92", "N93", "N94", "N95", "N96", "N99", "N100", "N101", "N102", "N103", "N104", "N105", "N106", "N107", "N108", "N111", "N112", "N113", "N114", "N115", "N116", "N117", "N118", "N119", "N120", "N123", "N124", "N125", "N126", "N127", "N128", "N129", "N130", "N131", "N132", "N135", "N136", "N137", "N138", "N139", "N140", "N141", "N142", "N219", "N224", "N227", "N230", "N231", "N234", "N237", "N241", "N246", "N253", "N256", "N259", "N262", "N263", "N266", "N269", "N272", "N275", "N278", "N281", "N284", "N287", "N290", "N294", "N297", "N301", "N305", "N309", "N313", "N316", "N319", "N322", "N325", "N328", "N331", "N334", "N337", "N340", "N343", "N346", "N349", "N352", "N355", "N143_I", "N144_I", "N145_I", "N146_I", "N147_I", "N148_I", "N149_I", "N150_I", "N151_I", "N152_I", "N153_I", "N154_I", "N155_I", "N156_I", "N157_I", "N158_I", "N159_I", "N160_I", "N161_I", "N162_I", "N163_I", "N164_I", "N165_I", "N166_I", "N167_I", "N168_I", "N169_I", "N170_I", "N171_I", "N172_I", "N173_I", "N174_I", "N175_I", "N176_I", "N177_I", "N178_I", "N179_I", "N180_I", "N181_I", "N182_I", "N183_I", "N184_I", "N185_I", "N186_I", "N187_I", "N188_I", "N189_I", "N190_I", "N191_I", "N192_I", "N193_I", "N194_I", "N195_I", "N196_I", "N197_I", "N198_I", "N199_I", "N200_I", "N201_I", "N202_I", "N203_I", "N204_I", "N205_I", "N206_I", "N207_I", "N208_I", "N209_I", "N210_I", "N211_I", "N212_I", "N213_I", "N214_I", "N215_I", "N216_I", "N217_I", "N218_I", "en", "N398", "N400", "N401", "N419", "N420", "N456", "N457", "N458", "N487", "N488", "N489", "N490", "N491", "N492", "N493", "N494", "N792", "N799", "N805", "N1026", "N1028", "N1029", "N1269", "N1277", "N1448", "N1726", "N1816", "N1817", "N1818", "N1819", "N1820", "N1821", "N1969", "N1970", "N1971", "N2010", "N2012", "N2014", "N2016", "N2018", "N2020", "N2022", "N2387", "N2388", "N2389", "N2390", "N2496", "N2643", "N2644", "N2891", "N2925", "N2970", "N2971", "N3038", "N3079", "N3546", "N3671", "N3803", "N3804", "N3809", "N3851", "N3875", "N3881", "N3882", "N143_O", "N144_O", "N145_O", "N146_O", "N147_O", "N148_O", "N149_O", "N150_O", "N151_O", "N152_O", "N153_O", "N154_O", "N155_O", "N156_O", "N157_O", "N158_O", "N159_O", "N160_O", "N161_O", "N162_O", "N163_O", "N164_O", "N165_O", "N166_O", "N167_O", "N168_O", "N169_O", "N170_O", "N171_O", "N172_O", "N173_O", "N174_O", "N175_O", "N176_O", "N177_O", "N178_O", "N179_O", "N180_O", "N181_O", "N182_O", "N183_O", "N184_O", "N185_O", "N186_O", "N187_O", "N188_O", "N189_O", "N190_O", "N191_O", "N192_O", "N193_O", "N194_O", "N195_O", "N196_O", "N197_O", "N198_O", "N199_O", "N200_O", "N201_O", "N202_O", "N203_O", "N204_O", "N205_O", "N206_O", "N207_O", "N208_O", "N209_O", "N210_O", "N211_O", "N212_O", "N213_O", "N214_O", "N215_O", "N216_O", "N217_O", "N218_O"]

# Generating a random number, to randomly select one of the parameters
randpara = random.randint(0, 232)

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