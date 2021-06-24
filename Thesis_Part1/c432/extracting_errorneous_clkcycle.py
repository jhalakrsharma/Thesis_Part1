import pandas as pd
import os
import csv
import subprocess
import random
import glob

final_compare = pd.DataFrame(columns = ["Clk", "Node", "N1", "N4", "N8", "N11", "N14", "N17", "N21", "N24", "N27", "N30", "N34", "N37", "N40", "N43", "N47", "N50", "N53", "N56", "N60", "N63", "N66", "N69", "N73", "N76", "N79", "N82", "N86", "N89", "N92", "N95", "N99", "N102", "N105", "N108", "N112", "N115", "N223", "N329", "N370", "N421", "N430", "N431", "N432", "N223g", "N329g", "N370g", "N421g", "N430g", "N431g", "N432g"])

#--------------------------------------------------------------------------------
# Extracting the line at which enable is 1
for faulty_csv in glob.glob('fault*.csv'):
    #print(faulty_csv)
    filename = faulty_csv.split( "_" )  #split on underscores
    first_half = filename[0]            #first part of the split is the sequence
    sec_half = filename[1]              #second part of the split is the shot

    extension = sec_half.split( "." )   #split on fullstop
    Node = extension[0]                 #first part of the split is the sequence
    #print(Node)
    ext = extension[1]                  #second part of the split is the shot
    rows = []

    sf = pd.read_csv(faulty_csv)
    sf = sf.loc[sf['en'] == 1]
    #print(sf)
    # Clock cycle at which error was enabled *
    time_en = sf.iloc[0,0]
    print("Clk = ",time_en)
    time_in = time_en - 2
    time_outf = time_en + 2
# #-----------------------------------------------------------------------------------
    # Reading the line previous to the line when error was enabled to extract inputs
    df = pd.read_csv(faulty_csv)
    # Previous line
    df = df.loc[df['Clk'] == time_in]
    #print(df)
    
    #extractting the input where enable is 1.

    # Value of input N1
    N1 = df.iloc[0,1]
    #print("N1   = ",N1)

    # Value of input N4
    N4 = df.iloc[0,2]
    #print("N4   = ",N4)

    # Value of input N8
    N8 = df.iloc[0,3]
    #print("N8   =",N8)
    
    # Value of input N11
    N11 = df.iloc[0,4]
    #print("N11  = ",N11)

    # Value of input N14
    N14 = df.iloc[0,5]
    #print("N14  = ",N14)

    # Value of input N17
    N17 = df.iloc[0,6]
    #print("N17  =",N17)

    # Value of input N21
    N21 = df.iloc[0,7]
    #print("N21  = ",N21)

    # Value of input N24
    N24 = df.iloc[0,8]
    #print("N24  = ",N24)

    # Value of input N27
    N27 = df.iloc[0,9]
    #print("N27  =",N27)

    # Value of input N30
    N30 = df.iloc[0,10]
    #print("N30  = ",N30)

    # Value of input N34
    N34 = df.iloc[0,11]
    #print("N34  = ",N34)

    # Value of input N37
    N37 = df.iloc[0,12]
    #print("N37  =",N37)
    
    # Value of input N40
    N40 = df.iloc[0,13]
    #print("N40  = ",N40)

    # Value of input N43
    N43 = df.iloc[0,14]
    #print("N43  = ",N43)

    # Value of input N47
    N47 = df.iloc[0,15]
    #print("N47  =",N47)
    
    # Value of input N50
    N50 = df.iloc[0,16]
    #print("N50  = ",N50)

    # Value of input N53
    N53 = df.iloc[0,17]
    #print("N53  = ",N53)

    # Value of input N56
    N56 = df.iloc[0,18]
    #print("N56  =",N56)
        
    # Value of input N60
    N60 = df.iloc[0,19]
    #print("N60  = ",N60)

    # Value of input N63
    N63 = df.iloc[0,20]
    #print("N63  = ",N63)

    # Value of input N66
    N66 = df.iloc[0,21]
    #print("N66  =",N66)
    
    # Value of input N69
    N69 = df.iloc[0,22]
    #print("N69  = ",N69)

    # Value of input N73
    N73 = df.iloc[0,23]
    #print("N73  = ",N73)

    # Value of input N76
    N76 = df.iloc[0,24]
    #print("N76  =",N76)
           
    # Value of input N79
    N79 = df.iloc[0,25]
    #print("N79  = ",N79)

    # Value of input N82
    N82 = df.iloc[0,26]
    #print("N82 = ",N82)

    # Value of input N86
    N86 = df.iloc[0,27]
    #print("N86 =",N86)
  
    # Value of input N89
    N89 = df.iloc[0,28]
    #print("N89 = ",N89)

    # Value of input N92
    N92 = df.iloc[0,29]
    #print("N92 = ",N92)

    # Value of input N95
    N95 = df.iloc[0,30]
    #print("N95 =",N95)
    
    # Value of input N99
    N99 = df.iloc[0,31]
    #print("N99 = ",N99)

    # Value of input N102
    N102 = df.iloc[0,32]
    #print("N102 =",N102)
    
    # Value of input N105
    N105 = df.iloc[0,33]
    #print("N105 = ",N105)

    # Value of input N108
    N108 = df.iloc[0,34]
    #print("N108 = ",N108)

    # Value of input N112
    N112 = df.iloc[0,35]
    #print("N112 =",N112)
           
    # Value of input N115
    N115 = df.iloc[0,36]
    #print("N115 = ",N115)
#--------------------------------------------------------------------------------
## Extracting faulty output values
    ff = pd.read_csv(faulty_csv)

    # Same line at which error was enabled
    faulty = ff.loc[ff['Clk'] == time_outf]
    #print(faulty)

    # Faulty value of N223
    N223 = faulty.iloc[0,38]
    #print("N223= ",N223)

    # Faulty value of N329
    N329 = faulty.iloc[0,39]
    #print("N329= ",N329)

    # Faulty value of N370
    N370 = faulty.iloc[0,40]
    #print("N370= ",N370)

    # Faulty value of N421
    N421 = faulty.iloc[0,41]
    #print("N421= ",N421)
    
    # Faulty value of N430
    N430 = faulty.iloc[0,42]
    #print("N430= ",N430)

    # Faulty value of N431
    N431 = faulty.iloc[0,43]
    #print("N431= ",N431)

    # Faulty value of N432
    N432 = faulty.iloc[0,44]
    #print("N432= ",N432)
#---------------------------------------------------------------------------------
    # Reading the golden output to extract correct value output
    cf = pd.read_csv('golden_c432_py.csv')

    # Same line at which error was enabled
    gold = cf.loc[cf['Clk'] == time_outf]
    #print("Golden outputline",gold)

    # Golden value of N223
    N223g = gold.iloc[0,38]
    #print("N223= ",N223g)

    # Golden value of N329
    N329g = gold.iloc[0,39]
    #print("N329= ",N329g)

    # Golden value of N370
    N370g = gold.iloc[0,40]
    #print("N370= ",N370g)

    # Golden value of N421
    N421g = gold.iloc[0,41]
    #print("N421= ",N421g)
    
    # Golden value of N430
    N430g = gold.iloc[0,42]
    #print("N430= ",N430g)

    # Golden value of N431
    N431g = gold.iloc[0,43]
    #print("N431= ",N431g)

    # Golden value of N432
    N432g = gold.iloc[0,44]
    #print("N432= ",N432g)
#---------------------------------------------------------------------------------
    #appending all values in order to form a row

    rows.append(time_in)
    rows.append(Node)
    rows.append(N1)
    rows.append(N4)
    rows.append(N8)
    rows.append(N11)
    rows.append(N14)
    rows.append(N17)
    rows.append(N21)
    rows.append(N24)
    rows.append(N27)
    rows.append(N30)
    rows.append(N34)
    rows.append(N37)
    rows.append(N40)
    rows.append(N43)
    rows.append(N47)
    rows.append(N50)
    rows.append(N53)
    rows.append(N56)
    rows.append(N60)
    rows.append(N63)
    rows.append(N66)
    rows.append(N69)
    rows.append(N73)
    rows.append(N76)
    rows.append(N79)
    rows.append(N82)
    rows.append(N86)
    rows.append(N89)
    rows.append(N92)
    rows.append(N95)
    rows.append(N99)
    rows.append(N102)
    rows.append(N105)
    rows.append(N108)
    rows.append(N112)
    rows.append(N115)

#output rows append (faulty) 
    rows.append(N223)
    rows.append(N329)
    rows.append(N370)
    rows.append(N421)
    rows.append(N430)
    rows.append(N431)
    rows.append(N432)

#output rows append (golden)      
    rows.append(N223g)
    rows.append(N329g)
    rows.append(N370g)
    rows.append(N421g)
    rows.append(N430g)
    rows.append(N431g)
    rows.append(N432g)
    #print(rows)

    final_compare = final_compare.append(pd.Series(rows, index = ["Clk", "Node", "N1", "N4", "N8", "N11", "N14", "N17", "N21", "N24", "N27", "N30", "N34", "N37", "N40", "N43", "N47", "N50", "N53", "N56", "N60", "N63", "N66", "N69", "N73", "N76", "N79", "N82", "N86", "N89", "N92", "N95", "N99", "N102", "N105", "N108", "N112", "N115", "N223", "N329", "N370", "N421", "N430", "N431", "N432", "N223g", "N329g", "N370g", "N421g", "N430g", "N431g", "N432g"]), ignore_index=True)
##---------------------------------------------------------------------------------
#print(final_compare)

N223_Comp = pd.to_numeric(final_compare['N223']) != pd.to_numeric(final_compare['N223g'])
N223_Comp = N223_Comp.astype(int)

N329_Comp = pd.to_numeric(final_compare['N329']) != pd.to_numeric(final_compare['N329g'])
N329_Comp = N329_Comp.astype(int)

N370_Comp = pd.to_numeric(final_compare['N370']) != pd.to_numeric(final_compare['N370g'])
N370_Comp = N370_Comp.astype(int)

N421_Comp = pd.to_numeric(final_compare['N421']) != pd.to_numeric(final_compare['N421g'])
N421_Comp = N421_Comp.astype(int)

N430_Comp = pd.to_numeric(final_compare['N430']) != pd.to_numeric(final_compare['N430g'])
N430_Comp = N430_Comp.astype(int)

N431_Comp = pd.to_numeric(final_compare['N431']) != pd.to_numeric(final_compare['N431g'])
N431_Comp = N431_Comp.astype(int)

N432_Comp = pd.to_numeric(final_compare['N432']) != pd.to_numeric(final_compare['N432g'])
N432_Comp = N432_Comp.astype(int)


final_compare = final_compare.assign(N223_Comp = N223_Comp.values)
final_compare = final_compare.assign(N329_Comp = N329_Comp.values)
final_compare = final_compare.assign(N370_Comp = N370_Comp.values)
final_compare = final_compare.assign(N421_Comp = N421_Comp.values)
final_compare = final_compare.assign(N430_Comp = N430_Comp.values)
final_compare = final_compare.assign(N431_Comp = N431_Comp.values)
final_compare = final_compare.assign(N432_Comp = N432_Comp.values)

final_compare["M/S"] = final_compare["N223_Comp"] + final_compare["N329_Comp"] + final_compare["N370_Comp"] + final_compare["N421_Comp"] + final_compare["N430_Comp"] + final_compare["N431_Comp"] + final_compare["N432_Comp"] 

final_compare.index.rename('Sr.No.', inplace=True)

final_compare.to_csv("compare.csv")

# final_compare = final_compare.loc[final_compare['M/S'] == 2]
# #print(final_compare)
# #Cri_Node = final_compare.iloc[:,1]
# #print(Cri_Node)
# #Multiple = final_compare.iloc[:,11]
# #print(Multiple)
# #final_compare = final_compare.assign(Multiple=Multiple.values)
# #final_compare = final_compare.assign(Cri_Node=Cri_Node.values)
# final_compare.to_csv("Critical.csv")
