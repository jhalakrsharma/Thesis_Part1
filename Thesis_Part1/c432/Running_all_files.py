import os
import sys


# os.chdir('D:\\Thesis\\python files\\c432')
# cwd = os.getcwd()
# print(cwd)
os.system('python create_multiple_faulty_files.py')
os.system('python injecting_fault_replacing_parameter.py')
os.system('python randomize.py')
os.system('python extracting_errorneous_clkcycle.py')
