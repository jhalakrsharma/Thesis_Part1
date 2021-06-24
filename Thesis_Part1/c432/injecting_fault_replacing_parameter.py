import re

parameters = ['N1', 'N4', 'N8', 'N11', 'N14', 'N17', 'N21', 'N24', 'N27', 'N30', 'N34', 'N37', 'N40', 'N43', 'N47', 'N50', 'N53', 'N56', 'N60', 'N63', 'N66', 'N69', 'N73', 'N76', 'N79', 'N82', 'N86',  'N89', 'N92', 'N95', 'N99', 'N102', 'N105', 'N108', 'N112', 'N115', 'N223', 'N329', 'N370',  'N421', 'N430', 'N431', 'N432', 'd1', 'd4', 'd8', 'd11', 'd14', 'd17', 'd21', 'd24', 'd27', 'd30', 'd34', 'd37', 'd40', 'd43', 'd47', 'd50', 'd53', 'd56', 'd60', 'd63', 'd66',  'd69', 'd73', 'd76', 'd79', 'd82', 'd86', 'd89', 'd92', 'd95', 'd99', 'd102', 'd105', 'd108', 'd112', 'd115', 'd223', 'd329', 'd370', 'd421', 'd430', 'd431', 'd432', 'N118', 'N119',  'N122', 'N123', 'N126', 'N127', 'N130', 'N131', 'N134', 'N135', 'N138', 'N139', 'N142',  'N143', 'N146', 'N147', 'N150', 'N151', 'N154', 'N157', 'N158', 'N159', 'N162', 'N165',  'N168', 'N171', 'N174', 'N177', 'N180', 'N183', 'N184', 'N185', 'N186', 'N187', 'N188',  'N189', 'N190', 'N191', 'N192', 'N193', 'N194', 'N195', 'N196', 'N197', 'N198', 'N199', 'N203', 'N213', 'N224', 'N227', 'N230', 'N233', 'N236', 'N239', 'N242', 'N243', 'N246', 'N247', 'N250', 'N251', 'N254', 'N255', 'N256', 'N257', 'N258', 'N259', 'N260', 'N263', 'N264', 'N267', 'N270', 'N273', 'N276', 'N279', 'N282', 'N285', 'N288', 'N289', 'N290', 'N291', 'N292', 'N293', 'N294', 'N295', 'N296', 'N300', 'N301', 'N302', 'N303', 'N304', 'N305', 'N306', 'N307', 'N308', 'N309', 'N319', 'N330', 'N331', 'N332', 'N333', 'N334', 'N335', 'N336', 'N337', 'N338', 'N339', 'N340', 'N341', 'N342', 'N343', 'N344', 'N345', 'N346', 'N347', 'N348', 'N349', 'N350', 'N351', 'N352', 'N353', 'N354', 'N355', 'N356', 'N357', 'N360', 'N371', 'N372', 'N373', 'N374', 'N375', 'N376', 'N377', 'N378', 'N379', 'N380', 'N381', 'N386', 'N393', 'N399', 'N404', 'N407', 'N411', 'N414', 'N415', 'N416', 'N417', 'N418', 'N419', 'N420', 'N422', 'N425', 'N428', 'N429', 'N223', 'N329', 'N370', 'N421', 'N430', 'N431', 'N432']
for parameter in parameters:
    lines_output = []
    with open('fault' + parameter + '.v', 'r') as k:
        lines = k.readlines()

    for item in lines:
        if(re.match("^(|\t)(xor|nand|and|nor|or|not|xnor|dff)", item)):
            if(re.search("/*\("+ parameter +",", item)):
                lines_output.append(item)
            elif(re.search("/*\(error,", item)):
                lines_output.append(item)
            elif(re.search("( |,)" + parameter + "( |,|\))", item)):
                item = item.replace(parameter, "error")
                lines_output.append(item)
            else:
                lines_output.append(item)
        else:
            lines_output.append(item)

    with open('fault' + parameter + '.v', 'w') as n:
        for item in lines_output:
            n.write("%s" % item)