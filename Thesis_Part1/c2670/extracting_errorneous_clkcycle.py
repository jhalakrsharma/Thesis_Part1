import pandas as pd
import os
import csv
import subprocess
import random
import glob

final_compare = pd.DataFrame(columns = ["Clk", "Node", "N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8", "N11", "N14", "N15", "N16", "N19", "N20", "N21", "N22", "N23", "N24", "N25", "N26", "N27", "N28", "N29", "N32", "N33", "N34", "N35", "N36", "N37", "N40", "N43", "N44", "N47", "N48", "N49", "N50", "N51", "N52", "N53", "N54", "N55", "N56", "N57", "N60", "N61", "N62", "N63", "N64", "N65", "N66", "N67", "N68", "N69", "N72", "N73", "N74", "N75", "N76", "N77", "N78", "N79", "N80", "N81", "N82", "N85", "N86", "N87", "N88", "N89", "N90", "N91", "N92", "N93", "N94", "N95", "N96", "N99", "N100", "N101", "N102", "N103", "N104", "N105", "N106", "N107", "N108", "N111", "N112", "N113", "N114", "N115", "N116", "N117", "N118", "N119", "N120", "N123", "N124", "N125", "N126", "N127", "N128", "N129", "N130", "N131", "N132", "N135", "N136", "N137", "N138", "N139", "N140", "N141", "N142", "N219", "N224", "N227", "N230", "N231", "N234", "N237", "N241", "N246", "N253", "N256", "N259", "N262", "N263", "N266", "N269", "N272", "N275", "N278", "N281", "N284", "N287", "N290", "N294", "N297", "N301", "N305", "N309", "N313", "N316", "N319", "N322", "N325", "N328", "N331", "N334", "N337", "N340", "N343", "N346", "N349", "N352", "N355", "N143_I", "N144_I", "N145_I", "N146_I", "N147_I", "N148_I", "N149_I", "N150_I", "N151_I", "N152_I", "N153_I", "N154_I", "N155_I", "N156_I", "N157_I", "N158_I", "N159_I", "N160_I", "N161_I", "N162_I", "N163_I", "N164_I", "N165_I", "N166_I", "N167_I", "N168_I", "N169_I", "N170_I", "N171_I", "N172_I", "N173_I", "N174_I", "N175_I", "N176_I", "N177_I", "N178_I", "N179_I", "N180_I", "N181_I", "N182_I", "N183_I", "N184_I", "N185_I", "N186_I", "N187_I", "N188_I", "N189_I", "N190_I", "N191_I", "N192_I", "N193_I", "N194_I", "N195_I", "N196_I", "N197_I", "N198_I", "N199_I", "N200_I", "N201_I", "N202_I", "N203_I", "N204_I", "N205_I", "N206_I", "N207_I", "N208_I", "N209_I", "N210_I", "N211_I", "N212_I", "N213_I", "N214_I", "N215_I", "N216_I", "N217_I", "N218_I", "N398", "N400", "N401", "N419", "N420", "N456", "N457", "N458", "N487", "N488", "N489", "N490", "N491", "N492", "N493", "N494", "N792", "N799", "N805", "N1026", "N1028", "N1029", "N1269", "N1277", "N1448", "N1726", "N1816", "N1817", "N1818", "N1819", "N1820", "N1821", "N1969", "N1970", "N1971", "N2010", "N2012", "N2014", "N2016", "N2018", "N2020", "N2022", "N2387", "N2388", "N2389", "N2390", "N2496", "N2643", "N2644", "N2891", "N2925", "N2970", "N2971", "N3038", "N3079", "N3546", "N3671", "N3803", "N3804", "N3809", "N3851", "N3875", "N3881", "N3882", "N143_O", "N144_O", "N145_O", "N146_O", "N147_O", "N148_O", "N149_O", "N150_O", "N151_O", "N152_O", "N153_O", "N154_O", "N155_O", "N156_O", "N157_O", "N158_O", "N159_O", "N160_O", "N161_O", "N162_O", "N163_O", "N164_O", "N165_O", "N166_O", "N167_O", "N168_O", "N169_O", "N170_O", "N171_O", "N172_O", "N173_O", "N174_O", "N175_O", "N176_O", "N177_O", "N178_O", "N179_O", "N180_O", "N181_O", "N182_O", "N183_O", "N184_O", "N185_O", "N186_O", "N187_O", "N188_O", "N189_O", "N190_O", "N191_O", "N192_O", "N193_O", "N194_O", "N195_O", "N196_O", "N197_O", "N198_O", "N199_O", "N200_O", "N201_O", "N202_O", "N203_O", "N204_O", "N205_O", "N206_O", "N207_O", "N208_O", "N209_O", "N210_O", "N211_O", "N212_O", "N213_O", "N214_O", "N215_O", "N216_O", "N217_O", "N218_O", "N398g", "N400g", "N401g", "N419g", "N420g", "N456g", "N457g", "N458g", "N487g", "N488g", "N489g", "N490g", "N491g", "N492g", "N493g", "N494g", "N792g", "N799g", "N805g", "N1026g", "N1028g", "N1029g", "N1269g", "N1277g", "N1448g", "N1726g", "N1816g", "N1817g", "N1818g", "N1819g", "N1820g", "N1821g", "N1969g", "N1970g", "N1971g", "N2010g", "N2012g", "N2014g", "N2016g", "N2018g", "N2020g", "N2022g", "N2387g", "N2388g", "N2389g", "N2390g", "N2496g", "N2643g", "N2644g", "N2891g", "N2925g", "N2970g", "N2971g", "N3038g", "N3079g", "N3546g", "N3671g", "N3803g", "N3804g", "N3809g", "N3851g", "N3875g", "N3881g", "N3882g", "N143_Og", "N144_Og", "N145_Og", "N146_Og", "N147_Og", "N148_Og", "N149_Og", "N150_Og", "N151_Og", "N152_Og", "N153_Og", "N154_Og", "N155_Og", "N156_Og", "N157_Og", "N158_Og", "N159_Og", "N160_Og", "N161_Og", "N162_Og", "N163_Og", "N164_Og", "N165_Og", "N166_Og", "N167_Og", "N168_Og", "N169_Og", "N170_Og", "N171_Og", "N172_Og", "N173_Og", "N174_Og", "N175_Og", "N176_Og", "N177_Og", "N178_Og", "N179_Og", "N180_Og", "N181_Og", "N182_Og", "N183_Og", "N184_Og", "N185_Og", "N186_Og", "N187_Og", "N188_Og", "N189_Og", "N190_Og", "N191_Og", "N192_Og", "N193_Og", "N194_Og", "N195_Og", "N196_Og", "N197_Og", "N198_Og", "N199_Og", "N200_Og", "N201_Og", "N202_Og", "N203_Og", "N204_Og", "N205_Og", "N206_Og", "N207_Og", "N208_Og", "N209_Og", "N210_Og", "N211_Og", "N212_Og", "N213_Og", "N214_Og", "N215_Og", "N216_Og", "N217_Og", "N218_Og"])

#--------------------------------------------------------------------------------
# Extracting the line at which enable is 1
for faulty_csv in glob.glob('fault*.csv'):
    #print(faulty_csv)
    name, rest = faulty_csv.split("_", 1) 
    #print("name=", name)
    #print(rest)

    extension = rest.split( "." )   #split on fullstop
    Node = extension[0]                 #first part of the split is the sequence
    #print("Node=", Node)
    ext = extension[1]                  #second part of the split is the shot
    # print("ext=", ext)
    rows = []

    sf = pd.read_csv(faulty_csv, low_memory=False)
    sf = sf.loc[sf['en'] == 1]
    #print(sf)
    # Clock cycle at which error was enabled *
    time_en = sf.iloc[0,0]
    print("Clk = ",time_en)
    time_in = time_en - 2
    time_outf = time_en + 2
# #-----------------------------------------------------------------------------------
    # Reading the line previous to the line when error was enabled to extract inputs
    df = pd.read_csv(faulty_csv, low_memory=False)
    # Previous line
    df = df.loc[df['Clk'] == time_in]
    #print(df)
    
    #extracting the input where enable is 1.
  
    N1 = df.iloc[0,1]
    N2 = df.iloc[0,2]
    N3 = df.iloc[0,3]
    N4 = df.iloc[0,4]
    N5 = df.iloc[0,5]
    N6 = df.iloc[0,6]
    N7 = df.iloc[0,7]
    N8 = df.iloc[0,8]
    N11 = df.iloc[0,9]
    N14 = df.iloc[0,10]
    N15 = df.iloc[0,11]
    N16 = df.iloc[0,12]
    N19 = df.iloc[0,13]
    N20 = df.iloc[0,14]
    N21 = df.iloc[0,15]
    N22 = df.iloc[0,16]
    N23 = df.iloc[0,17]
    N24 = df.iloc[0,18]
    N25 = df.iloc[0,19]
    N26 = df.iloc[0,20]
    N27 = df.iloc[0,21]
    N28 = df.iloc[0,22]
    N29 = df.iloc[0,23]
    N32 = df.iloc[0,24]
    N33 = df.iloc[0,25]
    N34 = df.iloc[0,26]
    N35 = df.iloc[0,27]
    N36 = df.iloc[0,28]
    N37 = df.iloc[0,29]
    N40 = df.iloc[0,30]
    N43 = df.iloc[0,31]
    N44 = df.iloc[0,32]
    N47 = df.iloc[0,33]
    N48 = df.iloc[0,34]
    N49 = df.iloc[0,35]
    N50 = df.iloc[0,36]
    N51 = df.iloc[0,37]
    N52 = df.iloc[0,38]
    N53 = df.iloc[0,39]
    N54 = df.iloc[0,40]
    N55 = df.iloc[0,41]
    N56 = df.iloc[0,42]
    N57 = df.iloc[0,43]
    N60 = df.iloc[0,44]
    N61 = df.iloc[0,45]
    N62 = df.iloc[0,46]
    N63 = df.iloc[0,47]
    N64 = df.iloc[0,48]
    N65 = df.iloc[0,49]
    N66 = df.iloc[0,50]
    N67 = df.iloc[0,51]
    N68 = df.iloc[0,52]
    N69 = df.iloc[0,53]
    N72 = df.iloc[0,54]
    N73 = df.iloc[0,55]
    N74 = df.iloc[0,56]
    N75 = df.iloc[0,57]
    N76 = df.iloc[0,58]
    N77 = df.iloc[0,59]
    N78 = df.iloc[0,60]
    N79 = df.iloc[0,61]
    N80 = df.iloc[0,62]
    N81 = df.iloc[0,63]
    N82 = df.iloc[0,64]
    N85 = df.iloc[0,65]
    N86 = df.iloc[0,66]
    N87 = df.iloc[0,67]
    N88 = df.iloc[0,68]
    N89 = df.iloc[0,69]
    N90 = df.iloc[0,70]
    N91 = df.iloc[0,71]
    N92 = df.iloc[0,72]
    N93 = df.iloc[0,73]
    N94 = df.iloc[0,74]
    N95 = df.iloc[0,75]
    N96 = df.iloc[0,76]
    N99 = df.iloc[0,77]
    N100 = df.iloc[0,78]
    N101 = df.iloc[0,79]
    N102 = df.iloc[0,80]
    N103 = df.iloc[0,81]
    N104 = df.iloc[0,82]
    N105 = df.iloc[0,83]
    N106 = df.iloc[0,84]
    N107 = df.iloc[0,85]
    N108 = df.iloc[0,86]
    N111 = df.iloc[0,87]
    N112 = df.iloc[0,88]
    N113 = df.iloc[0,89]
    N114 = df.iloc[0,90]
    N115 = df.iloc[0,91]
    N116 = df.iloc[0,92]
    N117 = df.iloc[0,93]
    N118 = df.iloc[0,94]
    N119 = df.iloc[0,95]
    N120 = df.iloc[0,96]
    N123 = df.iloc[0,97]
    N124 = df.iloc[0,98]
    N125 = df.iloc[0,99]
    N126 = df.iloc[0,100]
    N127 = df.iloc[0,101]
    N128 = df.iloc[0,102]
    N129 = df.iloc[0,103]
    N130 = df.iloc[0,104]
    N131 = df.iloc[0,105]
    N132 = df.iloc[0,106]
    N135 = df.iloc[0,107]
    N136 = df.iloc[0,108]
    N137 = df.iloc[0,109]
    N138 = df.iloc[0,110]
    N139 = df.iloc[0,111]
    N140 = df.iloc[0,112]
    N141 = df.iloc[0,113]
    N142 = df.iloc[0,114]
    N219 = df.iloc[0,115]
    N224 = df.iloc[0,116]
    N227 = df.iloc[0,117]
    N230 = df.iloc[0,118]
    N231 = df.iloc[0,119]
    N234 = df.iloc[0,120]
    N237 = df.iloc[0,121]
    N241 = df.iloc[0,122]
    N246 = df.iloc[0,123]
    N253 = df.iloc[0,124]
    N256 = df.iloc[0,125]
    N259 = df.iloc[0,126]
    N262 = df.iloc[0,127]
    N263 = df.iloc[0,128]
    N266 = df.iloc[0,129]
    N269 = df.iloc[0,130]
    N272 = df.iloc[0,131]
    N275 = df.iloc[0,132]
    N278 = df.iloc[0,133]
    N281 = df.iloc[0,134]
    N284 = df.iloc[0,135]
    N287 = df.iloc[0,136]
    N290 = df.iloc[0,137]
    N294 = df.iloc[0,138]
    N297 = df.iloc[0,139]
    N301 = df.iloc[0,140]
    N305 = df.iloc[0,141]
    N309 = df.iloc[0,142]
    N313 = df.iloc[0,143]
    N316 = df.iloc[0,144]
    N319 = df.iloc[0,145]
    N322 = df.iloc[0,146]
    N325 = df.iloc[0,147]
    N328 = df.iloc[0,148]
    N331 = df.iloc[0,149]
    N334 = df.iloc[0,150]
    N337 = df.iloc[0,151]
    N340 = df.iloc[0,152]
    N343 = df.iloc[0,153]
    N346 = df.iloc[0,154]
    N349 = df.iloc[0,155]
    N352 = df.iloc[0,156]
    N355 = df.iloc[0,157]
    N143_I = df.iloc[0,158]
    N144_I = df.iloc[0,159]
    N145_I = df.iloc[0,160]
    N146_I = df.iloc[0,161]
    N147_I = df.iloc[0,162]
    N148_I = df.iloc[0,163]
    N149_I = df.iloc[0,164]
    N150_I = df.iloc[0,165]
    N151_I = df.iloc[0,166]
    N152_I = df.iloc[0,167]
    N153_I = df.iloc[0,168]
    N154_I = df.iloc[0,169]
    N155_I = df.iloc[0,170]
    N156_I = df.iloc[0,171]
    N157_I = df.iloc[0,172]
    N158_I = df.iloc[0,173]
    N159_I = df.iloc[0,174]
    N160_I = df.iloc[0,175]
    N161_I = df.iloc[0,176]
    N162_I = df.iloc[0,177]
    N163_I = df.iloc[0,178]
    N164_I = df.iloc[0,179]
    N165_I = df.iloc[0,180]
    N166_I = df.iloc[0,181]
    N167_I = df.iloc[0,182]
    N168_I = df.iloc[0,183]
    N169_I = df.iloc[0,184]
    N170_I = df.iloc[0,185]
    N171_I = df.iloc[0,186]
    N172_I = df.iloc[0,187]
    N173_I = df.iloc[0,188]
    N174_I = df.iloc[0,189]
    N175_I = df.iloc[0,190]
    N176_I = df.iloc[0,191]
    N177_I = df.iloc[0,192]
    N178_I = df.iloc[0,193]
    N179_I = df.iloc[0,194]
    N180_I = df.iloc[0,195]
    N181_I = df.iloc[0,196]
    N182_I = df.iloc[0,197]
    N183_I = df.iloc[0,198]
    N184_I = df.iloc[0,199]
    N185_I = df.iloc[0,200]
    N186_I = df.iloc[0,201]
    N187_I = df.iloc[0,202]
    N188_I = df.iloc[0,203]
    N189_I = df.iloc[0,204]
    N190_I = df.iloc[0,205]
    N191_I = df.iloc[0,206]
    N192_I = df.iloc[0,207]
    N193_I = df.iloc[0,208]
    N194_I = df.iloc[0,209]
    N195_I = df.iloc[0,210]
    N196_I = df.iloc[0,211]
    N197_I = df.iloc[0,212]
    N198_I = df.iloc[0,213]
    N199_I = df.iloc[0,214]
    N200_I = df.iloc[0,215]
    N201_I = df.iloc[0,216]
    N202_I = df.iloc[0,217]
    N203_I = df.iloc[0,218]
    N204_I = df.iloc[0,219]
    N205_I = df.iloc[0,220]
    N206_I = df.iloc[0,221]
    N207_I = df.iloc[0,222]
    N208_I = df.iloc[0,223]
    N209_I = df.iloc[0,224]
    N210_I = df.iloc[0,225]
    N211_I = df.iloc[0,226]
    N212_I = df.iloc[0,227]
    N213_I = df.iloc[0,228]
    N214_I = df.iloc[0,229]
    N215_I = df.iloc[0,230]
    N216_I = df.iloc[0,231]
    N217_I = df.iloc[0,232]
    N218_I = df.iloc[0,233]

#--------------------------------------------------------------------------------
## Extracting faulty output values
    ff = pd.read_csv(faulty_csv)

    # Same line at which error was enabled
    faulty = ff.loc[ff['Clk'] == time_outf]     
    #print(faulty)

    N398 = faulty.iloc[0,235]
    N400 = faulty.iloc[0,236]
    N401 = faulty.iloc[0,237]
    N419 = faulty.iloc[0,238]
    N420 = faulty.iloc[0,239]
    N456 = faulty.iloc[0,240]
    N457 = faulty.iloc[0,241]
    N458 = faulty.iloc[0,242]
    N487 = faulty.iloc[0,243]
    N488 = faulty.iloc[0,244]
    N489 = faulty.iloc[0,245]
    N490 = faulty.iloc[0,246]
    N491 = faulty.iloc[0,247]
    N492 = faulty.iloc[0,248]
    N493 = faulty.iloc[0,249]
    N494 = faulty.iloc[0,250]
    N792 = faulty.iloc[0,251]
    N799 = faulty.iloc[0,252]
    N805 = faulty.iloc[0,253]
    N1026 = faulty.iloc[0,254]
    N1028 = faulty.iloc[0,255]
    N1029 = faulty.iloc[0,256]
    N1269 = faulty.iloc[0,257]
    N1277 = faulty.iloc[0,258]
    N1448 = faulty.iloc[0,259]
    N1726 = faulty.iloc[0,260]
    N1816 = faulty.iloc[0,261]
    N1817 = faulty.iloc[0,262]
    N1818 = faulty.iloc[0,263]
    N1819 = faulty.iloc[0,264]
    N1820 = faulty.iloc[0,265]
    N1821 = faulty.iloc[0,266]
    N1969 = faulty.iloc[0,267]
    N1970 = faulty.iloc[0,268]
    N1971 = faulty.iloc[0,269]
    N2010 = faulty.iloc[0,270]
    N2012 = faulty.iloc[0,271]
    N2014 = faulty.iloc[0,272]
    N2016 = faulty.iloc[0,273]
    N2018 = faulty.iloc[0,274]
    N2020 = faulty.iloc[0,275]
    N2022 = faulty.iloc[0,276]
    N2387 = faulty.iloc[0,277]
    N2388 = faulty.iloc[0,278]
    N2389 = faulty.iloc[0,279]
    N2390 = faulty.iloc[0,280]
    N2496 = faulty.iloc[0,281]
    N2643 = faulty.iloc[0,282]
    N2644 = faulty.iloc[0,283]
    N2891 = faulty.iloc[0,284]
    N2925 = faulty.iloc[0,285]
    N2970 = faulty.iloc[0,286]
    N2971 = faulty.iloc[0,287]
    N3038 = faulty.iloc[0,288]
    N3079 = faulty.iloc[0,289]
    N3546 = faulty.iloc[0,290]
    N3671 = faulty.iloc[0,291]
    N3803 = faulty.iloc[0,292]
    N3804 = faulty.iloc[0,293]
    N3809 = faulty.iloc[0,294]
    N3851 = faulty.iloc[0,295]
    N3875 = faulty.iloc[0,296]
    N3881 = faulty.iloc[0,297]
    N3882 = faulty.iloc[0,298]
    N143_O = faulty.iloc[0,299]
    N144_O = faulty.iloc[0,300]
    N145_O = faulty.iloc[0,301]
    N146_O = faulty.iloc[0,302]
    N147_O = faulty.iloc[0,303]
    N148_O = faulty.iloc[0,304]
    N149_O = faulty.iloc[0,305]
    N150_O = faulty.iloc[0,306]
    N151_O = faulty.iloc[0,307]
    N152_O = faulty.iloc[0,308]
    N153_O = faulty.iloc[0,309]
    N154_O = faulty.iloc[0,310]
    N155_O = faulty.iloc[0,311]
    N156_O = faulty.iloc[0,312]
    N157_O = faulty.iloc[0,313]
    N158_O = faulty.iloc[0,314]
    N159_O = faulty.iloc[0,315]
    N160_O = faulty.iloc[0,316]
    N161_O = faulty.iloc[0,317]
    N162_O = faulty.iloc[0,318]
    N163_O = faulty.iloc[0,319]
    N164_O = faulty.iloc[0,320]
    N165_O = faulty.iloc[0,321]
    N166_O = faulty.iloc[0,322]
    N167_O = faulty.iloc[0,323]
    N168_O = faulty.iloc[0,324]
    N169_O = faulty.iloc[0,325]
    N170_O = faulty.iloc[0,326]
    N171_O = faulty.iloc[0,327]
    N172_O = faulty.iloc[0,328]
    N173_O = faulty.iloc[0,329]
    N174_O = faulty.iloc[0,330]
    N175_O = faulty.iloc[0,331]
    N176_O = faulty.iloc[0,332]
    N177_O = faulty.iloc[0,333]
    N178_O = faulty.iloc[0,334]
    N179_O = faulty.iloc[0,335]
    N180_O = faulty.iloc[0,336]
    N181_O = faulty.iloc[0,337]
    N182_O = faulty.iloc[0,338]
    N183_O = faulty.iloc[0,339]
    N184_O = faulty.iloc[0,340]
    N185_O = faulty.iloc[0,341]
    N186_O = faulty.iloc[0,342]
    N187_O = faulty.iloc[0,343]
    N188_O = faulty.iloc[0,344]
    N189_O = faulty.iloc[0,345]
    N190_O = faulty.iloc[0,346]
    N191_O = faulty.iloc[0,347]
    N192_O = faulty.iloc[0,348]
    N193_O = faulty.iloc[0,349]
    N194_O = faulty.iloc[0,350]
    N195_O = faulty.iloc[0,351]
    N196_O = faulty.iloc[0,352]
    N197_O = faulty.iloc[0,353]
    N198_O = faulty.iloc[0,354]
    N199_O = faulty.iloc[0,355]
    N200_O = faulty.iloc[0,356]
    N201_O = faulty.iloc[0,357]
    N202_O = faulty.iloc[0,358]
    N203_O = faulty.iloc[0,359]
    N204_O = faulty.iloc[0,360]
    N205_O = faulty.iloc[0,361]
    N206_O = faulty.iloc[0,362]
    N207_O = faulty.iloc[0,363]
    N208_O = faulty.iloc[0,364]
    N209_O = faulty.iloc[0,365]
    N210_O = faulty.iloc[0,366]
    N211_O = faulty.iloc[0,367]
    N212_O = faulty.iloc[0,368]
    N213_O = faulty.iloc[0,369]
    N214_O = faulty.iloc[0,370]
    N215_O = faulty.iloc[0,371]
    N216_O = faulty.iloc[0,372]
    N217_O = faulty.iloc[0,373]
    N218_O = faulty.iloc[0,374]   

#---------------------------------------------------------------------------------
    # Reading the golden output to extract correct value output
    cf = pd.read_csv('golden_c2670_iverilog_py.csv',low_memory=False)

    # Same line at which error was enabled
    gold = cf.loc[cf['Clk'] == time_outf]
    #print("Golden outputline",gold)
    
    N398g = gold.iloc[0,235]
    N400g = gold.iloc[0,236]
    N401g = gold.iloc[0,237]
    N419g = gold.iloc[0,238]
    N420g = gold.iloc[0,239]
    N456g = gold.iloc[0,240]
    N457g = gold.iloc[0,241]
    N458g = gold.iloc[0,242]
    N487g = gold.iloc[0,243]
    N488g = gold.iloc[0,244]
    N489g = gold.iloc[0,245]
    N490g = gold.iloc[0,246]
    N491g = gold.iloc[0,247]
    N492g = gold.iloc[0,248]
    N493g = gold.iloc[0,249]
    N494g = gold.iloc[0,250]
    N792g = gold.iloc[0,251]
    N799g = gold.iloc[0,252]
    N805g = gold.iloc[0,253]
    N1026g = gold.iloc[0,254]
    N1028g = gold.iloc[0,255]
    N1029g = gold.iloc[0,256]
    N1269g = gold.iloc[0,257]
    N1277g = gold.iloc[0,258]
    N1448g = gold.iloc[0,259]
    N1726g = gold.iloc[0,260]
    N1816g = gold.iloc[0,261]
    N1817g = gold.iloc[0,262]
    N1818g = gold.iloc[0,263]
    N1819g = gold.iloc[0,264]
    N1820g = gold.iloc[0,265]
    N1821g = gold.iloc[0,266]
    N1969g = gold.iloc[0,267]
    N1970g = gold.iloc[0,268]
    N1971g = gold.iloc[0,269]
    N2010g = gold.iloc[0,270]
    N2012g = gold.iloc[0,271]
    N2014g = gold.iloc[0,272]
    N2016g = gold.iloc[0,273]
    N2018g = gold.iloc[0,274]
    N2020g = gold.iloc[0,275]
    N2022g = gold.iloc[0,276]
    N2387g = gold.iloc[0,277]
    N2388g = gold.iloc[0,278]
    N2389g = gold.iloc[0,279]
    N2390g = gold.iloc[0,280]
    N2496g = gold.iloc[0,281]
    N2643g = gold.iloc[0,282]
    N2644g = gold.iloc[0,283]
    N2891g = gold.iloc[0,284]
    N2925g = gold.iloc[0,285]
    N2970g = gold.iloc[0,286]
    N2971g = gold.iloc[0,287]
    N3038g = gold.iloc[0,288]
    N3079g = gold.iloc[0,289]
    N3546g = gold.iloc[0,290]
    N3671g = gold.iloc[0,291]
    N3803g = gold.iloc[0,292]
    N3804g = gold.iloc[0,293]
    N3809g = gold.iloc[0,294]
    N3851g = gold.iloc[0,295]
    N3875g = gold.iloc[0,296]
    N3881g = gold.iloc[0,297]
    N3882g = gold.iloc[0,298]
    N143_Og = gold.iloc[0,299]
    N144_Og = gold.iloc[0,300]
    N145_Og = gold.iloc[0,301]
    N146_Og = gold.iloc[0,302]
    N147_Og = gold.iloc[0,303]
    N148_Og = gold.iloc[0,304]
    N149_Og = gold.iloc[0,305]
    N150_Og = gold.iloc[0,306]
    N151_Og = gold.iloc[0,307]
    N152_Og = gold.iloc[0,308]
    N153_Og = gold.iloc[0,309]
    N154_Og = gold.iloc[0,310]
    N155_Og = gold.iloc[0,311]
    N156_Og = gold.iloc[0,312]
    N157_Og = gold.iloc[0,313]
    N158_Og = gold.iloc[0,314]
    N159_Og = gold.iloc[0,315]
    N160_Og = gold.iloc[0,316]
    N161_Og = gold.iloc[0,317]
    N162_Og = gold.iloc[0,318]
    N163_Og = gold.iloc[0,319]
    N164_Og = gold.iloc[0,320]
    N165_Og = gold.iloc[0,321]
    N166_Og = gold.iloc[0,322]
    N167_Og = gold.iloc[0,323]
    N168_Og = gold.iloc[0,324]
    N169_Og = gold.iloc[0,325]
    N170_Og = gold.iloc[0,326]
    N171_Og = gold.iloc[0,327]
    N172_Og = gold.iloc[0,328]
    N173_Og = gold.iloc[0,329]
    N174_Og = gold.iloc[0,330]
    N175_Og = gold.iloc[0,331]
    N176_Og = gold.iloc[0,332]
    N177_Og = gold.iloc[0,333]
    N178_Og = gold.iloc[0,334]
    N179_Og = gold.iloc[0,335]
    N180_Og = gold.iloc[0,336]
    N181_Og = gold.iloc[0,337]
    N182_Og = gold.iloc[0,338]
    N183_Og = gold.iloc[0,339]
    N184_Og = gold.iloc[0,340]
    N185_Og = gold.iloc[0,341]
    N186_Og = gold.iloc[0,342]
    N187_Og = gold.iloc[0,343]
    N188_Og = gold.iloc[0,344]
    N189_Og = gold.iloc[0,345]
    N190_Og = gold.iloc[0,346]
    N191_Og = gold.iloc[0,347]
    N192_Og = gold.iloc[0,348]
    N193_Og = gold.iloc[0,349]
    N194_Og = gold.iloc[0,350]
    N195_Og = gold.iloc[0,351]
    N196_Og = gold.iloc[0,352]
    N197_Og = gold.iloc[0,353]
    N198_Og = gold.iloc[0,354]
    N199_Og = gold.iloc[0,355]
    N200_Og = gold.iloc[0,356]
    N201_Og = gold.iloc[0,357]
    N202_Og = gold.iloc[0,358]
    N203_Og = gold.iloc[0,359]
    N204_Og = gold.iloc[0,360]
    N205_Og = gold.iloc[0,361]
    N206_Og = gold.iloc[0,362]
    N207_Og = gold.iloc[0,363]
    N208_Og = gold.iloc[0,364]
    N209_Og = gold.iloc[0,365]
    N210_Og = gold.iloc[0,366]
    N211_Og = gold.iloc[0,367]
    N212_Og = gold.iloc[0,368]
    N213_Og = gold.iloc[0,369]
    N214_Og = gold.iloc[0,370]
    N215_Og = gold.iloc[0,371]
    N216_Og = gold.iloc[0,372]
    N217_Og = gold.iloc[0,373]
    N218_Og = gold.iloc[0,374]

#---------------------------------------------------------------------------------
    #appending all values in order to form a row
    rows.append(time_in)
    rows.append(Node)
# Input columns    
    rows.append(N1)
    rows.append(N2)
    rows.append(N3)
    rows.append(N4)
    rows.append(N5)
    rows.append(N6)
    rows.append(N7)
    rows.append(N8)
    rows.append(N11)
    rows.append(N14)
    rows.append(N15)
    rows.append(N16)
    rows.append(N19)
    rows.append(N20)
    rows.append(N21)
    rows.append(N22)
    rows.append(N23)
    rows.append(N24)
    rows.append(N25)
    rows.append(N26)
    rows.append(N27)
    rows.append(N28)
    rows.append(N29)
    rows.append(N32)
    rows.append(N33)
    rows.append(N34)
    rows.append(N35)
    rows.append(N36)
    rows.append(N37)
    rows.append(N40)
    rows.append(N43)
    rows.append(N44)
    rows.append(N47)
    rows.append(N48)
    rows.append(N49)
    rows.append(N50)
    rows.append(N51)
    rows.append(N52)
    rows.append(N53)
    rows.append(N54)
    rows.append(N55)
    rows.append(N56)
    rows.append(N57)
    rows.append(N60)
    rows.append(N61)
    rows.append(N62)
    rows.append(N63)
    rows.append(N64)
    rows.append(N65)
    rows.append(N66)
    rows.append(N67)
    rows.append(N68)
    rows.append(N69)
    rows.append(N72)
    rows.append(N73)
    rows.append(N74)
    rows.append(N75)
    rows.append(N76)
    rows.append(N77)
    rows.append(N78)
    rows.append(N79)
    rows.append(N80)
    rows.append(N81)
    rows.append(N82)
    rows.append(N85)
    rows.append(N86)
    rows.append(N87)
    rows.append(N88)
    rows.append(N89)
    rows.append(N90)
    rows.append(N91)
    rows.append(N92)
    rows.append(N93)
    rows.append(N94)
    rows.append(N95)
    rows.append(N96)
    rows.append(N99)
    rows.append(N100)
    rows.append(N101)
    rows.append(N102)
    rows.append(N103)
    rows.append(N104)
    rows.append(N105)
    rows.append(N106)
    rows.append(N107)
    rows.append(N108)
    rows.append(N111)
    rows.append(N112)
    rows.append(N113)
    rows.append(N114)
    rows.append(N115)
    rows.append(N116)
    rows.append(N117)
    rows.append(N118)
    rows.append(N119)
    rows.append(N120)
    rows.append(N123)
    rows.append(N124)
    rows.append(N125)
    rows.append(N126)
    rows.append(N127)
    rows.append(N128)
    rows.append(N129)
    rows.append(N130)
    rows.append(N131)
    rows.append(N132)
    rows.append(N135)
    rows.append(N136)
    rows.append(N137)
    rows.append(N138)
    rows.append(N139)
    rows.append(N140)
    rows.append(N141)
    rows.append(N142)
    rows.append(N219)
    rows.append(N224)
    rows.append(N227)
    rows.append(N230)
    rows.append(N231)
    rows.append(N234)
    rows.append(N237)
    rows.append(N241)
    rows.append(N246)
    rows.append(N253)
    rows.append(N256)
    rows.append(N259)
    rows.append(N262)
    rows.append(N263)
    rows.append(N266)
    rows.append(N269)
    rows.append(N272)
    rows.append(N275)
    rows.append(N278)
    rows.append(N281)
    rows.append(N284)
    rows.append(N287)
    rows.append(N290)
    rows.append(N294)
    rows.append(N297)
    rows.append(N301)
    rows.append(N305)
    rows.append(N309)
    rows.append(N313)
    rows.append(N316)
    rows.append(N319)
    rows.append(N322)
    rows.append(N325)
    rows.append(N328)
    rows.append(N331)
    rows.append(N334)
    rows.append(N337)
    rows.append(N340)
    rows.append(N343)
    rows.append(N346)
    rows.append(N349)
    rows.append(N352)
    rows.append(N355)
    rows.append(N143_I)
    rows.append(N144_I)
    rows.append(N145_I)
    rows.append(N146_I)
    rows.append(N147_I)
    rows.append(N148_I)
    rows.append(N149_I)
    rows.append(N150_I)
    rows.append(N151_I)
    rows.append(N152_I)
    rows.append(N153_I)
    rows.append(N154_I)
    rows.append(N155_I)
    rows.append(N156_I)
    rows.append(N157_I)
    rows.append(N158_I)
    rows.append(N159_I)
    rows.append(N160_I)
    rows.append(N161_I)
    rows.append(N162_I)
    rows.append(N163_I)
    rows.append(N164_I)
    rows.append(N165_I)
    rows.append(N166_I)
    rows.append(N167_I)
    rows.append(N168_I)
    rows.append(N169_I)
    rows.append(N170_I)
    rows.append(N171_I)
    rows.append(N172_I)
    rows.append(N173_I)
    rows.append(N174_I)
    rows.append(N175_I)
    rows.append(N176_I)
    rows.append(N177_I)
    rows.append(N178_I)
    rows.append(N179_I)
    rows.append(N180_I)
    rows.append(N181_I)
    rows.append(N182_I)
    rows.append(N183_I)
    rows.append(N184_I)
    rows.append(N185_I)
    rows.append(N186_I)
    rows.append(N187_I)
    rows.append(N188_I)
    rows.append(N189_I)
    rows.append(N190_I)
    rows.append(N191_I)
    rows.append(N192_I)
    rows.append(N193_I)
    rows.append(N194_I)
    rows.append(N195_I)
    rows.append(N196_I)
    rows.append(N197_I)
    rows.append(N198_I)
    rows.append(N199_I)
    rows.append(N200_I)
    rows.append(N201_I)
    rows.append(N202_I)
    rows.append(N203_I)
    rows.append(N204_I)
    rows.append(N205_I)
    rows.append(N206_I)
    rows.append(N207_I)
    rows.append(N208_I)
    rows.append(N209_I)
    rows.append(N210_I)
    rows.append(N211_I)
    rows.append(N212_I)
    rows.append(N213_I)
    rows.append(N214_I)
    rows.append(N215_I)
    rows.append(N216_I)
    rows.append(N217_I)
    rows.append(N218_I)

    #output rows
    rows.append(N398)
    rows.append(N400)
    rows.append(N401)
    rows.append(N419)
    rows.append(N420)
    rows.append(N456)
    rows.append(N457)
    rows.append(N458)
    rows.append(N487)
    rows.append(N488)
    rows.append(N489)
    rows.append(N490)
    rows.append(N491)
    rows.append(N492)
    rows.append(N493)
    rows.append(N494)
    rows.append(N792)
    rows.append(N799)
    rows.append(N805)
    rows.append(N1026)
    rows.append(N1028)
    rows.append(N1029)
    rows.append(N1269)
    rows.append(N1277)
    rows.append(N1448)
    rows.append(N1726)
    rows.append(N1816)
    rows.append(N1817)
    rows.append(N1818)
    rows.append(N1819)
    rows.append(N1820)
    rows.append(N1821)
    rows.append(N1969)
    rows.append(N1970)
    rows.append(N1971)
    rows.append(N2010)
    rows.append(N2012)
    rows.append(N2014)
    rows.append(N2016)
    rows.append(N2018)
    rows.append(N2020)
    rows.append(N2022)
    rows.append(N2387)
    rows.append(N2388)
    rows.append(N2389)
    rows.append(N2390)
    rows.append(N2496)
    rows.append(N2643)
    rows.append(N2644)
    rows.append(N2891)
    rows.append(N2925)
    rows.append(N2970)
    rows.append(N2971)
    rows.append(N3038)
    rows.append(N3079)
    rows.append(N3546)
    rows.append(N3671)
    rows.append(N3803)
    rows.append(N3804)
    rows.append(N3809)
    rows.append(N3851)
    rows.append(N3875)
    rows.append(N3881)
    rows.append(N3882)
    rows.append(N143_O)
    rows.append(N144_O)
    rows.append(N145_O)
    rows.append(N146_O)
    rows.append(N147_O)
    rows.append(N148_O)
    rows.append(N149_O)
    rows.append(N150_O)
    rows.append(N151_O)
    rows.append(N152_O)
    rows.append(N153_O)
    rows.append(N154_O)
    rows.append(N155_O)
    rows.append(N156_O)
    rows.append(N157_O)
    rows.append(N158_O)
    rows.append(N159_O)
    rows.append(N160_O)
    rows.append(N161_O)
    rows.append(N162_O)
    rows.append(N163_O)
    rows.append(N164_O)
    rows.append(N165_O)
    rows.append(N166_O)
    rows.append(N167_O)
    rows.append(N168_O)
    rows.append(N169_O)
    rows.append(N170_O)
    rows.append(N171_O)
    rows.append(N172_O)
    rows.append(N173_O)
    rows.append(N174_O)
    rows.append(N175_O)
    rows.append(N176_O)
    rows.append(N177_O)
    rows.append(N178_O)
    rows.append(N179_O)
    rows.append(N180_O)
    rows.append(N181_O)
    rows.append(N182_O)
    rows.append(N183_O)
    rows.append(N184_O)
    rows.append(N185_O)
    rows.append(N186_O)
    rows.append(N187_O)
    rows.append(N188_O)
    rows.append(N189_O)
    rows.append(N190_O)
    rows.append(N191_O)
    rows.append(N192_O)
    rows.append(N193_O)
    rows.append(N194_O)
    rows.append(N195_O)
    rows.append(N196_O)
    rows.append(N197_O)
    rows.append(N198_O)
    rows.append(N199_O)
    rows.append(N200_O)
    rows.append(N201_O)
    rows.append(N202_O)
    rows.append(N203_O)
    rows.append(N204_O)
    rows.append(N205_O)
    rows.append(N206_O)
    rows.append(N207_O)
    rows.append(N208_O)
    rows.append(N209_O)
    rows.append(N210_O)
    rows.append(N211_O)
    rows.append(N212_O)
    rows.append(N213_O)
    rows.append(N214_O)
    rows.append(N215_O)
    rows.append(N216_O)
    rows.append(N217_O)
    rows.append(N218_O)

    #golden output rows
    rows.append(N398g)
    rows.append(N400g)
    rows.append(N401g)
    rows.append(N419g)
    rows.append(N420g)
    rows.append(N456g)
    rows.append(N457g)
    rows.append(N458g)
    rows.append(N487g)
    rows.append(N488g)
    rows.append(N489g)
    rows.append(N490g)
    rows.append(N491g)
    rows.append(N492g)
    rows.append(N493g)
    rows.append(N494g)
    rows.append(N792g)
    rows.append(N799g)
    rows.append(N805g)
    rows.append(N1026g)
    rows.append(N1028g)
    rows.append(N1029g)
    rows.append(N1269g)
    rows.append(N1277g)
    rows.append(N1448g)
    rows.append(N1726g)
    rows.append(N1816g)
    rows.append(N1817g)
    rows.append(N1818g)
    rows.append(N1819g)
    rows.append(N1820g)
    rows.append(N1821g)
    rows.append(N1969g)
    rows.append(N1970g)
    rows.append(N1971g)
    rows.append(N2010g)
    rows.append(N2012g)
    rows.append(N2014g)
    rows.append(N2016g)
    rows.append(N2018g)
    rows.append(N2020g)
    rows.append(N2022g)
    rows.append(N2387g)
    rows.append(N2388g)
    rows.append(N2389g)
    rows.append(N2390g)
    rows.append(N2496g)
    rows.append(N2643g)
    rows.append(N2644g)
    rows.append(N2891g)
    rows.append(N2925g)
    rows.append(N2970g)
    rows.append(N2971g)
    rows.append(N3038g)
    rows.append(N3079g)
    rows.append(N3546g)
    rows.append(N3671g)
    rows.append(N3803g)
    rows.append(N3804g)
    rows.append(N3809g)
    rows.append(N3851g)
    rows.append(N3875g)
    rows.append(N3881g)
    rows.append(N3882g)
    rows.append(N143_Og)
    rows.append(N144_Og)
    rows.append(N145_Og)
    rows.append(N146_Og)
    rows.append(N147_Og)
    rows.append(N148_Og)
    rows.append(N149_Og)
    rows.append(N150_Og)
    rows.append(N151_Og)
    rows.append(N152_Og)
    rows.append(N153_Og)
    rows.append(N154_Og)
    rows.append(N155_Og)
    rows.append(N156_Og)
    rows.append(N157_Og)
    rows.append(N158_Og)
    rows.append(N159_Og)
    rows.append(N160_Og)
    rows.append(N161_Og)
    rows.append(N162_Og)
    rows.append(N163_Og)
    rows.append(N164_Og)
    rows.append(N165_Og)
    rows.append(N166_Og)
    rows.append(N167_Og)
    rows.append(N168_Og)
    rows.append(N169_Og)
    rows.append(N170_Og)
    rows.append(N171_Og)
    rows.append(N172_Og)
    rows.append(N173_Og)
    rows.append(N174_Og)
    rows.append(N175_Og)
    rows.append(N176_Og)
    rows.append(N177_Og)
    rows.append(N178_Og)
    rows.append(N179_Og)
    rows.append(N180_Og)
    rows.append(N181_Og)
    rows.append(N182_Og)
    rows.append(N183_Og)
    rows.append(N184_Og)
    rows.append(N185_Og)
    rows.append(N186_Og)
    rows.append(N187_Og)
    rows.append(N188_Og)
    rows.append(N189_Og)
    rows.append(N190_Og)
    rows.append(N191_Og)
    rows.append(N192_Og)
    rows.append(N193_Og)
    rows.append(N194_Og)
    rows.append(N195_Og)
    rows.append(N196_Og)
    rows.append(N197_Og)
    rows.append(N198_Og)
    rows.append(N199_Og)
    rows.append(N200_Og)
    rows.append(N201_Og)
    rows.append(N202_Og)
    rows.append(N203_Og)
    rows.append(N204_Og)
    rows.append(N205_Og)
    rows.append(N206_Og)
    rows.append(N207_Og)
    rows.append(N208_Og)
    rows.append(N209_Og)
    rows.append(N210_Og)
    rows.append(N211_Og)
    rows.append(N212_Og)
    rows.append(N213_Og)
    rows.append(N214_Og)
    rows.append(N215_Og)
    rows.append(N216_Og)
    rows.append(N217_Og)
    rows.append(N218_Og)

    #print(rows)
    final_compare = final_compare.append(pd.Series(rows, index = ["Clk", "Node", "N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8", "N11", "N14", "N15", "N16", "N19", "N20", "N21", "N22", "N23", "N24", "N25", "N26", "N27", "N28", "N29", "N32", "N33", "N34", "N35", "N36", "N37", "N40", "N43", "N44", "N47", "N48", "N49", "N50", "N51", "N52", "N53", "N54", "N55", "N56", "N57", "N60", "N61", "N62", "N63", "N64", "N65", "N66", "N67", "N68", "N69", "N72", "N73", "N74", "N75", "N76", "N77", "N78", "N79", "N80", "N81", "N82", "N85", "N86", "N87", "N88", "N89", "N90", "N91", "N92", "N93", "N94", "N95", "N96", "N99", "N100", "N101", "N102", "N103", "N104", "N105", "N106", "N107", "N108", "N111", "N112", "N113", "N114", "N115", "N116", "N117", "N118", "N119", "N120", "N123", "N124", "N125", "N126", "N127", "N128", "N129", "N130", "N131", "N132", "N135", "N136", "N137", "N138", "N139", "N140", "N141", "N142", "N219", "N224", "N227", "N230", "N231", "N234", "N237", "N241", "N246", "N253", "N256", "N259", "N262", "N263", "N266", "N269", "N272", "N275", "N278", "N281", "N284", "N287", "N290", "N294", "N297", "N301", "N305", "N309", "N313", "N316", "N319", "N322", "N325", "N328", "N331", "N334", "N337", "N340", "N343", "N346", "N349", "N352", "N355", "N143_I", "N144_I", "N145_I", "N146_I", "N147_I", "N148_I", "N149_I", "N150_I", "N151_I", "N152_I", "N153_I", "N154_I", "N155_I", "N156_I", "N157_I", "N158_I", "N159_I", "N160_I", "N161_I", "N162_I", "N163_I", "N164_I", "N165_I", "N166_I", "N167_I", "N168_I", "N169_I", "N170_I", "N171_I", "N172_I", "N173_I", "N174_I", "N175_I", "N176_I", "N177_I", "N178_I", "N179_I", "N180_I", "N181_I", "N182_I", "N183_I", "N184_I", "N185_I", "N186_I", "N187_I", "N188_I", "N189_I", "N190_I", "N191_I", "N192_I", "N193_I", "N194_I", "N195_I", "N196_I", "N197_I", "N198_I", "N199_I", "N200_I", "N201_I", "N202_I", "N203_I", "N204_I", "N205_I", "N206_I", "N207_I", "N208_I", "N209_I", "N210_I", "N211_I", "N212_I", "N213_I", "N214_I", "N215_I", "N216_I", "N217_I", "N218_I", "N398", "N400", "N401", "N419", "N420", "N456", "N457", "N458", "N487", "N488", "N489", "N490", "N491", "N492", "N493", "N494", "N792", "N799", "N805", "N1026", "N1028", "N1029", "N1269", "N1277", "N1448", "N1726", "N1816", "N1817", "N1818", "N1819", "N1820", "N1821", "N1969", "N1970", "N1971", "N2010", "N2012", "N2014", "N2016", "N2018", "N2020", "N2022", "N2387", "N2388", "N2389", "N2390", "N2496", "N2643", "N2644", "N2891", "N2925", "N2970", "N2971", "N3038", "N3079", "N3546", "N3671", "N3803", "N3804", "N3809", "N3851", "N3875", "N3881", "N3882", "N143_O", "N144_O", "N145_O", "N146_O", "N147_O", "N148_O", "N149_O", "N150_O", "N151_O", "N152_O", "N153_O", "N154_O", "N155_O", "N156_O", "N157_O", "N158_O", "N159_O", "N160_O", "N161_O", "N162_O", "N163_O", "N164_O", "N165_O", "N166_O", "N167_O", "N168_O", "N169_O", "N170_O", "N171_O", "N172_O", "N173_O", "N174_O", "N175_O", "N176_O", "N177_O", "N178_O", "N179_O", "N180_O", "N181_O", "N182_O", "N183_O", "N184_O", "N185_O", "N186_O", "N187_O", "N188_O", "N189_O", "N190_O", "N191_O", "N192_O", "N193_O", "N194_O", "N195_O", "N196_O", "N197_O", "N198_O", "N199_O", "N200_O", "N201_O", "N202_O", "N203_O", "N204_O", "N205_O", "N206_O", "N207_O", "N208_O", "N209_O", "N210_O", "N211_O", "N212_O", "N213_O", "N214_O", "N215_O", "N216_O", "N217_O", "N218_O", "N398g", "N400g", "N401g", "N419g", "N420g", "N456g", "N457g", "N458g", "N487g", "N488g", "N489g", "N490g", "N491g", "N492g", "N493g", "N494g", "N792g", "N799g", "N805g", "N1026g", "N1028g", "N1029g", "N1269g", "N1277g", "N1448g", "N1726g", "N1816g", "N1817g", "N1818g", "N1819g", "N1820g", "N1821g", "N1969g", "N1970g", "N1971g", "N2010g", "N2012g", "N2014g", "N2016g", "N2018g", "N2020g", "N2022g", "N2387g", "N2388g", "N2389g", "N2390g", "N2496g", "N2643g", "N2644g", "N2891g", "N2925g", "N2970g", "N2971g", "N3038g", "N3079g", "N3546g", "N3671g", "N3803g", "N3804g", "N3809g", "N3851g", "N3875g", "N3881g", "N3882g", "N143_Og", "N144_Og", "N145_Og", "N146_Og", "N147_Og", "N148_Og", "N149_Og", "N150_Og", "N151_Og", "N152_Og", "N153_Og", "N154_Og", "N155_Og", "N156_Og", "N157_Og", "N158_Og", "N159_Og", "N160_Og", "N161_Og", "N162_Og", "N163_Og", "N164_Og", "N165_Og", "N166_Og", "N167_Og", "N168_Og", "N169_Og", "N170_Og", "N171_Og", "N172_Og", "N173_Og", "N174_Og", "N175_Og", "N176_Og", "N177_Og", "N178_Og", "N179_Og", "N180_Og", "N181_Og", "N182_Og", "N183_Og", "N184_Og", "N185_Og", "N186_Og", "N187_Og", "N188_Og", "N189_Og", "N190_Og", "N191_Og", "N192_Og", "N193_Og", "N194_Og", "N195_Og", "N196_Og", "N197_Og", "N198_Og", "N199_Og", "N200_Og", "N201_Og", "N202_Og", "N203_Og", "N204_Og", "N205_Og", "N206_Og", "N207_Og", "N208_Og", "N209_Og", "N210_Og", "N211_Og", "N212_Og", "N213_Og", "N214_Og", "N215_Og", "N216_Og", "N217_Og", "N218_Og"]), ignore_index=True)
##---------------------------------------------------------------------------------
#print(final_compare)

N398_Comp = pd.to_numeric(final_compare['N398']) != pd.to_numeric(final_compare['N398g'])
N398_Comp = N398_Comp.astype(int)
N400_Comp = pd.to_numeric(final_compare['N400']) != pd.to_numeric(final_compare['N400g'])
N400_Comp = N400_Comp.astype(int)
N401_Comp = pd.to_numeric(final_compare['N401']) != pd.to_numeric(final_compare['N401g'])
N401_Comp = N401_Comp.astype(int)
N419_Comp = pd.to_numeric(final_compare['N419']) != pd.to_numeric(final_compare['N419g'])
N419_Comp = N419_Comp.astype(int)
N420_Comp = pd.to_numeric(final_compare['N420']) != pd.to_numeric(final_compare['N420g'])
N420_Comp = N420_Comp.astype(int)
N456_Comp = pd.to_numeric(final_compare['N456']) != pd.to_numeric(final_compare['N456g'])
N456_Comp = N456_Comp.astype(int)
N457_Comp = pd.to_numeric(final_compare['N457']) != pd.to_numeric(final_compare['N457g'])
N457_Comp = N457_Comp.astype(int)
N458_Comp = pd.to_numeric(final_compare['N458']) != pd.to_numeric(final_compare['N458g'])
N458_Comp = N458_Comp.astype(int)
N487_Comp = pd.to_numeric(final_compare['N487']) != pd.to_numeric(final_compare['N487g'])
N487_Comp = N487_Comp.astype(int)
N488_Comp = pd.to_numeric(final_compare['N488']) != pd.to_numeric(final_compare['N488g'])
N488_Comp = N488_Comp.astype(int)
N489_Comp = pd.to_numeric(final_compare['N489']) != pd.to_numeric(final_compare['N489g'])
N489_Comp = N489_Comp.astype(int)
N490_Comp = pd.to_numeric(final_compare['N490']) != pd.to_numeric(final_compare['N490g'])
N490_Comp = N490_Comp.astype(int)
N491_Comp = pd.to_numeric(final_compare['N491']) != pd.to_numeric(final_compare['N491g'])
N491_Comp = N491_Comp.astype(int)
N492_Comp = pd.to_numeric(final_compare['N492']) != pd.to_numeric(final_compare['N492g'])
N492_Comp = N492_Comp.astype(int)
N493_Comp = pd.to_numeric(final_compare['N493']) != pd.to_numeric(final_compare['N493g'])
N493_Comp = N493_Comp.astype(int)
N494_Comp = pd.to_numeric(final_compare['N494']) != pd.to_numeric(final_compare['N494g'])
N494_Comp = N494_Comp.astype(int)
N792_Comp = pd.to_numeric(final_compare['N792']) != pd.to_numeric(final_compare['N792g'])
N792_Comp = N792_Comp.astype(int)
N799_Comp = pd.to_numeric(final_compare['N799']) != pd.to_numeric(final_compare['N799g'])
N799_Comp = N799_Comp.astype(int)
N805_Comp = pd.to_numeric(final_compare['N805']) != pd.to_numeric(final_compare['N805g'])
N805_Comp = N805_Comp.astype(int)
N1026_Comp = pd.to_numeric(final_compare['N1026']) != pd.to_numeric(final_compare['N1026g'])
N1026_Comp = N1026_Comp.astype(int)
N1028_Comp = pd.to_numeric(final_compare['N1028']) != pd.to_numeric(final_compare['N1028g'])
N1028_Comp = N1028_Comp.astype(int)
N1029_Comp = pd.to_numeric(final_compare['N1029']) != pd.to_numeric(final_compare['N1029g'])
N1029_Comp = N1029_Comp.astype(int)
N1269_Comp = pd.to_numeric(final_compare['N1269']) != pd.to_numeric(final_compare['N1269g'])
N1269_Comp = N1269_Comp.astype(int)
N1277_Comp = pd.to_numeric(final_compare['N1277']) != pd.to_numeric(final_compare['N1277g'])
N1277_Comp = N1277_Comp.astype(int)
N1448_Comp = pd.to_numeric(final_compare['N1448']) != pd.to_numeric(final_compare['N1448g'])
N1448_Comp = N1448_Comp.astype(int)
N1726_Comp = pd.to_numeric(final_compare['N1726']) != pd.to_numeric(final_compare['N1726g'])
N1726_Comp = N1726_Comp.astype(int)
N1816_Comp = pd.to_numeric(final_compare['N1816']) != pd.to_numeric(final_compare['N1816g'])
N1816_Comp = N1816_Comp.astype(int)
N1817_Comp = pd.to_numeric(final_compare['N1817']) != pd.to_numeric(final_compare['N1817g'])
N1817_Comp = N1817_Comp.astype(int)
N1818_Comp = pd.to_numeric(final_compare['N1818']) != pd.to_numeric(final_compare['N1818g'])
N1818_Comp = N1818_Comp.astype(int)
N1819_Comp = pd.to_numeric(final_compare['N1819']) != pd.to_numeric(final_compare['N1819g'])
N1819_Comp = N1819_Comp.astype(int)
N1820_Comp = pd.to_numeric(final_compare['N1820']) != pd.to_numeric(final_compare['N1820g'])
N1820_Comp = N1820_Comp.astype(int)
N1821_Comp = pd.to_numeric(final_compare['N1821']) != pd.to_numeric(final_compare['N1821g'])
N1821_Comp = N1821_Comp.astype(int)
N1969_Comp = pd.to_numeric(final_compare['N1969']) != pd.to_numeric(final_compare['N1969g'])
N1969_Comp = N1969_Comp.astype(int)
N1970_Comp = pd.to_numeric(final_compare['N1970']) != pd.to_numeric(final_compare['N1970g'])
N1970_Comp = N1970_Comp.astype(int)
N1971_Comp = pd.to_numeric(final_compare['N1971']) != pd.to_numeric(final_compare['N1971g'])
N1971_Comp = N1971_Comp.astype(int)
N2010_Comp = pd.to_numeric(final_compare['N2010']) != pd.to_numeric(final_compare['N2010g'])
N2010_Comp = N2010_Comp.astype(int)
N2012_Comp = pd.to_numeric(final_compare['N2012']) != pd.to_numeric(final_compare['N2012g'])
N2012_Comp = N2012_Comp.astype(int)
N2014_Comp = pd.to_numeric(final_compare['N2014']) != pd.to_numeric(final_compare['N2014g'])
N2014_Comp = N2014_Comp.astype(int)
N2016_Comp = pd.to_numeric(final_compare['N2016']) != pd.to_numeric(final_compare['N2016g'])
N2016_Comp = N2016_Comp.astype(int)
N2018_Comp = pd.to_numeric(final_compare['N2018']) != pd.to_numeric(final_compare['N2018g'])
N2018_Comp = N2018_Comp.astype(int)
N2020_Comp = pd.to_numeric(final_compare['N2020']) != pd.to_numeric(final_compare['N2020g'])
N2020_Comp = N2020_Comp.astype(int)
N2022_Comp = pd.to_numeric(final_compare['N2022']) != pd.to_numeric(final_compare['N2022g'])
N2022_Comp = N2022_Comp.astype(int)
N2387_Comp = pd.to_numeric(final_compare['N2387']) != pd.to_numeric(final_compare['N2387g'])
N2387_Comp = N2387_Comp.astype(int)
N2388_Comp = pd.to_numeric(final_compare['N2388']) != pd.to_numeric(final_compare['N2388g'])
N2388_Comp = N2388_Comp.astype(int)
N2389_Comp = pd.to_numeric(final_compare['N2389']) != pd.to_numeric(final_compare['N2389g'])
N2389_Comp = N2389_Comp.astype(int)
N2390_Comp = pd.to_numeric(final_compare['N2390']) != pd.to_numeric(final_compare['N2390g'])
N2390_Comp = N2390_Comp.astype(int)
N2496_Comp = pd.to_numeric(final_compare['N2496']) != pd.to_numeric(final_compare['N2496g'])
N2496_Comp = N2496_Comp.astype(int)
N2643_Comp = pd.to_numeric(final_compare['N2643']) != pd.to_numeric(final_compare['N2643g'])
N2643_Comp = N2643_Comp.astype(int)
N2644_Comp = pd.to_numeric(final_compare['N2644']) != pd.to_numeric(final_compare['N2644g'])
N2644_Comp = N2644_Comp.astype(int)
N2891_Comp = pd.to_numeric(final_compare['N2891']) != pd.to_numeric(final_compare['N2891g'])
N2891_Comp = N2891_Comp.astype(int)
N2925_Comp = pd.to_numeric(final_compare['N2925']) != pd.to_numeric(final_compare['N2925g'])
N2925_Comp = N2925_Comp.astype(int)
N2970_Comp = pd.to_numeric(final_compare['N2970']) != pd.to_numeric(final_compare['N2970g'])
N2970_Comp = N2970_Comp.astype(int)
N2971_Comp = pd.to_numeric(final_compare['N2971']) != pd.to_numeric(final_compare['N2971g'])
N2971_Comp = N2971_Comp.astype(int)
N3038_Comp = pd.to_numeric(final_compare['N3038']) != pd.to_numeric(final_compare['N3038g'])
N3038_Comp = N3038_Comp.astype(int)
N3079_Comp = pd.to_numeric(final_compare['N3079']) != pd.to_numeric(final_compare['N3079g'])
N3079_Comp = N3079_Comp.astype(int)
N3546_Comp = pd.to_numeric(final_compare['N3546']) != pd.to_numeric(final_compare['N3546g'])
N3546_Comp = N3546_Comp.astype(int)
N3671_Comp = pd.to_numeric(final_compare['N3671']) != pd.to_numeric(final_compare['N3671g'])
N3671_Comp = N3671_Comp.astype(int)
N3803_Comp = pd.to_numeric(final_compare['N3803']) != pd.to_numeric(final_compare['N3803g'])
N3803_Comp = N3803_Comp.astype(int)
N3804_Comp = pd.to_numeric(final_compare['N3804']) != pd.to_numeric(final_compare['N3804g'])
N3804_Comp = N3804_Comp.astype(int)
N3809_Comp = pd.to_numeric(final_compare['N3809']) != pd.to_numeric(final_compare['N3809g'])
N3809_Comp = N3809_Comp.astype(int)
N3851_Comp = pd.to_numeric(final_compare['N3851']) != pd.to_numeric(final_compare['N3851g'])
N3851_Comp = N3851_Comp.astype(int)
N3875_Comp = pd.to_numeric(final_compare['N3875']) != pd.to_numeric(final_compare['N3875g'])
N3875_Comp = N3875_Comp.astype(int)
N3881_Comp = pd.to_numeric(final_compare['N3881']) != pd.to_numeric(final_compare['N3881g'])
N3881_Comp = N3881_Comp.astype(int)
N3882_Comp = pd.to_numeric(final_compare['N3882']) != pd.to_numeric(final_compare['N3882g'])
N3882_Comp = N3882_Comp.astype(int)
N143_O_Comp = pd.to_numeric(final_compare['N143_O']) != pd.to_numeric(final_compare['N143_Og'])
N143_O_Comp = N143_O_Comp.astype(int)
N144_O_Comp = pd.to_numeric(final_compare['N144_O']) != pd.to_numeric(final_compare['N144_Og'])
N144_O_Comp = N144_O_Comp.astype(int)
N145_O_Comp = pd.to_numeric(final_compare['N145_O']) != pd.to_numeric(final_compare['N145_Og'])
N145_O_Comp = N145_O_Comp.astype(int)
N146_O_Comp = pd.to_numeric(final_compare['N146_O']) != pd.to_numeric(final_compare['N146_Og'])
N146_O_Comp = N146_O_Comp.astype(int)
N147_O_Comp = pd.to_numeric(final_compare['N147_O']) != pd.to_numeric(final_compare['N147_Og'])
N147_O_Comp = N147_O_Comp.astype(int)
N148_O_Comp = pd.to_numeric(final_compare['N148_O']) != pd.to_numeric(final_compare['N148_Og'])
N148_O_Comp = N148_O_Comp.astype(int)
N149_O_Comp = pd.to_numeric(final_compare['N149_O']) != pd.to_numeric(final_compare['N149_Og'])
N149_O_Comp = N149_O_Comp.astype(int)
N150_O_Comp = pd.to_numeric(final_compare['N150_O']) != pd.to_numeric(final_compare['N150_Og'])
N150_O_Comp = N150_O_Comp.astype(int)
N151_O_Comp = pd.to_numeric(final_compare['N151_O']) != pd.to_numeric(final_compare['N151_Og'])
N151_O_Comp = N151_O_Comp.astype(int)
N152_O_Comp = pd.to_numeric(final_compare['N152_O']) != pd.to_numeric(final_compare['N152_Og'])
N152_O_Comp = N152_O_Comp.astype(int)
N153_O_Comp = pd.to_numeric(final_compare['N153_O']) != pd.to_numeric(final_compare['N153_Og'])
N153_O_Comp = N153_O_Comp.astype(int)
N154_O_Comp = pd.to_numeric(final_compare['N154_O']) != pd.to_numeric(final_compare['N154_Og'])
N154_O_Comp = N154_O_Comp.astype(int)
N155_O_Comp = pd.to_numeric(final_compare['N155_O']) != pd.to_numeric(final_compare['N155_Og'])
N155_O_Comp = N155_O_Comp.astype(int)
N156_O_Comp = pd.to_numeric(final_compare['N156_O']) != pd.to_numeric(final_compare['N156_Og'])
N156_O_Comp = N156_O_Comp.astype(int)
N157_O_Comp = pd.to_numeric(final_compare['N157_O']) != pd.to_numeric(final_compare['N157_Og'])
N157_O_Comp = N157_O_Comp.astype(int)
N158_O_Comp = pd.to_numeric(final_compare['N158_O']) != pd.to_numeric(final_compare['N158_Og'])
N158_O_Comp = N158_O_Comp.astype(int)
N159_O_Comp = pd.to_numeric(final_compare['N159_O']) != pd.to_numeric(final_compare['N159_Og'])
N159_O_Comp = N159_O_Comp.astype(int)
N160_O_Comp = pd.to_numeric(final_compare['N160_O']) != pd.to_numeric(final_compare['N160_Og'])
N160_O_Comp = N160_O_Comp.astype(int)
N161_O_Comp = pd.to_numeric(final_compare['N161_O']) != pd.to_numeric(final_compare['N161_Og'])
N161_O_Comp = N161_O_Comp.astype(int)
N162_O_Comp = pd.to_numeric(final_compare['N162_O']) != pd.to_numeric(final_compare['N162_Og'])
N162_O_Comp = N162_O_Comp.astype(int)
N163_O_Comp = pd.to_numeric(final_compare['N163_O']) != pd.to_numeric(final_compare['N163_Og'])
N163_O_Comp = N163_O_Comp.astype(int)
N164_O_Comp = pd.to_numeric(final_compare['N164_O']) != pd.to_numeric(final_compare['N164_Og'])
N164_O_Comp = N164_O_Comp.astype(int)
N165_O_Comp = pd.to_numeric(final_compare['N165_O']) != pd.to_numeric(final_compare['N165_Og'])
N165_O_Comp = N165_O_Comp.astype(int)
N166_O_Comp = pd.to_numeric(final_compare['N166_O']) != pd.to_numeric(final_compare['N166_Og'])
N166_O_Comp = N166_O_Comp.astype(int)
N167_O_Comp = pd.to_numeric(final_compare['N167_O']) != pd.to_numeric(final_compare['N167_Og'])
N167_O_Comp = N167_O_Comp.astype(int)
N168_O_Comp = pd.to_numeric(final_compare['N168_O']) != pd.to_numeric(final_compare['N168_Og'])
N168_O_Comp = N168_O_Comp.astype(int)
N169_O_Comp = pd.to_numeric(final_compare['N169_O']) != pd.to_numeric(final_compare['N169_Og'])
N169_O_Comp = N169_O_Comp.astype(int)
N170_O_Comp = pd.to_numeric(final_compare['N170_O']) != pd.to_numeric(final_compare['N170_Og'])
N170_O_Comp = N170_O_Comp.astype(int)
N171_O_Comp = pd.to_numeric(final_compare['N171_O']) != pd.to_numeric(final_compare['N171_Og'])
N171_O_Comp = N171_O_Comp.astype(int)
N172_O_Comp = pd.to_numeric(final_compare['N172_O']) != pd.to_numeric(final_compare['N172_Og'])
N172_O_Comp = N172_O_Comp.astype(int)
N173_O_Comp = pd.to_numeric(final_compare['N173_O']) != pd.to_numeric(final_compare['N173_Og'])
N173_O_Comp = N173_O_Comp.astype(int)
N174_O_Comp = pd.to_numeric(final_compare['N174_O']) != pd.to_numeric(final_compare['N174_Og'])
N174_O_Comp = N174_O_Comp.astype(int)
N175_O_Comp = pd.to_numeric(final_compare['N175_O']) != pd.to_numeric(final_compare['N175_Og'])
N175_O_Comp = N175_O_Comp.astype(int)
N176_O_Comp = pd.to_numeric(final_compare['N176_O']) != pd.to_numeric(final_compare['N176_Og'])
N176_O_Comp = N176_O_Comp.astype(int)
N177_O_Comp = pd.to_numeric(final_compare['N177_O']) != pd.to_numeric(final_compare['N177_Og'])
N177_O_Comp = N177_O_Comp.astype(int)
N178_O_Comp = pd.to_numeric(final_compare['N178_O']) != pd.to_numeric(final_compare['N178_Og'])
N178_O_Comp = N178_O_Comp.astype(int)
N179_O_Comp = pd.to_numeric(final_compare['N179_O']) != pd.to_numeric(final_compare['N179_Og'])
N179_O_Comp = N179_O_Comp.astype(int)
N180_O_Comp = pd.to_numeric(final_compare['N180_O']) != pd.to_numeric(final_compare['N180_Og'])
N180_O_Comp = N180_O_Comp.astype(int)
N181_O_Comp = pd.to_numeric(final_compare['N181_O']) != pd.to_numeric(final_compare['N181_Og'])
N181_O_Comp = N181_O_Comp.astype(int)
N182_O_Comp = pd.to_numeric(final_compare['N182_O']) != pd.to_numeric(final_compare['N182_Og'])
N182_O_Comp = N182_O_Comp.astype(int)
N183_O_Comp = pd.to_numeric(final_compare['N183_O']) != pd.to_numeric(final_compare['N183_Og'])
N183_O_Comp = N183_O_Comp.astype(int)
N184_O_Comp = pd.to_numeric(final_compare['N184_O']) != pd.to_numeric(final_compare['N184_Og'])
N184_O_Comp = N184_O_Comp.astype(int)
N185_O_Comp = pd.to_numeric(final_compare['N185_O']) != pd.to_numeric(final_compare['N185_Og'])
N185_O_Comp = N185_O_Comp.astype(int)
N186_O_Comp = pd.to_numeric(final_compare['N186_O']) != pd.to_numeric(final_compare['N186_Og'])
N186_O_Comp = N186_O_Comp.astype(int)
N187_O_Comp = pd.to_numeric(final_compare['N187_O']) != pd.to_numeric(final_compare['N187_Og'])
N187_O_Comp = N187_O_Comp.astype(int)
N188_O_Comp = pd.to_numeric(final_compare['N188_O']) != pd.to_numeric(final_compare['N188_Og'])
N188_O_Comp = N188_O_Comp.astype(int)
N189_O_Comp = pd.to_numeric(final_compare['N189_O']) != pd.to_numeric(final_compare['N189_Og'])
N189_O_Comp = N189_O_Comp.astype(int)
N190_O_Comp = pd.to_numeric(final_compare['N190_O']) != pd.to_numeric(final_compare['N190_Og'])
N190_O_Comp = N190_O_Comp.astype(int)
N191_O_Comp = pd.to_numeric(final_compare['N191_O']) != pd.to_numeric(final_compare['N191_Og'])
N191_O_Comp = N191_O_Comp.astype(int)
N192_O_Comp = pd.to_numeric(final_compare['N192_O']) != pd.to_numeric(final_compare['N192_Og'])
N192_O_Comp = N192_O_Comp.astype(int)
N193_O_Comp = pd.to_numeric(final_compare['N193_O']) != pd.to_numeric(final_compare['N193_Og'])
N193_O_Comp = N193_O_Comp.astype(int)
N194_O_Comp = pd.to_numeric(final_compare['N194_O']) != pd.to_numeric(final_compare['N194_Og'])
N194_O_Comp = N194_O_Comp.astype(int)
N195_O_Comp = pd.to_numeric(final_compare['N195_O']) != pd.to_numeric(final_compare['N195_Og'])
N195_O_Comp = N195_O_Comp.astype(int)
N196_O_Comp = pd.to_numeric(final_compare['N196_O']) != pd.to_numeric(final_compare['N196_Og'])
N196_O_Comp = N196_O_Comp.astype(int)
N197_O_Comp = pd.to_numeric(final_compare['N197_O']) != pd.to_numeric(final_compare['N197_Og'])
N197_O_Comp = N197_O_Comp.astype(int)
N198_O_Comp = pd.to_numeric(final_compare['N198_O']) != pd.to_numeric(final_compare['N198_Og'])
N198_O_Comp = N198_O_Comp.astype(int)
N199_O_Comp = pd.to_numeric(final_compare['N199_O']) != pd.to_numeric(final_compare['N199_Og'])
N199_O_Comp = N199_O_Comp.astype(int)
N200_O_Comp = pd.to_numeric(final_compare['N200_O']) != pd.to_numeric(final_compare['N200_Og'])
N200_O_Comp = N200_O_Comp.astype(int)
N201_O_Comp = pd.to_numeric(final_compare['N201_O']) != pd.to_numeric(final_compare['N201_Og'])
N201_O_Comp = N201_O_Comp.astype(int)
N202_O_Comp = pd.to_numeric(final_compare['N202_O']) != pd.to_numeric(final_compare['N202_Og'])
N202_O_Comp = N202_O_Comp.astype(int)
N203_O_Comp = pd.to_numeric(final_compare['N203_O']) != pd.to_numeric(final_compare['N203_Og'])
N203_O_Comp = N203_O_Comp.astype(int)
N204_O_Comp = pd.to_numeric(final_compare['N204_O']) != pd.to_numeric(final_compare['N204_Og'])
N204_O_Comp = N204_O_Comp.astype(int)
N205_O_Comp = pd.to_numeric(final_compare['N205_O']) != pd.to_numeric(final_compare['N205_Og'])
N205_O_Comp = N205_O_Comp.astype(int)
N206_O_Comp = pd.to_numeric(final_compare['N206_O']) != pd.to_numeric(final_compare['N206_Og'])
N206_O_Comp = N206_O_Comp.astype(int)
N207_O_Comp = pd.to_numeric(final_compare['N207_O']) != pd.to_numeric(final_compare['N207_Og'])
N207_O_Comp = N207_O_Comp.astype(int)
N208_O_Comp = pd.to_numeric(final_compare['N208_O']) != pd.to_numeric(final_compare['N208_Og'])
N208_O_Comp = N208_O_Comp.astype(int)
N209_O_Comp = pd.to_numeric(final_compare['N209_O']) != pd.to_numeric(final_compare['N209_Og'])
N209_O_Comp = N209_O_Comp.astype(int)
N210_O_Comp = pd.to_numeric(final_compare['N210_O']) != pd.to_numeric(final_compare['N210_Og'])
N210_O_Comp = N210_O_Comp.astype(int)
N211_O_Comp = pd.to_numeric(final_compare['N211_O']) != pd.to_numeric(final_compare['N211_Og'])
N211_O_Comp = N211_O_Comp.astype(int)
N212_O_Comp = pd.to_numeric(final_compare['N212_O']) != pd.to_numeric(final_compare['N212_Og'])
N212_O_Comp = N212_O_Comp.astype(int)
N213_O_Comp = pd.to_numeric(final_compare['N213_O']) != pd.to_numeric(final_compare['N213_Og'])
N213_O_Comp = N213_O_Comp.astype(int)
N214_O_Comp = pd.to_numeric(final_compare['N214_O']) != pd.to_numeric(final_compare['N214_Og'])
N214_O_Comp = N214_O_Comp.astype(int)
N215_O_Comp = pd.to_numeric(final_compare['N215_O']) != pd.to_numeric(final_compare['N215_Og'])
N215_O_Comp = N215_O_Comp.astype(int)
N216_O_Comp = pd.to_numeric(final_compare['N216_O']) != pd.to_numeric(final_compare['N216_Og'])
N216_O_Comp = N216_O_Comp.astype(int)
N217_O_Comp = pd.to_numeric(final_compare['N217_O']) != pd.to_numeric(final_compare['N217_Og'])
N217_O_Comp = N217_O_Comp.astype(int)
N218_O_Comp = pd.to_numeric(final_compare['N218_O']) != pd.to_numeric(final_compare['N218_Og'])
N218_O_Comp = N218_O_Comp.astype(int)

final_compare = final_compare.assign(N398_Comp = N398_Comp.values)
final_compare = final_compare.assign(N400_Comp = N400_Comp.values)
final_compare = final_compare.assign(N401_Comp = N401_Comp.values)
final_compare = final_compare.assign(N419_Comp = N419_Comp.values)
final_compare = final_compare.assign(N420_Comp = N420_Comp.values)
final_compare = final_compare.assign(N456_Comp = N456_Comp.values)
final_compare = final_compare.assign(N457_Comp = N457_Comp.values)
final_compare = final_compare.assign(N458_Comp = N458_Comp.values)
final_compare = final_compare.assign(N487_Comp = N487_Comp.values)
final_compare = final_compare.assign(N488_Comp = N488_Comp.values)
final_compare = final_compare.assign(N489_Comp = N489_Comp.values)
final_compare = final_compare.assign(N490_Comp = N490_Comp.values)
final_compare = final_compare.assign(N491_Comp = N491_Comp.values)
final_compare = final_compare.assign(N492_Comp = N492_Comp.values)
final_compare = final_compare.assign(N493_Comp = N493_Comp.values)
final_compare = final_compare.assign(N494_Comp = N494_Comp.values)
final_compare = final_compare.assign(N792_Comp = N792_Comp.values)
final_compare = final_compare.assign(N799_Comp = N799_Comp.values)
final_compare = final_compare.assign(N805_Comp = N805_Comp.values)
final_compare = final_compare.assign(N1026_Comp = N1026_Comp.values)
final_compare = final_compare.assign(N1028_Comp = N1028_Comp.values)
final_compare = final_compare.assign(N1029_Comp = N1029_Comp.values)
final_compare = final_compare.assign(N1269_Comp = N1269_Comp.values)
final_compare = final_compare.assign(N1277_Comp = N1277_Comp.values)
final_compare = final_compare.assign(N1448_Comp = N1448_Comp.values)
final_compare = final_compare.assign(N1726_Comp = N1726_Comp.values)
final_compare = final_compare.assign(N1816_Comp = N1816_Comp.values)
final_compare = final_compare.assign(N1817_Comp = N1817_Comp.values)
final_compare = final_compare.assign(N1818_Comp = N1818_Comp.values)
final_compare = final_compare.assign(N1819_Comp = N1819_Comp.values)
final_compare = final_compare.assign(N1820_Comp = N1820_Comp.values)
final_compare = final_compare.assign(N1821_Comp = N1821_Comp.values)
final_compare = final_compare.assign(N1969_Comp = N1969_Comp.values)
final_compare = final_compare.assign(N1970_Comp = N1970_Comp.values)
final_compare = final_compare.assign(N1971_Comp = N1971_Comp.values)
final_compare = final_compare.assign(N2010_Comp = N2010_Comp.values)
final_compare = final_compare.assign(N2012_Comp = N2012_Comp.values)
final_compare = final_compare.assign(N2014_Comp = N2014_Comp.values)
final_compare = final_compare.assign(N2016_Comp = N2016_Comp.values)
final_compare = final_compare.assign(N2018_Comp = N2018_Comp.values)
final_compare = final_compare.assign(N2020_Comp = N2020_Comp.values)
final_compare = final_compare.assign(N2022_Comp = N2022_Comp.values)
final_compare = final_compare.assign(N2387_Comp = N2387_Comp.values)
final_compare = final_compare.assign(N2388_Comp = N2388_Comp.values)
final_compare = final_compare.assign(N2389_Comp = N2389_Comp.values)
final_compare = final_compare.assign(N2390_Comp = N2390_Comp.values)
final_compare = final_compare.assign(N2496_Comp = N2496_Comp.values)
final_compare = final_compare.assign(N2643_Comp = N2643_Comp.values)
final_compare = final_compare.assign(N2644_Comp = N2644_Comp.values)
final_compare = final_compare.assign(N2891_Comp = N2891_Comp.values)
final_compare = final_compare.assign(N2925_Comp = N2925_Comp.values)
final_compare = final_compare.assign(N2970_Comp = N2970_Comp.values)
final_compare = final_compare.assign(N2971_Comp = N2971_Comp.values)
final_compare = final_compare.assign(N3038_Comp = N3038_Comp.values)
final_compare = final_compare.assign(N3079_Comp = N3079_Comp.values)
final_compare = final_compare.assign(N3546_Comp = N3546_Comp.values)
final_compare = final_compare.assign(N3671_Comp = N3671_Comp.values)
final_compare = final_compare.assign(N3803_Comp = N3803_Comp.values)
final_compare = final_compare.assign(N3804_Comp = N3804_Comp.values)
final_compare = final_compare.assign(N3809_Comp = N3809_Comp.values)
final_compare = final_compare.assign(N3851_Comp = N3851_Comp.values)
final_compare = final_compare.assign(N3875_Comp = N3875_Comp.values)
final_compare = final_compare.assign(N3881_Comp = N3881_Comp.values)
final_compare = final_compare.assign(N3882_Comp = N3882_Comp.values)
final_compare = final_compare.assign(N143_O_Comp = N143_O_Comp.values)
final_compare = final_compare.assign(N144_O_Comp = N144_O_Comp.values)
final_compare = final_compare.assign(N145_O_Comp = N145_O_Comp.values)
final_compare = final_compare.assign(N146_O_Comp = N146_O_Comp.values)
final_compare = final_compare.assign(N147_O_Comp = N147_O_Comp.values)
final_compare = final_compare.assign(N148_O_Comp = N148_O_Comp.values)
final_compare = final_compare.assign(N149_O_Comp = N149_O_Comp.values)
final_compare = final_compare.assign(N150_O_Comp = N150_O_Comp.values)
final_compare = final_compare.assign(N151_O_Comp = N151_O_Comp.values)
final_compare = final_compare.assign(N152_O_Comp = N152_O_Comp.values)
final_compare = final_compare.assign(N153_O_Comp = N153_O_Comp.values)
final_compare = final_compare.assign(N154_O_Comp = N154_O_Comp.values)
final_compare = final_compare.assign(N155_O_Comp = N155_O_Comp.values)
final_compare = final_compare.assign(N156_O_Comp = N156_O_Comp.values)
final_compare = final_compare.assign(N157_O_Comp = N157_O_Comp.values)
final_compare = final_compare.assign(N158_O_Comp = N158_O_Comp.values)
final_compare = final_compare.assign(N159_O_Comp = N159_O_Comp.values)
final_compare = final_compare.assign(N160_O_Comp = N160_O_Comp.values)
final_compare = final_compare.assign(N161_O_Comp = N161_O_Comp.values)
final_compare = final_compare.assign(N162_O_Comp = N162_O_Comp.values)
final_compare = final_compare.assign(N163_O_Comp = N163_O_Comp.values)
final_compare = final_compare.assign(N164_O_Comp = N164_O_Comp.values)
final_compare = final_compare.assign(N165_O_Comp = N165_O_Comp.values)
final_compare = final_compare.assign(N166_O_Comp = N166_O_Comp.values)
final_compare = final_compare.assign(N167_O_Comp = N167_O_Comp.values)
final_compare = final_compare.assign(N168_O_Comp = N168_O_Comp.values)
final_compare = final_compare.assign(N169_O_Comp = N169_O_Comp.values)
final_compare = final_compare.assign(N170_O_Comp = N170_O_Comp.values)
final_compare = final_compare.assign(N171_O_Comp = N171_O_Comp.values)
final_compare = final_compare.assign(N172_O_Comp = N172_O_Comp.values)
final_compare = final_compare.assign(N173_O_Comp = N173_O_Comp.values)
final_compare = final_compare.assign(N174_O_Comp = N174_O_Comp.values)
final_compare = final_compare.assign(N175_O_Comp = N175_O_Comp.values)
final_compare = final_compare.assign(N176_O_Comp = N176_O_Comp.values)
final_compare = final_compare.assign(N177_O_Comp = N177_O_Comp.values)
final_compare = final_compare.assign(N178_O_Comp = N178_O_Comp.values)
final_compare = final_compare.assign(N179_O_Comp = N179_O_Comp.values)
final_compare = final_compare.assign(N180_O_Comp = N180_O_Comp.values)
final_compare = final_compare.assign(N181_O_Comp = N181_O_Comp.values)
final_compare = final_compare.assign(N182_O_Comp = N182_O_Comp.values)
final_compare = final_compare.assign(N183_O_Comp = N183_O_Comp.values)
final_compare = final_compare.assign(N184_O_Comp = N184_O_Comp.values)
final_compare = final_compare.assign(N185_O_Comp = N185_O_Comp.values)
final_compare = final_compare.assign(N186_O_Comp = N186_O_Comp.values)
final_compare = final_compare.assign(N187_O_Comp = N187_O_Comp.values)
final_compare = final_compare.assign(N188_O_Comp = N188_O_Comp.values)
final_compare = final_compare.assign(N189_O_Comp = N189_O_Comp.values)
final_compare = final_compare.assign(N190_O_Comp = N190_O_Comp.values)
final_compare = final_compare.assign(N191_O_Comp = N191_O_Comp.values)
final_compare = final_compare.assign(N192_O_Comp = N192_O_Comp.values)
final_compare = final_compare.assign(N193_O_Comp = N193_O_Comp.values)
final_compare = final_compare.assign(N194_O_Comp = N194_O_Comp.values)
final_compare = final_compare.assign(N195_O_Comp = N195_O_Comp.values)
final_compare = final_compare.assign(N196_O_Comp = N196_O_Comp.values)
final_compare = final_compare.assign(N197_O_Comp = N197_O_Comp.values)
final_compare = final_compare.assign(N198_O_Comp = N198_O_Comp.values)
final_compare = final_compare.assign(N199_O_Comp = N199_O_Comp.values)
final_compare = final_compare.assign(N200_O_Comp = N200_O_Comp.values)
final_compare = final_compare.assign(N201_O_Comp = N201_O_Comp.values)
final_compare = final_compare.assign(N202_O_Comp = N202_O_Comp.values)
final_compare = final_compare.assign(N203_O_Comp = N203_O_Comp.values)
final_compare = final_compare.assign(N204_O_Comp = N204_O_Comp.values)
final_compare = final_compare.assign(N205_O_Comp = N205_O_Comp.values)
final_compare = final_compare.assign(N206_O_Comp = N206_O_Comp.values)
final_compare = final_compare.assign(N207_O_Comp = N207_O_Comp.values)
final_compare = final_compare.assign(N208_O_Comp = N208_O_Comp.values)
final_compare = final_compare.assign(N209_O_Comp = N209_O_Comp.values)
final_compare = final_compare.assign(N210_O_Comp = N210_O_Comp.values)
final_compare = final_compare.assign(N211_O_Comp = N211_O_Comp.values)
final_compare = final_compare.assign(N212_O_Comp = N212_O_Comp.values)
final_compare = final_compare.assign(N213_O_Comp = N213_O_Comp.values)
final_compare = final_compare.assign(N214_O_Comp = N214_O_Comp.values)
final_compare = final_compare.assign(N215_O_Comp = N215_O_Comp.values)
final_compare = final_compare.assign(N216_O_Comp = N216_O_Comp.values)
final_compare = final_compare.assign(N217_O_Comp = N217_O_Comp.values)
final_compare = final_compare.assign(N218_O_Comp = N218_O_Comp.values)

final_compare["M/S"] = final_compare["N398_Comp"] + final_compare["N400_Comp"] + final_compare["N401_Comp"] + final_compare["N419_Comp"] + final_compare["N420_Comp"] + final_compare["N456_Comp"] + final_compare["N457_Comp"] + final_compare["N458_Comp"] + final_compare["N487_Comp"] + final_compare["N488_Comp"] + final_compare["N489_Comp"] + final_compare["N490_Comp"] + final_compare["N491_Comp"] + final_compare["N492_Comp"] + final_compare["N493_Comp"] + final_compare["N494_Comp"] + final_compare["N792_Comp"] + final_compare["N799_Comp"] + final_compare["N805_Comp"] + final_compare["N1026_Comp"] + final_compare["N1028_Comp"] + final_compare["N1029_Comp"] + final_compare["N1269_Comp"] + final_compare["N1277_Comp"] + final_compare["N1448_Comp"] + final_compare["N1726_Comp"] + final_compare["N1816_Comp"] + final_compare["N1817_Comp"] + final_compare["N1818_Comp"] + final_compare["N1819_Comp"] + final_compare["N1820_Comp"] + final_compare["N1821_Comp"] + final_compare["N1969_Comp"] + final_compare["N1970_Comp"] + final_compare["N1971_Comp"] + final_compare["N2010_Comp"] + final_compare["N2012_Comp"] + final_compare["N2014_Comp"] + final_compare["N2016_Comp"] + final_compare["N2018_Comp"] + final_compare["N2020_Comp"] + final_compare["N2022_Comp"] + final_compare["N2387_Comp"] + final_compare["N2388_Comp"] + final_compare["N2389_Comp"] + final_compare["N2390_Comp"] + final_compare["N2496_Comp"] + final_compare["N2643_Comp"] + final_compare["N2644_Comp"] + final_compare["N2891_Comp"] + final_compare["N2925_Comp"] + final_compare["N2970_Comp"] + final_compare["N2971_Comp"] + final_compare["N3038_Comp"] + final_compare["N3079_Comp"] + final_compare["N3546_Comp"] + final_compare["N3671_Comp"] + final_compare["N3803_Comp"] + final_compare["N3804_Comp"] + final_compare["N3809_Comp"] + final_compare["N3851_Comp"] + final_compare["N3875_Comp"] + final_compare["N3881_Comp"] + final_compare["N3882_Comp"] + final_compare["N143_O_Comp"] + final_compare["N144_O_Comp"] + final_compare["N145_O_Comp"] + final_compare["N146_O_Comp"] + final_compare["N147_O_Comp"] + final_compare["N148_O_Comp"] + final_compare["N149_O_Comp"] + final_compare["N150_O_Comp"] + final_compare["N151_O_Comp"] + final_compare["N152_O_Comp"] + final_compare["N153_O_Comp"] + final_compare["N154_O_Comp"] + final_compare["N155_O_Comp"] + final_compare["N156_O_Comp"] + final_compare["N157_O_Comp"] + final_compare["N158_O_Comp"] + final_compare["N159_O_Comp"] + final_compare["N160_O_Comp"] + final_compare["N161_O_Comp"] + final_compare["N162_O_Comp"] + final_compare["N163_O_Comp"] + final_compare["N164_O_Comp"] + final_compare["N165_O_Comp"] + final_compare["N166_O_Comp"] + final_compare["N167_O_Comp"] + final_compare["N168_O_Comp"] + final_compare["N169_O_Comp"] + final_compare["N170_O_Comp"] + final_compare["N171_O_Comp"] + final_compare["N172_O_Comp"] + final_compare["N173_O_Comp"] + final_compare["N174_O_Comp"] + final_compare["N175_O_Comp"] + final_compare["N176_O_Comp"] + final_compare["N177_O_Comp"] + final_compare["N178_O_Comp"] + final_compare["N179_O_Comp"] + final_compare["N180_O_Comp"] + final_compare["N181_O_Comp"] + final_compare["N182_O_Comp"] + final_compare["N183_O_Comp"] + final_compare["N184_O_Comp"] + final_compare["N185_O_Comp"] + final_compare["N186_O_Comp"] + final_compare["N187_O_Comp"] + final_compare["N188_O_Comp"] + final_compare["N189_O_Comp"] + final_compare["N190_O_Comp"] + final_compare["N191_O_Comp"] + final_compare["N192_O_Comp"] + final_compare["N193_O_Comp"] + final_compare["N194_O_Comp"] + final_compare["N195_O_Comp"] + final_compare["N196_O_Comp"] + final_compare["N197_O_Comp"] + final_compare["N198_O_Comp"] + final_compare["N199_O_Comp"] + final_compare["N200_O_Comp"] + final_compare["N201_O_Comp"] + final_compare["N202_O_Comp"] + final_compare["N203_O_Comp"] + final_compare["N204_O_Comp"] + final_compare["N205_O_Comp"] + final_compare["N206_O_Comp"] + final_compare["N207_O_Comp"] + final_compare["N208_O_Comp"] + final_compare["N209_O_Comp"] + final_compare["N210_O_Comp"] + final_compare["N211_O_Comp"] + final_compare["N212_O_Comp"] + final_compare["N213_O_Comp"] + final_compare["N214_O_Comp"] + final_compare["N215_O_Comp"] + final_compare["N216_O_Comp"] + final_compare["N217_O_Comp"] + final_compare["N218_O_Comp"] 
final_compare.index.rename('Sr.No.', inplace=True)
final_compare.to_csv("compare_c2670.csv")


# x are coming even in golden file
# z coming in N389 node in clk = 624





# final_compare = final_compare.loc[final_compare['M/S'] == 2]
# #print(final_compare)
# #Cri_Node = final_compare.iloc[:,1]
# #print(Cri_Node)
# #Multiple = final_compare.iloc[:,11]
# #print(Multiple)
# #final_compare = final_compare.assign(Multiple=Multiple.values)
# #final_compare = final_compare.assign(Cri_Node=Cri_Node.values)
# final_compare.to_csv("Critical.csv")
