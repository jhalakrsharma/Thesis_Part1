import pandas as pd
import os
import csv
import subprocess
import random
import glob

#final_compare = pd.DataFrame(columns = ["Clk", "Node", "A", "B", "Cin", "Sum_f", "Cout_f", "Sum_g", "Cout_g"])
final_compare = pd.DataFrame(columns = ["Clk", "Node", "N1", "N13", "N20", "N33", "N41", "N45", "N50", "N58", "N68", "N77", "N87", "N97", "N107", "N116", "N124", "N125", "N128", "N132", "N137", "N143", "N150", "N159", "N169", "N179", "N190", "N200", "N213", "N222", "N223", "N226", "N232", "N238", "N244", "N250", "N257", "N264", "N270", "N274", "N283", "N294", "N303", "N311", "N317", "N322", "N326", "N329", "N330", "N343", "N349", "N350", "N1713", "N1947", "N3195", "N3833", "N3987", "N4028", "N4145", "N4589", "N4667", "N4815", "N4944", "N5002", "N5045", "N5047", "N5078", "N5102", "N5120", "N5121", "N5192", "N5231", "N5360", "N5361", "N1713g", "N1947g", "N3195g", "N3833g", "N3987g", "N4028g", "N4145g", "N4589g", "N4667g", "N4815g", "N4944g", "N5002g", "N5045g", "N5047g", "N5078g", "N5102g", "N5120g", "N5121g", "N5192g", "N5231g", "N5360g", "N5361g"])

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
    N1 = df.iloc[0,1]
    N13 = df.iloc[0,2]
    N20 = df.iloc[0,3]
    N33 = df.iloc[0,4]
    N41 = df.iloc[0,5]
    N45 = df.iloc[0,6]
    N50 = df.iloc[0,7]
    N58 = df.iloc[0,8]
    N68 = df.iloc[0,9]
    N77 = df.iloc[0,10]
    N87 = df.iloc[0,11]
    N97 = df.iloc[0,12]
    N107 = df.iloc[0,13]
    N116 = df.iloc[0,14]
    N124 = df.iloc[0,15]
    N125 = df.iloc[0,16]
    N128 = df.iloc[0,17]
    N132 = df.iloc[0,18]
    N137 = df.iloc[0,19]
    N143 = df.iloc[0,20]
    N150 = df.iloc[0,21]
    N159 = df.iloc[0,22]
    N169 = df.iloc[0,23]
    N179 = df.iloc[0,24]
    N190 = df.iloc[0,25]
    N200 = df.iloc[0,26]
    N213 = df.iloc[0,27]
    N222 = df.iloc[0,28]
    N223 = df.iloc[0,29]
    N226 = df.iloc[0,30]
    N232 = df.iloc[0,31]
    N238 = df.iloc[0,32]
    N244 = df.iloc[0,33]
    N250 = df.iloc[0,34]
    N257 = df.iloc[0,35]
    N264 = df.iloc[0,36]
    N270 = df.iloc[0,37]
    N274 = df.iloc[0,38]
    N283 = df.iloc[0,39]
    N294 = df.iloc[0,40]
    N303 = df.iloc[0,41]
    N311 = df.iloc[0,42]
    N317 = df.iloc[0,43]
    N322 = df.iloc[0,44]
    N326 = df.iloc[0,45]
    N329 = df.iloc[0,46]
    N330 = df.iloc[0,47]
    N343 = df.iloc[0,48]
    N349 = df.iloc[0,49]
    N350 = df.iloc[0,50]
   
#--------------------------------------------------------------------------------
## Extracting faulty output values
    ff = pd.read_csv(faulty_csv)

    # Same line at which error was enabled
    faulty = ff.loc[ff['Clk'] == time_outf]     
    #print(faulty)

    N1713 = faulty.iloc[0,52]
    N1947 = faulty.iloc[0,53]
    N3195 = faulty.iloc[0,54]
    N3833 = faulty.iloc[0,55]
    N3987 = faulty.iloc[0,56]
    N4028 = faulty.iloc[0,57]
    N4145 = faulty.iloc[0,58]
    N4589 = faulty.iloc[0,59]
    N4667 = faulty.iloc[0,60]
    N4815 = faulty.iloc[0,61]
    N4944 = faulty.iloc[0,62]
    N5002 = faulty.iloc[0,63]
    N5045 = faulty.iloc[0,64]
    N5047 = faulty.iloc[0,65]
    N5078 = faulty.iloc[0,66]
    N5102 = faulty.iloc[0,67]
    N5120 = faulty.iloc[0,68]
    N5121 = faulty.iloc[0,69]
    N5192 = faulty.iloc[0,70]
    N5231 = faulty.iloc[0,71]
    N5360 = faulty.iloc[0,72]
    N5361 = faulty.iloc[0,73]

#---------------------------------------------------------------------------------
    # Reading the golden output to extract correct value output
    cf = pd.read_csv('golden_c3540_iverilog_after_change.csv')

    # Same line at which error was enabled
    gold = cf.loc[cf['Clk'] == time_outf]
    #print("Golden outputline",gold)

    N1713g = gold.iloc[0,52]
    N1947g = gold.iloc[0,53]
    N3195g = gold.iloc[0,54]
    N3833g = gold.iloc[0,55]
    N3987g = gold.iloc[0,56]
    N4028g = gold.iloc[0,57]
    N4145g = gold.iloc[0,58]
    N4589g = gold.iloc[0,59]
    N4667g = gold.iloc[0,60]
    N4815g = gold.iloc[0,61]
    N4944g = gold.iloc[0,62]
    N5002g = gold.iloc[0,63]
    N5045g = gold.iloc[0,64]
    N5047g = gold.iloc[0,65]
    N5078g = gold.iloc[0,66]
    N5102g = gold.iloc[0,67]
    N5120g = gold.iloc[0,68]
    N5121g = gold.iloc[0,69]
    N5192g = gold.iloc[0,70]
    N5231g = gold.iloc[0,71]
    N5360g = gold.iloc[0,72]
    N5361g = gold.iloc[0,73]

#---------------------------------------------------------------------------------
    #appending all values in order to form a row
    rows.append(time_in)
    rows.append(Node)
# Input columns    
    rows.append(N1)
    rows.append(N13)
    rows.append(N20)
    rows.append(N33)
    rows.append(N41)
    rows.append(N45)
    rows.append(N50)
    rows.append(N58)
    rows.append(N68)
    rows.append(N77)
    rows.append(N87)
    rows.append(N97)
    rows.append(N107)
    rows.append(N116)
    rows.append(N124)
    rows.append(N125)
    rows.append(N128)
    rows.append(N132)
    rows.append(N137)
    rows.append(N143)
    rows.append(N150)
    rows.append(N159)
    rows.append(N169)
    rows.append(N179)
    rows.append(N190)
    rows.append(N200)
    rows.append(N213)
    rows.append(N222)
    rows.append(N223)
    rows.append(N226)
    rows.append(N232)
    rows.append(N238)
    rows.append(N244)
    rows.append(N250)
    rows.append(N257)
    rows.append(N264)
    rows.append(N270)
    rows.append(N274)
    rows.append(N283)
    rows.append(N294)
    rows.append(N303)
    rows.append(N311)
    rows.append(N317)
    rows.append(N322)
    rows.append(N326)
    rows.append(N329)
    rows.append(N330)
    rows.append(N343)
    rows.append(N349)
    rows.append(N350)

    #faulty outputs
    rows.append(N1713)
    rows.append(N1947)
    rows.append(N3195)
    rows.append(N3833)
    rows.append(N3987)
    rows.append(N4028)
    rows.append(N4145)
    rows.append(N4589)
    rows.append(N4667)
    rows.append(N4815)
    rows.append(N4944)
    rows.append(N5002)
    rows.append(N5045)
    rows.append(N5047)
    rows.append(N5078)
    rows.append(N5102)
    rows.append(N5120)
    rows.append(N5121)
    rows.append(N5192)
    rows.append(N5231)
    rows.append(N5360)
    rows.append(N5361)

    #golden outputs
    rows.append(N1713g)
    rows.append(N1947g)
    rows.append(N3195g)
    rows.append(N3833g)
    rows.append(N3987g)
    rows.append(N4028g)
    rows.append(N4145g)
    rows.append(N4589g)
    rows.append(N4667g)
    rows.append(N4815g)
    rows.append(N4944g)
    rows.append(N5002g)
    rows.append(N5045g)
    rows.append(N5047g)
    rows.append(N5078g)
    rows.append(N5102g)
    rows.append(N5120g)
    rows.append(N5121g)
    rows.append(N5192g)
    rows.append(N5231g)
    rows.append(N5360g)
    rows.append(N5361g)

    #print(rows)
    final_compare = final_compare.append(pd.Series(rows, index = ["Clk", "Node", "N1", "N13", "N20", "N33", "N41", "N45", "N50", "N58", "N68", "N77", "N87", "N97", "N107", "N116", "N124", "N125", "N128", "N132", "N137", "N143", "N150", "N159", "N169", "N179", "N190", "N200", "N213", "N222", "N223", "N226", "N232", "N238", "N244", "N250", "N257", "N264", "N270", "N274", "N283", "N294", "N303", "N311", "N317", "N322", "N326", "N329", "N330", "N343", "N349", "N350", "N1713", "N1947", "N3195", "N3833", "N3987", "N4028", "N4145", "N4589", "N4667", "N4815", "N4944", "N5002", "N5045", "N5047", "N5078", "N5102", "N5120", "N5121", "N5192", "N5231", "N5360", "N5361", "N1713g", "N1947g", "N3195g", "N3833g", "N3987g", "N4028g", "N4145g", "N4589g", "N4667g", "N4815g", "N4944g", "N5002g", "N5045g", "N5047g", "N5078g", "N5102g", "N5120g", "N5121g", "N5192g", "N5231g", "N5360g", "N5361g"]), ignore_index=True)
##---------------------------------------------------------------------------------
#print(final_compare)
N1713_Comp = pd.to_numeric(final_compare['N1713']) != pd.to_numeric(final_compare['N1713g'])
N1713_Comp = N1713_Comp.astype(int)
N1947_Comp = pd.to_numeric(final_compare['N1947']) != pd.to_numeric(final_compare['N1947g'])
N1947_Comp = N1947_Comp.astype(int)
N3195_Comp = pd.to_numeric(final_compare['N3195']) != pd.to_numeric(final_compare['N3195g'])
N3195_Comp = N3195_Comp.astype(int)
N3833_Comp = pd.to_numeric(final_compare['N3833']) != pd.to_numeric(final_compare['N3833g'])
N3833_Comp = N3833_Comp.astype(int)
N3987_Comp = pd.to_numeric(final_compare['N3987']) != pd.to_numeric(final_compare['N3987g'])
N3987_Comp = N3987_Comp.astype(int)
N4028_Comp = pd.to_numeric(final_compare['N4028']) != pd.to_numeric(final_compare['N4028g'])
N4028_Comp = N4028_Comp.astype(int)
N4145_Comp = pd.to_numeric(final_compare['N4145']) != pd.to_numeric(final_compare['N4145g'])
N4145_Comp = N4145_Comp.astype(int)
N4589_Comp = pd.to_numeric(final_compare['N4589']) != pd.to_numeric(final_compare['N4589g'])
N4589_Comp = N4589_Comp.astype(int)
N4667_Comp = pd.to_numeric(final_compare['N4667']) != pd.to_numeric(final_compare['N4667g'])
N4667_Comp = N4667_Comp.astype(int)
N4815_Comp = pd.to_numeric(final_compare['N4815']) != pd.to_numeric(final_compare['N4815g'])
N4815_Comp = N4815_Comp.astype(int)
N4944_Comp = pd.to_numeric(final_compare['N4944']) != pd.to_numeric(final_compare['N4944g'])
N4944_Comp = N4944_Comp.astype(int)
N5002_Comp = pd.to_numeric(final_compare['N5002']) != pd.to_numeric(final_compare['N5002g'])
N5002_Comp = N5002_Comp.astype(int)
N5045_Comp = pd.to_numeric(final_compare['N5045']) != pd.to_numeric(final_compare['N5045g'])
N5045_Comp = N5045_Comp.astype(int)
N5047_Comp = pd.to_numeric(final_compare['N5047']) != pd.to_numeric(final_compare['N5047g'])
N5047_Comp = N5047_Comp.astype(int)
N5078_Comp = pd.to_numeric(final_compare['N5078']) != pd.to_numeric(final_compare['N5078g'])
N5078_Comp = N5078_Comp.astype(int)
N5102_Comp = pd.to_numeric(final_compare['N5102']) != pd.to_numeric(final_compare['N5102g'])
N5102_Comp = N5102_Comp.astype(int)
N5120_Comp = pd.to_numeric(final_compare['N5120']) != pd.to_numeric(final_compare['N5120g'])
N5120_Comp = N5120_Comp.astype(int)
N5121_Comp = pd.to_numeric(final_compare['N5121']) != pd.to_numeric(final_compare['N5121g'])
N5121_Comp = N5121_Comp.astype(int)
N5192_Comp = pd.to_numeric(final_compare['N5192']) != pd.to_numeric(final_compare['N5192g'])
N5192_Comp = N5192_Comp.astype(int)
N5231_Comp = pd.to_numeric(final_compare['N5231']) != pd.to_numeric(final_compare['N5231g'])
N5231_Comp = N5231_Comp.astype(int)
N5360_Comp = pd.to_numeric(final_compare['N5360']) != pd.to_numeric(final_compare['N5360g'])
N5360_Comp = N5360_Comp.astype(int)
N5361_Comp = pd.to_numeric(final_compare['N5361']) != pd.to_numeric(final_compare['N5361g'])
N5361_Comp = N5361_Comp.astype(int)


final_compare = final_compare.assign(N1713_Comp = N1713_Comp.values)
final_compare = final_compare.assign(N1947_Comp = N1947_Comp.values)
final_compare = final_compare.assign(N3195_Comp = N3195_Comp.values)
final_compare = final_compare.assign(N3833_Comp = N3833_Comp.values)
final_compare = final_compare.assign(N3987_Comp = N3987_Comp.values)
final_compare = final_compare.assign(N4028_Comp = N4028_Comp.values)
final_compare = final_compare.assign(N4145_Comp = N4145_Comp.values)
final_compare = final_compare.assign(N4589_Comp = N4589_Comp.values)
final_compare = final_compare.assign(N4667_Comp = N4667_Comp.values)
final_compare = final_compare.assign(N4815_Comp = N4815_Comp.values)
final_compare = final_compare.assign(N4944_Comp = N4944_Comp.values)
final_compare = final_compare.assign(N5002_Comp = N5002_Comp.values)
final_compare = final_compare.assign(N5045_Comp = N5045_Comp.values)
final_compare = final_compare.assign(N5047_Comp = N5047_Comp.values)
final_compare = final_compare.assign(N5078_Comp = N5078_Comp.values)
final_compare = final_compare.assign(N5102_Comp = N5102_Comp.values)
final_compare = final_compare.assign(N5120_Comp = N5120_Comp.values)
final_compare = final_compare.assign(N5121_Comp = N5121_Comp.values)
final_compare = final_compare.assign(N5192_Comp = N5192_Comp.values)
final_compare = final_compare.assign(N5231_Comp = N5231_Comp.values)
final_compare = final_compare.assign(N5360_Comp = N5360_Comp.values)
final_compare = final_compare.assign(N5361_Comp = N5361_Comp.values)


final_compare["M/S"] = final_compare["N1713_Comp"] + final_compare["N1947_Comp"] + final_compare["N3195_Comp"] + final_compare["N3833_Comp"] + final_compare["N3987_Comp"] + final_compare["N4028_Comp"] + final_compare["N4145_Comp"] + final_compare["N4589_Comp"] + final_compare["N4667_Comp"] + final_compare["N4815_Comp"] + final_compare["N4944_Comp"] + final_compare["N5002_Comp"] + final_compare["N5045_Comp"] + final_compare["N5047_Comp"] + final_compare["N5078_Comp"] + final_compare["N5102_Comp"] + final_compare["N5120_Comp"] + final_compare["N5121_Comp"] + final_compare["N5192_Comp"] + final_compare["N5231_Comp"] + final_compare["N5360_Comp"] + final_compare["N5361_Comp"]
final_compare.index.rename('Sr.No.', inplace=True)
final_compare.to_csv("compare_c3540.csv")

# final_compare = final_compare.loc[final_compare['M/S'] == 2]
# #print(final_compare)
# #Cri_Node = final_compare.iloc[:,1]
# #print(Cri_Node)
# #Multiple = final_compare.iloc[:,11]
# #print(Multiple)
# #final_compare = final_compare.assign(Multiple=Multiple.values)
# #final_compare = final_compare.assign(Cri_Node=Cri_Node.values)
# final_compare.to_csv("Critical.csv")
