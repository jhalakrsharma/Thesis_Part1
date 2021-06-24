import re

parameters = ['N1', 'N8', 'N13', 'N17', 'N26', 'N29', 'N36', 'N42', 'N51', 'N55', 'N59', 'N68', 'N72', 'N73', 'N74', 'N75', 'N80', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N96', 'N101', 'N106', 'N111', 'N116', 'N121', 'N126', 'N130', 'N135', 'N138', 'N143', 'N146', 'N149', 'N152', 'N153', 'N156', 'N159', 'N165', 'N171', 'N177', 'N183', 'N189', 'N195', 'N201', 'N207', 'N210', 'N219', 'N228', 'N237', 'N246', 'N255', 'N259', 'N260', 'N261', 'N267', 'N268']
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




# for parameter in parameters:
#     lines_output = []
#     with open('fault' + parameter + '.v', 'r') as k:
#         lines = k.readlines()
#     print(parameter)
#     for item in lines:
#         if(re.match("^(|\t)(xor|nand|and|nor|or|not|xnor|dff|buf)", item)):
#             if(re.search("/*\("+ parameter +",", item)):
#                 lines_output.append(item)
#             elif(re.search("/*\(error,", item)):
#                 lines_output.append(item)
#             elif(re.search("( |,)" + parameter + "( |,|\))", item)):
#                 item = item.replace(parameter, "error")
#                 lines_output.append(item)
#             else:
#                 lines_output.append(item)
#         else:
#             lines_output.append(item)
#     #print(lines_output)
#     with open('fault' + parameter + '.v', 'w') as n:
#         for item in lines_output:
#             n.write("%s" % item)
