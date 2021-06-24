import pandas as pd
import os
import csv
import subprocess
import random
import glob

final_compare = pd.DataFrame(columns = ["Clk", "Node", "A", "B", "Cin", "Sum_f", "Cout_f", "Sum_g", "Cout_g"])

#--------------------------------------------------------------------------------
# Extracting the line at which enable is 1
for faulty_csv in glob.glob('fault*.csv'):
    print(faulty_csv)
    filename = faulty_csv.split( "_" )  #split on underscores
    first_half = filename[0]            #first part of the split is the sequence
    sec_half = filename[1]              #second part of the split is the shot

    extension = sec_half.split( "." )   #split on fullstop
    Node = extension[0]                 #first part of the split is the sequence
    ext = extension[1]                  #second part of the split is the shot

    rows = []

    sf = pd.read_csv(faulty_csv)
    sf = sf.loc[sf['en'] == 1]
    print(sf)
    # Clock cycle at which error was enabled *
    time_en = sf.iloc[0,0]
    print("Clk = ",time_en)
    time_in = time_en - 2
    time_outf = time_en + 2
#-----------------------------------------------------------------------------------
    # Reading the line previous to the line when error was enabled to extract inputs
    df = pd.read_csv(faulty_csv)
    # Previous line
    df = df.loc[df['J'] == time_in]
    #print(df)

    # Value of input A
    Ain = df.iloc[0,1]
    #print("A = ",Ain)

    # Value of input B
    Bin = df.iloc[0,2]
    #print("B = ", Bin)

    # Value of input Cin
    Cin_in = df.iloc[0,3]
    #print("Cin=",Cin_in)
#--------------------------------------------------------------------------------
# Extracting faulty sum and cout values
    ff = pd.read_csv(faulty_csv)

    # Same line at which error was enabled
    faulty = ff.loc[ff['J'] == time_outf]
    #print(faulty)

    # Correct value of sum
    Sum_f = faulty.iloc[0,5]
    #print("Sum_f= ",Sum_f)

    # Correct value of Cout
    Cout_f = faulty.iloc[0,6]
    #print("Cout_f= ",Cout_f)

    #---------------------------------------------------------------------------------
    # Reading the golden output to extract correct value of sum and Cout
    cf = pd.read_csv('golden_csv.csv')

    # Same line at which error was enabled
    gold = cf.loc[cf['J'] == time_outf]
    #print(gold)

    # Correct value of sum
    Sum_g = gold.iloc[0,5]
    #print("Sum_g= ",Sum_g)

    # Correct value of Cout
    Cout_g = gold.iloc[0,6]
    #print("Cout_g= ",Cout_g)

    #---------------------------------------------------------------------------------
    #appending all values in order to form a row

    rows.append(time_en)
    rows.append(Node)
    rows.append(Ain)
    rows.append(Bin)
    rows.append(Cin_in)
    rows.append(Sum_f)
    rows.append(Cout_f)
    rows.append(Sum_g)
    rows.append(Cout_g)
    #print(rows)
    final_compare = final_compare.append(pd.Series(rows, index = ["Clk", "Node", "A", "B", "Cin", "Sum_f", "Cout_f", "Sum_g", "Cout_g"]), ignore_index=True)
    #---------------------------------------------------------------------------------
#print(final_compare)

Sum_Comp = pd.to_numeric(final_compare['Sum_f']) != pd.to_numeric(final_compare['Sum_g'])
Sum_Comp =  Sum_Comp.astype(int)
Cout_Comp = pd.to_numeric(final_compare['Cout_f']) != pd.to_numeric(final_compare['Cout_g'])
Cout_Comp = Cout_Comp.astype(int)

final_compare = final_compare.assign(Sum_Comp=Sum_Comp.values)
final_compare = final_compare.assign(Cout_Comp=Cout_Comp.values)
final_compare["M/S"] = final_compare["Cout_Comp"] + final_compare["Sum_Comp"]
final_compare.index.rename('Simulation', inplace=True)
final_compare.to_csv("compare.csv")

final_compare = final_compare.loc[final_compare['M/S'] == 2]
#print(final_compare)
#Cri_Node = final_compare.iloc[:,1]
#print(Cri_Node)
#Multiple = final_compare.iloc[:,11]
#print(Multiple)
#final_compare = final_compare.assign(Multiple=Multiple.values)
#final_compare = final_compare.assign(Cri_Node=Cri_Node.values)
final_compare.to_csv("Critical.csv")
