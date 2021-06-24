import re

parameters =  ['N1', 'N13', 'N20', 'N33', 'N41', 'N45', 'N50', 'N58', 'N68', 'N77', 'N87', 'N97', 'N107', 'N116', 'N124', 'N125', 'N128', 'N132', 'N137', 'N143', 'N150', 'N159', 'N169', 'N179', 'N190', 'N200', 'N213', 'N222', 'N223', 'N226', 'N232', 'N238', 'N244', 'N250', 'N257', 'N264', 'N270', 'N274', 'N283', 'N294', 'N303', 'N311', 'N317', 'N322', 'N326', 'N329', 'N330', 'N343', 'N349', 'N350']
for parameter in parameters:
	lines_output = []
	
	with open('fault' + parameter + '.v', 'r') as k:
		lines = k.readlines()
		
	#print(parameter)
	
	for item in lines:
		if(re.match("^(|\t)(dff)", item)):
			#print("done")
			find1 = "(" + parameter + ","
			find2 = " " + parameter + ","
			item = item.replace(find1, "(error,")
			item = item.replace(find2, " error,")
			lines_output.append(item)
		else:
			lines_output.append(item)
	
	with open('fault' + parameter + '.v', 'w') as n:
		for item in lines_output:
			n.write("%s" % item)