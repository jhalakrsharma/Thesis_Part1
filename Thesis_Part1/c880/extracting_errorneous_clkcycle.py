import pandas as pd
import os
import csv
import subprocess
import random
import glob

final_compare = pd.DataFrame(columns = ["Clk", "Node", "N1", "N8", "N13", "N17", "N26", "N29", "N36", "N42", "N51", "N55", "N59", "N68", "N72", "N73", "N74", "N75", "N80", "N85", "N86", "N87", "N88", "N89", "N90", "N91", "N96", "N101", "N106", "N111", "N116", "N121", "N126", "N130", "N135", "N138", "N143", "N146", "N149", "N152", "N153", "N156", "N159", "N165", "N171", "N177", "N183", "N189", "N195", "N201", "N207", "N210", "N219", "N228", "N237", "N246", "N255", "N259", "N260", "N261", "N267", "N268", "N388", "N389", "N390", "N391", "N418", "N419", "N420", "N421", "N422", "N423", "N446", "N447", "N448", "N449", "N450", "N767", "N768", "N850", "N863", "N864", "N865", "N866", "N874", "N878", "N879", "N880", "N388g", "N389g", "N390g", "N391g", "N418g", "N419g", "N420g", "N421g", "N422g", "N423g", "N446g", "N447g", "N448g", "N449g", "N450g", "N767g", "N768g", "N850g", "N863g", "N864g", "N865g", "N866g", "N874g", "N878g", "N879g", "N880g"])

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
#-----------------------------------------------------------------------------------
    # Reading the line previous to the line when error was enabled to extract inputs
    df = pd.read_csv(faulty_csv)
    # Previous line
    df = df.loc[df['Clk'] == time_in]
    #print(df)
    
    #extractting the input where enable is 1.

    N1 = df.iloc[0,1]
    N8 = df.iloc[0,2]
    N13= df.iloc[0,3]
    N17= df.iloc[0,4]
    N26= df.iloc[0,5]
    N29= df.iloc[0,6]
    N36= df.iloc[0,7]
    N42= df.iloc[0,8]
    N51= df.iloc[0,9]
    N55= df.iloc[0,10]
    N59= df.iloc[0,11]
    N68= df.iloc[0,12]
    N72= df.iloc[0,13]
    N73= df.iloc[0,14]
    N74= df.iloc[0,15]
    N75= df.iloc[0,16]
    N80= df.iloc[0,17]
    N85= df.iloc[0,18]
    N86= df.iloc[0,19]
    N87= df.iloc[0,20]
    N88= df.iloc[0,21]
    N89= df.iloc[0,22]
    N90= df.iloc[0,23]
    N91= df.iloc[0,24]
    N96= df.iloc[0,25]
    N101= df.iloc[0,26]
    N106= df.iloc[0,27]
    N111= df.iloc[0,28]
    N116= df.iloc[0,29]
    N121= df.iloc[0,30]
    N126= df.iloc[0,31]
    N130= df.iloc[0,32]
    N135= df.iloc[0,33]
    N138= df.iloc[0,34]
    N143= df.iloc[0,35]
    N146= df.iloc[0,36]
    N149= df.iloc[0,37]
    N152= df.iloc[0,38]
    N153= df.iloc[0,39]
    N156= df.iloc[0,40]
    N159= df.iloc[0,41]
    N165= df.iloc[0,42]
    N171= df.iloc[0,43]
    N177= df.iloc[0,44]
    N183= df.iloc[0,45]
    N189= df.iloc[0,46]
    N195= df.iloc[0,47]
    N201= df.iloc[0,48]
    N207= df.iloc[0,49]
    N210= df.iloc[0,50]
    N219= df.iloc[0,51]
    N228= df.iloc[0,52]
    N237= df.iloc[0,53]
    N246= df.iloc[0,54]
    N255= df.iloc[0,55]
    N259= df.iloc[0,56]
    N260= df.iloc[0,57]
    N261= df.iloc[0,58]
    N267= df.iloc[0,59]
    N268= df.iloc[0,60]
#--------------------------------------------------------------------------------
## Extracting faulty output values
    ff = pd.read_csv(faulty_csv)

    # Same line at which error was enabled
    faulty = ff.loc[ff['Clk'] == time_outf]
    #print(faulty)

    N388 = faulty.iloc[0,62]
    N389 = faulty.iloc[0,63]
    N390 = faulty.iloc[0,64]
    N391 = faulty.iloc[0,65]
    N418 = faulty.iloc[0,66]
    N419 = faulty.iloc[0,67]
    N420 = faulty.iloc[0,68]
    N421 = faulty.iloc[0,69]
    N422 = faulty.iloc[0,70]
    N423 = faulty.iloc[0,71]
    N446 = faulty.iloc[0,72]
    N447 = faulty.iloc[0,73]
    N448 = faulty.iloc[0,74]
    N449 = faulty.iloc[0,75]
    N450 = faulty.iloc[0,76]
    N767 = faulty.iloc[0,77]
    N768 = faulty.iloc[0,78]
    N850 = faulty.iloc[0,79]
    N863 = faulty.iloc[0,80]
    N864 = faulty.iloc[0,81]
    N865 = faulty.iloc[0,82]
    N866 = faulty.iloc[0,83]
    N874 = faulty.iloc[0,84]
    N878 = faulty.iloc[0,85]
    N879 = faulty.iloc[0,86]
    N880 = faulty.iloc[0,87]
#---------------------------------------------------------------------------------
    # Reading the golden output to extract correct value output
    cf = pd.read_csv('golden_c880_iverilog_py.csv')

    # Same line at which error was enabled
    gold = cf.loc[cf['Clk'] == time_outf]
    #print("Golden outputline",gold)

    N388g = gold.iloc[0,62]
    N389g = gold.iloc[0,63]
    N390g = gold.iloc[0,64]
    N391g = gold.iloc[0,65]
    N418g = gold.iloc[0,66]
    N419g = gold.iloc[0,67]
    N420g = gold.iloc[0,68]
    N421g = gold.iloc[0,69]
    N422g = gold.iloc[0,70]
    N423g = gold.iloc[0,71]
    N446g = gold.iloc[0,72]
    N447g = gold.iloc[0,73]
    N448g = gold.iloc[0,74]
    N449g = gold.iloc[0,75]
    N450g = gold.iloc[0,76]
    N767g = gold.iloc[0,77]
    N768g = gold.iloc[0,78]
    N850g = gold.iloc[0,79]
    N863g = gold.iloc[0,80]
    N864g = gold.iloc[0,81]
    N865g = gold.iloc[0,82]
    N866g = gold.iloc[0,83]
    N874g = gold.iloc[0,84]
    N878g = gold.iloc[0,85]
    N879g = gold.iloc[0,86]
    N880g = gold.iloc[0,87]
#---------------------------------------------------------------------------------
    #appending all values in order to form a row

    rows.append(time_in)
    rows.append(Node)
    rows.append(N1)
    rows.append(N8)
    rows.append(N13)
    rows.append(N17)
    rows.append(N26)
    rows.append(N29)
    rows.append(N36)
    rows.append(N42)
    rows.append(N51)
    rows.append(N55)
    rows.append(N59)
    rows.append(N68)
    rows.append(N72)
    rows.append(N73)
    rows.append(N74)
    rows.append(N75)
    rows.append(N80)
    rows.append(N85)
    rows.append(N86)
    rows.append(N87)
    rows.append(N88)
    rows.append(N89)
    rows.append(N90)
    rows.append(N91)
    rows.append(N96)
    rows.append(N101)
    rows.append(N106)
    rows.append(N111)
    rows.append(N116)
    rows.append(N121)
    rows.append(N126)
    rows.append(N130)
    rows.append(N135)
    rows.append(N138)
    rows.append(N143)
    rows.append(N146)
    rows.append(N149)
    rows.append(N152)
    rows.append(N153)
    rows.append(N156)
    rows.append(N159)
    rows.append(N165)
    rows.append(N171)
    rows.append(N177)
    rows.append(N183)
    rows.append(N189)
    rows.append(N195)
    rows.append(N201)
    rows.append(N207)
    rows.append(N210)
    rows.append(N219)
    rows.append(N228)
    rows.append(N237)
    rows.append(N246)
    rows.append(N255)
    rows.append(N259)
    rows.append(N260)
    rows.append(N261)
    rows.append(N267)
    rows.append(N268)

#output rows append (faulty) 
    rows.append(N388)
    rows.append(N389)
    rows.append(N390)
    rows.append(N391)
    rows.append(N418)
    rows.append(N419)
    rows.append(N420)
    rows.append(N421)
    rows.append(N422)
    rows.append(N423)
    rows.append(N446)
    rows.append(N447)
    rows.append(N448)
    rows.append(N449)
    rows.append(N450)
    rows.append(N767)
    rows.append(N768)
    rows.append(N850)
    rows.append(N863)
    rows.append(N864)
    rows.append(N865)
    rows.append(N866)
    rows.append(N874)
    rows.append(N878)
    rows.append(N879)
    rows.append(N880)

#output rows append (golden)      
    rows.append(N388g)
    rows.append(N389g)
    rows.append(N390g)
    rows.append(N391g)
    rows.append(N418g)
    rows.append(N419g)
    rows.append(N420g)
    rows.append(N421g)
    rows.append(N422g)
    rows.append(N423g)
    rows.append(N446g)
    rows.append(N447g)
    rows.append(N448g)
    rows.append(N449g)
    rows.append(N450g)
    rows.append(N767g)
    rows.append(N768g)
    rows.append(N850g)
    rows.append(N863g)
    rows.append(N864g)
    rows.append(N865g)
    rows.append(N866g)
    rows.append(N874g)
    rows.append(N878g)
    rows.append(N879g)
    rows.append(N880g)
    #print(rows)

    final_compare = final_compare.append(pd.Series(rows, index = ["Clk", "Node", "N1", "N8", "N13", "N17", "N26", "N29", "N36", "N42", "N51", "N55", "N59", "N68", "N72", "N73", "N74", "N75", "N80", "N85", "N86", "N87", "N88", "N89", "N90", "N91", "N96", "N101", "N106", "N111", "N116", "N121", "N126", "N130", "N135", "N138", "N143", "N146", "N149", "N152", "N153", "N156", "N159", "N165", "N171", "N177", "N183", "N189", "N195", "N201", "N207", "N210", "N219", "N228", "N237", "N246", "N255", "N259", "N260", "N261", "N267", "N268", "N388", "N389", "N390", "N391", "N418", "N419", "N420", "N421", "N422", "N423", "N446", "N447", "N448", "N449", "N450", "N767", "N768", "N850", "N863", "N864", "N865", "N866", "N874", "N878", "N879", "N880", "N388g", "N389g", "N390g", "N391g", "N418g", "N419g", "N420g", "N421g", "N422g", "N423g", "N446g", "N447g", "N448g", "N449g", "N450g", "N767g", "N768g", "N850g", "N863g", "N864g", "N865g", "N866g", "N874g", "N878g", "N879g", "N880g"]), ignore_index=True)
##---------------------------------------------------------------------------------
#print(final_compare)

N388_Comp = pd.to_numeric(final_compare['N388']) != pd.to_numeric(final_compare['N388g'])
N388_Comp = N388_Comp.astype(int)

N389_Comp = pd.to_numeric(final_compare['N389']) != pd.to_numeric(final_compare['N389g'])
N389_Comp = N389_Comp.astype(int)

N390_Comp = pd.to_numeric(final_compare['N390']) != pd.to_numeric(final_compare['N390g'])
N390_Comp = N390_Comp.astype(int)

N391_Comp = pd.to_numeric(final_compare['N391']) != pd.to_numeric(final_compare['N391g'])
N391_Comp = N391_Comp.astype(int)

N418_Comp = pd.to_numeric(final_compare['N418']) != pd.to_numeric(final_compare['N418g'])
N418_Comp = N418_Comp.astype(int)

N419_Comp = pd.to_numeric(final_compare['N419']) != pd.to_numeric(final_compare['N419g'])
N419_Comp = N419_Comp.astype(int)

N420_Comp = pd.to_numeric(final_compare['N420']) != pd.to_numeric(final_compare['N420g'])
N420_Comp = N420_Comp.astype(int)

N421_Comp = pd.to_numeric(final_compare['N421']) != pd.to_numeric(final_compare['N421g'])
N421_Comp = N421_Comp.astype(int)

N422_Comp = pd.to_numeric(final_compare['N422']) != pd.to_numeric(final_compare['N422g'])
N422_Comp = N422_Comp.astype(int)

N423_Comp = pd.to_numeric(final_compare['N423']) != pd.to_numeric(final_compare['N423g'])
N423_Comp = N423_Comp.astype(int)

N446_Comp = pd.to_numeric(final_compare['N446']) != pd.to_numeric(final_compare['N446g'])
N446_Comp = N446_Comp.astype(int)

N447_Comp = pd.to_numeric(final_compare['N447']) != pd.to_numeric(final_compare['N447g'])
N447_Comp = N447_Comp.astype(int)

N448_Comp = pd.to_numeric(final_compare['N448']) != pd.to_numeric(final_compare['N448g'])
N448_Comp = N448_Comp.astype(int)

N449_Comp = pd.to_numeric(final_compare['N449']) != pd.to_numeric(final_compare['N449g'])
N449_Comp = N449_Comp.astype(int)

N450_Comp = pd.to_numeric(final_compare['N450']) != pd.to_numeric(final_compare['N450g'])
N450_Comp = N450_Comp.astype(int)

N767_Comp = pd.to_numeric(final_compare['N767']) != pd.to_numeric(final_compare['N767g'])
N767_Comp = N767_Comp.astype(int)

N768_Comp = pd.to_numeric(final_compare['N768']) != pd.to_numeric(final_compare['N768g'])
N768_Comp = N768_Comp.astype(int)

N850_Comp = pd.to_numeric(final_compare['N850']) != pd.to_numeric(final_compare['N850g'])
N850_Comp = N850_Comp.astype(int)

N863_Comp = pd.to_numeric(final_compare['N863']) != pd.to_numeric(final_compare['N863g'])
N863_Comp = N863_Comp.astype(int)

N864_Comp = pd.to_numeric(final_compare['N864']) != pd.to_numeric(final_compare['N864g'])
N864_Comp = N864_Comp.astype(int)

N865_Comp = pd.to_numeric(final_compare['N865']) != pd.to_numeric(final_compare['N865g'])
N865_Comp = N865_Comp.astype(int)

N866_Comp = pd.to_numeric(final_compare['N866']) != pd.to_numeric(final_compare['N866g'])
N866_Comp = N866_Comp.astype(int)

N874_Comp = pd.to_numeric(final_compare['N874']) != pd.to_numeric(final_compare['N874g'])
N874_Comp = N874_Comp.astype(int)

N878_Comp = pd.to_numeric(final_compare['N878']) != pd.to_numeric(final_compare['N878g'])
N878_Comp = N878_Comp.astype(int)

N879_Comp = pd.to_numeric(final_compare['N879']) != pd.to_numeric(final_compare['N879g'])
N879_Comp = N879_Comp.astype(int)

N880_Comp = pd.to_numeric(final_compare['N880']) != pd.to_numeric(final_compare['N880g'])
N880_Comp = N880_Comp.astype(int)

final_compare = final_compare.assign(N388_Comp = N388_Comp.values)
final_compare = final_compare.assign(N389_Comp = N389_Comp.values)
final_compare = final_compare.assign(N390_Comp = N390_Comp.values)
final_compare = final_compare.assign(N391_Comp = N391_Comp.values)
final_compare = final_compare.assign(N418_Comp = N418_Comp.values)
final_compare = final_compare.assign(N419_Comp = N419_Comp.values)
final_compare = final_compare.assign(N420_Comp = N420_Comp.values)
final_compare = final_compare.assign(N421_Comp = N421_Comp.values)
final_compare = final_compare.assign(N422_Comp = N422_Comp.values)
final_compare = final_compare.assign(N423_Comp = N423_Comp.values)
final_compare = final_compare.assign(N446_Comp = N446_Comp.values)
final_compare = final_compare.assign(N447_Comp = N447_Comp.values)
final_compare = final_compare.assign(N448_Comp = N448_Comp.values)
final_compare = final_compare.assign(N449_Comp = N449_Comp.values)
final_compare = final_compare.assign(N450_Comp = N450_Comp.values)
final_compare = final_compare.assign(N767_Comp = N767_Comp.values)
final_compare = final_compare.assign(N768_Comp = N768_Comp.values)
final_compare = final_compare.assign(N850_Comp = N850_Comp.values)
final_compare = final_compare.assign(N863_Comp = N863_Comp.values)
final_compare = final_compare.assign(N864_Comp = N864_Comp.values)
final_compare = final_compare.assign(N865_Comp = N865_Comp.values)
final_compare = final_compare.assign(N866_Comp = N866_Comp.values)
final_compare = final_compare.assign(N874_Comp = N874_Comp.values)
final_compare = final_compare.assign(N878_Comp = N878_Comp.values)
final_compare = final_compare.assign(N879_Comp = N879_Comp.values)
final_compare = final_compare.assign(N880_Comp = N880_Comp.values)

final_compare["M/S"] = final_compare["N388_Comp"] + final_compare["N389_Comp"] + final_compare["N390_Comp"] + final_compare["N391_Comp"] + final_compare["N418_Comp"] + final_compare["N419_Comp"] + final_compare["N420_Comp"] + final_compare["N421_Comp"] + final_compare["N422_Comp"] + final_compare["N423_Comp"] + final_compare["N446_Comp"] + final_compare["N447_Comp"] + final_compare["N448_Comp"] + final_compare["N449_Comp"] + final_compare["N450_Comp"] + final_compare["N767_Comp"] + final_compare["N768_Comp"] + final_compare["N850_Comp"] + final_compare["N863_Comp"] + final_compare["N864_Comp"] + final_compare["N865_Comp"] + final_compare["N866_Comp"] + final_compare["N874_Comp"] + final_compare["N878_Comp"] + final_compare["N879_Comp"] + final_compare["N880_Comp"] 

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
