import pandas as pd
import os
import csv
import subprocess
import random
import glob

final_compare = pd.DataFrame(columns = ["Clk", "Node", "N1", "N5", "N9", "N13", "N17", "N21", "N25", "N29", "N33", "N37", "N41", "N45", "N49", "N53", "N57", "N61", "N65", "N69", "N73", "N77", "N81", "N85", "N89", "N93", "N97", "N101", "N105", "N109", "N113", "N117", "N121", "N125", "N129", "N130", "N131", "N132", "N133", "N134", "N135", "N136", "N137", "N724", "N725", "N726", "N727", "N728", "N729", "N730", "N731", "N732", "N733", "N734", "N735", "N736", "N737", "N738", "N739", "N740", "N741", "N742", "N743", "N744", "N745", "N746", "N747", "N748", "N749", "N750", "N751", "N752", "N753", "N754", "N755", "N724g", "N725g", "N726g", "N727g", "N728g", "N729g", "N730g", "N731g", "N732g", "N733g", "N734g", "N735g", "N736g", "N737g", "N738g", "N739g", "N740g", "N741g", "N742g", "N743g", "N744g", "N745g", "N746g", "N747g", "N748g", "N749g", "N750g", "N751g", "N752g", "N753g", "N754g", "N755g"])

#--------------------------------------------------------------------------------
# Extracting the line at which enable is 1
for faulty_csv in glob.glob('D:\\Thesis\\python files\\c499\\fault*.csv'):
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

    # Value of input N5
    N5 = df.iloc[0,2]
    #print("N5   = ",N5)

    # Value of input N9
    N9 = df.iloc[0,3]
    #print("N9   =",N9)
    
    # Value of input N13
    N13 = df.iloc[0,4]
    #print("N13  = ",N13)

    # Value of input N17
    N17 = df.iloc[0,5]
    #print("N17  = ",N17)

    # Value of input N21
    N21 = df.iloc[0,6]
    #print("N21  =",N21)

    # Value of input N25
    N25 = df.iloc[0,7]
    #print("N25  = ",N25)

    # Value of input N29
    N29 = df.iloc[0,8]
    #print("N29  = ",N29)

    # Value of input N33
    N33 = df.iloc[0,9]
    #print("N33  =",N33)
    
    # Value of input N37
    N37 = df.iloc[0,10]
    #print("N37  = ",N37)

    # Value of input N41
    N41 = df.iloc[0,11]
    #print("N41  = ",N41)

    # Value of input N45
    N45 = df.iloc[0,12]
    #print("N45  =",N45)
    
    # Value of input N49
    N49 = df.iloc[0,13]
    #print("N49  = ",N49)

    # Value of input N53
    N53 = df.iloc[0,14]
    #print("N53  = ",N53)

    # Value of input N57
    N57 = df.iloc[0,15]
    #print("N57  =",N57)
    
    # Value of input N61
    N61 = df.iloc[0,16]
    #print("N61  = ",N61)

    # Value of input N65
    N65 = df.iloc[0,17]
    #print("N65  = ",N65)

    # Value of input N69
    N69 = df.iloc[0,18]
    #print("N69  =",N69)
    
    # Value of input N73
    N73 = df.iloc[0,19]
    #print("N73  = ",N73)

    # Value of input N77
    N77 = df.iloc[0,20]
    #print("N77  = ",N77)

    # Value of input N81
    N81 = df.iloc[0,21]
    #print("N81  =",N81)
    
    # Value of input N85
    N85 = df.iloc[0,22]
    #print("N85  = ",N85)

    # Value of input N89
    N89 = df.iloc[0,23]
    #print("N89  = ",N89)

    # Value of input N93
    N93 = df.iloc[0,24]
    #print("N93  =",N93)
           
    # Value of input N97
    N97 = df.iloc[0,25]
    #print("N97  = ",N97)

    # Value of input N101
    N101 = df.iloc[0,26]
    #print("N101 = ",N101)

    # Value of input N105
    N105 = df.iloc[0,27]
    #print("N105 =",N105)
    
    # Value of input N109
    N109 = df.iloc[0,28]
    #print("N109 = ",N109)

    # Value of input N113
    N113 = df.iloc[0,29]
    #print("N113 = ",N113)

    # Value of input N117
    N117 = df.iloc[0,30]
    #print("N117 =",N117)
    
    # Value of input N121
    N121 = df.iloc[0,31]
    #print("N121 = ",N121)

    # Value of input N125
    N125 = df.iloc[0,32]
    #print("N125 =",N125)
    
    # Value of input N129
    N129 = df.iloc[0,33]
    #print("N129 = ",N129)

    # Value of input N130
    N130 = df.iloc[0,34]
    #print("N130 = ",N130)

    # Value of input N131
    N131 = df.iloc[0,35]
    #print("N131 =",N131)
           
    # Value of input N132
    N132 = df.iloc[0,36]
    #print("N132 = ",N132)

    # Value of input N133
    N133 = df.iloc[0,37]
    #print("N133 = ",N133)

    # Value of input N134
    N134 = df.iloc[0,38]
    #print("N134 =",N134)
    
    # Value of input N135
    N135 = df.iloc[0,39]
    #print("N135 = ",N135)

    # Value of input N136
    N136 = df.iloc[0,40]
    #print("N136 = ",N136)

    # Value of input N137
    N137 = df.iloc[0,41]
    #print("N137 =",N137)
#--------------------------------------------------------------------------------
## Extracting faulty output values
    ff = pd.read_csv(faulty_csv)

    # Same line at which error was enabled
    faulty = ff.loc[ff['Clk'] == time_outf]
    #print(faulty)

    # Faulty value of N724
    N724 = faulty.iloc[0,43]
    #print("N724= ",N724)

    # Faulty value of N725
    N725 = faulty.iloc[0,44]
    #print("N725= ",N725)

    # Faulty value of N726
    N726 = faulty.iloc[0,45]
    #print("N726= ",N726)

    # Faulty value of N727
    N727 = faulty.iloc[0,46]
    #print("N727= ",N727)
    
    # Faulty value of N728
    N728 = faulty.iloc[0,47]
    #print("N728= ",N728)

    # Faulty value of N729
    N729 = faulty.iloc[0,48]
    #print("N729= ",N729)

    # Faulty value of N730
    N730 = faulty.iloc[0,49]
    #print("N730= ",N730)

    # Faulty value of N731
    N731 = faulty.iloc[0,50]
    #print("N731= ",N731)
    
    # Faulty value of N732
    N732 = faulty.iloc[0,51]
    #print("N732= ",N732)

    # Faulty value of N733
    N733 = faulty.iloc[0,52]
    #print("N733= ",N733)

    # Faulty value of N734
    N734 = faulty.iloc[0,53]
    #print("N734= ",N734)

    # Faulty value of N735
    N735 = faulty.iloc[0,54]
    #print("N735= ",N735)    
    
    # Faulty value of N736
    N736 = faulty.iloc[0,55]
    #print("N736= ",N736)

    # Faulty value of N737
    N737 = faulty.iloc[0,56]
    #print("N737= ",N737)

    # Faulty value of N738
    N738 = faulty.iloc[0,57]
    #print("N738= ",N738)

    # Faulty value of N739
    N739 = faulty.iloc[0,58]
    #print("N739= ",N739)
    
    # Faulty value of N740
    N740 = faulty.iloc[0,59]
    #print("N740= ",N740)

    # Faulty value of N741
    N741 = faulty.iloc[0,60]
    #print("N741= ",N741)

    # Faulty value of N742
    N742 = faulty.iloc[0,61]
    #print("N742= ",N742)

    # Faulty value of N743
    N743 = faulty.iloc[0,62]
    #print("N743= ",N743)    
    
    # Faulty value of N744
    N744 = faulty.iloc[0,63]
    #print("N744= ",N744)

    # Faulty value of N745
    N745 = faulty.iloc[0,64]
    #print("N745= ",N745)

    # Faulty value of N746
    N746 = faulty.iloc[0,65]
    #print("N746= ",N746)

    # Faulty value of N747
    N747 = faulty.iloc[0,66]
    #print("N747= ",N747)
    
    # Faulty value of N748
    N748 = faulty.iloc[0,67]
    #print("N748= ",N748)

    # Faulty value of N749
    N749 = faulty.iloc[0,68]
    #print("N749= ",N749)

    # Faulty value of N750
    N750 = faulty.iloc[0,69]
    #print("N750= ",N750)

    # Faulty value of N751
    N751 = faulty.iloc[0,70]
    #print("N751= ",N751)    
    
    # Faulty value of N752
    N752 = faulty.iloc[0,71]
    #print("N752= ",N752)

    # Faulty value of N753
    N753 = faulty.iloc[0,72]
    #print("N753= ",N753)

    # Faulty value of N754
    N754 = faulty.iloc[0,73]
    #print("N754= ",N754)

    # Faulty value of N755
    N755 = faulty.iloc[0,74]
    #print("N755= ",N755)
#---------------------------------------------------------------------------------
    # Reading the golden output to extract correct value output
    cf = pd.read_csv('D:\\Thesis\\python files\\c499\\golden_c499.csv')

    # Same line at which error was enabled
    gold = cf.loc[cf['Clk'] == time_outf]
    #print("Golden outputline",gold)

    # Correct value of N724
    N724g = gold.iloc[0,43]
    #print("N724g= ",N724g)

    # Correct value of N725
    N725g = gold.iloc[0,44]
    #print("N725g= ",N725g)

    # Correct value of N726
    N726g = gold.iloc[0,45]
    #print("N726g= ",N726g)

    # Correct value of N727
    N727g = gold.iloc[0,46]
    #print("N727g= ",N727g)
    
    # Correct value of N728
    N728g = gold.iloc[0,47]
    #print("N728g= ",N728g)

    # Correct value of N729
    N729g = gold.iloc[0,48]
    #print("N729g= ",N729g)

    # Correct value of N730
    N730g = gold.iloc[0,49]
    #print("N730g= ",N730g)

    # Correct value of N731
    N731g = gold.iloc[0,50]
    #print("N731g= ",N731g)
    
    # Correct value of N732
    N732g = gold.iloc[0,51]
    #print("N732g= ",N732g)

    # Correct value of N733
    N733g = gold.iloc[0,52]
    #print("N733g= ",N733g)

    # Correct value of N734
    N734g = gold.iloc[0,53]
    #print("N734g= ",N734g)

    # Correct value of N735
    N735g = gold.iloc[0,54]
    #print("N735g= ",N735g)    
    
    # Correct value of N736
    N736g = gold.iloc[0,55]
    #print("N736g= ",N736g)

    # Correct value of N737
    N737g = gold.iloc[0,56]
    #print("N737g= ",N737g)

    # Correct value of N738
    N738g = gold.iloc[0,57]
    #print("N738g= ",N738g)

    # Correct value of N739
    N739g = gold.iloc[0,58]
    #print("N739g= ",N739g)
    
    # Correct value of N740
    N740g = gold.iloc[0,59]
    #print("N740g= ",N740g)

    # Correct value of N741
    N741g = gold.iloc[0,60]
    #print("N741g= ",N741g)

    # Correct value of N742
    N742g = gold.iloc[0,61]
    #print("N742g= ",N742g)

    # Correct value of N743
    N743g = gold.iloc[0,62]
    #print("N743g= ",N743g)    
    
    # Correct value of N744
    N744g = gold.iloc[0,63]
    #print("N744g= ",N744g)

    # Correct value of N745
    N745g = gold.iloc[0,64]
    #print("N745g= ",N745g)

    # Correct value of N746
    N746g = gold.iloc[0,65]
    #print("N746g= ",N746g)

    # Correct value of N747
    N747g = gold.iloc[0,66]
    #print("N747g= ",N747g)
    
    # Correct value of N748
    N748g = gold.iloc[0,67]
    #print("N748g= ",N748g)

    # Correct value of N749
    N749g = gold.iloc[0,68]
    #print("N749g= ",N749g)

    # Correct value of N750
    N750g = gold.iloc[0,69]
    #print("N750g= ",N750g)

    # Correct value of N751
    N751g = gold.iloc[0,70]
    #print("N751g= ",N751g)    
    
    # Correct value of N752
    N752g = gold.iloc[0,71]
    #print("N752g= ",N752g)

    # Correct value of N753
    N753g = gold.iloc[0,72]
    #print("N753g= ",N753g)

    # Correct value of N754
    N754g = gold.iloc[0,73]
    #print("N754g= ",N754g)

    # Correct value of N755
    N755g = gold.iloc[0,74]
    #print("N755g= ",N755g)

#---------------------------------------------------------------------------------
    #appending all values in order to form a row

    rows.append(time_in)
    rows.append(Node)
    rows.append(N1)
    rows.append(N5)
    rows.append(N9)
    rows.append(N13)
    rows.append(N17)
    rows.append(N21)
    rows.append(N25)
    rows.append(N29)
    rows.append(N33)
    rows.append(N37)
    rows.append(N41)
    rows.append(N45)
    rows.append(N49)
    rows.append(N53)
    rows.append(N57)
    rows.append(N61)
    rows.append(N65)
    rows.append(N69)
    rows.append(N73)
    rows.append(N77)
    rows.append(N81)
    rows.append(N85)
    rows.append(N89)
    rows.append(N93)
    rows.append(N97)
    rows.append(N101)
    rows.append(N105)
    rows.append(N109)
    rows.append(N113)
    rows.append(N117)
    rows.append(N121)
    rows.append(N125)
    rows.append(N129)
    rows.append(N130)
    rows.append(N131)
    rows.append(N132)
    rows.append(N133)
    rows.append(N134)
    rows.append(N135)
    rows.append(N136)
    rows.append(N137)
    rows.append(N724)
    rows.append(N725)
    rows.append(N726)
    rows.append(N727)
    rows.append(N728)
    rows.append(N729)
    rows.append(N730)
    rows.append(N731)
    rows.append(N732)
    rows.append(N733)
    rows.append(N734)
    rows.append(N735)
    rows.append(N736)
    rows.append(N737)
    rows.append(N738)
    rows.append(N739)
    rows.append(N740)
    rows.append(N741)
    rows.append(N742)
    rows.append(N743)
    rows.append(N744)
    rows.append(N745)
    rows.append(N746)
    rows.append(N747)
    rows.append(N748)
    rows.append(N749)
    rows.append(N750)
    rows.append(N751)
    rows.append(N752)
    rows.append(N753)
    rows.append(N754)
    rows.append(N755)
    rows.append(N724g)
    rows.append(N725g)
    rows.append(N726g)
    rows.append(N727g)
    rows.append(N728g)
    rows.append(N729g)
    rows.append(N730g)
    rows.append(N731g)
    rows.append(N732g)
    rows.append(N733g)
    rows.append(N734g)
    rows.append(N735g)
    rows.append(N736g)
    rows.append(N737g)
    rows.append(N738g)
    rows.append(N739g)
    rows.append(N740g)
    rows.append(N741g)
    rows.append(N742g)
    rows.append(N743g)
    rows.append(N744g)
    rows.append(N745g)
    rows.append(N746g)
    rows.append(N747g)
    rows.append(N748g)
    rows.append(N749g)
    rows.append(N750g)
    rows.append(N751g)
    rows.append(N752g)
    rows.append(N753g)
    rows.append(N754g)
    rows.append(N755g)
    #print(rows)
    final_compare = final_compare.append(pd.Series(rows, index = ["Clk", "Node", "N1", "N5", "N9", "N13", "N17", "N21", "N25", "N29", "N33", "N37", "N41", "N45", "N49", "N53", "N57", "N61", "N65", "N69", "N73", "N77", "N81", "N85", "N89", "N93", "N97", "N101", "N105", "N109", "N113", "N117", "N121", "N125", "N129", "N130", "N131", "N132", "N133", "N134", "N135", "N136", "N137", "N724", "N725", "N726", "N727", "N728", "N729", "N730", "N731", "N732", "N733", "N734", "N735", "N736", "N737", "N738", "N739", "N740", "N741", "N742", "N743", "N744", "N745", "N746", "N747", "N748", "N749", "N750", "N751", "N752", "N753", "N754", "N755", "N724g", "N725g", "N726g", "N727g", "N728g", "N729g", "N730g", "N731g", "N732g", "N733g", "N734g", "N735g", "N736g", "N737g", "N738g", "N739g", "N740g", "N741g", "N742g", "N743g", "N744g", "N745g", "N746g", "N747g", "N748g", "N749g", "N750g", "N751g", "N752g", "N753g", "N754g", "N755g"]), ignore_index=True)
##---------------------------------------------------------------------------------
#print(final_compare)

N724_Comp = pd.to_numeric(final_compare['N724']) != pd.to_numeric(final_compare['N724g'])
N724_Comp = N724_Comp.astype(int)
N725_Comp = pd.to_numeric(final_compare['N725']) != pd.to_numeric(final_compare['N725g'])
N725_Comp = N725_Comp.astype(int)
N726_Comp = pd.to_numeric(final_compare['N726']) != pd.to_numeric(final_compare['N726g'])
N726_Comp = N726_Comp.astype(int)
N727_Comp = pd.to_numeric(final_compare['N727']) != pd.to_numeric(final_compare['N727g'])
N727_Comp = N727_Comp.astype(int)
N728_Comp = pd.to_numeric(final_compare['N728']) != pd.to_numeric(final_compare['N728g'])
N728_Comp = N728_Comp.astype(int)
N729_Comp = pd.to_numeric(final_compare['N729']) != pd.to_numeric(final_compare['N729g'])
N729_Comp = N729_Comp.astype(int)
N730_Comp = pd.to_numeric(final_compare['N730']) != pd.to_numeric(final_compare['N730g'])
N730_Comp = N730_Comp.astype(int)
N731_Comp = pd.to_numeric(final_compare['N731']) != pd.to_numeric(final_compare['N731g'])
N731_Comp = N731_Comp.astype(int)
N732_Comp = pd.to_numeric(final_compare['N732']) != pd.to_numeric(final_compare['N732g'])
N732_Comp = N732_Comp.astype(int)
N733_Comp = pd.to_numeric(final_compare['N733']) != pd.to_numeric(final_compare['N733g'])
N733_Comp = N733_Comp.astype(int)
N734_Comp = pd.to_numeric(final_compare['N734']) != pd.to_numeric(final_compare['N734g'])
N734_Comp = N734_Comp.astype(int)
N735_Comp = pd.to_numeric(final_compare['N735']) != pd.to_numeric(final_compare['N735g'])
N735_Comp = N735_Comp.astype(int)
N736_Comp = pd.to_numeric(final_compare['N736']) != pd.to_numeric(final_compare['N736g'])
N736_Comp = N736_Comp.astype(int)
N737_Comp = pd.to_numeric(final_compare['N737']) != pd.to_numeric(final_compare['N737g'])
N737_Comp = N737_Comp.astype(int)
N738_Comp = pd.to_numeric(final_compare['N738']) != pd.to_numeric(final_compare['N738g'])
N738_Comp = N738_Comp.astype(int)
N739_Comp = pd.to_numeric(final_compare['N739']) != pd.to_numeric(final_compare['N739g'])
N739_Comp = N739_Comp.astype(int)
N740_Comp = pd.to_numeric(final_compare['N740']) != pd.to_numeric(final_compare['N740g'])
N740_Comp = N740_Comp.astype(int)
N741_Comp = pd.to_numeric(final_compare['N741']) != pd.to_numeric(final_compare['N741g'])
N741_Comp = N741_Comp.astype(int)
N742_Comp = pd.to_numeric(final_compare['N742']) != pd.to_numeric(final_compare['N742g'])
N742_Comp = N742_Comp.astype(int)
N743_Comp = pd.to_numeric(final_compare['N743']) != pd.to_numeric(final_compare['N743g'])
N743_Comp = N743_Comp.astype(int)
N744_Comp = pd.to_numeric(final_compare['N744']) != pd.to_numeric(final_compare['N744g'])
N744_Comp = N744_Comp.astype(int)
N745_Comp = pd.to_numeric(final_compare['N745']) != pd.to_numeric(final_compare['N745g'])
N745_Comp = N745_Comp.astype(int)
N746_Comp = pd.to_numeric(final_compare['N746']) != pd.to_numeric(final_compare['N746g'])
N746_Comp = N746_Comp.astype(int)
N747_Comp = pd.to_numeric(final_compare['N747']) != pd.to_numeric(final_compare['N747g'])
N747_Comp = N747_Comp.astype(int)
N748_Comp = pd.to_numeric(final_compare['N748']) != pd.to_numeric(final_compare['N748g'])
N748_Comp = N748_Comp.astype(int)
N749_Comp = pd.to_numeric(final_compare['N749']) != pd.to_numeric(final_compare['N749g'])
N749_Comp = N749_Comp.astype(int)
N750_Comp = pd.to_numeric(final_compare['N750']) != pd.to_numeric(final_compare['N750g'])
N750_Comp = N750_Comp.astype(int)
N751_Comp = pd.to_numeric(final_compare['N751']) != pd.to_numeric(final_compare['N751g'])
N751_Comp = N751_Comp.astype(int)
N752_Comp = pd.to_numeric(final_compare['N752']) != pd.to_numeric(final_compare['N752g'])
N752_Comp = N752_Comp.astype(int)
N753_Comp = pd.to_numeric(final_compare['N753']) != pd.to_numeric(final_compare['N753g'])
N753_Comp = N753_Comp.astype(int)
N754_Comp = pd.to_numeric(final_compare['N754']) != pd.to_numeric(final_compare['N754g'])
N754_Comp = N754_Comp.astype(int)
N755_Comp = pd.to_numeric(final_compare['N755']) != pd.to_numeric(final_compare['N755g'])
N755_Comp = N755_Comp.astype(int)

final_compare = final_compare.assign(N724_Comp = N724_Comp.values)
final_compare = final_compare.assign(N725_Comp = N725_Comp.values)
final_compare = final_compare.assign(N726_Comp = N726_Comp.values)
final_compare = final_compare.assign(N727_Comp = N727_Comp.values)
final_compare = final_compare.assign(N728_Comp = N728_Comp.values)
final_compare = final_compare.assign(N729_Comp = N729_Comp.values)
final_compare = final_compare.assign(N730_Comp = N730_Comp.values)
final_compare = final_compare.assign(N731_Comp = N731_Comp.values)
final_compare = final_compare.assign(N732_Comp = N732_Comp.values)
final_compare = final_compare.assign(N733_Comp = N733_Comp.values)
final_compare = final_compare.assign(N734_Comp = N734_Comp.values)
final_compare = final_compare.assign(N735_Comp = N735_Comp.values)
final_compare = final_compare.assign(N736_Comp = N736_Comp.values)
final_compare = final_compare.assign(N737_Comp = N737_Comp.values)
final_compare = final_compare.assign(N738_Comp = N738_Comp.values)
final_compare = final_compare.assign(N739_Comp = N739_Comp.values)
final_compare = final_compare.assign(N740_Comp = N740_Comp.values)
final_compare = final_compare.assign(N741_Comp = N741_Comp.values)
final_compare = final_compare.assign(N742_Comp = N742_Comp.values)
final_compare = final_compare.assign(N743_Comp = N743_Comp.values)
final_compare = final_compare.assign(N744_Comp = N744_Comp.values)
final_compare = final_compare.assign(N745_Comp = N745_Comp.values)
final_compare = final_compare.assign(N746_Comp = N746_Comp.values)
final_compare = final_compare.assign(N747_Comp = N747_Comp.values)
final_compare = final_compare.assign(N748_Comp = N748_Comp.values)
final_compare = final_compare.assign(N749_Comp = N749_Comp.values)
final_compare = final_compare.assign(N750_Comp = N750_Comp.values)
final_compare = final_compare.assign(N751_Comp = N751_Comp.values)
final_compare = final_compare.assign(N752_Comp = N752_Comp.values)
final_compare = final_compare.assign(N753_Comp = N753_Comp.values)
final_compare = final_compare.assign(N754_Comp = N754_Comp.values)
final_compare = final_compare.assign(N755_Comp = N755_Comp.values)

final_compare["M/S"] = final_compare["N724_Comp"] + final_compare["N725_Comp"] + final_compare["N726_Comp"] + final_compare["N727_Comp"] + final_compare["N728_Comp"] + final_compare["N729_Comp"] + final_compare["N730_Comp"] + final_compare["N731_Comp"] + final_compare["N732_Comp"] + final_compare["N733_Comp"] + final_compare["N734_Comp"] + final_compare["N735_Comp"] + final_compare["N736_Comp"] + final_compare["N737_Comp"] + final_compare["N738_Comp"] + final_compare["N739_Comp"] + final_compare["N740_Comp"] + final_compare["N741_Comp"] + final_compare["N742_Comp"] + final_compare["N743_Comp"] + final_compare["N744_Comp"] + final_compare["N745_Comp"] + final_compare["N746_Comp"] + final_compare["N747_Comp"] + final_compare["N748_Comp"] + final_compare["N749_Comp"] + final_compare["N750_Comp"] + final_compare["N751_Comp"] + final_compare["N752_Comp"] + final_compare["N753_Comp"] + final_compare["N754_Comp"] + final_compare["N755_Comp"]
final_compare.index.rename('Sr.No.', inplace=True)
final_compare.to_csv("D:\\Thesis\\python files\\c499\\compare.csv")

# final_compare = final_compare.loc[final_compare['M/S'] == 2]
# #print(final_compare)
# #Cri_Node = final_compare.iloc[:,1]
# #print(Cri_Node)
# #Multiple = final_compare.iloc[:,11]
# #print(Multiple)
# #final_compare = final_compare.assign(Multiple=Multiple.values)
# #final_compare = final_compare.assign(Cri_Node=Cri_Node.values)
# final_compare.to_csv("Critical.csv")
