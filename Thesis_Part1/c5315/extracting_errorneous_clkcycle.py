import pandas as pd
import os
import csv
import subprocess
import random
import glob

#clk, Node, inputs, faulty outputs, golden outputs
final_compare = pd.DataFrame(columns = ["Clk", "Node", "N1", "N4", "N11", "N14", "N17", "N20", "N23", "N24", "N25", "N26", "N27", "N31", "N34", "N37", "N40", "N43", "N46", "N49", "N52", "N53", "N54", "N61", "N64", "N67", "N70", "N73", "N76", "N79", "N80", "N81", "N82", "N83", "N86", "N87", "N88", "N91", "N94", "N97", "N100", "N103", "N106", "N109", "N112", "N113", "N114", "N115", "N116", "N117", "N118", "N119", "N120", "N121", "N122", "N123", "N126", "N127", "N128", "N129", "N130", "N131", "N132", "N135", "N136", "N137", "N140", "N141", "N145", "N146", "N149", "N152", "N155", "N158", "N161", "N164", "N167", "N170", "N173", "N176", "N179", "N182", "N185", "N188", "N191", "N194", "N197", "N200", "N203", "N206", "N209", "N210", "N217", "N218", "N225", "N226", "N233", "N234", "N241", "N242", "N245", "N248", "N251", "N254", "N257", "N264", "N265", "N272", "N273", "N280", "N281", "N288", "N289", "N292", "N293", "N299", "N302", "N307", "N308", "N315", "N316", "N323", "N324", "N331", "N332", "N335", "N338", "N341", "N348", "N351", "N358", "N361", "N366", "N369", "N372", "N373", "N374", "N386", "N389", "N400", "N411", "N422", "N435", "N446", "N457", "N468", "N479", "N490", "N503", "N514", "N523", "N534", "N545", "N549", "N552", "N556", "N559", "N562", "N566", "N571", "N574", "N577", "N580", "N583", "N588", "N591", "N592", "N595", "N596", "N597", "N598", "N599", "N603", "N607", "N610", "N613", "N616", "N619", "N625", "N631", "N709", "N816", "N1066", "N1137", "N1138", "N1139", "N1140", "N1141", "N1142", "N1143", "N1144", "N1145", "N1147", "N1152", "N1153", "N1154", "N1155", "N1972", "N2054", "N2060", "N2061", "N2139", "N2142", "N2309", "N2387", "N2527", "N2584", "N2590", "N2623", "N3357", "N3358", "N3359", "N3360", "N3604", "N3613", "N4272", "N4275", "N4278", "N4279", "N4737", "N4738", "N4739", "N4740", "N5240", "N5388", "N6641", "N6643", "N6646", "N6648", "N6716", "N6877", "N6924", "N6925", "N6926", "N6927", "N7015", "N7363", "N7365", "N7432", "N7449", "N7465", "N7466", "N7467", "N7469", "N7470", "N7471", "N7472", "N7473", "N7474", "N7476", "N7503", "N7504", "N7506", "N7511", "N7515", "N7516", "N7517", "N7518", "N7519", "N7520", "N7521", "N7522", "N7600", "N7601", "N7602", "N7603", "N7604", "N7605", "N7606", "N7607", "N7626", "N7698", "N7699", "N7700", "N7701", "N7702", "N7703", "N7704", "N7705", "N7706", "N7707", "N7735", "N7736", "N7737", "N7738", "N7739", "N7740", "N7741", "N7742", "N7754", "N7755", "N7756", "N7757", "N7758", "N7759", "N7760", "N7761", "N8075", "N8076", "N8123", "N8124", "N8127", "N8128", "N709g", "N816g", "N1066g", "N1137g", "N1138g", "N1139g", "N1140g", "N1141g", "N1142g", "N1143g", "N1144g", "N1145g", "N1147g", "N1152g", "N1153g", "N1154g", "N1155g", "N1972g", "N2054g", "N2060g", "N2061g", "N2139g", "N2142g", "N2309g", "N2387g", "N2527g", "N2584g", "N2590g", "N2623g", "N3357g", "N3358g", "N3359g", "N3360g", "N3604g", "N3613g", "N4272g", "N4275g", "N4278g", "N4279g", "N4737g", "N4738g", "N4739g", "N4740g", "N5240g", "N5388g", "N6641g", "N6643g", "N6646g", "N6648g", "N6716g", "N6877g", "N6924g", "N6925g", "N6926g", "N6927g", "N7015g", "N7363g", "N7365g", "N7432g", "N7449g", "N7465g", "N7466g", "N7467g", "N7469g", "N7470g", "N7471g", "N7472g", "N7473g", "N7474g", "N7476g", "N7503g", "N7504g", "N7506g", "N7511g", "N7515g", "N7516g", "N7517g", "N7518g", "N7519g", "N7520g", "N7521g", "N7522g", "N7600g", "N7601g", "N7602g", "N7603g", "N7604g", "N7605g", "N7606g", "N7607g", "N7626g", "N7698g", "N7699g", "N7700g", "N7701g", "N7702g", "N7703g", "N7704g", "N7705g", "N7706g", "N7707g", "N7735g", "N7736g", "N7737g", "N7738g", "N7739g", "N7740g", "N7741g", "N7742g", "N7754g", "N7755g", "N7756g", "N7757g", "N7758g", "N7759g", "N7760g", "N7761g", "N8075g", "N8076g", "N8123g", "N8124g", "N8127g", "N8128g"])

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
    N4 = df.iloc[0,2]
    N11 = df.iloc[0,3]
    N14 = df.iloc[0,4]
    N17 = df.iloc[0,5]
    N20 = df.iloc[0,6]
    N23 = df.iloc[0,7]
    N24 = df.iloc[0,8]
    N25 = df.iloc[0,9]
    N26 = df.iloc[0,10]
    N27 = df.iloc[0,11]
    N31 = df.iloc[0,12]
    N34 = df.iloc[0,13]
    N37 = df.iloc[0,14]
    N40 = df.iloc[0,15]
    N43 = df.iloc[0,16]
    N46 = df.iloc[0,17]
    N49 = df.iloc[0,18]
    N52 = df.iloc[0,19]
    N53 = df.iloc[0,20]
    N54 = df.iloc[0,21]
    N61 = df.iloc[0,22]
    N64 = df.iloc[0,23]
    N67 = df.iloc[0,24]
    N70 = df.iloc[0,25]
    N73 = df.iloc[0,26]
    N76 = df.iloc[0,27]
    N79 = df.iloc[0,28]
    N80 = df.iloc[0,29]
    N81 = df.iloc[0,30]
    N82 = df.iloc[0,31]
    N83 = df.iloc[0,32]
    N86 = df.iloc[0,33]
    N87 = df.iloc[0,34]
    N88 = df.iloc[0,35]
    N91 = df.iloc[0,36]
    N94 = df.iloc[0,37]
    N97 = df.iloc[0,38]
    N100 = df.iloc[0,39]
    N103 = df.iloc[0,40]
    N106 = df.iloc[0,41]
    N109 = df.iloc[0,42]
    N112 = df.iloc[0,43]
    N113 = df.iloc[0,44]
    N114 = df.iloc[0,45]
    N115 = df.iloc[0,46]
    N116 = df.iloc[0,47]
    N117 = df.iloc[0,48]
    N118 = df.iloc[0,49]
    N119 = df.iloc[0,50]
    N120 = df.iloc[0,51]
    N121 = df.iloc[0,52]
    N122 = df.iloc[0,53]
    N123 = df.iloc[0,54]
    N126 = df.iloc[0,55]
    N127 = df.iloc[0,56]
    N128 = df.iloc[0,57]
    N129 = df.iloc[0,58]
    N130 = df.iloc[0,59]
    N131 = df.iloc[0,60]
    N132 = df.iloc[0,61]
    N135 = df.iloc[0,62]
    N136 = df.iloc[0,63]
    N137 = df.iloc[0,64]
    N140 = df.iloc[0,65]
    N141 = df.iloc[0,66]
    N145 = df.iloc[0,67]
    N146 = df.iloc[0,68]
    N149 = df.iloc[0,69]
    N152 = df.iloc[0,70]
    N155 = df.iloc[0,71]
    N158 = df.iloc[0,72]
    N161 = df.iloc[0,73]
    N164 = df.iloc[0,74]
    N167 = df.iloc[0,75]
    N170 = df.iloc[0,76]
    N173 = df.iloc[0,77]
    N176 = df.iloc[0,78]
    N179 = df.iloc[0,79]
    N182 = df.iloc[0,80]
    N185 = df.iloc[0,81]
    N188 = df.iloc[0,82]
    N191 = df.iloc[0,83]
    N194 = df.iloc[0,84]
    N197 = df.iloc[0,85]
    N200 = df.iloc[0,86]
    N203 = df.iloc[0,87]
    N206 = df.iloc[0,88]
    N209 = df.iloc[0,89]
    N210 = df.iloc[0,90]
    N217 = df.iloc[0,91]
    N218 = df.iloc[0,92]
    N225 = df.iloc[0,93]
    N226 = df.iloc[0,94]
    N233 = df.iloc[0,95]
    N234 = df.iloc[0,96]
    N241 = df.iloc[0,97]
    N242 = df.iloc[0,98]
    N245 = df.iloc[0,99]
    N248 = df.iloc[0,100]
    N251 = df.iloc[0,101]
    N254 = df.iloc[0,102]
    N257 = df.iloc[0,103]
    N264 = df.iloc[0,104]
    N265 = df.iloc[0,105]
    N272 = df.iloc[0,106]
    N273 = df.iloc[0,107]
    N280 = df.iloc[0,108]
    N281 = df.iloc[0,109]
    N288 = df.iloc[0,110]
    N289 = df.iloc[0,111]
    N292 = df.iloc[0,112]
    N293 = df.iloc[0,113]
    N299 = df.iloc[0,114]
    N302 = df.iloc[0,115]
    N307 = df.iloc[0,116]
    N308 = df.iloc[0,117]
    N315 = df.iloc[0,118]
    N316 = df.iloc[0,119]
    N323 = df.iloc[0,120]
    N324 = df.iloc[0,121]
    N331 = df.iloc[0,122]
    N332 = df.iloc[0,123]
    N335 = df.iloc[0,124]
    N338 = df.iloc[0,125]
    N341 = df.iloc[0,126]
    N348 = df.iloc[0,127]
    N351 = df.iloc[0,128]
    N358 = df.iloc[0,129]
    N361 = df.iloc[0,130]
    N366 = df.iloc[0,131]
    N369 = df.iloc[0,132]
    N372 = df.iloc[0,133]
    N373 = df.iloc[0,134]
    N374 = df.iloc[0,135]
    N386 = df.iloc[0,136]
    N389 = df.iloc[0,137]
    N400 = df.iloc[0,138]
    N411 = df.iloc[0,139]
    N422 = df.iloc[0,140]
    N435 = df.iloc[0,141]
    N446 = df.iloc[0,142]
    N457 = df.iloc[0,143]
    N468 = df.iloc[0,144]
    N479 = df.iloc[0,145]
    N490 = df.iloc[0,146]
    N503 = df.iloc[0,147]
    N514 = df.iloc[0,148]
    N523 = df.iloc[0,149]
    N534 = df.iloc[0,150]
    N545 = df.iloc[0,151]
    N549 = df.iloc[0,152]
    N552 = df.iloc[0,153]
    N556 = df.iloc[0,154]
    N559 = df.iloc[0,155]
    N562 = df.iloc[0,156]
    N566 = df.iloc[0,157]
    N571 = df.iloc[0,158]
    N574 = df.iloc[0,159]
    N577 = df.iloc[0,160]
    N580 = df.iloc[0,161]
    N583 = df.iloc[0,162]
    N588 = df.iloc[0,163]
    N591 = df.iloc[0,164]
    N592 = df.iloc[0,165]
    N595 = df.iloc[0,166]
    N596 = df.iloc[0,167]
    N597 = df.iloc[0,168]
    N598 = df.iloc[0,169]
    N599 = df.iloc[0,170]
    N603 = df.iloc[0,171]
    N607 = df.iloc[0,172]
    N610 = df.iloc[0,173]
    N613 = df.iloc[0,174]
    N616 = df.iloc[0,175]
    N619 = df.iloc[0,176]
    N625 = df.iloc[0,177]
    N631 = df.iloc[0,178]
   
#--------------------------------------------------------------------------------
## Extracting faulty output values
    ff = pd.read_csv(faulty_csv)

    # Same line at which error was enabled
    faulty = ff.loc[ff['Clk'] == time_outf]     
    #print(faulty)

    N709 = faulty.iloc[0,180]
    #print(N709)
    N816 = faulty.iloc[0,181]
    print(N816)
    N1066 = faulty.iloc[0,182]
    N1137 = faulty.iloc[0,183]
    N1138 = faulty.iloc[0,184]
    N1139 = faulty.iloc[0,185]
    N1140 = faulty.iloc[0,186]
    N1141 = faulty.iloc[0,187]
    N1142 = faulty.iloc[0,188]
    N1143 = faulty.iloc[0,189]
    N1144 = faulty.iloc[0,190]
    N1145 = faulty.iloc[0,191]
    N1147 = faulty.iloc[0,192]
    N1152 = faulty.iloc[0,193]
    N1153 = faulty.iloc[0,194]
    N1154 = faulty.iloc[0,195]
    N1155 = faulty.iloc[0,196]
    N1972 = faulty.iloc[0,197]
    N2054 = faulty.iloc[0,198]
    N2060 = faulty.iloc[0,199]
    N2061 = faulty.iloc[0,200]
    N2139 = faulty.iloc[0,201]
    N2142 = faulty.iloc[0,202]
    N2309 = faulty.iloc[0,203]
    N2387 = faulty.iloc[0,204]
    N2527 = faulty.iloc[0,205]
    N2584 = faulty.iloc[0,206]
    N2590 = faulty.iloc[0,207]
    N2623 = faulty.iloc[0,208]
    N3357 = faulty.iloc[0,209]
    N3358 = faulty.iloc[0,210]
    N3359 = faulty.iloc[0,211]
    N3360 = faulty.iloc[0,212]
    N3604 = faulty.iloc[0,213]
    N3613 = faulty.iloc[0,214]
    N4272 = faulty.iloc[0,215]
    N4275 = faulty.iloc[0,216]
    N4278 = faulty.iloc[0,217]
    N4279 = faulty.iloc[0,218]
    N4737 = faulty.iloc[0,219]
    N4738 = faulty.iloc[0,220]
    N4739 = faulty.iloc[0,221]
    N4740 = faulty.iloc[0,222]
    N5240 = faulty.iloc[0,223]
    N5388 = faulty.iloc[0,224]
    N6641 = faulty.iloc[0,225]
    N6643 = faulty.iloc[0,226]
    N6646 = faulty.iloc[0,227]
    N6648 = faulty.iloc[0,228]
    N6716 = faulty.iloc[0,229]
    N6877 = faulty.iloc[0,230]
    N6924 = faulty.iloc[0,231]
    N6925 = faulty.iloc[0,232]
    N6926 = faulty.iloc[0,233]
    N6927 = faulty.iloc[0,234]
    N7015 = faulty.iloc[0,235]
    N7363 = faulty.iloc[0,236]
    N7365 = faulty.iloc[0,237]
    N7432 = faulty.iloc[0,238]
    N7449 = faulty.iloc[0,239]
    N7465 = faulty.iloc[0,240]
    N7466 = faulty.iloc[0,241]
    N7467 = faulty.iloc[0,242]
    N7469 = faulty.iloc[0,243]
    N7470 = faulty.iloc[0,244]
    N7471 = faulty.iloc[0,245]
    N7472 = faulty.iloc[0,246]
    N7473 = faulty.iloc[0,247]
    N7474 = faulty.iloc[0,248]
    N7476 = faulty.iloc[0,249]
    N7503 = faulty.iloc[0,250]
    N7504 = faulty.iloc[0,251]
    N7506 = faulty.iloc[0,252]
    N7511 = faulty.iloc[0,253]
    N7515 = faulty.iloc[0,254]
    N7516 = faulty.iloc[0,255]
    N7517 = faulty.iloc[0,256]
    N7518 = faulty.iloc[0,257]
    N7519 = faulty.iloc[0,258]
    N7520 = faulty.iloc[0,259]
    N7521 = faulty.iloc[0,260]
    N7522 = faulty.iloc[0,261]
    N7600 = faulty.iloc[0,262]
    N7601 = faulty.iloc[0,263]
    N7602 = faulty.iloc[0,264]
    N7603 = faulty.iloc[0,265]
    N7604 = faulty.iloc[0,266]
    N7605 = faulty.iloc[0,267]
    N7606 = faulty.iloc[0,268]
    N7607 = faulty.iloc[0,269]
    N7626 = faulty.iloc[0,270]
    N7698 = faulty.iloc[0,271]
    N7699 = faulty.iloc[0,272]
    N7700 = faulty.iloc[0,273]
    N7701 = faulty.iloc[0,274]
    N7702 = faulty.iloc[0,275]
    N7703 = faulty.iloc[0,276]
    N7704 = faulty.iloc[0,277]
    N7705 = faulty.iloc[0,278]
    N7706 = faulty.iloc[0,279]
    N7707 = faulty.iloc[0,280]
    N7735 = faulty.iloc[0,281]
    N7736 = faulty.iloc[0,282]
    N7737 = faulty.iloc[0,283]
    N7738 = faulty.iloc[0,284]
    N7739 = faulty.iloc[0,285]
    N7740 = faulty.iloc[0,286]
    N7741 = faulty.iloc[0,287]
    N7742 = faulty.iloc[0,288]
    N7754 = faulty.iloc[0,289]
    N7755 = faulty.iloc[0,290]
    N7756 = faulty.iloc[0,291]
    N7757 = faulty.iloc[0,292]
    N7758 = faulty.iloc[0,293]
    N7759 = faulty.iloc[0,294]
    N7760 = faulty.iloc[0,295]
    N7761 = faulty.iloc[0,296]
    N8075 = faulty.iloc[0,297]
    N8076 = faulty.iloc[0,298]
    N8123 = faulty.iloc[0,299]
    N8124 = faulty.iloc[0,300]
    N8127 = faulty.iloc[0,301]
    N8128 = faulty.iloc[0,302]
    
#---------------------------------------------------------------------------------
    # Reading the golden output to extract correct value output
    cf = pd.read_csv('golden_c5315_iverilog_py.csv')

    # Same line at which error was enabled
    gold = cf.loc[cf['Clk'] == time_outf]
    #print("Golden outputline",gold)

    N709g = gold.iloc[0,180]
    #print(N709g)
    N816g = gold.iloc[0,181]
    N1066g = gold.iloc[0,182]
    N1137g = gold.iloc[0,183]
    N1138g = gold.iloc[0,184]
    N1139g = gold.iloc[0,185]
    N1140g = gold.iloc[0,186]
    N1141g = gold.iloc[0,187]
    N1142g = gold.iloc[0,188]
    N1143g = gold.iloc[0,189]
    N1144g = gold.iloc[0,190]
    N1145g = gold.iloc[0,191]
    N1147g = gold.iloc[0,192]
    N1152g = gold.iloc[0,193]
    N1153g = gold.iloc[0,194]
    N1154g = gold.iloc[0,195]
    N1155g = gold.iloc[0,196]
    N1972g = gold.iloc[0,197]
    N2054g = gold.iloc[0,198]
    N2060g = gold.iloc[0,199]
    N2061g = gold.iloc[0,200]
    N2139g = gold.iloc[0,201]
    N2142g = gold.iloc[0,202]
    N2309g = gold.iloc[0,203]
    N2387g = gold.iloc[0,204]
    N2527g = gold.iloc[0,205]
    N2584g = gold.iloc[0,206]
    N2590g = gold.iloc[0,207]
    N2623g = gold.iloc[0,208]
    N3357g = gold.iloc[0,209]
    N3358g = gold.iloc[0,210]
    N3359g = gold.iloc[0,211]
    N3360g = gold.iloc[0,212]
    N3604g = gold.iloc[0,213]
    N3613g = gold.iloc[0,214]
    N4272g = gold.iloc[0,215]
    N4275g = gold.iloc[0,216]
    N4278g = gold.iloc[0,217]
    N4279g = gold.iloc[0,218]
    N4737g = gold.iloc[0,219]
    N4738g = gold.iloc[0,220]
    N4739g = gold.iloc[0,221]
    N4740g = gold.iloc[0,222]
    N5240g = gold.iloc[0,223]
    N5388g = gold.iloc[0,224]
    N6641g = gold.iloc[0,225]
    N6643g = gold.iloc[0,226]
    N6646g = gold.iloc[0,227]
    N6648g = gold.iloc[0,228]
    N6716g = gold.iloc[0,229]
    N6877g = gold.iloc[0,230]
    N6924g = gold.iloc[0,231]
    N6925g = gold.iloc[0,232]
    N6926g = gold.iloc[0,233]
    N6927g = gold.iloc[0,234]
    N7015g = gold.iloc[0,235]
    N7363g = gold.iloc[0,236]
    N7365g = gold.iloc[0,237]
    N7432g = gold.iloc[0,238]
    N7449g = gold.iloc[0,239]
    N7465g = gold.iloc[0,240]
    N7466g = gold.iloc[0,241]
    N7467g = gold.iloc[0,242]
    N7469g = gold.iloc[0,243]
    N7470g = gold.iloc[0,244]
    N7471g = gold.iloc[0,245]
    N7472g = gold.iloc[0,246]
    N7473g = gold.iloc[0,247]
    N7474g = gold.iloc[0,248]
    N7476g = gold.iloc[0,249]
    N7503g = gold.iloc[0,250]
    N7504g = gold.iloc[0,251]
    N7506g = gold.iloc[0,252]
    N7511g = gold.iloc[0,253]
    N7515g = gold.iloc[0,254]
    N7516g = gold.iloc[0,255]
    N7517g = gold.iloc[0,256]
    N7518g = gold.iloc[0,257]
    N7519g = gold.iloc[0,258]
    N7520g = gold.iloc[0,259]
    N7521g = gold.iloc[0,260]
    N7522g = gold.iloc[0,261]
    N7600g = gold.iloc[0,262]
    N7601g = gold.iloc[0,263]
    N7602g = gold.iloc[0,264]
    N7603g = gold.iloc[0,265]
    N7604g = gold.iloc[0,266]
    N7605g = gold.iloc[0,267]
    N7606g = gold.iloc[0,268]
    N7607g = gold.iloc[0,269]
    N7626g = gold.iloc[0,270]
    N7698g = gold.iloc[0,271]
    N7699g = gold.iloc[0,272]
    N7700g = gold.iloc[0,273]
    N7701g = gold.iloc[0,274]
    N7702g = gold.iloc[0,275]
    N7703g = gold.iloc[0,276]
    N7704g = gold.iloc[0,277]
    N7705g = gold.iloc[0,278]
    N7706g = gold.iloc[0,279]
    N7707g = gold.iloc[0,280]
    N7735g = gold.iloc[0,281]
    N7736g = gold.iloc[0,282]
    N7737g = gold.iloc[0,283]
    N7738g = gold.iloc[0,284]
    N7739g = gold.iloc[0,285]
    N7740g = gold.iloc[0,286]
    N7741g = gold.iloc[0,287]
    N7742g = gold.iloc[0,288]
    N7754g = gold.iloc[0,289]
    N7755g = gold.iloc[0,290]
    N7756g = gold.iloc[0,291]
    N7757g = gold.iloc[0,292]
    N7758g = gold.iloc[0,293]
    N7759g = gold.iloc[0,294]
    N7760g = gold.iloc[0,295]
    N7761g = gold.iloc[0,296]
    N8075g = gold.iloc[0,297]
    N8076g = gold.iloc[0,298]
    N8123g = gold.iloc[0,299]
    N8124g = gold.iloc[0,300]
    N8127g = gold.iloc[0,301]
    N8128g = gold.iloc[0,302]

#---------------------------------------------------------------------------------
    #appending all values in order to form a row
    rows.append(time_in)
    rows.append(Node)
# Input columns    
    rows.append(N1)
    rows.append(N4)
    rows.append(N11)
    rows.append(N14)
    rows.append(N17)
    rows.append(N20)
    rows.append(N23)
    rows.append(N24)
    rows.append(N25)
    rows.append(N26)
    rows.append(N27)
    rows.append(N31)
    rows.append(N34)
    rows.append(N37)
    rows.append(N40)
    rows.append(N43)
    rows.append(N46)
    rows.append(N49)
    rows.append(N52)
    rows.append(N53)
    rows.append(N54)
    rows.append(N61)
    rows.append(N64)
    rows.append(N67)
    rows.append(N70)
    rows.append(N73)
    rows.append(N76)
    rows.append(N79)
    rows.append(N80)
    rows.append(N81)
    rows.append(N82)
    rows.append(N83)
    rows.append(N86)
    rows.append(N87)
    rows.append(N88)
    rows.append(N91)
    rows.append(N94)
    rows.append(N97)
    rows.append(N100)
    rows.append(N103)
    rows.append(N106)
    rows.append(N109)
    rows.append(N112)
    rows.append(N113)
    rows.append(N114)
    rows.append(N115)
    rows.append(N116)
    rows.append(N117)
    rows.append(N118)
    rows.append(N119)
    rows.append(N120)
    rows.append(N121)
    rows.append(N122)
    rows.append(N123)
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
    rows.append(N140)
    rows.append(N141)
    rows.append(N145)
    rows.append(N146)
    rows.append(N149)
    rows.append(N152)
    rows.append(N155)
    rows.append(N158)
    rows.append(N161)
    rows.append(N164)
    rows.append(N167)
    rows.append(N170)
    rows.append(N173)
    rows.append(N176)
    rows.append(N179)
    rows.append(N182)
    rows.append(N185)
    rows.append(N188)
    rows.append(N191)
    rows.append(N194)
    rows.append(N197)
    rows.append(N200)
    rows.append(N203)
    rows.append(N206)
    rows.append(N209)
    rows.append(N210)
    rows.append(N217)
    rows.append(N218)
    rows.append(N225)
    rows.append(N226)
    rows.append(N233)
    rows.append(N234)
    rows.append(N241)
    rows.append(N242)
    rows.append(N245)
    rows.append(N248)
    rows.append(N251)
    rows.append(N254)
    rows.append(N257)
    rows.append(N264)
    rows.append(N265)
    rows.append(N272)
    rows.append(N273)
    rows.append(N280)
    rows.append(N281)
    rows.append(N288)
    rows.append(N289)
    rows.append(N292)
    rows.append(N293)
    rows.append(N299)
    rows.append(N302)
    rows.append(N307)
    rows.append(N308)
    rows.append(N315)
    rows.append(N316)
    rows.append(N323)
    rows.append(N324)
    rows.append(N331)
    rows.append(N332)
    rows.append(N335)
    rows.append(N338)
    rows.append(N341)
    rows.append(N348)
    rows.append(N351)
    rows.append(N358)
    rows.append(N361)
    rows.append(N366)
    rows.append(N369)
    rows.append(N372)
    rows.append(N373)
    rows.append(N374)
    rows.append(N386)
    rows.append(N389)
    rows.append(N400)
    rows.append(N411)
    rows.append(N422)
    rows.append(N435)
    rows.append(N446)
    rows.append(N457)
    rows.append(N468)
    rows.append(N479)
    rows.append(N490)
    rows.append(N503)
    rows.append(N514)
    rows.append(N523)
    rows.append(N534)
    rows.append(N545)
    rows.append(N549)
    rows.append(N552)
    rows.append(N556)
    rows.append(N559)
    rows.append(N562)
    rows.append(N566)
    rows.append(N571)
    rows.append(N574)
    rows.append(N577)
    rows.append(N580)
    rows.append(N583)
    rows.append(N588)
    rows.append(N591)
    rows.append(N592)
    rows.append(N595)
    rows.append(N596)
    rows.append(N597)
    rows.append(N598)
    rows.append(N599)
    rows.append(N603)
    rows.append(N607)
    rows.append(N610)
    rows.append(N613)
    rows.append(N616)
    rows.append(N619)
    rows.append(N625)
    rows.append(N631)

    #faulty_outputs
    rows.append(N709)
    rows.append(N816)
    rows.append(N1066)
    rows.append(N1137)
    rows.append(N1138)
    rows.append(N1139)
    rows.append(N1140)
    rows.append(N1141)
    rows.append(N1142)
    rows.append(N1143)
    rows.append(N1144)
    rows.append(N1145)
    rows.append(N1147)
    rows.append(N1152)
    rows.append(N1153)
    rows.append(N1154)
    rows.append(N1155)
    rows.append(N1972)
    rows.append(N2054)
    rows.append(N2060)
    rows.append(N2061)
    rows.append(N2139)
    rows.append(N2142)
    rows.append(N2309)
    rows.append(N2387)
    rows.append(N2527)
    rows.append(N2584)
    rows.append(N2590)
    rows.append(N2623)
    rows.append(N3357)
    rows.append(N3358)
    rows.append(N3359)
    rows.append(N3360)
    rows.append(N3604)
    rows.append(N3613)
    rows.append(N4272)
    rows.append(N4275)
    rows.append(N4278)
    rows.append(N4279)
    rows.append(N4737)
    rows.append(N4738)
    rows.append(N4739)
    rows.append(N4740)
    rows.append(N5240)
    rows.append(N5388)
    rows.append(N6641)
    rows.append(N6643)
    rows.append(N6646)
    rows.append(N6648)
    rows.append(N6716)
    rows.append(N6877)
    rows.append(N6924)
    rows.append(N6925)
    rows.append(N6926)
    rows.append(N6927)
    rows.append(N7015)
    rows.append(N7363)
    rows.append(N7365)
    rows.append(N7432)
    rows.append(N7449)
    rows.append(N7465)
    rows.append(N7466)
    rows.append(N7467)
    rows.append(N7469)
    rows.append(N7470)
    rows.append(N7471)
    rows.append(N7472)
    rows.append(N7473)
    rows.append(N7474)
    rows.append(N7476)
    rows.append(N7503)
    rows.append(N7504)
    rows.append(N7506)
    rows.append(N7511)
    rows.append(N7515)
    rows.append(N7516)
    rows.append(N7517)
    rows.append(N7518)
    rows.append(N7519)
    rows.append(N7520)
    rows.append(N7521)
    rows.append(N7522)
    rows.append(N7600)
    rows.append(N7601)
    rows.append(N7602)
    rows.append(N7603)
    rows.append(N7604)
    rows.append(N7605)
    rows.append(N7606)
    rows.append(N7607)
    rows.append(N7626)
    rows.append(N7698)
    rows.append(N7699)
    rows.append(N7700)
    rows.append(N7701)
    rows.append(N7702)
    rows.append(N7703)
    rows.append(N7704)
    rows.append(N7705)
    rows.append(N7706)
    rows.append(N7707)
    rows.append(N7735)
    rows.append(N7736)
    rows.append(N7737)
    rows.append(N7738)
    rows.append(N7739)
    rows.append(N7740)
    rows.append(N7741)
    rows.append(N7742)
    rows.append(N7754)
    rows.append(N7755)
    rows.append(N7756)
    rows.append(N7757)
    rows.append(N7758)
    rows.append(N7759)
    rows.append(N7760)
    rows.append(N7761)
    rows.append(N8075)
    rows.append(N8076)
    rows.append(N8123)
    rows.append(N8124)
    rows.append(N8127)
    rows.append(N8128)

    #golden_outputs
    rows.append(N709g)
    rows.append(N816g)
    rows.append(N1066g)
    rows.append(N1137g)
    rows.append(N1138g)
    rows.append(N1139g)
    rows.append(N1140g)
    rows.append(N1141g)
    rows.append(N1142g)
    rows.append(N1143g)
    rows.append(N1144g)
    rows.append(N1145g)
    rows.append(N1147g)
    rows.append(N1152g)
    rows.append(N1153g)
    rows.append(N1154g)
    rows.append(N1155g)
    rows.append(N1972g)
    rows.append(N2054g)
    rows.append(N2060g)
    rows.append(N2061g)
    rows.append(N2139g)
    rows.append(N2142g)
    rows.append(N2309g)
    rows.append(N2387g)
    rows.append(N2527g)
    rows.append(N2584g)
    rows.append(N2590g)
    rows.append(N2623g)
    rows.append(N3357g)
    rows.append(N3358g)
    rows.append(N3359g)
    rows.append(N3360g)
    rows.append(N3604g)
    rows.append(N3613g)
    rows.append(N4272g)
    rows.append(N4275g)
    rows.append(N4278g)
    rows.append(N4279g)
    rows.append(N4737g)
    rows.append(N4738g)
    rows.append(N4739g)
    rows.append(N4740g)
    rows.append(N5240g)
    rows.append(N5388g)
    rows.append(N6641g)
    rows.append(N6643g)
    rows.append(N6646g)
    rows.append(N6648g)
    rows.append(N6716g)
    rows.append(N6877g)
    rows.append(N6924g)
    rows.append(N6925g)
    rows.append(N6926g)
    rows.append(N6927g)
    rows.append(N7015g)
    rows.append(N7363g)
    rows.append(N7365g)
    rows.append(N7432g)
    rows.append(N7449g)
    rows.append(N7465g)
    rows.append(N7466g)
    rows.append(N7467g)
    rows.append(N7469g)
    rows.append(N7470g)
    rows.append(N7471g)
    rows.append(N7472g)
    rows.append(N7473g)
    rows.append(N7474g)
    rows.append(N7476g)
    rows.append(N7503g)
    rows.append(N7504g)
    rows.append(N7506g)
    rows.append(N7511g)
    rows.append(N7515g)
    rows.append(N7516g)
    rows.append(N7517g)
    rows.append(N7518g)
    rows.append(N7519g)
    rows.append(N7520g)
    rows.append(N7521g)
    rows.append(N7522g)
    rows.append(N7600g)
    rows.append(N7601g)
    rows.append(N7602g)
    rows.append(N7603g)
    rows.append(N7604g)
    rows.append(N7605g)
    rows.append(N7606g)
    rows.append(N7607g)
    rows.append(N7626g)
    rows.append(N7698g)
    rows.append(N7699g)
    rows.append(N7700g)
    rows.append(N7701g)
    rows.append(N7702g)
    rows.append(N7703g)
    rows.append(N7704g)
    rows.append(N7705g)
    rows.append(N7706g)
    rows.append(N7707g)
    rows.append(N7735g)
    rows.append(N7736g)
    rows.append(N7737g)
    rows.append(N7738g)
    rows.append(N7739g)
    rows.append(N7740g)
    rows.append(N7741g)
    rows.append(N7742g)
    rows.append(N7754g)
    rows.append(N7755g)
    rows.append(N7756g)
    rows.append(N7757g)
    rows.append(N7758g)
    rows.append(N7759g)
    rows.append(N7760g)
    rows.append(N7761g)
    rows.append(N8075g)
    rows.append(N8076g)
    rows.append(N8123g)
    rows.append(N8124g)
    rows.append(N8127g)
    rows.append(N8128g)

    #print(rows)
    final_compare = final_compare.append(pd.Series(rows, index = ["Clk", "Node", "N1", "N4", "N11", "N14", "N17", "N20", "N23", "N24", "N25", "N26", "N27", "N31", "N34", "N37", "N40", "N43", "N46", "N49", "N52", "N53", "N54", "N61", "N64", "N67", "N70", "N73", "N76", "N79", "N80", "N81", "N82", "N83", "N86", "N87", "N88", "N91", "N94", "N97", "N100", "N103", "N106", "N109", "N112", "N113", "N114", "N115", "N116", "N117", "N118", "N119", "N120", "N121", "N122", "N123", "N126", "N127", "N128", "N129", "N130", "N131", "N132", "N135", "N136", "N137", "N140", "N141", "N145", "N146", "N149", "N152", "N155", "N158", "N161", "N164", "N167", "N170", "N173", "N176", "N179", "N182", "N185", "N188", "N191", "N194", "N197", "N200", "N203", "N206", "N209", "N210", "N217", "N218", "N225", "N226", "N233", "N234", "N241", "N242", "N245", "N248", "N251", "N254", "N257", "N264", "N265", "N272", "N273", "N280", "N281", "N288", "N289", "N292", "N293", "N299", "N302", "N307", "N308", "N315", "N316", "N323", "N324", "N331", "N332", "N335", "N338", "N341", "N348", "N351", "N358", "N361", "N366", "N369", "N372", "N373", "N374", "N386", "N389", "N400", "N411", "N422", "N435", "N446", "N457", "N468", "N479", "N490", "N503", "N514", "N523", "N534", "N545", "N549", "N552", "N556", "N559", "N562", "N566", "N571", "N574", "N577", "N580", "N583", "N588", "N591", "N592", "N595", "N596", "N597", "N598", "N599", "N603", "N607", "N610", "N613", "N616", "N619", "N625", "N631", "N709", "N816", "N1066", "N1137", "N1138", "N1139", "N1140", "N1141", "N1142", "N1143", "N1144", "N1145", "N1147", "N1152", "N1153", "N1154", "N1155", "N1972", "N2054", "N2060", "N2061", "N2139", "N2142", "N2309", "N2387", "N2527", "N2584", "N2590", "N2623", "N3357", "N3358", "N3359", "N3360", "N3604", "N3613", "N4272", "N4275", "N4278", "N4279", "N4737", "N4738", "N4739", "N4740", "N5240", "N5388", "N6641", "N6643", "N6646", "N6648", "N6716", "N6877", "N6924", "N6925", "N6926", "N6927", "N7015", "N7363", "N7365", "N7432", "N7449", "N7465", "N7466", "N7467", "N7469", "N7470", "N7471", "N7472", "N7473", "N7474", "N7476", "N7503", "N7504", "N7506", "N7511", "N7515", "N7516", "N7517", "N7518", "N7519", "N7520", "N7521", "N7522", "N7600", "N7601", "N7602", "N7603", "N7604", "N7605", "N7606", "N7607", "N7626", "N7698", "N7699", "N7700", "N7701", "N7702", "N7703", "N7704", "N7705", "N7706", "N7707", "N7735", "N7736", "N7737", "N7738", "N7739", "N7740", "N7741", "N7742", "N7754", "N7755", "N7756", "N7757", "N7758", "N7759", "N7760", "N7761", "N8075", "N8076", "N8123", "N8124", "N8127", "N8128", "N709g", "N816g", "N1066g", "N1137g", "N1138g", "N1139g", "N1140g", "N1141g", "N1142g", "N1143g", "N1144g", "N1145g", "N1147g", "N1152g", "N1153g", "N1154g", "N1155g", "N1972g", "N2054g", "N2060g", "N2061g", "N2139g", "N2142g", "N2309g", "N2387g", "N2527g", "N2584g", "N2590g", "N2623g", "N3357g", "N3358g", "N3359g", "N3360g", "N3604g", "N3613g", "N4272g", "N4275g", "N4278g", "N4279g", "N4737g", "N4738g", "N4739g", "N4740g", "N5240g", "N5388g", "N6641g", "N6643g", "N6646g", "N6648g", "N6716g", "N6877g", "N6924g", "N6925g", "N6926g", "N6927g", "N7015g", "N7363g", "N7365g", "N7432g", "N7449g", "N7465g", "N7466g", "N7467g", "N7469g", "N7470g", "N7471g", "N7472g", "N7473g", "N7474g", "N7476g", "N7503g", "N7504g", "N7506g", "N7511g", "N7515g", "N7516g", "N7517g", "N7518g", "N7519g", "N7520g", "N7521g", "N7522g", "N7600g", "N7601g", "N7602g", "N7603g", "N7604g", "N7605g", "N7606g", "N7607g", "N7626g", "N7698g", "N7699g", "N7700g", "N7701g", "N7702g", "N7703g", "N7704g", "N7705g", "N7706g", "N7707g", "N7735g", "N7736g", "N7737g", "N7738g", "N7739g", "N7740g", "N7741g", "N7742g", "N7754g", "N7755g", "N7756g", "N7757g", "N7758g", "N7759g", "N7760g", "N7761g", "N8075g", "N8076g", "N8123g", "N8124g", "N8127g", "N8128g"]), ignore_index=True)
##---------------------------------------------------------------------------------
#print(final_compare)

N709_Comp = pd.to_numeric(final_compare['N709']) != pd.to_numeric(final_compare['N709g'])
N709_Comp = N709_Comp.astype(int)
N816_Comp = pd.to_numeric(final_compare['N816']) != pd.to_numeric(final_compare['N816g'])
N816_Comp = N816_Comp.astype(int)
N1066_Comp = pd.to_numeric(final_compare['N1066']) != pd.to_numeric(final_compare['N1066g'])
N1066_Comp = N1066_Comp.astype(int)
N1137_Comp = pd.to_numeric(final_compare['N1137']) != pd.to_numeric(final_compare['N1137g'])
N1137_Comp = N1137_Comp.astype(int)
N1138_Comp = pd.to_numeric(final_compare['N1138']) != pd.to_numeric(final_compare['N1138g'])
N1138_Comp = N1138_Comp.astype(int)
N1139_Comp = pd.to_numeric(final_compare['N1139']) != pd.to_numeric(final_compare['N1139g'])
N1139_Comp = N1139_Comp.astype(int)
N1140_Comp = pd.to_numeric(final_compare['N1140']) != pd.to_numeric(final_compare['N1140g'])
N1140_Comp = N1140_Comp.astype(int)
N1141_Comp = pd.to_numeric(final_compare['N1141']) != pd.to_numeric(final_compare['N1141g'])
N1141_Comp = N1141_Comp.astype(int)
N1142_Comp = pd.to_numeric(final_compare['N1142']) != pd.to_numeric(final_compare['N1142g'])
N1142_Comp = N1142_Comp.astype(int)
N1143_Comp = pd.to_numeric(final_compare['N1143']) != pd.to_numeric(final_compare['N1143g'])
N1143_Comp = N1143_Comp.astype(int)
N1144_Comp = pd.to_numeric(final_compare['N1144']) != pd.to_numeric(final_compare['N1144g'])
N1144_Comp = N1144_Comp.astype(int)
N1145_Comp = pd.to_numeric(final_compare['N1145']) != pd.to_numeric(final_compare['N1145g'])
N1145_Comp = N1145_Comp.astype(int)
N1147_Comp = pd.to_numeric(final_compare['N1147']) != pd.to_numeric(final_compare['N1147g'])
N1147_Comp = N1147_Comp.astype(int)
N1152_Comp = pd.to_numeric(final_compare['N1152']) != pd.to_numeric(final_compare['N1152g'])
N1152_Comp = N1152_Comp.astype(int)
N1153_Comp = pd.to_numeric(final_compare['N1153']) != pd.to_numeric(final_compare['N1153g'])
N1153_Comp = N1153_Comp.astype(int)
N1154_Comp = pd.to_numeric(final_compare['N1154']) != pd.to_numeric(final_compare['N1154g'])
N1154_Comp = N1154_Comp.astype(int)
N1155_Comp = pd.to_numeric(final_compare['N1155']) != pd.to_numeric(final_compare['N1155g'])
N1155_Comp = N1155_Comp.astype(int)
N1972_Comp = pd.to_numeric(final_compare['N1972']) != pd.to_numeric(final_compare['N1972g'])
N1972_Comp = N1972_Comp.astype(int)
N2054_Comp = pd.to_numeric(final_compare['N2054']) != pd.to_numeric(final_compare['N2054g'])
N2054_Comp = N2054_Comp.astype(int)
N2060_Comp = pd.to_numeric(final_compare['N2060']) != pd.to_numeric(final_compare['N2060g'])
N2060_Comp = N2060_Comp.astype(int)
N2061_Comp = pd.to_numeric(final_compare['N2061']) != pd.to_numeric(final_compare['N2061g'])
N2061_Comp = N2061_Comp.astype(int)
N2139_Comp = pd.to_numeric(final_compare['N2139']) != pd.to_numeric(final_compare['N2139g'])
N2139_Comp = N2139_Comp.astype(int)
N2142_Comp = pd.to_numeric(final_compare['N2142']) != pd.to_numeric(final_compare['N2142g'])
N2142_Comp = N2142_Comp.astype(int)
N2309_Comp = pd.to_numeric(final_compare['N2309']) != pd.to_numeric(final_compare['N2309g'])
N2309_Comp = N2309_Comp.astype(int)
N2387_Comp = pd.to_numeric(final_compare['N2387']) != pd.to_numeric(final_compare['N2387g'])
N2387_Comp = N2387_Comp.astype(int)
N2527_Comp = pd.to_numeric(final_compare['N2527']) != pd.to_numeric(final_compare['N2527g'])
N2527_Comp = N2527_Comp.astype(int)
N2584_Comp = pd.to_numeric(final_compare['N2584']) != pd.to_numeric(final_compare['N2584g'])
N2584_Comp = N2584_Comp.astype(int)
N2590_Comp = pd.to_numeric(final_compare['N2590']) != pd.to_numeric(final_compare['N2590g'])
N2590_Comp = N2590_Comp.astype(int)
N2623_Comp = pd.to_numeric(final_compare['N2623']) != pd.to_numeric(final_compare['N2623g'])
N2623_Comp = N2623_Comp.astype(int)
N3357_Comp = pd.to_numeric(final_compare['N3357']) != pd.to_numeric(final_compare['N3357g'])
N3357_Comp = N3357_Comp.astype(int)
N3358_Comp = pd.to_numeric(final_compare['N3358']) != pd.to_numeric(final_compare['N3358g'])
N3358_Comp = N3358_Comp.astype(int)
N3359_Comp = pd.to_numeric(final_compare['N3359']) != pd.to_numeric(final_compare['N3359g'])
N3359_Comp = N3359_Comp.astype(int)
N3360_Comp = pd.to_numeric(final_compare['N3360']) != pd.to_numeric(final_compare['N3360g'])
N3360_Comp = N3360_Comp.astype(int)
N3604_Comp = pd.to_numeric(final_compare['N3604']) != pd.to_numeric(final_compare['N3604g'])
N3604_Comp = N3604_Comp.astype(int)
N3613_Comp = pd.to_numeric(final_compare['N3613']) != pd.to_numeric(final_compare['N3613g'])
N3613_Comp = N3613_Comp.astype(int)
N4272_Comp = pd.to_numeric(final_compare['N4272']) != pd.to_numeric(final_compare['N4272g'])
N4272_Comp = N4272_Comp.astype(int)
N4275_Comp = pd.to_numeric(final_compare['N4275']) != pd.to_numeric(final_compare['N4275g'])
N4275_Comp = N4275_Comp.astype(int)
N4278_Comp = pd.to_numeric(final_compare['N4278']) != pd.to_numeric(final_compare['N4278g'])
N4278_Comp = N4278_Comp.astype(int)
N4279_Comp = pd.to_numeric(final_compare['N4279']) != pd.to_numeric(final_compare['N4279g'])
N4279_Comp = N4279_Comp.astype(int)
N4737_Comp = pd.to_numeric(final_compare['N4737']) != pd.to_numeric(final_compare['N4737g'])
N4737_Comp = N4737_Comp.astype(int)
N4738_Comp = pd.to_numeric(final_compare['N4738']) != pd.to_numeric(final_compare['N4738g'])
N4738_Comp = N4738_Comp.astype(int)
N4739_Comp = pd.to_numeric(final_compare['N4739']) != pd.to_numeric(final_compare['N4739g'])
N4739_Comp = N4739_Comp.astype(int)
N4740_Comp = pd.to_numeric(final_compare['N4740']) != pd.to_numeric(final_compare['N4740g'])
N4740_Comp = N4740_Comp.astype(int)
N5240_Comp = pd.to_numeric(final_compare['N5240']) != pd.to_numeric(final_compare['N5240g'])
N5240_Comp = N5240_Comp.astype(int)
N5388_Comp = pd.to_numeric(final_compare['N5388']) != pd.to_numeric(final_compare['N5388g'])
N5388_Comp = N5388_Comp.astype(int)
N6641_Comp = pd.to_numeric(final_compare['N6641']) != pd.to_numeric(final_compare['N6641g'])
N6641_Comp = N6641_Comp.astype(int)
N6643_Comp = pd.to_numeric(final_compare['N6643']) != pd.to_numeric(final_compare['N6643g'])
N6643_Comp = N6643_Comp.astype(int)
N6646_Comp = pd.to_numeric(final_compare['N6646']) != pd.to_numeric(final_compare['N6646g'])
N6646_Comp = N6646_Comp.astype(int)
N6648_Comp = pd.to_numeric(final_compare['N6648']) != pd.to_numeric(final_compare['N6648g'])
N6648_Comp = N6648_Comp.astype(int)
N6716_Comp = pd.to_numeric(final_compare['N6716']) != pd.to_numeric(final_compare['N6716g'])
N6716_Comp = N6716_Comp.astype(int)
N6877_Comp = pd.to_numeric(final_compare['N6877']) != pd.to_numeric(final_compare['N6877g'])
N6877_Comp = N6877_Comp.astype(int)
N6924_Comp = pd.to_numeric(final_compare['N6924']) != pd.to_numeric(final_compare['N6924g'])
N6924_Comp = N6924_Comp.astype(int)
N6925_Comp = pd.to_numeric(final_compare['N6925']) != pd.to_numeric(final_compare['N6925g'])
N6925_Comp = N6925_Comp.astype(int)
N6926_Comp = pd.to_numeric(final_compare['N6926']) != pd.to_numeric(final_compare['N6926g'])
N6926_Comp = N6926_Comp.astype(int)
N6927_Comp = pd.to_numeric(final_compare['N6927']) != pd.to_numeric(final_compare['N6927g'])
N6927_Comp = N6927_Comp.astype(int)
N7015_Comp = pd.to_numeric(final_compare['N7015']) != pd.to_numeric(final_compare['N7015g'])
N7015_Comp = N7015_Comp.astype(int)
N7363_Comp = pd.to_numeric(final_compare['N7363']) != pd.to_numeric(final_compare['N7363g'])
N7363_Comp = N7363_Comp.astype(int)
N7365_Comp = pd.to_numeric(final_compare['N7365']) != pd.to_numeric(final_compare['N7365g'])
N7365_Comp = N7365_Comp.astype(int)
N7432_Comp = pd.to_numeric(final_compare['N7432']) != pd.to_numeric(final_compare['N7432g'])
N7432_Comp = N7432_Comp.astype(int)
N7449_Comp = pd.to_numeric(final_compare['N7449']) != pd.to_numeric(final_compare['N7449g'])
N7449_Comp = N7449_Comp.astype(int)
N7465_Comp = pd.to_numeric(final_compare['N7465']) != pd.to_numeric(final_compare['N7465g'])
N7465_Comp = N7465_Comp.astype(int)
N7466_Comp = pd.to_numeric(final_compare['N7466']) != pd.to_numeric(final_compare['N7466g'])
N7466_Comp = N7466_Comp.astype(int)
N7467_Comp = pd.to_numeric(final_compare['N7467']) != pd.to_numeric(final_compare['N7467g'])
N7467_Comp = N7467_Comp.astype(int)
N7469_Comp = pd.to_numeric(final_compare['N7469']) != pd.to_numeric(final_compare['N7469g'])
N7469_Comp = N7469_Comp.astype(int)
N7470_Comp = pd.to_numeric(final_compare['N7470']) != pd.to_numeric(final_compare['N7470g'])
N7470_Comp = N7470_Comp.astype(int)
N7471_Comp = pd.to_numeric(final_compare['N7471']) != pd.to_numeric(final_compare['N7471g'])
N7471_Comp = N7471_Comp.astype(int)
N7472_Comp = pd.to_numeric(final_compare['N7472']) != pd.to_numeric(final_compare['N7472g'])
N7472_Comp = N7472_Comp.astype(int)
N7473_Comp = pd.to_numeric(final_compare['N7473']) != pd.to_numeric(final_compare['N7473g'])
N7473_Comp = N7473_Comp.astype(int)
N7474_Comp = pd.to_numeric(final_compare['N7474']) != pd.to_numeric(final_compare['N7474g'])
N7474_Comp = N7474_Comp.astype(int)
N7476_Comp = pd.to_numeric(final_compare['N7476']) != pd.to_numeric(final_compare['N7476g'])
N7476_Comp = N7476_Comp.astype(int)
N7503_Comp = pd.to_numeric(final_compare['N7503']) != pd.to_numeric(final_compare['N7503g'])
N7503_Comp = N7503_Comp.astype(int)
N7504_Comp = pd.to_numeric(final_compare['N7504']) != pd.to_numeric(final_compare['N7504g'])
N7504_Comp = N7504_Comp.astype(int)
N7506_Comp = pd.to_numeric(final_compare['N7506']) != pd.to_numeric(final_compare['N7506g'])
N7506_Comp = N7506_Comp.astype(int)
N7511_Comp = pd.to_numeric(final_compare['N7511']) != pd.to_numeric(final_compare['N7511g'])
N7511_Comp = N7511_Comp.astype(int)
N7515_Comp = pd.to_numeric(final_compare['N7515']) != pd.to_numeric(final_compare['N7515g'])
N7515_Comp = N7515_Comp.astype(int)
N7516_Comp = pd.to_numeric(final_compare['N7516']) != pd.to_numeric(final_compare['N7516g'])
N7516_Comp = N7516_Comp.astype(int)
N7517_Comp = pd.to_numeric(final_compare['N7517']) != pd.to_numeric(final_compare['N7517g'])
N7517_Comp = N7517_Comp.astype(int)
N7518_Comp = pd.to_numeric(final_compare['N7518']) != pd.to_numeric(final_compare['N7518g'])
N7518_Comp = N7518_Comp.astype(int)
N7519_Comp = pd.to_numeric(final_compare['N7519']) != pd.to_numeric(final_compare['N7519g'])
N7519_Comp = N7519_Comp.astype(int)
N7520_Comp = pd.to_numeric(final_compare['N7520']) != pd.to_numeric(final_compare['N7520g'])
N7520_Comp = N7520_Comp.astype(int)
N7521_Comp = pd.to_numeric(final_compare['N7521']) != pd.to_numeric(final_compare['N7521g'])
N7521_Comp = N7521_Comp.astype(int)
N7522_Comp = pd.to_numeric(final_compare['N7522']) != pd.to_numeric(final_compare['N7522g'])
N7522_Comp = N7522_Comp.astype(int)
N7600_Comp = pd.to_numeric(final_compare['N7600']) != pd.to_numeric(final_compare['N7600g'])
N7600_Comp = N7600_Comp.astype(int)
N7601_Comp = pd.to_numeric(final_compare['N7601']) != pd.to_numeric(final_compare['N7601g'])
N7601_Comp = N7601_Comp.astype(int)
N7602_Comp = pd.to_numeric(final_compare['N7602']) != pd.to_numeric(final_compare['N7602g'])
N7602_Comp = N7602_Comp.astype(int)
N7603_Comp = pd.to_numeric(final_compare['N7603']) != pd.to_numeric(final_compare['N7603g'])
N7603_Comp = N7603_Comp.astype(int)
N7604_Comp = pd.to_numeric(final_compare['N7604']) != pd.to_numeric(final_compare['N7604g'])
N7604_Comp = N7604_Comp.astype(int)
N7605_Comp = pd.to_numeric(final_compare['N7605']) != pd.to_numeric(final_compare['N7605g'])
N7605_Comp = N7605_Comp.astype(int)
N7606_Comp = pd.to_numeric(final_compare['N7606']) != pd.to_numeric(final_compare['N7606g'])
N7606_Comp = N7606_Comp.astype(int)
N7607_Comp = pd.to_numeric(final_compare['N7607']) != pd.to_numeric(final_compare['N7607g'])
N7607_Comp = N7607_Comp.astype(int)
N7626_Comp = pd.to_numeric(final_compare['N7626']) != pd.to_numeric(final_compare['N7626g'])
N7626_Comp = N7626_Comp.astype(int)
N7698_Comp = pd.to_numeric(final_compare['N7698']) != pd.to_numeric(final_compare['N7698g'])
N7698_Comp = N7698_Comp.astype(int)
N7699_Comp = pd.to_numeric(final_compare['N7699']) != pd.to_numeric(final_compare['N7699g'])
N7699_Comp = N7699_Comp.astype(int)
N7700_Comp = pd.to_numeric(final_compare['N7700']) != pd.to_numeric(final_compare['N7700g'])
N7700_Comp = N7700_Comp.astype(int)
N7701_Comp = pd.to_numeric(final_compare['N7701']) != pd.to_numeric(final_compare['N7701g'])
N7701_Comp = N7701_Comp.astype(int)
N7702_Comp = pd.to_numeric(final_compare['N7702']) != pd.to_numeric(final_compare['N7702g'])
N7702_Comp = N7702_Comp.astype(int)
N7703_Comp = pd.to_numeric(final_compare['N7703']) != pd.to_numeric(final_compare['N7703g'])
N7703_Comp = N7703_Comp.astype(int)
N7704_Comp = pd.to_numeric(final_compare['N7704']) != pd.to_numeric(final_compare['N7704g'])
N7704_Comp = N7704_Comp.astype(int)
N7705_Comp = pd.to_numeric(final_compare['N7705']) != pd.to_numeric(final_compare['N7705g'])
N7705_Comp = N7705_Comp.astype(int)
N7706_Comp = pd.to_numeric(final_compare['N7706']) != pd.to_numeric(final_compare['N7706g'])
N7706_Comp = N7706_Comp.astype(int)
N7707_Comp = pd.to_numeric(final_compare['N7707']) != pd.to_numeric(final_compare['N7707g'])
N7707_Comp = N7707_Comp.astype(int)
N7735_Comp = pd.to_numeric(final_compare['N7735']) != pd.to_numeric(final_compare['N7735g'])
N7735_Comp = N7735_Comp.astype(int)
N7736_Comp = pd.to_numeric(final_compare['N7736']) != pd.to_numeric(final_compare['N7736g'])
N7736_Comp = N7736_Comp.astype(int)
N7737_Comp = pd.to_numeric(final_compare['N7737']) != pd.to_numeric(final_compare['N7737g'])
N7737_Comp = N7737_Comp.astype(int)
N7738_Comp = pd.to_numeric(final_compare['N7738']) != pd.to_numeric(final_compare['N7738g'])
N7738_Comp = N7738_Comp.astype(int)
N7739_Comp = pd.to_numeric(final_compare['N7739']) != pd.to_numeric(final_compare['N7739g'])
N7739_Comp = N7739_Comp.astype(int)
N7740_Comp = pd.to_numeric(final_compare['N7740']) != pd.to_numeric(final_compare['N7740g'])
N7740_Comp = N7740_Comp.astype(int)
N7741_Comp = pd.to_numeric(final_compare['N7741']) != pd.to_numeric(final_compare['N7741g'])
N7741_Comp = N7741_Comp.astype(int)
N7742_Comp = pd.to_numeric(final_compare['N7742']) != pd.to_numeric(final_compare['N7742g'])
N7742_Comp = N7742_Comp.astype(int)
N7754_Comp = pd.to_numeric(final_compare['N7754']) != pd.to_numeric(final_compare['N7754g'])
N7754_Comp = N7754_Comp.astype(int)
N7755_Comp = pd.to_numeric(final_compare['N7755']) != pd.to_numeric(final_compare['N7755g'])
N7755_Comp = N7755_Comp.astype(int)
N7756_Comp = pd.to_numeric(final_compare['N7756']) != pd.to_numeric(final_compare['N7756g'])
N7756_Comp = N7756_Comp.astype(int)
N7757_Comp = pd.to_numeric(final_compare['N7757']) != pd.to_numeric(final_compare['N7757g'])
N7757_Comp = N7757_Comp.astype(int)
N7758_Comp = pd.to_numeric(final_compare['N7758']) != pd.to_numeric(final_compare['N7758g'])
N7758_Comp = N7758_Comp.astype(int)
N7759_Comp = pd.to_numeric(final_compare['N7759']) != pd.to_numeric(final_compare['N7759g'])
N7759_Comp = N7759_Comp.astype(int)
N7760_Comp = pd.to_numeric(final_compare['N7760']) != pd.to_numeric(final_compare['N7760g'])
N7760_Comp = N7760_Comp.astype(int)
N7761_Comp = pd.to_numeric(final_compare['N7761']) != pd.to_numeric(final_compare['N7761g'])
N7761_Comp = N7761_Comp.astype(int)
N8075_Comp = pd.to_numeric(final_compare['N8075']) != pd.to_numeric(final_compare['N8075g'])
N8075_Comp = N8075_Comp.astype(int)
N8076_Comp = pd.to_numeric(final_compare['N8076']) != pd.to_numeric(final_compare['N8076g'])
N8076_Comp = N8076_Comp.astype(int)
N8123_Comp = pd.to_numeric(final_compare['N8123']) != pd.to_numeric(final_compare['N8123g'])
N8123_Comp = N8123_Comp.astype(int)
N8124_Comp = pd.to_numeric(final_compare['N8124']) != pd.to_numeric(final_compare['N8124g'])
N8124_Comp = N8124_Comp.astype(int)
N8127_Comp = pd.to_numeric(final_compare['N8127']) != pd.to_numeric(final_compare['N8127g'])
N8127_Comp = N8127_Comp.astype(int)
N8128_Comp = pd.to_numeric(final_compare['N8128']) != pd.to_numeric(final_compare['N8128g'])
N8128_Comp = N8128_Comp.astype(int)

final_compare = final_compare.assign(N709_Comp = N709_Comp.values)
final_compare = final_compare.assign(N816_Comp = N816_Comp.values)
final_compare = final_compare.assign(N1066_Comp = N1066_Comp.values)
final_compare = final_compare.assign(N1137_Comp = N1137_Comp.values)
final_compare = final_compare.assign(N1138_Comp = N1138_Comp.values)
final_compare = final_compare.assign(N1139_Comp = N1139_Comp.values)
final_compare = final_compare.assign(N1140_Comp = N1140_Comp.values)
final_compare = final_compare.assign(N1141_Comp = N1141_Comp.values)
final_compare = final_compare.assign(N1142_Comp = N1142_Comp.values)
final_compare = final_compare.assign(N1143_Comp = N1143_Comp.values)
final_compare = final_compare.assign(N1144_Comp = N1144_Comp.values)
final_compare = final_compare.assign(N1145_Comp = N1145_Comp.values)
final_compare = final_compare.assign(N1147_Comp = N1147_Comp.values)
final_compare = final_compare.assign(N1152_Comp = N1152_Comp.values)
final_compare = final_compare.assign(N1153_Comp = N1153_Comp.values)
final_compare = final_compare.assign(N1154_Comp = N1154_Comp.values)
final_compare = final_compare.assign(N1155_Comp = N1155_Comp.values)
final_compare = final_compare.assign(N1972_Comp = N1972_Comp.values)
final_compare = final_compare.assign(N2054_Comp = N2054_Comp.values)
final_compare = final_compare.assign(N2060_Comp = N2060_Comp.values)
final_compare = final_compare.assign(N2061_Comp = N2061_Comp.values)
final_compare = final_compare.assign(N2139_Comp = N2139_Comp.values)
final_compare = final_compare.assign(N2142_Comp = N2142_Comp.values)
final_compare = final_compare.assign(N2309_Comp = N2309_Comp.values)
final_compare = final_compare.assign(N2387_Comp = N2387_Comp.values)
final_compare = final_compare.assign(N2527_Comp = N2527_Comp.values)
final_compare = final_compare.assign(N2584_Comp = N2584_Comp.values)
final_compare = final_compare.assign(N2590_Comp = N2590_Comp.values)
final_compare = final_compare.assign(N2623_Comp = N2623_Comp.values)
final_compare = final_compare.assign(N3357_Comp = N3357_Comp.values)
final_compare = final_compare.assign(N3358_Comp = N3358_Comp.values)
final_compare = final_compare.assign(N3359_Comp = N3359_Comp.values)
final_compare = final_compare.assign(N3360_Comp = N3360_Comp.values)
final_compare = final_compare.assign(N3604_Comp = N3604_Comp.values)
final_compare = final_compare.assign(N3613_Comp = N3613_Comp.values)
final_compare = final_compare.assign(N4272_Comp = N4272_Comp.values)
final_compare = final_compare.assign(N4275_Comp = N4275_Comp.values)
final_compare = final_compare.assign(N4278_Comp = N4278_Comp.values)
final_compare = final_compare.assign(N4279_Comp = N4279_Comp.values)
final_compare = final_compare.assign(N4737_Comp = N4737_Comp.values)
final_compare = final_compare.assign(N4738_Comp = N4738_Comp.values)
final_compare = final_compare.assign(N4739_Comp = N4739_Comp.values)
final_compare = final_compare.assign(N4740_Comp = N4740_Comp.values)
final_compare = final_compare.assign(N5240_Comp = N5240_Comp.values)
final_compare = final_compare.assign(N5388_Comp = N5388_Comp.values)
final_compare = final_compare.assign(N6641_Comp = N6641_Comp.values)
final_compare = final_compare.assign(N6643_Comp = N6643_Comp.values)
final_compare = final_compare.assign(N6646_Comp = N6646_Comp.values)
final_compare = final_compare.assign(N6648_Comp = N6648_Comp.values)
final_compare = final_compare.assign(N6716_Comp = N6716_Comp.values)
final_compare = final_compare.assign(N6877_Comp = N6877_Comp.values)
final_compare = final_compare.assign(N6924_Comp = N6924_Comp.values)
final_compare = final_compare.assign(N6925_Comp = N6925_Comp.values)
final_compare = final_compare.assign(N6926_Comp = N6926_Comp.values)
final_compare = final_compare.assign(N6927_Comp = N6927_Comp.values)
final_compare = final_compare.assign(N7015_Comp = N7015_Comp.values)
final_compare = final_compare.assign(N7363_Comp = N7363_Comp.values)
final_compare = final_compare.assign(N7365_Comp = N7365_Comp.values)
final_compare = final_compare.assign(N7432_Comp = N7432_Comp.values)
final_compare = final_compare.assign(N7449_Comp = N7449_Comp.values)
final_compare = final_compare.assign(N7465_Comp = N7465_Comp.values)
final_compare = final_compare.assign(N7466_Comp = N7466_Comp.values)
final_compare = final_compare.assign(N7467_Comp = N7467_Comp.values)
final_compare = final_compare.assign(N7469_Comp = N7469_Comp.values)
final_compare = final_compare.assign(N7470_Comp = N7470_Comp.values)
final_compare = final_compare.assign(N7471_Comp = N7471_Comp.values)
final_compare = final_compare.assign(N7472_Comp = N7472_Comp.values)
final_compare = final_compare.assign(N7473_Comp = N7473_Comp.values)
final_compare = final_compare.assign(N7474_Comp = N7474_Comp.values)
final_compare = final_compare.assign(N7476_Comp = N7476_Comp.values)
final_compare = final_compare.assign(N7503_Comp = N7503_Comp.values)
final_compare = final_compare.assign(N7504_Comp = N7504_Comp.values)
final_compare = final_compare.assign(N7506_Comp = N7506_Comp.values)
final_compare = final_compare.assign(N7511_Comp = N7511_Comp.values)
final_compare = final_compare.assign(N7515_Comp = N7515_Comp.values)
final_compare = final_compare.assign(N7516_Comp = N7516_Comp.values)
final_compare = final_compare.assign(N7517_Comp = N7517_Comp.values)
final_compare = final_compare.assign(N7518_Comp = N7518_Comp.values)
final_compare = final_compare.assign(N7519_Comp = N7519_Comp.values)
final_compare = final_compare.assign(N7520_Comp = N7520_Comp.values)
final_compare = final_compare.assign(N7521_Comp = N7521_Comp.values)
final_compare = final_compare.assign(N7522_Comp = N7522_Comp.values)
final_compare = final_compare.assign(N7600_Comp = N7600_Comp.values)
final_compare = final_compare.assign(N7601_Comp = N7601_Comp.values)
final_compare = final_compare.assign(N7602_Comp = N7602_Comp.values)
final_compare = final_compare.assign(N7603_Comp = N7603_Comp.values)
final_compare = final_compare.assign(N7604_Comp = N7604_Comp.values)
final_compare = final_compare.assign(N7605_Comp = N7605_Comp.values)
final_compare = final_compare.assign(N7606_Comp = N7606_Comp.values)
final_compare = final_compare.assign(N7607_Comp = N7607_Comp.values)
final_compare = final_compare.assign(N7626_Comp = N7626_Comp.values)
final_compare = final_compare.assign(N7698_Comp = N7698_Comp.values)
final_compare = final_compare.assign(N7699_Comp = N7699_Comp.values)
final_compare = final_compare.assign(N7700_Comp = N7700_Comp.values)
final_compare = final_compare.assign(N7701_Comp = N7701_Comp.values)
final_compare = final_compare.assign(N7702_Comp = N7702_Comp.values)
final_compare = final_compare.assign(N7703_Comp = N7703_Comp.values)
final_compare = final_compare.assign(N7704_Comp = N7704_Comp.values)
final_compare = final_compare.assign(N7705_Comp = N7705_Comp.values)
final_compare = final_compare.assign(N7706_Comp = N7706_Comp.values)
final_compare = final_compare.assign(N7707_Comp = N7707_Comp.values)
final_compare = final_compare.assign(N7735_Comp = N7735_Comp.values)
final_compare = final_compare.assign(N7736_Comp = N7736_Comp.values)
final_compare = final_compare.assign(N7737_Comp = N7737_Comp.values)
final_compare = final_compare.assign(N7738_Comp = N7738_Comp.values)
final_compare = final_compare.assign(N7739_Comp = N7739_Comp.values)
final_compare = final_compare.assign(N7740_Comp = N7740_Comp.values)
final_compare = final_compare.assign(N7741_Comp = N7741_Comp.values)
final_compare = final_compare.assign(N7742_Comp = N7742_Comp.values)
final_compare = final_compare.assign(N7754_Comp = N7754_Comp.values)
final_compare = final_compare.assign(N7755_Comp = N7755_Comp.values)
final_compare = final_compare.assign(N7756_Comp = N7756_Comp.values)
final_compare = final_compare.assign(N7757_Comp = N7757_Comp.values)
final_compare = final_compare.assign(N7758_Comp = N7758_Comp.values)
final_compare = final_compare.assign(N7759_Comp = N7759_Comp.values)
final_compare = final_compare.assign(N7760_Comp = N7760_Comp.values)
final_compare = final_compare.assign(N7761_Comp = N7761_Comp.values)
final_compare = final_compare.assign(N8075_Comp = N8075_Comp.values)
final_compare = final_compare.assign(N8076_Comp = N8076_Comp.values)
final_compare = final_compare.assign(N8123_Comp = N8123_Comp.values)
final_compare = final_compare.assign(N8124_Comp = N8124_Comp.values)
final_compare = final_compare.assign(N8127_Comp = N8127_Comp.values)
final_compare = final_compare.assign(N8128_Comp = N8128_Comp.values)


final_compare["M/S"] = final_compare["N709_Comp"] + final_compare["N816_Comp"] + final_compare["N1066_Comp"] + final_compare["N1137_Comp"] + final_compare["N1138_Comp"] + final_compare["N1139_Comp"] + final_compare["N1140_Comp"] + final_compare["N1141_Comp"] + final_compare["N1142_Comp"] + final_compare["N1143_Comp"] + final_compare["N1144_Comp"] + final_compare["N1145_Comp"] + final_compare["N1147_Comp"] + final_compare["N1152_Comp"] + final_compare["N1153_Comp"] + final_compare["N1154_Comp"] + final_compare["N1155_Comp"] + final_compare["N1972_Comp"] + final_compare["N2054_Comp"] + final_compare["N2060_Comp"] + final_compare["N2061_Comp"] + final_compare["N2139_Comp"] + final_compare["N2142_Comp"] + final_compare["N2309_Comp"] + final_compare["N2387_Comp"] + final_compare["N2527_Comp"] + final_compare["N2584_Comp"] + final_compare["N2590_Comp"] + final_compare["N2623_Comp"] + final_compare["N3357_Comp"] + final_compare["N3358_Comp"] + final_compare["N3359_Comp"] + final_compare["N3360_Comp"] + final_compare["N3604_Comp"] + final_compare["N3613_Comp"] + final_compare["N4272_Comp"] + final_compare["N4275_Comp"] + final_compare["N4278_Comp"] + final_compare["N4279_Comp"] + final_compare["N4737_Comp"] + final_compare["N4738_Comp"] + final_compare["N4739_Comp"] + final_compare["N4740_Comp"] + final_compare["N5240_Comp"] + final_compare["N5388_Comp"] + final_compare["N6641_Comp"] + final_compare["N6643_Comp"] + final_compare["N6646_Comp"] + final_compare["N6648_Comp"] + final_compare["N6716_Comp"] + final_compare["N6877_Comp"] + final_compare["N6924_Comp"] + final_compare["N6925_Comp"] + final_compare["N6926_Comp"] + final_compare["N6927_Comp"] + final_compare["N7015_Comp"] + final_compare["N7363_Comp"] + final_compare["N7365_Comp"] + final_compare["N7432_Comp"] + final_compare["N7449_Comp"] + final_compare["N7465_Comp"] + final_compare["N7466_Comp"] + final_compare["N7467_Comp"] + final_compare["N7469_Comp"] + final_compare["N7470_Comp"] + final_compare["N7471_Comp"] + final_compare["N7472_Comp"] + final_compare["N7473_Comp"] + final_compare["N7474_Comp"] + final_compare["N7476_Comp"] + final_compare["N7503_Comp"] + final_compare["N7504_Comp"] + final_compare["N7506_Comp"] + final_compare["N7511_Comp"] + final_compare["N7515_Comp"] + final_compare["N7516_Comp"] + final_compare["N7517_Comp"] + final_compare["N7518_Comp"] + final_compare["N7519_Comp"] + final_compare["N7520_Comp"] + final_compare["N7521_Comp"] + final_compare["N7522_Comp"] + final_compare["N7600_Comp"] + final_compare["N7601_Comp"] + final_compare["N7602_Comp"] + final_compare["N7603_Comp"] + final_compare["N7604_Comp"] + final_compare["N7605_Comp"] + final_compare["N7606_Comp"] + final_compare["N7607_Comp"] + final_compare["N7626_Comp"] + final_compare["N7698_Comp"] + final_compare["N7699_Comp"] + final_compare["N7700_Comp"] + final_compare["N7701_Comp"] + final_compare["N7702_Comp"] + final_compare["N7703_Comp"] + final_compare["N7704_Comp"] + final_compare["N7705_Comp"] + final_compare["N7706_Comp"] + final_compare["N7707_Comp"] + final_compare["N7735_Comp"] + final_compare["N7736_Comp"] + final_compare["N7737_Comp"] + final_compare["N7738_Comp"] + final_compare["N7739_Comp"] + final_compare["N7740_Comp"] + final_compare["N7741_Comp"] + final_compare["N7742_Comp"] + final_compare["N7754_Comp"] + final_compare["N7755_Comp"] + final_compare["N7756_Comp"] + final_compare["N7757_Comp"] + final_compare["N7758_Comp"] + final_compare["N7759_Comp"] + final_compare["N7760_Comp"] + final_compare["N7761_Comp"] + final_compare["N8075_Comp"] + final_compare["N8076_Comp"] + final_compare["N8123_Comp"] + final_compare["N8124_Comp"] + final_compare["N8127_Comp"] + final_compare["N8128_Comp"]
final_compare.index.rename('Sr.No.', inplace=True)
final_compare.to_csv("compare_c5315.csv")

# final_compare = final_compare.loc[final_compare['M/S'] == 2]
# #print(final_compare)
# #Cri_Node = final_compare.iloc[:,1]
# #print(Cri_Node)
# #Multiple = final_compare.iloc[:,11]
# #print(Multiple)
# #final_compare = final_compare.assign(Multiple=Multiple.values)
# #final_compare = final_compare.assign(Cri_Node=Cri_Node.values)
# final_compare.to_csv("Critical.csv")
