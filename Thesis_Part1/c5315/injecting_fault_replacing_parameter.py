import re

parameters =  ['N1', 'N4', 'N11', 'N14', 'N17', 'N20', 'N23', 'N24', 'N25', 'N26', 'N27', 'N31', 'N34', 'N37', 'N40', 'N43', 'N46', 'N49', 'N52', 'N53', 'N54', 'N61', 'N64', 'N67', 'N70', 'N73', 'N76', 'N79', 'N80', 'N81', 'N82', 'N83', 'N86', 'N87', 'N88', 'N91', 'N94', 'N97', 'N100', 'N103', 'N106', 'N109', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N135', 'N136', 'N137', 'N140', 'N141', 'N145', 'N146', 'N149', 'N152', 'N155', 'N158', 'N161', 'N164', 'N167', 'N170', 'N173', 'N176', 'N179', 'N182', 'N185', 'N188', 'N191', 'N194', 'N197', 'N200', 'N203', 'N206', 'N209', 'N210', 'N217', 'N218', 'N225', 'N226', 'N233', 'N234', 'N241', 'N242', 'N245', 'N248', 'N251', 'N254', 'N257', 'N264', 'N265', 'N272', 'N273', 'N280', 'N281', 'N288', 'N289', 'N292', 'N293', 'N299', 'N302', 'N307', 'N308', 'N315', 'N316', 'N323', 'N324', 'N331', 'N332', 'N335', 'N338', 'N341', 'N348', 'N351', 'N358', 'N361', 'N366', 'N369', 'N372', 'N373', 'N374', 'N386', 'N389', 'N400', 'N411', 'N422', 'N435', 'N446', 'N457', 'N468', 'N479', 'N490', 'N503', 'N514', 'N523', 'N534', 'N545', 'N549', 'N552', 'N556', 'N559', 'N562', 'N566', 'N571', 'N574', 'N577', 'N580', 'N583', 'N588', 'N591', 'N592', 'N595', 'N596', 'N597', 'N598', 'N599', 'N603', 'N607', 'N610', 'N613', 'N616', 'N619', 'N625', 'N631']
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
