import pandas as pd
import os
import csv
import subprocess
import random
import glob

final_compare = pd.DataFrame(columns = ["Clk", "Node", "N1", "N18", "N35", "N52", "N69", "N86", "N103", "N120", "N137", "N154", "N171", "N188", "N205", "N222", "N239", "N256", "N273", "N290", "N307", "N324", "N341", "N358", "N375", "N392", "N409", "N426", "N443", "N460", "N477", "N494", "N511", "N528", "N545", "N1581", "N1901", "N2223", "N2548", "N2877", "N3211", "N3552", "N3895", "N4241", "N4591", "N4946", "N5308", "N5672", "N5971", "N6123", "N6150", "N6160", "N6170", "N6180", "N6190", "N6200", "N6210", "N6220", "N6230", "N6240", "N6250", "N6260", "N6270", "N6280", "N6287", "N6288", "N545g", "N1581g", "N1901g", "N2223g", "N2548g", "N2877g", "N3211g", "N3552g", "N3895g", "N4241g", "N4591g", "N4946g", "N5308g", "N5672g", "N5971g", "N6123g", "N6150g", "N6160g", "N6170g", "N6180g", "N6190g", "N6200g", "N6210g", "N6220g", "N6230g", "N6240g", "N6250g", "N6260g", "N6270g", "N6280g", "N6287g", "N6288g"])

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
    time_in = time_en - 2;
    time_outf = time_en + 2;
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
                            
    # Value of input N18
    N18 = df.iloc[0,2]
    #print("N18   = ",N18)

    # Value of input N35
    N35 = df.iloc[0,3]
    #print("N35   =",N35)
    
    # Value of input N52
    N52 = df.iloc[0,4]
    #print("N52  = ",N52)

    # Value of input N69
    N69 = df.iloc[0,5]
    #print("N69  = ",N69)

    # Value of input N86
    N86 = df.iloc[0,6]
    #print("N86  =",N86)

    # Value of input N103
    N103 = df.iloc[0,7]
    #print("N103  = ",N103)

    # Value of input N120
    N120 = df.iloc[0,8]
    #print("N120  = ",N120) 

    # Value of input N137
    N137 = df.iloc[0,9]
    #print("N137  =",N137)
    
    # Value of input N154
    N154 = df.iloc[0,10]
    #print("N154  = ",N154)

    # Value of input N171
    N171 = df.iloc[0,11]
    #print("N171  = ",N171)

    # Value of input N188
    N188 = df.iloc[0,12]
    #print("N188  =",N188)
    
    # Value of input N205
    N205 = df.iloc[0,13]
    #print("N205  = ",N205)

    # Value of input N222
    N222 = df.iloc[0,14]
    #print("N222  = ",N222)

    # Value of input N239
    N239 = df.iloc[0,15]     
    #print("N239  =",N239)
    
    # Value of input N256
    N256 = df.iloc[0,16]
    #print("N256  = ",N256)

    # Value of input N273
    N273 = df.iloc[0,17]
    #print("N273  = ",N273)

    # Value of input N290
    N290 = df.iloc[0,18]
    #print("N290  =",N290)
    
    # Value of input N307
    N307 = df.iloc[0,19]
    #print("N307  = ",N307)

    # Value of input N324
    N324 = df.iloc[0,20]
    #print("N324  = ",N324)

    # Value of input N341
    N341 = df.iloc[0,21]
    #print("N341  =",N341)
    
    # Value of input N358
    N358 = df.iloc[0,22]
    #print("N358  = ",N358)

    # Value of input N375
    N375 = df.iloc[0,23]    
    #print("N375  = ",N375)

    # Value of input N392
    N392 = df.iloc[0,24]
    #print("N392  =",N392)
           
    # Value of input N409
    N409 = df.iloc[0,25]
    #print("N409  = ",N409)

    # Value of input N426
    N426 = df.iloc[0,26]
    #print("N426 = ",N426)

    # Value of input N443
    N443 = df.iloc[0,27]
    #print("N443 =",N443)
    
    # Value of input N460
    N460 = df.iloc[0,28]
    #print("N460 = ",N460)

    # Value of input N477
    N477 = df.iloc[0,29]
    #print("N477 = ",N477)

    # Value of input N494
    N494 = df.iloc[0,30]
    #print("N494 =",N494)
    
    # Value of input N511
    N511 = df.iloc[0,31]
    #print("N511 = ",N511)

    # Value of input N528
    N528 = df.iloc[0,32]
    #print("N528 =",N528)
   
#--------------------------------------------------------------------------------
## Extracting faulty output values
    ff = pd.read_csv(faulty_csv)

    # Same line at which error was enabled
    faulty = ff.loc[ff['Clk'] == time_outf]     
    #print(faulty)

    # Faulty value of N545
    N545 = faulty.iloc[0,34]
    #print("N545= ",N545)

    # Faulty value of N1581
    N1581 = faulty.iloc[0,35]
    #print("N1581= ",N1581)

    # Faulty value of N1901
    N1901 = faulty.iloc[0,36]
    #print("N1901= ",N1901)

    # Faulty value of N2223
    N2223 = faulty.iloc[0,37]
    #print("N2223= ",N2223)
    
    # Faulty value of N2548
    N2548 = faulty.iloc[0,38]
    #print("N2548= ",N2548)

    # Faulty value of N2877
    N2877 = faulty.iloc[0,39]
    #print("N2877= ",N2877)

    # Faulty value of N3211
    N3211 = faulty.iloc[0,40]
    #print("N3211= ",N3211)

    # Faulty value of N3552
    N3552 = faulty.iloc[0,41]
    #print("N3552= ",N3552)
    
    # Faulty value of N3895
    N3895 = faulty.iloc[0,42]   
    #print("N3895= ",N3895)

    # Faulty value of N4241
    N4241 = faulty.iloc[0,43]
    #print("N4241= ",N4241)

    # Faulty value of N4591
    N4591 = faulty.iloc[0,44]
    #print("N4591= ",N4591)

    # Faulty value of N4946
    N4946 = faulty.iloc[0,45]
    #print("N4946= ",N4946)    
    
    # Faulty value of N5308
    N5308 = faulty.iloc[0,46]
    #print("N5308= ",N5308)

    # Faulty value of N5672
    N5672 = faulty.iloc[0,47]
    #print("N5672= ",N5672)

    # Faulty value of N5971
    N5971 = faulty.iloc[0,48]
    #print("N5971= ",N5971)

    # Faulty value of N6123
    N6123 = faulty.iloc[0,49]
    #print("N6123= ",N6123)
    
    # Faulty value of N6150
    N6150 = faulty.iloc[0,50]
    #print("N6150= ",N6150)

    # Faulty value of N6160
    N6160 = faulty.iloc[0,51]
    #print("N6160= ",N6160)

    # Faulty value of N6170
    N6170 = faulty.iloc[0,52]      
    #print("N6170= ",N6170)

    # Faulty value of N6180
    N6180 = faulty.iloc[0,53]
    #print("N6180= ",N6180)    
    
    # Faulty value of N6190
    N6190 = faulty.iloc[0,54]
    #print("N6190= ",N6190)

    # Faulty value of N6200
    N6200 = faulty.iloc[0,55]
    #print("N6200= ",N6200)

    # Faulty value of N6210
    N6210 = faulty.iloc[0,56]
    #print("N6210= ",N6210)

    # Faulty value of N6220
    N6220 = faulty.iloc[0,57]
    #print("N6220= ",N6220)
    
    # Faulty value of N6230
    N6230 = faulty.iloc[0,58]
    #print("N6230= ",N6230)

    # Faulty value of N6240
    N6240 = faulty.iloc[0,59]
    #print("N6240= ",N6240)

    # Faulty value of N6250
    N6250 = faulty.iloc[0,60]
    #print("N6250= ",N6250)

    # Faulty value of N6260
    N6260 = faulty.iloc[0,61]
    #print("N6260= ",N6260)    
    
    # Faulty value of N6270
    N6270 = faulty.iloc[0,62]       
    #print("N6270= ",N6270)

    # Faulty value of N6280
    N6280 = faulty.iloc[0,63]
    #print("N6280= ",N6280)

    # Faulty value of N6287
    N6287 = faulty.iloc[0,64]
    #print("N6287= ",N6287)

    # Faulty value of N6288
    N6288 = faulty.iloc[0,65]
    #print("N6288= ",N6288)
    
#---------------------------------------------------------------------------------
    # Reading the golden output to extract correct value output
    cf = pd.read_csv('goldenc6288.csv')

    # Same line at which error was enabled
    gold = cf.loc[cf['Clk'] == time_outf]
    #print("Golden outputline",gold)

    
    # Correct value of N545
    N545g = gold.iloc[0,34]
    #print("N545= ",N545)

    # Correct value of N1581
    N1581g = gold.iloc[0,35]
    #print("N1581= ",N1581)

    # Correct value of N1901
    N1901g = gold.iloc[0,36]
    #print("N1901= ",N1901)

    # Correct value of N2223
    N2223g = gold.iloc[0,37]
    #print("N2223= ",N2223)
    
    # Correct value of N2548
    N2548g = gold.iloc[0,38]
    #print("N2548= ",N2548)

    # Correct value of N2877
    N2877g = gold.iloc[0,39]
    #print("N2877= ",N2877)

    # Correct value of N3211
    N3211g = gold.iloc[0,40]
    #print("N3211= ",N3211)

    # Correct value of N3552
    N3552g = gold.iloc[0,41]
    #print("N3552= ",N3552)
    
    # Correct value of N3895
    N3895g = gold.iloc[0,42]   
    #print("N3895= ",N3895)

    # Correct value of N4241
    N4241g = gold.iloc[0,43]
    #print("N4241= ",N4241)

    # Correct value of N4591
    N4591g = gold.iloc[0,44]
    #print("N4591= ",N4591)

    # Correct value of N4946
    N4946g = gold.iloc[0,45]
    #print("N4946= ",N4946)    
    
    # Correct value of N5308
    N5308g = gold.iloc[0,46]
    #print("N5308= ",N5308)

    # Correct value of N5672
    N5672g = gold.iloc[0,47]
    #print("N5672= ",N5672)

    # Correct value of N5971
    N5971g = gold.iloc[0,48]
    #print("N5971= ",N5971)

    # Correct value of N6123
    N6123g = gold.iloc[0,49]
    #print("N6123= ",N6123)
    
    # Correct value of N6150
    N6150g = gold.iloc[0,50]
    #print("N6150= ",N6150)

    # Correct value of N6160
    N6160g = gold.iloc[0,51]
    #print("N6160= ",N6160)

    # Correct value of N6170
    N6170g = gold.iloc[0,52]      
    #print("N6170= ",N6170)

    # Correct value of N6180
    N6180g = gold.iloc[0,53]
    #print("N6180= ",N6180)    
    
    # Correct value of N6190
    N6190g = gold.iloc[0,54]
    #print("N6190= ",N6190)

    # Correct value of N6200
    N6200g = gold.iloc[0,55]
    #print("N6200= ",N6200)

    # Correct value of N6210
    N6210g = gold.iloc[0,56]
    #print("N6210= ",N6210)

    # Correct value of N6220
    N6220g = gold.iloc[0,57]
    #print("N6220= ",N6220)
    
    # Correct value of N6230
    N6230g = gold.iloc[0,58]
    #print("N6230= ",N6230)

    # Correct value of N6240
    N6240g = gold.iloc[0,59]
    #print("N6240= ",N6240)

    # Correct value of N6250
    N6250g = gold.iloc[0,60]
    #print("N6250= ",N6250)

    # Correct value of N6260
    N6260g = gold.iloc[0,61]
    #print("N6260= ",N6260)    
    
    # Correct value of N6270
    N6270g = gold.iloc[0,62]       
    #print("N6270= ",N6270)

    # Correct value of N6280
    N6280g = gold.iloc[0,63]
    #print("N6280= ",N6280)

    # Correct value of N6287
    N6287g = gold.iloc[0,64]
    #print("N6287= ",N6287)

    # Correct value of N6288
    N6288g = gold.iloc[0,65]
    #print("N6288= ",N6288)

#---------------------------------------------------------------------------------
    #appending all values in order to form a row
    rows.append(time_in)
    rows.append(Node)
# Input columns    
    rows.append(N1)
    rows.append(N18)
    rows.append(N35)
    rows.append(N52)
    rows.append(N69)
    rows.append(N86)
    rows.append(N103)
    rows.append(N120)
    rows.append(N137)
    rows.append(N154)
    rows.append(N171)
    rows.append(N188)
    rows.append(N205)
    rows.append(N222)
    rows.append(N239)
    rows.append(N256)
    rows.append(N273)
    rows.append(N290)
    rows.append(N307)
    rows.append(N324)
    rows.append(N341)
    rows.append(N358)
    rows.append(N375)
    rows.append(N392)
    rows.append(N409)
    rows.append(N426)
    rows.append(N443)
    rows.append(N460)
    rows.append(N477)
    rows.append(N494)
    rows.append(N511)
    rows.append(N528)
#Golden rows

    rows.append(N545g)
    rows.append(N1581g)
    rows.append(N1901g)
    rows.append(N2223g)
    rows.append(N2548g)
    rows.append(N2877g)
    rows.append(N3211g)
    rows.append(N3552g)
    rows.append(N3895g)
    rows.append(N4241g)
    rows.append(N4591g)
    rows.append(N4946g)
    rows.append(N5308g)
    rows.append(N5672g)
    rows.append(N5971g) 
    rows.append(N6123g)
    rows.append(N6150g)    
    rows.append(N6160g)
    rows.append(N6170g)
    rows.append(N6180g)
    rows.append(N6190g)
    rows.append(N6200g)
    rows.append(N6210g)
    rows.append(N6220g)
    rows.append(N6230g)
    rows.append(N6240g)
    rows.append(N6250g)
    rows.append(N6260g)
    rows.append(N6270g)
    rows.append(N6280g)
    rows.append(N6287g)
    rows.append(N6288g)

#FAULTY OUTPUT COLUMNS    
    rows.append(N545)
    rows.append(N1581)
    rows.append(N1901)
    rows.append(N2223)
    rows.append(N2548)
    rows.append(N2877)
    rows.append(N3211)
    rows.append(N3552)
    rows.append(N3895)
    rows.append(N4241)
    rows.append(N4591)
    rows.append(N4946)
    rows.append(N5308)
    rows.append(N5672)
    rows.append(N5971) 
    rows.append(N6123)
    rows.append(N6150)    
    rows.append(N6160)
    rows.append(N6170)
    rows.append(N6180)
    rows.append(N6190)
    rows.append(N6200)
    rows.append(N6210)
    rows.append(N6220)
    rows.append(N6230)
    rows.append(N6240)
    rows.append(N6250)
    rows.append(N6260)
    rows.append(N6270)
    rows.append(N6280)
    rows.append(N6287)
    rows.append(N6288)

    #print(rows)
    final_compare = final_compare.append(pd.Series(rows, index = ["Clk", "Node", "N1", "N18", "N35", "N52", "N69", "N86", "N103", "N120", "N137", "N154", "N171", "N188", "N205", "N222", "N239", "N256", "N273", "N290", "N307", "N324", "N341", "N358", "N375", "N392", "N409", "N426", "N443", "N460", "N477", "N494", "N511", "N528", "N545", "N1581", "N1901", "N2223", "N2548", "N2877", "N3211", "N3552", "N3895", "N4241", "N4591", "N4946", "N5308", "N5672", "N5971", "N6123", "N6150", "N6160", "N6170", "N6180", "N6190", "N6200", "N6210", "N6220", "N6230", "N6240", "N6250", "N6260", "N6270", "N6280", "N6287", "N6288", "N545g", "N1581g", "N1901g", "N2223g", "N2548g", "N2877g", "N3211g", "N3552g", "N3895g", "N4241g", "N4591g", "N4946g", "N5308g", "N5672g", "N5971g", "N6123g", "N6150g", "N6160g", "N6170g", "N6180g", "N6190g", "N6200g", "N6210g", "N6220g", "N6230g", "N6240g", "N6250g", "N6260g", "N6270g", "N6280g", "N6287g", "N6288g"]), ignore_index=True)
##---------------------------------------------------------------------------------
#print(final_compare)

N545_Comp = pd.to_numeric(final_compare['N545']) != pd.to_numeric(final_compare['N545g'])
N545_Comp = N545_Comp.astype(int)
N1581_Comp = pd.to_numeric(final_compare['N1581']) != pd.to_numeric(final_compare['N1581g'])
N1581_Comp = N1581_Comp.astype(int)
N1901_Comp = pd.to_numeric(final_compare['N1901']) != pd.to_numeric(final_compare['N1901g'])
N1901_Comp = N1901_Comp.astype(int)
N2223_Comp = pd.to_numeric(final_compare['N2223']) != pd.to_numeric(final_compare['N2223g'])
N2223_Comp = N2223_Comp.astype(int)
N2548_Comp = pd.to_numeric(final_compare['N2548']) != pd.to_numeric(final_compare['N2548g'])
N2548_Comp = N2548_Comp.astype(int)
N2877_Comp = pd.to_numeric(final_compare['N2877']) != pd.to_numeric(final_compare['N2877g'])
N2877_Comp = N2877_Comp.astype(int)
N3211_Comp = pd.to_numeric(final_compare['N3211']) != pd.to_numeric(final_compare['N3211g'])
N3211_Comp = N3211_Comp.astype(int)
N3552_Comp = pd.to_numeric(final_compare['N3552']) != pd.to_numeric(final_compare['N3552g'])
N3552_Comp = N3552_Comp.astype(int)
N3895_Comp = pd.to_numeric(final_compare['N3895']) != pd.to_numeric(final_compare['N3895g'])
N3895_Comp = N3895_Comp.astype(int)
N4241_Comp = pd.to_numeric(final_compare['N4241']) != pd.to_numeric(final_compare['N4241g'])
N4241_Comp = N4241_Comp.astype(int)
N4591_Comp = pd.to_numeric(final_compare['N4591']) != pd.to_numeric(final_compare['N4591g'])
N4591_Comp = N4591_Comp.astype(int)
N4946_Comp = pd.to_numeric(final_compare['N4946']) != pd.to_numeric(final_compare['N4946g'])
N4946_Comp = N4946_Comp.astype(int)
N5308_Comp = pd.to_numeric(final_compare['N5308']) != pd.to_numeric(final_compare['N5308g'])
N5308_Comp = N5308_Comp.astype(int)
N5672_Comp = pd.to_numeric(final_compare['N5672']) != pd.to_numeric(final_compare['N5672g'])
N5672_Comp = N5672_Comp.astype(int)
N5971_Comp = pd.to_numeric(final_compare['N5971']) != pd.to_numeric(final_compare['N5971g'])
N5971_Comp = N5971_Comp.astype(int)
N6123_Comp = pd.to_numeric(final_compare['N6123']) != pd.to_numeric(final_compare['N6123g'])
N6123_Comp = N6123_Comp.astype(int)
N6150_Comp = pd.to_numeric(final_compare['N6150']) != pd.to_numeric(final_compare['N6150g'])
N6150_Comp = N6150_Comp.astype(int)
N6160_Comp = pd.to_numeric(final_compare['N6160']) != pd.to_numeric(final_compare['N6160g'])
N6160_Comp = N6160_Comp.astype(int)
N6170_Comp = pd.to_numeric(final_compare['N6170']) != pd.to_numeric(final_compare['N6170g'])
N6170_Comp = N6170_Comp.astype(int)
N6180_Comp = pd.to_numeric(final_compare['N6180']) != pd.to_numeric(final_compare['N6180g'])
N6180_Comp = N6180_Comp.astype(int)
N6190_Comp = pd.to_numeric(final_compare['N6190']) != pd.to_numeric(final_compare['N6190g'])
N6190_Comp = N6190_Comp.astype(int)
N6200_Comp = pd.to_numeric(final_compare['N6200']) != pd.to_numeric(final_compare['N6200g'])
N6200_Comp = N6200_Comp.astype(int)
N6210_Comp = pd.to_numeric(final_compare['N6210']) != pd.to_numeric(final_compare['N6210g'])
N6210_Comp = N6210_Comp.astype(int)
N6220_Comp = pd.to_numeric(final_compare['N6220']) != pd.to_numeric(final_compare['N6220g'])
N6220_Comp = N6220_Comp.astype(int)
N6230_Comp = pd.to_numeric(final_compare['N6230']) != pd.to_numeric(final_compare['N6230g'])
N6230_Comp = N6230_Comp.astype(int)
N6240_Comp = pd.to_numeric(final_compare['N6240']) != pd.to_numeric(final_compare['N6240g'])
N6240_Comp = N6240_Comp.astype(int)
N6250_Comp = pd.to_numeric(final_compare['N6250']) != pd.to_numeric(final_compare['N6250g'])
N6250_Comp = N6250_Comp.astype(int)
N6260_Comp = pd.to_numeric(final_compare['N6260']) != pd.to_numeric(final_compare['N6260g'])
N6260_Comp = N6260_Comp.astype(int)
N6270_Comp = pd.to_numeric(final_compare['N6270']) != pd.to_numeric(final_compare['N6270g'])
N6270_Comp = N6270_Comp.astype(int)
N6280_Comp = pd.to_numeric(final_compare['N6280']) != pd.to_numeric(final_compare['N6280g'])
N6280_Comp = N6280_Comp.astype(int)
N6287_Comp = pd.to_numeric(final_compare['N6287']) != pd.to_numeric(final_compare['N6287g'])
N6287_Comp = N6287_Comp.astype(int)
N6288_Comp = pd.to_numeric(final_compare['N6288']) != pd.to_numeric(final_compare['N6288g'])
N6288_Comp = N6288_Comp.astype(int)

final_compare = final_compare.assign(N545_Comp  = N545_Comp.values)
final_compare = final_compare.assign(N1581_Comp = N1581_Comp.values)
final_compare = final_compare.assign(N1901_Comp = N1901_Comp.values)
final_compare = final_compare.assign(N2223_Comp = N2223_Comp.values)
final_compare = final_compare.assign(N2548_Comp = N2548_Comp.values)
final_compare = final_compare.assign(N2877_Comp = N2877_Comp.values)
final_compare = final_compare.assign(N3211_Comp = N3211_Comp.values)
final_compare = final_compare.assign(N3552_Comp = N3552_Comp.values)
final_compare = final_compare.assign(N3895_Comp = N3895_Comp.values)
final_compare = final_compare.assign(N4241_Comp = N4241_Comp.values)
final_compare = final_compare.assign(N4591_Comp = N4591_Comp.values)
final_compare = final_compare.assign(N4946_Comp = N4946_Comp.values)
final_compare = final_compare.assign(N5308_Comp = N5308_Comp.values)
final_compare = final_compare.assign(N5672_Comp = N5672_Comp.values)
final_compare = final_compare.assign(N5971_Comp = N5971_Comp.values)
final_compare = final_compare.assign(N6123_Comp = N6123_Comp.values)
final_compare = final_compare.assign(N6150_Comp = N6150_Comp.values)

final_compare = final_compare.assign(N6160_Comp = N6160_Comp.values)
final_compare = final_compare.assign(N6170_Comp = N6170_Comp.values)
final_compare = final_compare.assign(N6180_Comp = N6180_Comp.values)
final_compare = final_compare.assign(N6190_Comp = N6190_Comp.values)
final_compare = final_compare.assign(N6200_Comp = N6200_Comp.values)
final_compare = final_compare.assign(N6210_Comp = N6210_Comp.values)
final_compare = final_compare.assign(N6220_Comp = N6220_Comp.values)
final_compare = final_compare.assign(N6230_Comp = N6230_Comp.values)
final_compare = final_compare.assign(N6240_Comp = N6240_Comp.values)
final_compare = final_compare.assign(N6250_Comp = N6250_Comp.values)
final_compare = final_compare.assign(N6260_Comp = N6260_Comp.values)
final_compare = final_compare.assign(N6270_Comp = N6270_Comp.values)
final_compare = final_compare.assign(N6280_Comp = N6280_Comp.values)
final_compare = final_compare.assign(N6287_Comp = N6287_Comp.values)
final_compare = final_compare.assign(N6288_Comp = N6288_Comp.values)


final_compare["M/S"] = final_compare["N545_Comp"] + final_compare["N1581_Comp"] + final_compare["N1901_Comp"] + final_compare["N2223_Comp"] + final_compare["N2548_Comp"] + final_compare["N2877_Comp"] + final_compare["N3211_Comp"] + final_compare["N3552_Comp"] + final_compare["N4241_Comp"] + final_compare["N3895_Comp"] + final_compare["N4591_Comp"] + final_compare["N4946_Comp"] + final_compare["N5308_Comp"] + final_compare["N5672_Comp"] + final_compare["N5971_Comp"] + final_compare["N6123_Comp"] + final_compare["N6150_Comp"] + final_compare["N6160_Comp"] + final_compare["N6170_Comp"] + final_compare["N6180_Comp"] + final_compare["N6190_Comp"] + final_compare["N6200_Comp"] + final_compare["N6210_Comp"] + final_compare["N6220_Comp"] + final_compare["N6230_Comp"] + final_compare["N6240_Comp"] + final_compare["N6250_Comp"] + final_compare["N6260_Comp"] + final_compare["N6270_Comp"] + final_compare["N6280_Comp"] + final_compare["N6287_Comp"] + final_compare["N6288_Comp"] 
final_compare.index.rename('Sr.No.', inplace=True)
final_compare.to_csv("compare_c6288.csv")

# final_compare = final_compare.loc[final_compare['M/S'] == 2]
# #print(final_compare)
# #Cri_Node = final_compare.iloc[:,1]
# #print(Cri_Node)
# #Multiple = final_compare.iloc[:,11]
# #print(Multiple)
# #final_compare = final_compare.assign(Multiple=Multiple.values)
# #final_compare = final_compare.assign(Cri_Node=Cri_Node.values)
# final_compare.to_csv("Critical.csv")
