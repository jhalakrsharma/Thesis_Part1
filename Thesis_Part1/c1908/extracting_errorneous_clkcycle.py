import pandas as pd
import os
import csv
import subprocess
import random
import glob

final_compare = pd.DataFrame(columns = ["Clk", "Node", "N1", "N4", "N7", "N10", "N13", "N16", "N19", "N22", "N25", "N28", "N31", "N34", "N37", "N40", "N43", "N46", "N49", "N53", "N56", "N60", "N63", "N66", "N69", "N72", "N76", "N79", "N82", "N85", "N88", "N91", "N94", "N99", "N104", "N2753", "N2754", "N2755", "N2756", "N2762", "N2767", "N2768", "N2779", "N2780", "N2781", "N2782", "N2783", "N2784", "N2785", "N2786", "N2787", "N2811", "N2886", "N2887", "N2888", "N2889", "N2890", "N2891", "N2892", "N2899", "N2753g", "N2754g", "N2755g", "N2756g", "N2762g", "N2767g", "N2768g", "N2779g", "N2780g", "N2781g", "N2782g", "N2783g", "N2784g", "N2785g", "N2786g", "N2787g", "N2811g", "N2886g", "N2887g", "N2888g", "N2889g", "N2890g", "N2891g", "N2892g", "N2899g"])

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
    
    #extracting the input where enable is 1.
    
   	# Value of input N1
    N1 = df.iloc[0,1]
    #print("N1   = ",N1)
  
    # Value of input N4    
    N4 = df.iloc[0,2]
    #print("N4   = ",N4)  

    # Value of input N7
    N7 = df.iloc[0,3]
    #print("N7   =",N7)
    
    # Value of input N10
    N10 = df.iloc[0,4]
    #print("N10  = ",N10)

    # Value of input N13
    N13 = df.iloc[0,5]
    #print("N13  = ",N13)

    # Value of input N16
    N16 = df.iloc[0,6]
    #print("N16  =",N16)

    # Value of input N19
    N19 = df.iloc[0,7]
    #print("N19  = ",N19)

    # Value of input N22
    N22 = df.iloc[0,8]
    #print("N22  = ",N22) 

    # Value of input N25
    N25 = df.iloc[0,9]
    #print("N25  =",N25)
    
    # Value of input N28
    N28 = df.iloc[0,10]
    #print("N28  = ",N28)

    # Value of input N31
    N31 = df.iloc[0,11]
    #print("N31  = ",N31)

    # Value of input N34
    N34 = df.iloc[0,12]
    #print("N34  =",N34)
    
    # Value of input N37
    N37 = df.iloc[0,13]
    #print("N37  = ",N37)

    # Value of input N40
    N40 = df.iloc[0,14]
    #print("N40  = ",N40)

    # Value of input N43
    N43 = df.iloc[0,15]     
    #print("N43  =",N43)
    
    # Value of input N46
    N46 = df.iloc[0,16]
    #print("N46  = ",N46)

    # Value of input N49
    N49 = df.iloc[0,17]
    #print("N49  = ",N49)

    # Value of input N53
    N53 = df.iloc[0,18]
    #print("N53  =",N53)

    # Value of input N56
    N56 = df.iloc[0,19]
    #print("N56  = ",N56)

    # Value of input N60
    N60 = df.iloc[0,20]
    #print("N60  = ",N60)

    # Value of input N63
    N63 = df.iloc[0,21]
    #print("N63  =",N63)
    
    # Value of input N66
    N66 = df.iloc[0,22]
    #print("N66  = ",N66)

    # Value of input N69
    N69 = df.iloc[0,23]    
    #print("N69  = ",N69)

    # Value of input N72
    N72 = df.iloc[0,24]
    #print("N72  =",N72)
           
    # Value of input N76
    N76 = df.iloc[0,25]
    #print("N76  = ",N76)

    # Value of input N79
    N79 = df.iloc[0,26]
    #print("N79 = ",N79)

    # Value of input N82
    N82 = df.iloc[0,27]
    #print("N82 =",N82)
     
    # Value of input N85
    N85 = df.iloc[0,28]
    #print("N85 = ",N85)

    # Value of input N88
    N88 = df.iloc[0,29]
    #print("N88 = ",N88)

    # Value of input N91
    N91 = df.iloc[0,30]
    #print("N91 =",N91)
    
    # Value of input N94
    N94 = df.iloc[0,31]
    #print("N94 = ",N94)

    # Value of input N99
    N99 = df.iloc[0,32]
    #print("N99 =",N99)
   
    # Value of input N104
    N104 = df.iloc[0,33]
    #print("N104 =",N104)
   
#--------------------------------------------------------------------------------
## Extracting faulty output values
    ff = pd.read_csv(faulty_csv)

    # Same line at which error was enabled
    faulty = ff.loc[ff['Clk'] == time_outf]     
    #print(faulty)

    # Faulty value of N2753
    N2753 = faulty.iloc[0,35]
    #print("N2753= ",N2753)

    # Faulty value of N2754
    N2754 = faulty.iloc[0,36]
    #print("N2754= ",N2754)

    # Faulty value of N2755
    N2755 = faulty.iloc[0,37]
    #print("N2755= ",N2755)

    # Faulty value of N2756
    N2756 = faulty.iloc[0,38]
    #print("N2756= ",N2756)
    
    # Faulty value of N2762
    N2762 = faulty.iloc[0,39]
    #print("N2762= ",N2762)

    # Faulty value of N2767
    N2767 = faulty.iloc[0,40]
    #print("N2767= ",N2767)

    # Faulty value of N2768
    N2768 = faulty.iloc[0,41]
    #print("N2768= ",N2768)

    # Faulty value of N2779
    N2779 = faulty.iloc[0,42]
    #print("N2779= ",N2779)

    # Faulty value of N2780
    N2780 = faulty.iloc[0,43]   
    #print("N2780= ",N2780)

    # Faulty value of N2781
    N2781 = faulty.iloc[0,44]
    #print("N2781= ",N2781)

    # Faulty value of N2782
    N2782 = faulty.iloc[0,45]
    #print("N2782= ",N2782)

    # Faulty value of N2783
    N2783 = faulty.iloc[0,46]
    #print("N2783= ",N2783)    
    
    # Faulty value of N2784
    N2784 = faulty.iloc[0,47]
    #print("N2784= ",N2784)

    # Faulty value of N2785
    N2785 = faulty.iloc[0,48]
    #print("N2785= ",N2785)

    # Faulty value of N2786
    N2786 = faulty.iloc[0,49]
    #print("N2786= ",N2786)

    # Faulty value of N2787
    N2787 = faulty.iloc[0,50]
    #print("N2787= ",N2787)
    
    # Faulty value of N2811
    N2811 = faulty.iloc[0,51]
    #print("N2811= ",N2811)

    # Faulty value of N2886
    N2886 = faulty.iloc[0,52]
    #print("N2886= ",N2886)
 
    # Faulty value of N2887
    N2887 = faulty.iloc[0,53]      
    #print("N2887= ",N2887)

    # Faulty value of N2888
    N2888 = faulty.iloc[0,54]
    #print("N2888= ",N2888)    
    
    # Faulty value of N2889
    N2889 = faulty.iloc[0,55]
    #print("N2889= ",N2889)

    # Faulty value of N2890
    N2890 = faulty.iloc[0,56]
    #print("N2890= ",N2890)

    # Faulty value of N2891
    N2891 = faulty.iloc[0,57]
    #print("N2891= ",N2891)

    # Faulty value of N2892
    N2892 = faulty.iloc[0,58]
    #print("N2892= ",N2892)
    
    # Faulty value of N2899
    N2899 = faulty.iloc[0,59]
    #print("N2899= ",N2899)
    
#---------------------------------------------------------------------------------
    # Reading the golden output to extract correct value output
    cf = pd.read_csv('golden_c1908.csv')

    # Same line at which error was enabled
    gold = cf.loc[cf['Clk'] == time_outf]
    #print("Golden outputline",gold)

    # Correct value of N2753
    N2753g = gold.iloc[0,35]
    #print("N2753= ",N2753)

    # Correct value of N2754
    N2754g = gold.iloc[0,36]
    #print("N2754= ",N2754)

    # Correct value of N2755
    N2755g = gold.iloc[0,37]
    #print("N2755= ",N2755)

    # Correct value of N2756
    N2756g = gold.iloc[0,38]
    #print("N2756= ",N2756)
    
    # Correct value of N2762
    N2762g = gold.iloc[0,39]
    #print("N2762= ",N2762)

    # Correct value of N2767
    N2767g = gold.iloc[0,40]
    #print("N2767= ",N2767)

    # Correct value of N2768
    N2768g = gold.iloc[0,41]
    #print("N2768= ",N2768)

    # Correct value of N2779
    N2779g = gold.iloc[0,42]
    #print("N2779= ",N2779)

    # Correct value of N2780
    N2780g = gold.iloc[0,43]   
    #print("N2780= ",N2780)

    # Correct value of N2781
    N2781g = gold.iloc[0,44]
    #print("N2781= ",N2781)

    # Correct value of N2782
    N2782g = gold.iloc[0,45]
    #print("N2782= ",N2782)

    # Correct value of N2783
    N2783g = gold.iloc[0,46]
    #print("N2783= ",N2783)    
    
    # Correct value of N2784
    N2784g = gold.iloc[0,47]
    #print("N2784= ",N2784)

    # Correct value of N2785
    N2785g = gold.iloc[0,48]
    #print("N2785= ",N2785)

    # Correct value of N2786
    N2786g = gold.iloc[0,49]
    #print("N2786= ",N2786)

    # Correct value of N2787
    N2787g = gold.iloc[0,50]
    #print("N2787= ",N2787)
    
    # Correct value of N2811
    N2811g = gold.iloc[0,51]
    #print("N2811= ",N2811)

    # Correct value of N2886
    N2886g = gold.iloc[0,52]
    #print("N2886= ",N2886)
 
    # Correct value of N2887
    N2887g = gold.iloc[0,53]      
    #print("N2887= ",N2887)

    # Correct value of N2888
    N2888g = gold.iloc[0,54]
    #print("N2888= ",N2888)    
    
    # Correct value of N2889
    N2889g = gold.iloc[0,55]
    #print("N2889= ",N2889)

    # Correct value of N2890
    N2890g = gold.iloc[0,56]
    #print("N2890= ",N2890)

    # Correct value of N2891
    N2891g = gold.iloc[0,57]
    #print("N2891= ",N2891)

    # Correct value of N2892
    N2892g = gold.iloc[0,58]
    #print("N2892= ",N2892)
    
    # Correct value of N2899
    N2899g = gold.iloc[0,59]
    #print("N2899= ",N2899)

#---------------------------------------------------------------------------------
    #appending all values in order to form a row
    rows.append(time_in)
    rows.append(Node)
# Input columns    
    rows.append(N1)
    rows.append(N4)
    rows.append(N7)
    rows.append(N10)
    rows.append(N13)
    rows.append(N16)
    rows.append(N19)
    rows.append(N22)
    rows.append(N25)
    rows.append(N28)
    rows.append(N31)
    rows.append(N34)
    rows.append(N37)
    rows.append(N40)
    rows.append(N43)
    rows.append(N46)
    rows.append(N49)
    rows.append(N53)
    rows.append(N56)
    rows.append(N60)
    rows.append(N63)
    rows.append(N66)	
    rows.append(N69)
    rows.append(N72)
    rows.append(N76)
    rows.append(N79)
    rows.append(N82)
    rows.append(N85)
    rows.append(N88)
    rows.append(N91)
    rows.append(N94)
    rows.append(N99)
    rows.append(N104)
#Golden rows
    rows.append(N2753g)
    rows.append(N2754g)
    rows.append(N2755g)
    rows.append(N2756g)
    rows.append(N2762g)
    rows.append(N2767g)
    rows.append(N2768g)
    rows.append(N2779g)
    rows.append(N2780g)
    rows.append(N2781g)
    rows.append(N2782g)
    rows.append(N2783g)
    rows.append(N2784g)
    rows.append(N2785g)
    rows.append(N2786g) 
    rows.append(N2787g)
    rows.append(N2811g)    
    rows.append(N2886g)
    rows.append(N2887g)
    rows.append(N2888g)
    rows.append(N2889g)
    rows.append(N2890g)
    rows.append(N2891g)
    rows.append(N2892g)
    rows.append(N2899g)    

#FAULTY OUTPUT COLUMNS    
    rows.append(N2753)
    rows.append(N2754)
    rows.append(N2755)
    rows.append(N2756)
    rows.append(N2762)
    rows.append(N2767)
    rows.append(N2768)
    rows.append(N2779)
    rows.append(N2780)
    rows.append(N2781)
    rows.append(N2782)
    rows.append(N2783)
    rows.append(N2784)
    rows.append(N2785)
    rows.append(N2786) 
    rows.append(N2787)
    rows.append(N2811)    
    rows.append(N2886)
    rows.append(N2887)
    rows.append(N2888)
    rows.append(N2889)
    rows.append(N2890)
    rows.append(N2891)
    rows.append(N2892)
    rows.append(N2899)

    #print(rows)
    final_compare = final_compare.append(pd.Series(rows, index = ["Clk", "Node", "N1", "N4", "N7", "N10", "N13", "N16", "N19", "N22", "N25", "N28", "N31", "N34", "N37", "N40", "N43", "N46", "N49", "N53", "N56", "N60", "N63", "N66", "N69", "N72", "N76", "N79", "N82", "N85", "N88", "N91", "N94", "N99", "N104", "N2753", "N2754", "N2755", "N2756", "N2762", "N2767", "N2768", "N2779", "N2780", "N2781", "N2782", "N2783", "N2784", "N2785", "N2786", "N2787", "N2811", "N2886", "N2887", "N2888", "N2889", "N2890", "N2891", "N2892", "N2899", "N2753g", "N2754g", "N2755g", "N2756g", "N2762g", "N2767g", "N2768g", "N2779g", "N2780g", "N2781g", "N2782g", "N2783g", "N2784g", "N2785g", "N2786g", "N2787g", "N2811g", "N2886g", "N2887g", "N2888g", "N2889g", "N2890g", "N2891g", "N2892g", "N2899g"]), ignore_index=True)
##---------------------------------------------------------------------------------
#print(final_compare)

N2753_Comp = pd.to_numeric(final_compare['N2753']) != pd.to_numeric(final_compare['N2753g'])
N2753_Comp = N2753_Comp.astype(int)

N2754_Comp = pd.to_numeric(final_compare['N2754']) != pd.to_numeric(final_compare['N2754g'])
N2754_Comp = N2754_Comp.astype(int)

N2755_Comp = pd.to_numeric(final_compare['N2755']) != pd.to_numeric(final_compare['N2755g'])
N2755_Comp = N2755_Comp.astype(int)

N2756_Comp = pd.to_numeric(final_compare['N2756']) != pd.to_numeric(final_compare['N2756g'])
N2756_Comp = N2756_Comp.astype(int)

N2762_Comp = pd.to_numeric(final_compare['N2762']) != pd.to_numeric(final_compare['N2762g'])
N2762_Comp = N2762_Comp.astype(int)

N2767_Comp = pd.to_numeric(final_compare['N2767']) != pd.to_numeric(final_compare['N2767g'])
N2767_Comp = N2767_Comp.astype(int)

N2768_Comp = pd.to_numeric(final_compare['N2768']) != pd.to_numeric(final_compare['N2768g'])
N2768_Comp = N2768_Comp.astype(int)

N2779_Comp = pd.to_numeric(final_compare['N2779']) != pd.to_numeric(final_compare['N2779g'])
N2779_Comp = N2779_Comp.astype(int)

N2780_Comp = pd.to_numeric(final_compare['N2780']) != pd.to_numeric(final_compare['N2780g'])
N2780_Comp = N2780_Comp.astype(int)

N2781_Comp = pd.to_numeric(final_compare['N2781']) != pd.to_numeric(final_compare['N2781g'])
N2781_Comp = N2781_Comp.astype(int)

N2782_Comp = pd.to_numeric(final_compare['N2782']) != pd.to_numeric(final_compare['N2782g'])
N2782_Comp = N2782_Comp.astype(int)

N2783_Comp = pd.to_numeric(final_compare['N2783']) != pd.to_numeric(final_compare['N2783g'])
N2783_Comp = N2783_Comp.astype(int)

N2784_Comp = pd.to_numeric(final_compare['N2784']) != pd.to_numeric(final_compare['N2784g'])
N2784_Comp = N2784_Comp.astype(int)

N2785_Comp = pd.to_numeric(final_compare['N2785']) != pd.to_numeric(final_compare['N2785g'])
N2785_Comp = N2785_Comp.astype(int)

N2786_Comp = pd.to_numeric(final_compare['N2786']) != pd.to_numeric(final_compare['N2786g'])
N2786_Comp = N2786_Comp.astype(int)

N2787_Comp = pd.to_numeric(final_compare['N2787']) != pd.to_numeric(final_compare['N2787g'])
N2787_Comp = N2787_Comp.astype(int)

N2811_Comp = pd.to_numeric(final_compare['N2811']) != pd.to_numeric(final_compare['N2811g'])
N2811_Comp = N2811_Comp.astype(int)

N2886_Comp = pd.to_numeric(final_compare['N2886']) != pd.to_numeric(final_compare['N2886g'])
N2886_Comp = N2886_Comp.astype(int)

N2887_Comp = pd.to_numeric(final_compare['N2887']) != pd.to_numeric(final_compare['N2887g'])
N2887_Comp = N2887_Comp.astype(int)

N2888_Comp = pd.to_numeric(final_compare['N2888']) != pd.to_numeric(final_compare['N2888g'])
N2888_Comp = N2888_Comp.astype(int)

N2889_Comp = pd.to_numeric(final_compare['N2889']) != pd.to_numeric(final_compare['N2889g'])
N2889_Comp = N2889_Comp.astype(int)

N2890_Comp = pd.to_numeric(final_compare['N2890']) != pd.to_numeric(final_compare['N2890g'])
N2890_Comp = N2890_Comp.astype(int)

N2891_Comp = pd.to_numeric(final_compare['N2891']) != pd.to_numeric(final_compare['N2891g'])
N2891_Comp = N2891_Comp.astype(int)

N2892_Comp = pd.to_numeric(final_compare['N2892']) != pd.to_numeric(final_compare['N2892g'])
N2892_Comp = N2892_Comp.astype(int)

N2899_Comp = pd.to_numeric(final_compare['N2899']) != pd.to_numeric(final_compare['N2899g'])
N2899_Comp = N2899_Comp.astype(int)

final_compare = final_compare.assign(N2753_Comp = N2753_Comp.values)
final_compare = final_compare.assign(N2754_Comp = N2754_Comp.values)
final_compare = final_compare.assign(N2755_Comp = N2755_Comp.values)
final_compare = final_compare.assign(N2756_Comp = N2756_Comp.values)
final_compare = final_compare.assign(N2762_Comp = N2762_Comp.values)
final_compare = final_compare.assign(N2767_Comp = N2767_Comp.values)
final_compare = final_compare.assign(N2768_Comp = N2768_Comp.values)
final_compare = final_compare.assign(N2779_Comp = N2779_Comp.values)
final_compare = final_compare.assign(N2780_Comp = N2780_Comp.values)
final_compare = final_compare.assign(N2781_Comp = N2781_Comp.values)
final_compare = final_compare.assign(N2782_Comp = N2782_Comp.values)
final_compare = final_compare.assign(N2783_Comp = N2783_Comp.values)
final_compare = final_compare.assign(N2784_Comp = N2784_Comp.values)
final_compare = final_compare.assign(N2785_Comp = N2785_Comp.values)
final_compare = final_compare.assign(N2786_Comp = N2786_Comp.values)
final_compare = final_compare.assign(N2787_Comp = N2787_Comp.values)
final_compare = final_compare.assign(N2811_Comp = N2811_Comp.values)
final_compare = final_compare.assign(N2886_Comp = N2886_Comp.values)
final_compare = final_compare.assign(N2887_Comp = N2887_Comp.values)
final_compare = final_compare.assign(N2888_Comp = N2888_Comp.values)
final_compare = final_compare.assign(N2889_Comp = N2889_Comp.values)
final_compare = final_compare.assign(N2890_Comp = N2890_Comp.values)
final_compare = final_compare.assign(N2891_Comp = N2891_Comp.values)
final_compare = final_compare.assign(N2892_Comp = N2892_Comp.values)
final_compare = final_compare.assign(N2899_Comp = N2899_Comp.values)


final_compare["M/S"] = final_compare["N2753_Comp"] + final_compare["N2754_Comp"] + final_compare["N2755_Comp"] + final_compare["N2756_Comp"] + final_compare["N2762_Comp"] + final_compare["N2767_Comp"] + final_compare["N2768_Comp"] + final_compare["N2779_Comp"] + final_compare["N2781_Comp"] + final_compare["N2780_Comp"] + final_compare["N2782_Comp"] + final_compare["N2783_Comp"] + final_compare["N2784_Comp"] + final_compare["N2785_Comp"] + final_compare["N2786_Comp"] + final_compare["N2787_Comp"] + final_compare["N2811_Comp"] + final_compare["N2886_Comp"] + final_compare["N2887_Comp"] + final_compare["N2888_Comp"] + final_compare["N2889_Comp"] + final_compare["N2890_Comp"] + final_compare["N2891_Comp"] + final_compare["N2892_Comp"] + final_compare["N2899_Comp"]  
final_compare.index.rename('Sr.No.', inplace=True)
final_compare.to_csv("compare_c1908.csv")

# final_compare = final_compare.loc[final_compare['M/S'] == 2]
# #print(final_compare)
# #Cri_Node = final_compare.iloc[:,1]
# #print(Cri_Node)
# #Multiple = final_compare.iloc[:,11]
# #print(Multiple)
# #final_compare = final_compare.assign(Multiple=Multiple.values)
# #final_compare = final_compare.assign(Cri_Node=Cri_Node.values)
# final_compare.to_csv("Critical.csv")
