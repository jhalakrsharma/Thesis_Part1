import re

parameters =  ['N1', 'N2', 'N3', 'N6', 'N7', 'N10', 'N11', 'N16', 'N19', 'd1', 'd2', 'd3', 'd6', 'd7', 'N22', 'N23', 'd22', 'd23']
#print(type(parameters))
for parameter in parameters:
    lines_output = []
    with open('fault' + parameter + '.v', 'r') as k:
        lines = k.readlines()

    for item in lines:
        if(re.match("^(|\t)(xor|nand|and|nor|or|dff)", item)):
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
