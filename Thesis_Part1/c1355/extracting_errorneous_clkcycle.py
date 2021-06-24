import pandas as pd
import os
import csv
import subprocess
import random
import glob

final_compare = pd.DataFrame(columns = ["Clk", "Node", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "G11", "G12", "G13", "G14", "G15", "G16", "G17", "G18", "G19", "G20", "G21", "G22", "G23", "G24", "G25", "G26", "G27", "G28", "G29", "G30", "G31", "G32", "G33", "G34", "G35", "G36", "G37", "G38", "G39", "G40", "G41", "G1324", "G1325", "G1326", "G1327", "G1328", "G1329", "G1330", "G1331", "G1332", "G1333", "G1334", "G1335", "G1336", "G1337", "G1338", "G1339", "G1340", "G1341", "G1342", "G1343", "G1344", "G1345", "G1346", "G1347", "G1348", "G1349", "G1350", "G1351", "G1352", "G1353", "G1354", "G1355", "G1324g", "G1325g", "G1326g", "G1327g", "G1328g", "G1329g", "G1330g", "G1331g", "G1332g", "G1333g", "G1334g", "G1335g", "G1336g", "G1337g", "G1338g", "G1339g", "G1340g", "G1341g", "G1342g", "G1343g", "G1344g", "G1345g", "G1346g", "G1347g", "G1348g", "G1349g", "G1350g", "G1351g", "G1352g", "G1353g", "G1354g", "G1355g"])

#--------------------------------------------------------------------------------
# Extracting the line at which enable is 1
for faulty_csv in glob.glob('D:\\Thesis\\python files\\c1355\\fault*.csv'):
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
    
    # Value of input G1
    G1 = df.iloc[0,1]
    #print("G1   = ",G1)

    # Value of input G2
    G2 = df.iloc[0,2]
    #print("G2   = ",G2)

    # Value of input G3
    G3 = df.iloc[0,3]
    #print("G3   =",G3)
    
    # Value of input G4
    G4 = df.iloc[0,4]
    #print("G4  = ",G4)

    # Value of input G5
    G5 = df.iloc[0,5]
    #print("G5  = ",G5)

    # Value of input G6
    G6 = df.iloc[0,6]
    #print("G6  =",G6)

    # Value of input G7
    G7 = df.iloc[0,7]
    #print("G7  = ",G7)

    # Value of input G8
    G8 = df.iloc[0,8]
    #print("G8  = ",G8)

    # Value of input G9
    G9 = df.iloc[0,9]
    #print("G9  =",G9)
    
    # Value of input G10
    G10 = df.iloc[0,10]
    #print("G10  = ",G10)

    # Value of input G11
    G11 = df.iloc[0,11]
    #print("G11  = ",G11)

    # Value of input G12
    G12 = df.iloc[0,12]
    #print("G12  =",G12)
    
    # Value of input G13
    G13 = df.iloc[0,13]
    #print("G13  = ",G13)

    # Value of input G14
    G14 = df.iloc[0,14]
    #print("G14  = ",G14)

    # Value of input G15
    G15 = df.iloc[0,15]
    #print("G15  =",G15)
    
    # Value of input G16
    G16 = df.iloc[0,16]
    #print("G16  = ",G16)

    # Value of input G17
    G17 = df.iloc[0,17]
    #print("G17  = ",G17)

    # Value of input G18
    G18 = df.iloc[0,18]
    #print("G18  =",G18)
    
    # Value of input G19
    G19 = df.iloc[0,19]
    #print("G19  = ",G19)

    # Value of input G20
    G20 = df.iloc[0,20]
    #print("G20  = ",G20)

    # Value of input G21
    G21 = df.iloc[0,21]
    #print("G21  =",G21)
    
    # Value of input G22
    G22 = df.iloc[0,22]
    #print("G22  = ",G22)

    # Value of input G23
    G23 = df.iloc[0,23]
    #print("G23  = ",G23)

    # Value of input G24
    G24 = df.iloc[0,24]
    #print("G24  =",G24)
           
    # Value of input G25
    G25 = df.iloc[0,25]
    #print("G25  = ",G25)

    # Value of input G26
    G26 = df.iloc[0,26]
    #print("G26 = ",G26)

    # Value of input G27
    G27 = df.iloc[0,27]
    #print("G27 =",G27)
    
    # Value of input G28
    G28 = df.iloc[0,28]
    #print("G28 = ",G28)

    # Value of input G29
    G29 = df.iloc[0,29]
    #print("G29 = ",G29)

    # Value of input G30
    G30 = df.iloc[0,30]
    #print("G30 =",G30)
    
    # Value of input G31
    G31 = df.iloc[0,31]
    #print("G31 = ",G31)

    # Value of input G32
    G32 = df.iloc[0,32]
    #print("G32 =",G32)
    
    # Value of input G33
    G33 = df.iloc[0,33]
    #print("G33 = ",G33)

    # Value of input G34
    G34 = df.iloc[0,34]
    #print("G34 = ",G34)

    # Value of input G35
    G35 = df.iloc[0,35]
    #print("G35 =",G35)
           
    # Value of input G36
    G36 = df.iloc[0,36]
    #print("G36 = ",G36)

    # Value of input G37
    G37 = df.iloc[0,37]
    #print("G37 = ",G37)

    # Value of input G38
    G38 = df.iloc[0,38]
    #print("G38 =",G38)
    
    # Value of input G39
    G39 = df.iloc[0,39]
    #print("G39 = ",G39)

    # Value of input G40
    G40 = df.iloc[0,40]
    #print("G40 = ",G40)

    # Value of input G41
    G41 = df.iloc[0,41]
    #print("G41 =",G41)
#--------------------------------------------------------------------------------
## Extracting faulty output values
    ff = pd.read_csv(faulty_csv)

    # Same line at which error was enabled
    faulty = ff.loc[ff['Clk'] == time_outf]
    #print(faulty)

    # Faulty value of G1324
    G1324 = faulty.iloc[0,43]
    #print("G1324= ",G1324)

    # Faulty value of G1325
    G1325 = faulty.iloc[0,44]
    #print("G1325= ",G1325)

    # Faulty value of G1326
    G1326 = faulty.iloc[0,45]
    #print("G1326= ",G1326)

    # Faulty value of G1327
    G1327 = faulty.iloc[0,46]
    #print("G1327= ",G1327)
    
    # Faulty value of G1328
    G1328 = faulty.iloc[0,47]
    #print("G1328= ",G1328)

    # Faulty value of G1329
    G1329 = faulty.iloc[0,48]
    #print("G1329= ",G1329)

    # Faulty value of G1330
    G1330 = faulty.iloc[0,49]
    #print("G1330= ",G1330)

    # Faulty value of G1331
    G1331 = faulty.iloc[0,50]
    #print("G1331= ",G1331)
    
    # Faulty value of G1332
    G1332 = faulty.iloc[0,51]
    #print("G1332= ",G1332)

    # Faulty value of G1333
    G1333 = faulty.iloc[0,52]
    #print("G1333= ",G1333)

    # Faulty value of G1334
    G1334 = faulty.iloc[0,53]
    #print("G1334= ",G1334)

    # Faulty value of G1335
    G1335 = faulty.iloc[0,54]
    #print("G1335= ",G1335)    
    
    # Faulty value of G1336
    G1336 = faulty.iloc[0,55]
    #print("G1336= ",G1336)

    # Faulty value of G1337
    G1337 = faulty.iloc[0,56]
    #print("G1337= ",G1337)

    # Faulty value of G1338
    G1338 = faulty.iloc[0,57]
    #print("G1338= ",G1338)

    # Faulty value of G1339
    G1339 = faulty.iloc[0,58]
    #print("G1339= ",G1339)
    
    # Faulty value of G1340
    G1340 = faulty.iloc[0,59]
    #print("G1340= ",G1340)

    # Faulty value of G1341
    G1341 = faulty.iloc[0,60]
    #print("G1341= ",G1341)

    # Faulty value of G1342
    G1342 = faulty.iloc[0,61]
    #print("G1342= ",G1342)

    # Faulty value of G1343
    G1343 = faulty.iloc[0,62]
    #print("G1343= ",G1343)    
    
    # Faulty value of G1344
    G1344 = faulty.iloc[0,63]
    #print("G1344= ",G1344)

    # Faulty value of G1345
    G1345 = faulty.iloc[0,64]
    #print("G1345= ",G1345)

    # Faulty value of G1346
    G1346 = faulty.iloc[0,65]
    #print("G1346= ",G1346)

    # Faulty value of G1347
    G1347 = faulty.iloc[0,66]
    #print("G1347= ",G1347)
    
    # Faulty value of G1348
    G1348 = faulty.iloc[0,67]
    #print("G1348= ",G1348)

    # Faulty value of G1349
    G1349 = faulty.iloc[0,68]
    #print("G1349= ",G1349)

    # Faulty value of G1350
    G1350 = faulty.iloc[0,69]
    #print("G1350= ",G1350)

    # Faulty value of G1351
    G1351 = faulty.iloc[0,70]
    #print("G1351= ",G1351)    
    
    # Faulty value of G1352
    G1352 = faulty.iloc[0,71]
    #print("G1352= ",G1352)

    # Faulty value of G1353
    G1353 = faulty.iloc[0,72]
    #print("G1353= ",G1353)

    # Faulty value of G1354
    G1354 = faulty.iloc[0,73]
    #print("G1354= ",G1354)

    # Faulty value of G1355
    G1355 = faulty.iloc[0,74]
    #print("G1355= ",G1355)
    
#---------------------------------------------------------------------------------
    # Reading the golden output to extract correct value output
    cf = pd.read_csv('D:\\Thesis\\python files\\c1355\\goldenc1355.csv')

    # Same line at which error was enabled
    gold = cf.loc[cf['Clk'] == time_outf]
    #print("Golden outputline",gold)

    # Correct value of G1324
    G1324g = gold.iloc[0,43]
    #print("G1324= ",G1324)

    # Correct value of G1325
    G1325g = gold.iloc[0,44]
    #print("G1325= ",G1325)

    # Correct value of G1326
    G1326g = gold.iloc[0,45]
    #print("G1326= ",G1326)

    # Correct value of G1327
    G1327g = gold.iloc[0,46]
    #print("G1327= ",G1327)
    
    # Correct value of G1328
    G1328g = gold.iloc[0,47]
    #print("G1328= ",G1328)

    # Correct value of G1329
    G1329g = gold.iloc[0,48]
    #print("G1329= ",G1329)

    # Correct value of G1330
    G1330g = gold.iloc[0,49]
    #print("G1330= ",G1330)

    # Correct value of G1331
    G1331g = gold.iloc[0,50]
    #print("G1331= ",G1331)
    
    # Correct value of G1332
    G1332g = gold.iloc[0,51]
    #print("G1332= ",G1332)

    # Correct value of G1333
    G1333g = gold.iloc[0,52]
    #print("G1333= ",G1333)

    # Correct value of G1334
    G1334g = gold.iloc[0,53]
    #print("G1334= ",G1334)

    # Correct value of G1335
    G1335g = gold.iloc[0,54]
    #print("G1335= ",G1335)    
    
    # Correct value of G1336
    G1336g = gold.iloc[0,55]
    #print("G1336= ",G1336)

    # Correct value of G1337
    G1337g = gold.iloc[0,56]
    #print("G1337= ",G1337)

    # Correct value of G1338
    G1338g = gold.iloc[0,57]
    #print("G1338= ",G1338)

    # Correct value of G1339
    G1339g = gold.iloc[0,58]
    #print("G1339= ",G1339)
    
    # Correct value of G1340
    G1340g = gold.iloc[0,59]
    #print("G1340= ",G1340)

    # Correct value of G1341
    G1341g = gold.iloc[0,60]
    #print("G1341= ",G1341)

    # Correct value of G1342
    G1342g = gold.iloc[0,61]
    #print("G1342= ",G1342)

    # Correct value of G1343
    G1343g = gold.iloc[0,62]
    #print("G1343= ",G1343)    
    
    # Correct value of G1344
    G1344g = gold.iloc[0,63]
    #print("G1344= ",G1344)

    # Correct value of G1345
    G1345g = gold.iloc[0,64]
    #print("G1345= ",G1345)

    # Correct value of G1346
    G1346g = gold.iloc[0,65]
    #print("G1346= ",G1346)

    # Correct value of G1347
    G1347g = gold.iloc[0,66]
    #print("G1347= ",G1347)
    
    # Correct value of G1348
    G1348g = gold.iloc[0,67]
    #print("G1348= ",G1348)

    # Correct value of G1349
    G1349g = gold.iloc[0,68]
    #print("G1349= ",G1349)

    # Correct value of G1350
    G1350g = gold.iloc[0,69]
    #print("G1350= ",G1350)

    # Correct value of G1351
    G1351g = gold.iloc[0,70]
    #print("G1351= ",G1351)    
    
    # Correct value of G1352
    G1352g = gold.iloc[0,71]
    #print("G1352= ",G1352)

    # Correct value of G1353
    G1353g = gold.iloc[0,72]
    #print("G1353= ",G1353)

    # Correct value of G1354
    G1354g = gold.iloc[0,73]
    #print("G1354= ",G1354)

    # Correct value of G1355
    G1355g = gold.iloc[0,74]
    #print("G1355= ",G1355)

#---------------------------------------------------------------------------------
    #appending all values in order to form a row

    rows.append(time_in)
    rows.append(Node)
#Input columns    
    rows.append(G1)
    rows.append(G2)
    rows.append(G3)
    rows.append(G4)
    rows.append(G5)
    rows.append(G6)
    rows.append(G7)
    rows.append(G8)
    rows.append(G9)
    rows.append(G10)
    rows.append(G11)
    rows.append(G12)
    rows.append(G13)
    rows.append(G14)
    rows.append(G15)
    rows.append(G16)
    rows.append(G17)
    rows.append(G18)
    rows.append(G19)
    rows.append(G20)
    rows.append(G21)
    rows.append(G22)
    rows.append(G23)
    rows.append(G24)
    rows.append(G25)
    rows.append(G26)
    rows.append(G27)
    rows.append(G28)
    rows.append(G29)
    rows.append(G30)
    rows.append(G31)
    rows.append(G32)
    rows.append(G33)
    rows.append(G34)
    rows.append(G35)
    rows.append(G36)
    rows.append(G37)
    rows.append(G38)
    rows.append(G39)
    rows.append(G40)
    rows.append(G41)
#FAULTY OUTPUT COLUMNS    
    rows.append(G1324)
    rows.append(G1325)
    rows.append(G1326)
    rows.append(G1327)
    rows.append(G1328)
    rows.append(G1329)
    rows.append(G1330)
    rows.append(G1331)
    rows.append(G1332)
    rows.append(G1333)
    rows.append(G1334)
    rows.append(G1335)
    rows.append(G1336)
    rows.append(G1337)
    rows.append(G1338)
    rows.append(G1339)
    rows.append(G1340)    
    rows.append(G1341)
    rows.append(G1342)
    rows.append(G1343)
    rows.append(G1344)
    rows.append(G1345)
    rows.append(G1346)
    rows.append(G1347)
    rows.append(G1348)
    rows.append(G1349)
    rows.append(G1350)
    rows.append(G1351)
    rows.append(G1352)
    rows.append(G1353)
    rows.append(G1354)
    rows.append(G1355)
#golden rows
    rows.append(G1324g)
    rows.append(G1325g)
    rows.append(G1326g)
    rows.append(G1327g)
    rows.append(G1328g)
    rows.append(G1329g)
    rows.append(G1330g)
    rows.append(G1331g)
    rows.append(G1332g)
    rows.append(G1333g)
    rows.append(G1334g)
    rows.append(G1335g)
    rows.append(G1336g)
    rows.append(G1337g)
    rows.append(G1338g)
    rows.append(G1339g)
    rows.append(G1340g)
    rows.append(G1341g)
    rows.append(G1342g)
    rows.append(G1343g)
    rows.append(G1344g)
    rows.append(G1345g)
    rows.append(G1346g)
    rows.append(G1347g)
    rows.append(G1348g)
    rows.append(G1349g)
    rows.append(G1350g)
    rows.append(G1351g)
    rows.append(G1352g)
    rows.append(G1353g)
    rows.append(G1354g)
    rows.append(G1355g)
    #print(rows)
    final_compare = final_compare.append(pd.Series(rows, index = ["Clk", "Node", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "G11", "G12", "G13", "G14", "G15", "G16", "G17", "G18", "G19", "G20", "G21", "G22", "G23", "G24", "G25", "G26", "G27", "G28", "G29", "G30", "G31", "G32", "G33", "G34", "G35", "G36", "G37", "G38", "G39", "G40", "G41", "G1324", "G1325", "G1326", "G1327", "G1328", "G1329", "G1330", "G1331", "G1332", "G1333", "G1334", "G1335", "G1336", "G1337", "G1338", "G1339", "G1340", "G1341", "G1342", "G1343", "G1344", "G1345", "G1346", "G1347", "G1348", "G1349", "G1350", "G1351", "G1352", "G1353", "G1354", "G1355", "G1324g", "G1325g", "G1326g", "G1327g", "G1328g", "G1329g", "G1330g", "G1331g", "G1332g", "G1333g", "G1334g", "G1335g", "G1336g", "G1337g", "G1338g", "G1339g", "G1340g", "G1341g", "G1342g", "G1343g", "G1344g", "G1345g", "G1346g", "G1347g", "G1348g", "G1349g", "G1350g", "G1351g", "G1352g", "G1353g", "G1354g", "G1355g"]), ignore_index=True)
##---------------------------------------------------------------------------------
#print(final_compare)

G1324_Comp = pd.to_numeric(final_compare['G1324']) != pd.to_numeric(final_compare['G1324g'])
G1324_Comp = G1324_Comp.astype(int)
G1325_Comp = pd.to_numeric(final_compare['G1325']) != pd.to_numeric(final_compare['G1325g'])
G1325_Comp = G1325_Comp.astype(int)
G1326_Comp = pd.to_numeric(final_compare['G1326']) != pd.to_numeric(final_compare['G1326g'])
G1326_Comp = G1326_Comp.astype(int)
G1327_Comp = pd.to_numeric(final_compare['G1327']) != pd.to_numeric(final_compare['G1327g'])
G1327_Comp = G1327_Comp.astype(int)
G1328_Comp = pd.to_numeric(final_compare['G1328']) != pd.to_numeric(final_compare['G1328g'])
G1328_Comp = G1328_Comp.astype(int)
G1329_Comp = pd.to_numeric(final_compare['G1329']) != pd.to_numeric(final_compare['G1329g'])
G1329_Comp = G1329_Comp.astype(int)
G1330_Comp = pd.to_numeric(final_compare['G1330']) != pd.to_numeric(final_compare['G1330g'])
G1330_Comp = G1330_Comp.astype(int)
G1331_Comp = pd.to_numeric(final_compare['G1331']) != pd.to_numeric(final_compare['G1331g'])
G1331_Comp = G1331_Comp.astype(int)
G1332_Comp = pd.to_numeric(final_compare['G1332']) != pd.to_numeric(final_compare['G1332g'])
G1332_Comp = G1332_Comp.astype(int)
G1333_Comp = pd.to_numeric(final_compare['G1333']) != pd.to_numeric(final_compare['G1333g'])
G1333_Comp = G1333_Comp.astype(int)
G1334_Comp = pd.to_numeric(final_compare['G1334']) != pd.to_numeric(final_compare['G1334g'])
G1334_Comp = G1334_Comp.astype(int)
G1335_Comp = pd.to_numeric(final_compare['G1335']) != pd.to_numeric(final_compare['G1335g'])
G1335_Comp = G1335_Comp.astype(int)
G1336_Comp = pd.to_numeric(final_compare['G1336']) != pd.to_numeric(final_compare['G1336g'])
G1336_Comp = G1336_Comp.astype(int)
G1337_Comp = pd.to_numeric(final_compare['G1337']) != pd.to_numeric(final_compare['G1337g'])
G1337_Comp = G1337_Comp.astype(int)
G1338_Comp = pd.to_numeric(final_compare['G1338']) != pd.to_numeric(final_compare['G1338g'])
G1338_Comp = G1338_Comp.astype(int)
G1339_Comp = pd.to_numeric(final_compare['G1339']) != pd.to_numeric(final_compare['G1339g'])
G1339_Comp = G1339_Comp.astype(int)
G1340_Comp = pd.to_numeric(final_compare['G1340']) != pd.to_numeric(final_compare['G1340g'])
G1340_Comp = G1340_Comp.astype(int)
G1341_Comp = pd.to_numeric(final_compare['G1341']) != pd.to_numeric(final_compare['G1341g'])
G1341_Comp = G1341_Comp.astype(int)
G1342_Comp = pd.to_numeric(final_compare['G1342']) != pd.to_numeric(final_compare['G1342g'])
G1342_Comp = G1342_Comp.astype(int)
G1343_Comp = pd.to_numeric(final_compare['G1343']) != pd.to_numeric(final_compare['G1343g'])
G1343_Comp = G1343_Comp.astype(int)
G1344_Comp = pd.to_numeric(final_compare['G1344']) != pd.to_numeric(final_compare['G1344g'])
G1344_Comp = G1344_Comp.astype(int)
G1345_Comp = pd.to_numeric(final_compare['G1345']) != pd.to_numeric(final_compare['G1345g'])
G1345_Comp = G1345_Comp.astype(int)
G1346_Comp = pd.to_numeric(final_compare['G1346']) != pd.to_numeric(final_compare['G1346g'])
G1346_Comp = G1346_Comp.astype(int)
G1347_Comp = pd.to_numeric(final_compare['G1347']) != pd.to_numeric(final_compare['G1347g'])
G1347_Comp = G1347_Comp.astype(int)
G1348_Comp = pd.to_numeric(final_compare['G1348']) != pd.to_numeric(final_compare['G1348g'])
G1348_Comp = G1348_Comp.astype(int)
G1349_Comp = pd.to_numeric(final_compare['G1349']) != pd.to_numeric(final_compare['G1349g'])
G1349_Comp = G1349_Comp.astype(int)
G1350_Comp = pd.to_numeric(final_compare['G1350']) != pd.to_numeric(final_compare['G1350g'])
G1350_Comp = G1350_Comp.astype(int)
G1351_Comp = pd.to_numeric(final_compare['G1351']) != pd.to_numeric(final_compare['G1351g'])
G1351_Comp = G1351_Comp.astype(int)
G1352_Comp = pd.to_numeric(final_compare['G1352']) != pd.to_numeric(final_compare['G1352g'])
G1352_Comp = G1352_Comp.astype(int)
G1353_Comp = pd.to_numeric(final_compare['G1353']) != pd.to_numeric(final_compare['G1353g'])
G1353_Comp = G1353_Comp.astype(int)
G1354_Comp = pd.to_numeric(final_compare['G1354']) != pd.to_numeric(final_compare['G1354g'])
G1354_Comp = G1354_Comp.astype(int)
G1355_Comp = pd.to_numeric(final_compare['G1355']) != pd.to_numeric(final_compare['G1355g'])
G1355_Comp = G1355_Comp.astype(int)

final_compare = final_compare.assign(G1324_Comp = G1324_Comp.values)
final_compare = final_compare.assign(G1325_Comp = G1325_Comp.values)
final_compare = final_compare.assign(G1326_Comp = G1326_Comp.values)
final_compare = final_compare.assign(G1327_Comp = G1327_Comp.values)
final_compare = final_compare.assign(G1328_Comp = G1328_Comp.values)
final_compare = final_compare.assign(G1329_Comp = G1329_Comp.values)
final_compare = final_compare.assign(G1330_Comp = G1330_Comp.values)
final_compare = final_compare.assign(G1331_Comp = G1331_Comp.values)
final_compare = final_compare.assign(G1332_Comp = G1332_Comp.values)
final_compare = final_compare.assign(G1333_Comp = G1333_Comp.values)
final_compare = final_compare.assign(G1334_Comp = G1334_Comp.values)
final_compare = final_compare.assign(G1335_Comp = G1335_Comp.values)
final_compare = final_compare.assign(G1336_Comp = G1336_Comp.values)
final_compare = final_compare.assign(G1337_Comp = G1337_Comp.values)
final_compare = final_compare.assign(G1338_Comp = G1338_Comp.values)
final_compare = final_compare.assign(G1339_Comp = G1339_Comp.values)
final_compare = final_compare.assign(G1340_Comp = G1340_Comp.values)
final_compare = final_compare.assign(G1341_Comp = G1341_Comp.values)
final_compare = final_compare.assign(G1342_Comp = G1342_Comp.values)
final_compare = final_compare.assign(G1343_Comp = G1343_Comp.values)
final_compare = final_compare.assign(G1344_Comp = G1344_Comp.values)
final_compare = final_compare.assign(G1345_Comp = G1345_Comp.values)
final_compare = final_compare.assign(G1346_Comp = G1346_Comp.values)
final_compare = final_compare.assign(G1347_Comp = G1347_Comp.values)
final_compare = final_compare.assign(G1348_Comp = G1348_Comp.values)
final_compare = final_compare.assign(G1349_Comp = G1349_Comp.values)
final_compare = final_compare.assign(G1350_Comp = G1350_Comp.values)
final_compare = final_compare.assign(G1351_Comp = G1351_Comp.values)
final_compare = final_compare.assign(G1352_Comp = G1352_Comp.values)
final_compare = final_compare.assign(G1353_Comp = G1353_Comp.values)
final_compare = final_compare.assign(G1354_Comp = G1354_Comp.values)
final_compare = final_compare.assign(G1355_Comp = G1355_Comp.values)

final_compare["M/S"] = final_compare["G1324_Comp"] + final_compare["G1325_Comp"] + final_compare["G1326_Comp"] + final_compare["G1327_Comp"] + final_compare["G1328_Comp"] + final_compare["G1329_Comp"] + final_compare["G1330_Comp"] + final_compare["G1331_Comp"] + final_compare["G1332_Comp"] + final_compare["G1333_Comp"] + final_compare["G1334_Comp"] + final_compare["G1335_Comp"] + final_compare["G1336_Comp"] + final_compare["G1337_Comp"] + final_compare["G1338_Comp"] + final_compare["G1339_Comp"] + final_compare["G1340_Comp"] + final_compare["G1341_Comp"] + final_compare["G1342_Comp"] + final_compare["G1343_Comp"] + final_compare["G1344_Comp"] + final_compare["G1345_Comp"] + final_compare["G1346_Comp"] + final_compare["G1347_Comp"] + final_compare["G1348_Comp"] + final_compare["G1349_Comp"] + final_compare["G1350_Comp"] + final_compare["G1351_Comp"] + final_compare["G1352_Comp"] + final_compare["G1353_Comp"] + final_compare["G1354_Comp"] + final_compare["G1355_Comp"]
final_compare.index.rename('Sr.No.', inplace=True)
final_compare.to_csv("D:\\Thesis\\python files\\c1355\\compare.csv")

# final_compare = final_compare.loc[final_compare['M/S'] == 2]
# #print(final_compare)
# #Cri_Node = final_compare.iloc[:,1]
# #print(Cri_Node)
# #Multiple = final_compare.iloc[:,11]
# #print(Multiple)
# #final_compare = final_compare.assign(Multiple=Multiple.values)
# #final_compare = final_compare.assign(Cri_Node=Cri_Node.values)
# final_compare.to_csv("Critical.csv")
