# Final Python code

from collections import OrderedDict
import re
import random
import sys

#-------------------------------------------------------------------------------------------------------------------------------
### Creating an empty string to read the parameters.
parameters = ""

#-------------------------------------------------------------------------------------------------------------------------------
### Opening the file, reading line by line, searchin for input, output or wire keyboard and saving the lines in parameters string.
with open('c6288.v', 'r') as f:
    for line in f:
        if "input" in line or "wire" in line:
            # print(line.partition('//')[0])
            parameters += line.partition('//')[0]

#-------------------------------------------------------------------------------------------------------------------------------
### Removing tabs, new lines, input, output, wire, commas, semicolons, and splitting on spaces finally.
parameters = parameters.replace("\t", "")
parameters = parameters.replace("\n", "")
parameters = parameters.replace("input", "")
parameters = parameters.replace("output", "")

#-------------------------------------------------------------------------------------------------------------------------------
### Using regular expressions, to remove the [XX:XX] string in between.
parameters = re.sub("[\(\[].*?[\)\]]", "", parameters)
parameters = parameters.replace("wire", "")
parameters = parameters.replace(",", "")
parameters = parameters.replace(";","")
parameters = parameters.split(" ")

#-------------------------------------------------------------------------------------------------------------------------------
### Due to some spaces items in the list, removing them.
parameters = list(filter(None, parameters))
print ("Parameters = ", parameters)

#-------------------------------------------------------------------------------------------------------------------------------
### OrderedDict does the same and preserves the order.
parameters = list(OrderedDict.fromkeys(parameters))
#prints all parameters in new line
print(*parameters, sep = "\n")

# Removing clock from the list if present
if "clk" in parameters:
    parameters.remove("clk")
if "d" in parameters:
    parameters.remove("d")
if "q" in parameters:
    parameters.remove("q")
if "error" in parameters:
    parameters.remove("error")
if "reg" in parameters:
    parameters.remove("reg")
if "en" in parameters:
    parameters.remove("en")    
    print ("Parameters = ", parameters)
    number = len(parameters)
    print ("Number of parameters = ", number)
#-------------------------------------------------------------------------------------------------------------------------------
### Generte a for loop to include all the parameters to inject fault, and above that create as many files as the number of parameters

lookup      = 'endmodule'
lookup1     = 'dut'
linenumber  = []
linenumber2 = []
enable      = ", en);"
input2      = parameters
lines_output = []
# print(type(parameters))
#
for parameter in parameters:
    with open('fault{}.v'.format(parameter), "w") as f:
        with open('c6288.v', 'r') as h:
            for num, line in enumerate(h, 1):
                if lookup in line:
                    linenumber.append(num)

            change = "xor u1 (error, en, " + parameter + ");\n"

        with open('c6288.v', 'r') as k:
            lines = k.readlines()

        with open('fault1.v', 'w') as m:
            for i, line in enumerate(lines):
                if i == linenumber[0] - 1:
                    #print(linenumber[0])
                    m.write(change)
                m.write(line)

# #-------------------------------------------------------------------------------------------------------------------------------
# ## Opening fault1 file in read mode, saving the contents in variable named "lines"
        with open('fault1.v', 'r') as k:
            lines = k.readlines()
            #print(lines)

# # #-------------------------------------------------------------------------------------------------------------------------------
# ### Adding new reg 'en' in the testbench in the faulty file
        with open('fault1.v', 'r') as k:
            lines_again = k.readlines()

        with open('fault1.v', 'w') as b:
            for item in lines_again:
                #b.write("%s" % item)
                f.write("%s" % item)
