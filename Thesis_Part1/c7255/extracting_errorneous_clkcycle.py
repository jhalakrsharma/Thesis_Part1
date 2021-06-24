import pandas as pd
import os
import csv
import subprocess
import random
import glob

final_compare = pd.DataFrame(columns = ["Clk", "Node", "N1", "N5", "N9", "N12", "N15", "N18", "N23", "N26", "N29", "N32", "N35", "N38", "N41", "N44", "N47", "N50", "N53", "N54", "N55", "N56", "N57", "N58", "N59", "N60", "N61", "N62", "N63", "N64", "N65", "N66", "N69", "N70", "N73", "N74", "N75", "N76", "N77", "N78", "N79", "N80", "N81", "N82", "N83", "N84", "N85", "N86", "N87", "N88", "N89", "N94", "N97", "N100", "N103", "N106", "N109", "N110", "N111", "N112", "N113", "N114", "N115", "N118", "N121", "N124", "N127", "N130", "N133", "N134", "N135", "N138", "N141", "N144", "N147", "N150", "N151", "N152", "N153", "N154", "N155", "N156", "N157", "N158", "N159", "N160", "N161", "N162", "N163", "N164", "N165", "N166", "N167", "N168", "N169", "N170", "N171", "N172", "N173", "N174", "N175", "N176", "N177", "N178", "N179", "N180", "N181", "N182", "N183", "N184", "N185", "N186", "N187", "N188", "N189", "N190", "N191", "N192", "N193", "N194", "N195", "N196", "N197", "N198", "N199", "N200", "N201", "N202", "N203", "N204", "N205", "N206", "N207", "N208", "N209", "N210", "N211", "N212", "N213", "N214", "N215", "N216", "N217", "N218", "N219", "N220", "N221", "N222", "N223", "N224", "N225", "N226", "N227", "N228", "N229", "N230", "N231", "N232", "N233", "N234", "N235", "N236", "N237", "N238", "N239", "N240", "N242", "N245", "N248", "N251", "N254", "N257", "N260", "N263", "N267", "N271", "N274", "N277", "N280", "N283", "N286", "N289", "N293", "N296", "N299", "N303", "N307", "N310", "N313", "N316", "N319", "N322", "N325", "N328", "N331", "N334", "N337", "N340", "N343", "N346", "N349", "N352", "N355", "N358", "N361", "N364", "N367", "N382", "N241_I", "N387", "N388", "N478", "N482", "N484", "N486", "N489", "N492", "N501", "N505", "N507", "N509", "N511", "N513", "N515", "N517", "N519", "N535", "N537", "N539", "N541", "N543", "N545", "N547", "N549", "N551", "N553", "N556", "N559", "N561", "N563", "N565", "N567", "N569", "N571", "N573", "N582", "N643", "N707", "N813", "N881", "N882", "N883", "N884", "N885", "N889", "N945", "N1110", "N1111", "N1112", "N1113", "N1114", "N1489", "N1490", "N1781", "N10025", "N10101", "N10102", "N10103", "N10104", "N10109", "N10110", "N10111", "N10112", "N10350", "N10351", "N10352", "N10353", "N10574", "N10575", "N10576", "N10628", "N10632", "N10641", "N10704", "N10706", "N10711", "N10712", "N10713", "N10714", "N10715", "N10716", "N10717", "N10718", "N10729", "N10759", "N10760", "N10761", "N10762", "N10763", "N10827", "N10837", "N10838", "N10839", "N10840", "N10868", "N10869", "N10870", "N10871", "N10905", "N10906", "N10907", "N10908", "N11333", "N11334", "N11340", "N11342", "N241_O", "N387g", "N388g", "N478g", "N482g", "N484g", "N486g", "N489g", "N492g", "N501g", "N505g", "N507g", "N509g", "N511g", "N513g", "N515g", "N517g", "N519g", "N535g", "N537g", "N539g", "N541g", "N543g", "N545g", "N547g", "N549g", "N551g", "N553g", "N556g", "N559g", "N561g", "N563g", "N565g", "N567g", "N569g", "N571g", "N573g", "N582g", "N643g", "N707g", "N813g", "N881g", "N882g", "N883g", "N884g", "N885g", "N889g", "N945g", "N1110g", "N1111g", "N1112g", "N1113g", "N1114g", "N1489g", "N1490g", "N1781g", "N10025g", "N10101g", "N10102g", "N10103g", "N10104g", "N10109g", "N10110g", "N10111g", "N10112g", "N10350g", "N10351g", "N10352g", "N10353g", "N10574g", "N10575g", "N10576g", "N10628g", "N10632g", "N10641g", "N10704g", "N10706g", "N10711g", "N10712g", "N10713g", "N10714g", "N10715g", "N10716g", "N10717g", "N10718g", "N10729g", "N10759g", "N10760g", "N10761g", "N10762g", "N10763g", "N10827g", "N10837g", "N10838g", "N10839g", "N10840g", "N10868g", "N10869g", "N10870g", "N10871g", "N10905g", "N10906g", "N10907g", "N10908g", "N11333g", "N11334g", "N11340g", "N11342g", "N241_Og"])

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
    N5 = df.iloc[0,2]
    N9 = df.iloc[0,3]
    N12 = df.iloc[0,4]
    N15 = df.iloc[0,5]
    N18 = df.iloc[0,6]
    N23 = df.iloc[0,7]
    N26 = df.iloc[0,8]
    N29 = df.iloc[0,9]
    N32 = df.iloc[0,10]
    N35 = df.iloc[0,11]
    N38 = df.iloc[0,12]
    N41 = df.iloc[0,13]
    N44 = df.iloc[0,14]
    N47 = df.iloc[0,15]
    N50 = df.iloc[0,16]
    N53 = df.iloc[0,17]
    N54 = df.iloc[0,18]
    N55 = df.iloc[0,19]
    N56 = df.iloc[0,20]
    N57 = df.iloc[0,21]
    N58 = df.iloc[0,22]
    N59 = df.iloc[0,23]
    N60 = df.iloc[0,24]
    N61 = df.iloc[0,25]
    N62 = df.iloc[0,26]
    N63 = df.iloc[0,27]
    N64 = df.iloc[0,28]
    N65 = df.iloc[0,29]
    N66 = df.iloc[0,30]
    N69 = df.iloc[0,31]
    N70 = df.iloc[0,32]
    N73 = df.iloc[0,33]
    N74 = df.iloc[0,34]
    N75 = df.iloc[0,35]
    N76 = df.iloc[0,36]
    N77 = df.iloc[0,37]
    N78 = df.iloc[0,38]
    N79 = df.iloc[0,39]
    N80 = df.iloc[0,40]
    N81 = df.iloc[0,41]
    N82 = df.iloc[0,42]
    N83 = df.iloc[0,43]
    N84 = df.iloc[0,44]
    N85 = df.iloc[0,45]
    N86 = df.iloc[0,46]
    N87 = df.iloc[0,47]
    N88 = df.iloc[0,48]
    N89 = df.iloc[0,49]
    N94 = df.iloc[0,50]
    N97 = df.iloc[0,51]
    N100 = df.iloc[0,52]
    N103 = df.iloc[0,53]
    N106 = df.iloc[0,54]
    N109 = df.iloc[0,55]
    N110 = df.iloc[0,56]
    N111 = df.iloc[0,57]
    N112 = df.iloc[0,58]
    N113 = df.iloc[0,59]
    N114 = df.iloc[0,60]
    N115 = df.iloc[0,61]
    N118 = df.iloc[0,62]
    N121 = df.iloc[0,63]
    N124 = df.iloc[0,64]
    N127 = df.iloc[0,65]
    N130 = df.iloc[0,66]
    N133 = df.iloc[0,67]
    N134 = df.iloc[0,68]
    N135 = df.iloc[0,69]
    N138 = df.iloc[0,70]
    N141 = df.iloc[0,71]
    N144 = df.iloc[0,72]
    N147 = df.iloc[0,73]
    N150 = df.iloc[0,74]
    N151 = df.iloc[0,75]
    N152 = df.iloc[0,76]
    N153 = df.iloc[0,77]
    N154 = df.iloc[0,78]
    N155 = df.iloc[0,79]
    N156 = df.iloc[0,80]
    N157 = df.iloc[0,81]
    N158 = df.iloc[0,82]
    N159 = df.iloc[0,83]
    N160 = df.iloc[0,84]
    N161 = df.iloc[0,85]
    N162 = df.iloc[0,86]
    N163 = df.iloc[0,87]
    N164 = df.iloc[0,88]
    N165 = df.iloc[0,89]
    N166 = df.iloc[0,90]
    N167 = df.iloc[0,91]
    N168 = df.iloc[0,92]
    N169 = df.iloc[0,93]
    N170 = df.iloc[0,94]
    N171 = df.iloc[0,95]
    N172 = df.iloc[0,96]
    N173 = df.iloc[0,97]
    N174 = df.iloc[0,98]
    N175 = df.iloc[0,99]
    N176 = df.iloc[0,100]
    N177 = df.iloc[0,101]
    N178 = df.iloc[0,102]
    N179 = df.iloc[0,103]
    N180 = df.iloc[0,104]
    N181 = df.iloc[0,105]
    N182 = df.iloc[0,106]
    N183 = df.iloc[0,107]
    N184 = df.iloc[0,108]
    N185 = df.iloc[0,109]
    N186 = df.iloc[0,110]
    N187 = df.iloc[0,111]
    N188 = df.iloc[0,112]
    N189 = df.iloc[0,113]
    N190 = df.iloc[0,114]
    N191 = df.iloc[0,115]
    N192 = df.iloc[0,116]
    N193 = df.iloc[0,117]
    N194 = df.iloc[0,118]
    N195 = df.iloc[0,119]
    N196 = df.iloc[0,120]
    N197 = df.iloc[0,121]
    N198 = df.iloc[0,122]
    N199 = df.iloc[0,123]
    N200 = df.iloc[0,124]
    N201 = df.iloc[0,125]
    N202 = df.iloc[0,126]
    N203 = df.iloc[0,127]
    N204 = df.iloc[0,128]
    N205 = df.iloc[0,129]
    N206 = df.iloc[0,130]
    N207 = df.iloc[0,131]
    N208 = df.iloc[0,132]
    N209 = df.iloc[0,133]
    N210 = df.iloc[0,134]
    N211 = df.iloc[0,135]
    N212 = df.iloc[0,136]
    N213 = df.iloc[0,137]
    N214 = df.iloc[0,138]
    N215 = df.iloc[0,139]
    N216 = df.iloc[0,140]
    N217 = df.iloc[0,141]
    N218 = df.iloc[0,142]
    N219 = df.iloc[0,143]
    N220 = df.iloc[0,144]
    N221 = df.iloc[0,145]
    N222 = df.iloc[0,146]
    N223 = df.iloc[0,147]
    N224 = df.iloc[0,148]
    N225 = df.iloc[0,149]
    N226 = df.iloc[0,150]
    N227 = df.iloc[0,151]
    N228 = df.iloc[0,152]
    N229 = df.iloc[0,153]
    N230 = df.iloc[0,154]
    N231 = df.iloc[0,155]
    N232 = df.iloc[0,156]
    N233 = df.iloc[0,157]
    N234 = df.iloc[0,158]
    N235 = df.iloc[0,159]
    N236 = df.iloc[0,160]
    N237 = df.iloc[0,161]
    N238 = df.iloc[0,162]
    N239 = df.iloc[0,163]
    N240 = df.iloc[0,164]
    N242 = df.iloc[0,165]
    N245 = df.iloc[0,166]
    N248 = df.iloc[0,167]
    N251 = df.iloc[0,168]
    N254 = df.iloc[0,169]
    N257 = df.iloc[0,170]
    N260 = df.iloc[0,171]
    N263 = df.iloc[0,172]
    N267 = df.iloc[0,173]
    N271 = df.iloc[0,174]
    N274 = df.iloc[0,175]
    N277 = df.iloc[0,176]
    N280 = df.iloc[0,177]
    N283 = df.iloc[0,178]
    N286 = df.iloc[0,179]
    N289 = df.iloc[0,180]
    N293 = df.iloc[0,181]
    N296 = df.iloc[0,182]
    N299 = df.iloc[0,183]
    N303 = df.iloc[0,184]
    N307 = df.iloc[0,185]
    N310 = df.iloc[0,186]
    N313 = df.iloc[0,187]
    N316 = df.iloc[0,188]
    N319 = df.iloc[0,189]
    N322 = df.iloc[0,190]
    N325 = df.iloc[0,191]
    N328 = df.iloc[0,192]
    N331 = df.iloc[0,193]
    N334 = df.iloc[0,194]
    N337 = df.iloc[0,195]
    N340 = df.iloc[0,196]
    N343 = df.iloc[0,197]
    N346 = df.iloc[0,198]
    N349 = df.iloc[0,199]
    N352 = df.iloc[0,200]
    N355 = df.iloc[0,201]
    N358 = df.iloc[0,202]
    N361 = df.iloc[0,203]
    N364 = df.iloc[0,204]
    N367 = df.iloc[0,205]
    N382 = df.iloc[0,206]
    N241_I = df.iloc[0,207]
#--------------------------------------------------------------------------------
## Extracting faulty output values
    ff = pd.read_csv(faulty_csv)

    # Same line at which error was enabled
    faulty = ff.loc[ff['Clk'] == time_outf]     
    #print(faulty)

    N387 = faulty.iloc[0,209]
    N388 = faulty.iloc[0,210]
    N478 = faulty.iloc[0,211]
    N482 = faulty.iloc[0,212]
    N484 = faulty.iloc[0,213]
    N486 = faulty.iloc[0,214]
    # print(N486)
    N489 = faulty.iloc[0,215]
    N492 = faulty.iloc[0,216]
    N501 = faulty.iloc[0,217]
    # print(N501)
    N505 = faulty.iloc[0,218]
    N507 = faulty.iloc[0,219]
    N509 = faulty.iloc[0,220]
    N511 = faulty.iloc[0,221]
    N513 = faulty.iloc[0,222]
    N515 = faulty.iloc[0,223]
    N517 = faulty.iloc[0,224]
    N519 = faulty.iloc[0,225]
    N535 = faulty.iloc[0,226]
    N537 = faulty.iloc[0,227]
    N539 = faulty.iloc[0,228]
    N541 = faulty.iloc[0,229]
    N543 = faulty.iloc[0,230]
    N545 = faulty.iloc[0,231]
    N547 = faulty.iloc[0,232]
    N549 = faulty.iloc[0,233]
    N551 = faulty.iloc[0,234]
    # print(N551)
    N553 = faulty.iloc[0,235]
    N556 = faulty.iloc[0,236]
    N559 = faulty.iloc[0,237]
    N561 = faulty.iloc[0,238]
    N563 = faulty.iloc[0,239]
    N565 = faulty.iloc[0,240]
    # print(N565)
    N567 = faulty.iloc[0,241]
    N569 = faulty.iloc[0,242]
    N571 = faulty.iloc[0,243]
    print(N571)
    N573 = faulty.iloc[0,244]
    N582 = faulty.iloc[0,245]
    # print(N582)
    N643 = faulty.iloc[0,246]
    N707 = faulty.iloc[0,247]
    N813 = faulty.iloc[0,248]
    N881 = faulty.iloc[0,249]
    N882 = faulty.iloc[0,250]
    N883 = faulty.iloc[0,251]
    N884 = faulty.iloc[0,252]
    N885 = faulty.iloc[0,253]
    N889 = faulty.iloc[0,254]
    N945 = faulty.iloc[0,255]
    N1110 = faulty.iloc[0,256]
    N1111 = faulty.iloc[0,257]
    N1112 = faulty.iloc[0,258]
    N1113 = faulty.iloc[0,259]
    N1114 = faulty.iloc[0,260]
    N1489 = faulty.iloc[0,261]
    N1490 = faulty.iloc[0,262]
    N1781 = faulty.iloc[0,263]
    N10025 = faulty.iloc[0,264]
    N10101 = faulty.iloc[0,265]
    N10102 = faulty.iloc[0,266]
    N10103 = faulty.iloc[0,267]
    N10104 = faulty.iloc[0,268]
    N10109 = faulty.iloc[0,269]
    N10110 = faulty.iloc[0,270]
    N10111 = faulty.iloc[0,271]
    N10112 = faulty.iloc[0,272]
    N10350 = faulty.iloc[0,273]
    N10351 = faulty.iloc[0,274]
    N10352 = faulty.iloc[0,275]
    N10353 = faulty.iloc[0,276]
    N10574 = faulty.iloc[0,277]
    N10575 = faulty.iloc[0,278]
    N10576 = faulty.iloc[0,279]
    N10628 = faulty.iloc[0,280]
    N10632 = faulty.iloc[0,281]
    N10641 = faulty.iloc[0,282]
    N10704 = faulty.iloc[0,283]
    N10706 = faulty.iloc[0,284]
    N10711 = faulty.iloc[0,285]
    N10712 = faulty.iloc[0,286]
    N10713 = faulty.iloc[0,287]
    N10714 = faulty.iloc[0,288]
    N10715 = faulty.iloc[0,289]
    N10716 = faulty.iloc[0,290]
    N10717 = faulty.iloc[0,291]
    N10718 = faulty.iloc[0,292]
    N10729 = faulty.iloc[0,293]
    N10759 = faulty.iloc[0,294]
    N10760 = faulty.iloc[0,295]
    N10761 = faulty.iloc[0,296]
    N10762 = faulty.iloc[0,297]
    N10763 = faulty.iloc[0,298]
    N10827 = faulty.iloc[0,299]
    N10837 = faulty.iloc[0,300]
    N10838 = faulty.iloc[0,301]
    N10839 = faulty.iloc[0,302]
    N10840 = faulty.iloc[0,303]
    N10868 = faulty.iloc[0,304]
    N10869 = faulty.iloc[0,305]
    N10870 = faulty.iloc[0,306]
    N10871 = faulty.iloc[0,307]
    N10905 = faulty.iloc[0,308]
    N10906 = faulty.iloc[0,309]
    N10907 = faulty.iloc[0,310]
    N10908 = faulty.iloc[0,311]
    N11333 = faulty.iloc[0,312]
    N11334 = faulty.iloc[0,313]
    N11340 = faulty.iloc[0,314]
    N11342 = faulty.iloc[0,315]
    N241_O = faulty.iloc[0,316]
#---------------------------------------------------------------------------------
    # Reading the golden output to extract correct value output
    cf = pd.read_csv('golden_c7552_iverilog_py.csv',low_memory=False)

    # Same line at which error was enabled
    gold = cf.loc[cf['Clk'] == time_outf]
    #print("Golden outputline",gold)
        
    N387g = gold.iloc[0,209]
    N388g = gold.iloc[0,210]
    N478g = gold.iloc[0,211]
    N482g = gold.iloc[0,212]
    N484g = gold.iloc[0,213]
    N486g = gold.iloc[0,214]
    # print(N486g)
    N489g = gold.iloc[0,215]
    N492g = gold.iloc[0,216]
    N501g = gold.iloc[0,217]
    # print(N501g)
    N505g = gold.iloc[0,218]
    N507g = gold.iloc[0,219]
    N509g = gold.iloc[0,220]
    N511g = gold.iloc[0,221]
    N513g = gold.iloc[0,222]
    N515g = gold.iloc[0,223]
    N517g = gold.iloc[0,224]
    N519g = gold.iloc[0,225]
    N535g = gold.iloc[0,226]
    N537g = gold.iloc[0,227]
    N539g = gold.iloc[0,228]
    N541g = gold.iloc[0,229]
    N543g = gold.iloc[0,230]
    N545g = gold.iloc[0,231]
    N547g = gold.iloc[0,232]
    N549g = gold.iloc[0,233]
    N551g = gold.iloc[0,234]
    N553g = gold.iloc[0,235]
    N556g = gold.iloc[0,236]
    N559g = gold.iloc[0,237]
    N561g = gold.iloc[0,238]
    N563g = gold.iloc[0,239]
    N565g = gold.iloc[0,240]
    # print(N565g)
    N567g = gold.iloc[0,241]
    N569g = gold.iloc[0,242]
    N571g = gold.iloc[0,243]
    print(N571g)
    N573g = gold.iloc[0,244]
    N582g = gold.iloc[0,245]
    # print(N582g)
    N643g = gold.iloc[0,246]
    N707g = gold.iloc[0,247]
    N813g = gold.iloc[0,248]
    N881g = gold.iloc[0,249]
    N882g = gold.iloc[0,250]
    N883g = gold.iloc[0,251]
    N884g = gold.iloc[0,252]
    N885g = gold.iloc[0,253]
    N889g = gold.iloc[0,254]
    N945g = gold.iloc[0,255]
    N1110g = gold.iloc[0,256]
    N1111g = gold.iloc[0,257]
    N1112g = gold.iloc[0,258]
    N1113g = gold.iloc[0,259]
    N1114g = gold.iloc[0,260]
    N1489g = gold.iloc[0,261]
    N1490g = gold.iloc[0,262]
    N1781g = gold.iloc[0,263]
    N10025g = gold.iloc[0,264]
    N10101g = gold.iloc[0,265]
    N10102g = gold.iloc[0,266]
    N10103g = gold.iloc[0,267]
    N10104g = gold.iloc[0,268]
    N10109g = gold.iloc[0,269]
    N10110g = gold.iloc[0,270]
    N10111g = gold.iloc[0,271]
    N10112g = gold.iloc[0,272]
    N10350g = gold.iloc[0,273]
    N10351g = gold.iloc[0,274]
    N10352g = gold.iloc[0,275]
    N10353g = gold.iloc[0,276]
    N10574g = gold.iloc[0,277]
    N10575g = gold.iloc[0,278]
    N10576g = gold.iloc[0,279]
    N10628g = gold.iloc[0,280]
    N10632g = gold.iloc[0,281]
    N10641g = gold.iloc[0,282]
    N10704g = gold.iloc[0,283]
    N10706g = gold.iloc[0,284]
    N10711g = gold.iloc[0,285]
    N10712g = gold.iloc[0,286]
    N10713g = gold.iloc[0,287]
    N10714g = gold.iloc[0,288]
    N10715g = gold.iloc[0,289]
    N10716g = gold.iloc[0,290]
    N10717g = gold.iloc[0,291]
    N10718g = gold.iloc[0,292]
    N10729g = gold.iloc[0,293]
    N10759g = gold.iloc[0,294]
    N10760g = gold.iloc[0,295]
    N10761g = gold.iloc[0,296]
    N10762g = gold.iloc[0,297]
    N10763g = gold.iloc[0,298]
    N10827g = gold.iloc[0,299]
    N10837g = gold.iloc[0,300]
    N10838g = gold.iloc[0,301]
    N10839g = gold.iloc[0,302]
    N10840g = gold.iloc[0,303]
    N10868g = gold.iloc[0,304]
    N10869g = gold.iloc[0,305]
    N10870g = gold.iloc[0,306]
    N10871g = gold.iloc[0,307]
    N10905g = gold.iloc[0,308]
    N10906g = gold.iloc[0,309]
    N10907g = gold.iloc[0,310]
    N10908g = gold.iloc[0,311]
    N11333g = gold.iloc[0,312]
    N11334g = gold.iloc[0,313]
    N11340g = gold.iloc[0,314]
    N11342g = gold.iloc[0,315]
    N241_Og = gold.iloc[0,316]

#---------------------------------------------------------------------------------
    #appending all values in order to form a row
    rows.append(time_in)
    rows.append(Node)
# Input columns    
    rows.append(N1)
    rows.append(N5)
    rows.append(N9)
    rows.append(N12)
    rows.append(N15)
    rows.append(N18)
    rows.append(N23)
    rows.append(N26)
    rows.append(N29)
    rows.append(N32)
    rows.append(N35)
    rows.append(N38)
    rows.append(N41)
    rows.append(N44)
    rows.append(N47)
    rows.append(N50)
    rows.append(N53)
    rows.append(N54)
    rows.append(N55)
    rows.append(N56)
    rows.append(N57)
    rows.append(N58)
    rows.append(N59)
    rows.append(N60)
    rows.append(N61)
    rows.append(N62)
    rows.append(N63)
    rows.append(N64)
    rows.append(N65)
    rows.append(N66)
    rows.append(N69)
    rows.append(N70)
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
    rows.append(N83)
    rows.append(N84)
    rows.append(N85)
    rows.append(N86)
    rows.append(N87)
    rows.append(N88)
    rows.append(N89)
    rows.append(N94)
    rows.append(N97)
    rows.append(N100)
    rows.append(N103)
    rows.append(N106)
    rows.append(N109)
    rows.append(N110)
    rows.append(N111)
    rows.append(N112)
    rows.append(N113)
    rows.append(N114)
    rows.append(N115)
    rows.append(N118)
    rows.append(N121)
    rows.append(N124)
    rows.append(N127)
    rows.append(N130)
    rows.append(N133)
    rows.append(N134)
    rows.append(N135)
    rows.append(N138)
    rows.append(N141)
    rows.append(N144)
    rows.append(N147)
    rows.append(N150)
    rows.append(N151)
    rows.append(N152)
    rows.append(N153)
    rows.append(N154)
    rows.append(N155)
    rows.append(N156)
    rows.append(N157)
    rows.append(N158)
    rows.append(N159)
    rows.append(N160)
    rows.append(N161)
    rows.append(N162)
    rows.append(N163)
    rows.append(N164)
    rows.append(N165)
    rows.append(N166)
    rows.append(N167)
    rows.append(N168)
    rows.append(N169)
    rows.append(N170)
    rows.append(N171)
    rows.append(N172)
    rows.append(N173)
    rows.append(N174)
    rows.append(N175)
    rows.append(N176)
    rows.append(N177)
    rows.append(N178)
    rows.append(N179)
    rows.append(N180)
    rows.append(N181)
    rows.append(N182)
    rows.append(N183)
    rows.append(N184)
    rows.append(N185)
    rows.append(N186)
    rows.append(N187)
    rows.append(N188)
    rows.append(N189)
    rows.append(N190)
    rows.append(N191)
    rows.append(N192)
    rows.append(N193)
    rows.append(N194)
    rows.append(N195)
    rows.append(N196)
    rows.append(N197)
    rows.append(N198)
    rows.append(N199)
    rows.append(N200)
    rows.append(N201)
    rows.append(N202)
    rows.append(N203)
    rows.append(N204)
    rows.append(N205)
    rows.append(N206)
    rows.append(N207)
    rows.append(N208)
    rows.append(N209)
    rows.append(N210)
    rows.append(N211)
    rows.append(N212)
    rows.append(N213)
    rows.append(N214)
    rows.append(N215)
    rows.append(N216)
    rows.append(N217)
    rows.append(N218)
    rows.append(N219)
    rows.append(N220)
    rows.append(N221)
    rows.append(N222)
    rows.append(N223)
    rows.append(N224)
    rows.append(N225)
    rows.append(N226)
    rows.append(N227)
    rows.append(N228)
    rows.append(N229)
    rows.append(N230)
    rows.append(N231)
    rows.append(N232)
    rows.append(N233)
    rows.append(N234)
    rows.append(N235)
    rows.append(N236)
    rows.append(N237)
    rows.append(N238)
    rows.append(N239)
    rows.append(N240)
    rows.append(N242)
    rows.append(N245)
    rows.append(N248)
    rows.append(N251)
    rows.append(N254)
    rows.append(N257)
    rows.append(N260)
    rows.append(N263)
    rows.append(N267)
    rows.append(N271)
    rows.append(N274)
    rows.append(N277)
    rows.append(N280)
    rows.append(N283)
    rows.append(N286)
    rows.append(N289)
    rows.append(N293)
    rows.append(N296)
    rows.append(N299)
    rows.append(N303)
    rows.append(N307)
    rows.append(N310)
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
    rows.append(N358)
    rows.append(N361)
    rows.append(N364)
    rows.append(N367)
    rows.append(N382)
    rows.append(N241_I)

    #faulty output
    rows.append(N387)
    # print(N387)
    rows.append(N388)
    rows.append(N478)
    rows.append(N482)
    rows.append(N484)
    rows.append(N486)
    rows.append(N489)
    rows.append(N492)
    rows.append(N501)
    rows.append(N505)
    rows.append(N507)
    rows.append(N509)
    rows.append(N511)
    rows.append(N513)
    rows.append(N515)
    rows.append(N517)
    rows.append(N519)
    rows.append(N535)
    rows.append(N537)
    rows.append(N539)
    rows.append(N541)
    rows.append(N543)
    rows.append(N545)
    rows.append(N547)
    rows.append(N549)
    rows.append(N551)
    rows.append(N553)
    rows.append(N556)
    rows.append(N559)
    rows.append(N561)
    rows.append(N563)
    rows.append(N565)
    rows.append(N567)
    rows.append(N569)
    rows.append(N571)
    rows.append(N573)
    rows.append(N582)
    rows.append(N643)
    rows.append(N707)
    rows.append(N813)
    rows.append(N881)
    rows.append(N882)
    rows.append(N883)
    rows.append(N884)
    rows.append(N885)
    rows.append(N889)
    rows.append(N945)
    rows.append(N1110)
    rows.append(N1111)
    rows.append(N1112)
    rows.append(N1113)
    rows.append(N1114)
    rows.append(N1489)
    rows.append(N1490)
    rows.append(N1781)
    rows.append(N10025)
    rows.append(N10101)
    rows.append(N10102)
    rows.append(N10103)
    rows.append(N10104)
    rows.append(N10109)
    rows.append(N10110)
    rows.append(N10111)
    rows.append(N10112)
    rows.append(N10350)
    rows.append(N10351)
    rows.append(N10352)
    rows.append(N10353)
    rows.append(N10574)
    rows.append(N10575)
    rows.append(N10576)
    rows.append(N10628)
    rows.append(N10632)
    rows.append(N10641)
    rows.append(N10704)
    rows.append(N10706)
    rows.append(N10711)
    rows.append(N10712)
    rows.append(N10713)
    rows.append(N10714)
    rows.append(N10715)
    rows.append(N10716)
    rows.append(N10717)
    rows.append(N10718)
    rows.append(N10729)
    rows.append(N10759)
    rows.append(N10760)
    rows.append(N10761)
    rows.append(N10762)
    rows.append(N10763)
    rows.append(N10827)
    rows.append(N10837)
    rows.append(N10838)
    rows.append(N10839)
    rows.append(N10840)
    rows.append(N10868)
    rows.append(N10869)
    rows.append(N10870)
    rows.append(N10871)
    rows.append(N10905)
    rows.append(N10906)
    rows.append(N10907)
    rows.append(N10908)
    rows.append(N11333)
    rows.append(N11334)
    rows.append(N11340)
    rows.append(N11342)
    rows.append(N241_O)

    #golden output
    rows.append(N387g)
    # print(N387g)
    rows.append(N388g)
    rows.append(N478g)
    rows.append(N482g)
    rows.append(N484g)
    rows.append(N486g)
    rows.append(N489g)
    rows.append(N492g)
    rows.append(N501g)
    rows.append(N505g)
    rows.append(N507g)
    rows.append(N509g)
    rows.append(N511g)
    rows.append(N513g)
    rows.append(N515g)
    rows.append(N517g)
    rows.append(N519g)
    rows.append(N535g)
    rows.append(N537g)
    rows.append(N539g)
    rows.append(N541g)
    rows.append(N543g)
    rows.append(N545g)
    rows.append(N547g)
    rows.append(N549g)
    rows.append(N551g)
    rows.append(N553g)
    rows.append(N556g)
    rows.append(N559g)
    rows.append(N561g)
    rows.append(N563g)
    rows.append(N565g)
    rows.append(N567g)
    rows.append(N569g)
    rows.append(N571g)
    rows.append(N573g)
    rows.append(N582g)
    rows.append(N643g)
    rows.append(N707g)
    rows.append(N813g)
    rows.append(N881g)
    rows.append(N882g)
    rows.append(N883g)
    rows.append(N884g)
    rows.append(N885g)
    rows.append(N889g)
    rows.append(N945g)
    rows.append(N1110g)
    rows.append(N1111g)
    rows.append(N1112g)
    rows.append(N1113g)
    rows.append(N1114g)
    rows.append(N1489g)
    rows.append(N1490g)
    rows.append(N1781g)
    rows.append(N10025g)
    rows.append(N10101g)
    rows.append(N10102g)
    rows.append(N10103g)
    rows.append(N10104g)
    rows.append(N10109g)
    rows.append(N10110g)
    rows.append(N10111g)
    rows.append(N10112g)
    rows.append(N10350g)
    rows.append(N10351g)
    rows.append(N10352g)
    rows.append(N10353g)
    rows.append(N10574g)
    rows.append(N10575g)
    rows.append(N10576g)
    rows.append(N10628g)
    rows.append(N10632g)
    rows.append(N10641g)
    rows.append(N10704g)
    rows.append(N10706g)
    rows.append(N10711g)
    rows.append(N10712g)
    rows.append(N10713g)
    rows.append(N10714g)
    rows.append(N10715g)
    rows.append(N10716g)
    rows.append(N10717g)
    rows.append(N10718g)
    rows.append(N10729g)
    rows.append(N10759g)
    rows.append(N10760g)
    rows.append(N10761g)
    rows.append(N10762g)
    rows.append(N10763g)
    rows.append(N10827g)
    rows.append(N10837g)
    rows.append(N10838g)
    rows.append(N10839g)
    rows.append(N10840g)
    rows.append(N10868g)
    rows.append(N10869g)
    rows.append(N10870g)
    rows.append(N10871g)
    rows.append(N10905g)
    rows.append(N10906g)
    rows.append(N10907g)
    rows.append(N10908g)
    rows.append(N11333g)
    rows.append(N11334g)
    rows.append(N11340g)
    rows.append(N11342g)
    rows.append(N241_Og)

    #print(rows)
    final_compare = final_compare.append(pd.Series(rows, index = ["Clk", "Node", "N1", "N5", "N9", "N12", "N15", "N18", "N23", "N26", "N29", "N32", "N35", "N38", "N41", "N44", "N47", "N50", "N53", "N54", "N55", "N56", "N57", "N58", "N59", "N60", "N61", "N62", "N63", "N64", "N65", "N66", "N69", "N70", "N73", "N74", "N75", "N76", "N77", "N78", "N79", "N80", "N81", "N82", "N83", "N84", "N85", "N86", "N87", "N88", "N89", "N94", "N97", "N100", "N103", "N106", "N109", "N110", "N111", "N112", "N113", "N114", "N115", "N118", "N121", "N124", "N127", "N130", "N133", "N134", "N135", "N138", "N141", "N144", "N147", "N150", "N151", "N152", "N153", "N154", "N155", "N156", "N157", "N158", "N159", "N160", "N161", "N162", "N163", "N164", "N165", "N166", "N167", "N168", "N169", "N170", "N171", "N172", "N173", "N174", "N175", "N176", "N177", "N178", "N179", "N180", "N181", "N182", "N183", "N184", "N185", "N186", "N187", "N188", "N189", "N190", "N191", "N192", "N193", "N194", "N195", "N196", "N197", "N198", "N199", "N200", "N201", "N202", "N203", "N204", "N205", "N206", "N207", "N208", "N209", "N210", "N211", "N212", "N213", "N214", "N215", "N216", "N217", "N218", "N219", "N220", "N221", "N222", "N223", "N224", "N225", "N226", "N227", "N228", "N229", "N230", "N231", "N232", "N233", "N234", "N235", "N236", "N237", "N238", "N239", "N240", "N242", "N245", "N248", "N251", "N254", "N257", "N260", "N263", "N267", "N271", "N274", "N277", "N280", "N283", "N286", "N289", "N293", "N296", "N299", "N303", "N307", "N310", "N313", "N316", "N319", "N322", "N325", "N328", "N331", "N334", "N337", "N340", "N343", "N346", "N349", "N352", "N355", "N358", "N361", "N364", "N367", "N382", "N241_I", "N387", "N388", "N478", "N482", "N484", "N486", "N489", "N492", "N501", "N505", "N507", "N509", "N511", "N513", "N515", "N517", "N519", "N535", "N537", "N539", "N541", "N543", "N545", "N547", "N549", "N551", "N553", "N556", "N559", "N561", "N563", "N565", "N567", "N569", "N571", "N573", "N582", "N643", "N707", "N813", "N881", "N882", "N883", "N884", "N885", "N889", "N945", "N1110", "N1111", "N1112", "N1113", "N1114", "N1489", "N1490", "N1781", "N10025", "N10101", "N10102", "N10103", "N10104", "N10109", "N10110", "N10111", "N10112", "N10350", "N10351", "N10352", "N10353", "N10574", "N10575", "N10576", "N10628", "N10632", "N10641", "N10704", "N10706", "N10711", "N10712", "N10713", "N10714", "N10715", "N10716", "N10717", "N10718", "N10729", "N10759", "N10760", "N10761", "N10762", "N10763", "N10827", "N10837", "N10838", "N10839", "N10840", "N10868", "N10869", "N10870", "N10871", "N10905", "N10906", "N10907", "N10908", "N11333", "N11334", "N11340", "N11342", "N241_O", "N387g", "N388g", "N478g", "N482g", "N484g", "N486g", "N489g", "N492g", "N501g", "N505g", "N507g", "N509g", "N511g", "N513g", "N515g", "N517g", "N519g", "N535g", "N537g", "N539g", "N541g", "N543g", "N545g", "N547g", "N549g", "N551g", "N553g", "N556g", "N559g", "N561g", "N563g", "N565g", "N567g", "N569g", "N571g", "N573g", "N582g", "N643g", "N707g", "N813g", "N881g", "N882g", "N883g", "N884g", "N885g", "N889g", "N945g", "N1110g", "N1111g", "N1112g", "N1113g", "N1114g", "N1489g", "N1490g", "N1781g", "N10025g", "N10101g", "N10102g", "N10103g", "N10104g", "N10109g", "N10110g", "N10111g", "N10112g", "N10350g", "N10351g", "N10352g", "N10353g", "N10574g", "N10575g", "N10576g", "N10628g", "N10632g", "N10641g", "N10704g", "N10706g", "N10711g", "N10712g", "N10713g", "N10714g", "N10715g", "N10716g", "N10717g", "N10718g", "N10729g", "N10759g", "N10760g", "N10761g", "N10762g", "N10763g", "N10827g", "N10837g", "N10838g", "N10839g", "N10840g", "N10868g", "N10869g", "N10870g", "N10871g", "N10905g", "N10906g", "N10907g", "N10908g", "N11333g", "N11334g", "N11340g", "N11342g", "N241_Og"]), ignore_index=True)
##---------------------------------------------------------------------------------
#print(final_compare)

N387_Comp = pd.to_numeric(final_compare['N387']) != pd.to_numeric(final_compare['N387g'])
N387_Comp = N387_Comp.astype(int)
N388_Comp = pd.to_numeric(final_compare['N388']) != pd.to_numeric(final_compare['N388g'])
N388_Comp = N388_Comp.astype(int)
N478_Comp = pd.to_numeric(final_compare['N478']) != pd.to_numeric(final_compare['N478g'])
N478_Comp = N478_Comp.astype(int)
N482_Comp = pd.to_numeric(final_compare['N482']) != pd.to_numeric(final_compare['N482g'])
N482_Comp = N482_Comp.astype(int)
N484_Comp = pd.to_numeric(final_compare['N484']) != pd.to_numeric(final_compare['N484g'])
N484_Comp = N484_Comp.astype(int)
N486_Comp = pd.to_numeric(final_compare['N486']) != pd.to_numeric(final_compare['N486g'])
N486_Comp = N486_Comp.astype(int)
N489_Comp = pd.to_numeric(final_compare['N489']) != pd.to_numeric(final_compare['N489g'])
N489_Comp = N489_Comp.astype(int)
N492_Comp = pd.to_numeric(final_compare['N492']) != pd.to_numeric(final_compare['N492g'])
N492_Comp = N492_Comp.astype(int)
N501_Comp = pd.to_numeric(final_compare['N501']) != pd.to_numeric(final_compare['N501g'])
N501_Comp = N501_Comp.astype(int)
N505_Comp = pd.to_numeric(final_compare['N505']) != pd.to_numeric(final_compare['N505g'])
N505_Comp = N505_Comp.astype(int)
N507_Comp = pd.to_numeric(final_compare['N507']) != pd.to_numeric(final_compare['N507g'])
N507_Comp = N507_Comp.astype(int)
N509_Comp = pd.to_numeric(final_compare['N509']) != pd.to_numeric(final_compare['N509g'])
N509_Comp = N509_Comp.astype(int)
N511_Comp = pd.to_numeric(final_compare['N511']) != pd.to_numeric(final_compare['N511g'])
N511_Comp = N511_Comp.astype(int)
N513_Comp = pd.to_numeric(final_compare['N513']) != pd.to_numeric(final_compare['N513g'])
N513_Comp = N513_Comp.astype(int)
N515_Comp = pd.to_numeric(final_compare['N515']) != pd.to_numeric(final_compare['N515g'])
N515_Comp = N515_Comp.astype(int)
N517_Comp = pd.to_numeric(final_compare['N517']) != pd.to_numeric(final_compare['N517g'])
N517_Comp = N517_Comp.astype(int)
N519_Comp = pd.to_numeric(final_compare['N519']) != pd.to_numeric(final_compare['N519g'])
N519_Comp = N519_Comp.astype(int)
N535_Comp = pd.to_numeric(final_compare['N535']) != pd.to_numeric(final_compare['N535g'])
N535_Comp = N535_Comp.astype(int)
N537_Comp = pd.to_numeric(final_compare['N537']) != pd.to_numeric(final_compare['N537g'])
N537_Comp = N537_Comp.astype(int)
N539_Comp = pd.to_numeric(final_compare['N539']) != pd.to_numeric(final_compare['N539g'])
N539_Comp = N539_Comp.astype(int)
N541_Comp = pd.to_numeric(final_compare['N541']) != pd.to_numeric(final_compare['N541g'])
N541_Comp = N541_Comp.astype(int)
N543_Comp = pd.to_numeric(final_compare['N543']) != pd.to_numeric(final_compare['N543g'])
N543_Comp = N543_Comp.astype(int)
N545_Comp = pd.to_numeric(final_compare['N545']) != pd.to_numeric(final_compare['N545g'])
N545_Comp = N545_Comp.astype(int)
N547_Comp = pd.to_numeric(final_compare['N547']) != pd.to_numeric(final_compare['N547g'])
N547_Comp = N547_Comp.astype(int)
N549_Comp = pd.to_numeric(final_compare['N549']) != pd.to_numeric(final_compare['N549g'])
N549_Comp = N549_Comp.astype(int)
N551_Comp = pd.to_numeric(final_compare['N551']) != pd.to_numeric(final_compare['N551g'])
N551_Comp = N551_Comp.astype(int)
N553_Comp = pd.to_numeric(final_compare['N553']) != pd.to_numeric(final_compare['N553g'])
N553_Comp = N553_Comp.astype(int)
N556_Comp = pd.to_numeric(final_compare['N556']) != pd.to_numeric(final_compare['N556g'])
N556_Comp = N556_Comp.astype(int)
N559_Comp = pd.to_numeric(final_compare['N559']) != pd.to_numeric(final_compare['N559g'])
N559_Comp = N559_Comp.astype(int)
N561_Comp = pd.to_numeric(final_compare['N561']) != pd.to_numeric(final_compare['N561g'])
N561_Comp = N561_Comp.astype(int)
N563_Comp = pd.to_numeric(final_compare['N563']) != pd.to_numeric(final_compare['N563g'])
N563_Comp = N563_Comp.astype(int)
N565_Comp = pd.to_numeric(final_compare['N565']) != pd.to_numeric(final_compare['N565g'])
N565_Comp = N565_Comp.astype(int)
N567_Comp = pd.to_numeric(final_compare['N567']) != pd.to_numeric(final_compare['N567g'])
N567_Comp = N567_Comp.astype(int)
N569_Comp = pd.to_numeric(final_compare['N569']) != pd.to_numeric(final_compare['N569g'])
N569_Comp = N569_Comp.astype(int)
N571_Comp = pd.to_numeric(final_compare['N571']) != pd.to_numeric(final_compare['N571g'])
N571_Comp = N571_Comp.astype(int)
N573_Comp = pd.to_numeric(final_compare['N573']) != pd.to_numeric(final_compare['N573g'])
N573_Comp = N573_Comp.astype(int)
N582_Comp = pd.to_numeric(final_compare['N582']) != pd.to_numeric(final_compare['N582g'])
N582_Comp = N582_Comp.astype(int)
N643_Comp = pd.to_numeric(final_compare['N643']) != pd.to_numeric(final_compare['N643g'])
N643_Comp = N643_Comp.astype(int)
N707_Comp = pd.to_numeric(final_compare['N707']) != pd.to_numeric(final_compare['N707g'])
N707_Comp = N707_Comp.astype(int)
N813_Comp = pd.to_numeric(final_compare['N813']) != pd.to_numeric(final_compare['N813g'])
N813_Comp = N813_Comp.astype(int)
N881_Comp = pd.to_numeric(final_compare['N881']) != pd.to_numeric(final_compare['N881g'])
N881_Comp = N881_Comp.astype(int)
N882_Comp = pd.to_numeric(final_compare['N882']) != pd.to_numeric(final_compare['N882g'])
N882_Comp = N882_Comp.astype(int)
N883_Comp = pd.to_numeric(final_compare['N883']) != pd.to_numeric(final_compare['N883g'])
N883_Comp = N883_Comp.astype(int)
N884_Comp = pd.to_numeric(final_compare['N884']) != pd.to_numeric(final_compare['N884g'])
N884_Comp = N884_Comp.astype(int)
N885_Comp = pd.to_numeric(final_compare['N885']) != pd.to_numeric(final_compare['N885g'])
N885_Comp = N885_Comp.astype(int)
N889_Comp = pd.to_numeric(final_compare['N889']) != pd.to_numeric(final_compare['N889g'])
N889_Comp = N889_Comp.astype(int)
N945_Comp = pd.to_numeric(final_compare['N945']) != pd.to_numeric(final_compare['N945g'])
N945_Comp = N945_Comp.astype(int)
N1110_Comp = pd.to_numeric(final_compare['N1110']) != pd.to_numeric(final_compare['N1110g'])
N1110_Comp = N1110_Comp.astype(int)
N1111_Comp = pd.to_numeric(final_compare['N1111']) != pd.to_numeric(final_compare['N1111g'])
N1111_Comp = N1111_Comp.astype(int)
N1112_Comp = pd.to_numeric(final_compare['N1112']) != pd.to_numeric(final_compare['N1112g'])
N1112_Comp = N1112_Comp.astype(int)
N1113_Comp = pd.to_numeric(final_compare['N1113']) != pd.to_numeric(final_compare['N1113g'])
N1113_Comp = N1113_Comp.astype(int)
N1114_Comp = pd.to_numeric(final_compare['N1114']) != pd.to_numeric(final_compare['N1114g'])
N1114_Comp = N1114_Comp.astype(int)
N1489_Comp = pd.to_numeric(final_compare['N1489']) != pd.to_numeric(final_compare['N1489g'])
N1489_Comp = N1489_Comp.astype(int)
N1490_Comp = pd.to_numeric(final_compare['N1490']) != pd.to_numeric(final_compare['N1490g'])
N1490_Comp = N1490_Comp.astype(int)
N1781_Comp = pd.to_numeric(final_compare['N1781']) != pd.to_numeric(final_compare['N1781g'])
N1781_Comp = N1781_Comp.astype(int)
N10025_Comp = pd.to_numeric(final_compare['N10025']) != pd.to_numeric(final_compare['N10025g'])
N10025_Comp = N10025_Comp.astype(int)
N10101_Comp = pd.to_numeric(final_compare['N10101']) != pd.to_numeric(final_compare['N10101g'])
N10101_Comp = N10101_Comp.astype(int)
N10102_Comp = pd.to_numeric(final_compare['N10102']) != pd.to_numeric(final_compare['N10102g'])
N10102_Comp = N10102_Comp.astype(int)
N10103_Comp = pd.to_numeric(final_compare['N10103']) != pd.to_numeric(final_compare['N10103g'])
N10103_Comp = N10103_Comp.astype(int)
N10104_Comp = pd.to_numeric(final_compare['N10104']) != pd.to_numeric(final_compare['N10104g'])
N10104_Comp = N10104_Comp.astype(int)
N10109_Comp = pd.to_numeric(final_compare['N10109']) != pd.to_numeric(final_compare['N10109g'])
N10109_Comp = N10109_Comp.astype(int)
N10110_Comp = pd.to_numeric(final_compare['N10110']) != pd.to_numeric(final_compare['N10110g'])
N10110_Comp = N10110_Comp.astype(int)
N10111_Comp = pd.to_numeric(final_compare['N10111']) != pd.to_numeric(final_compare['N10111g'])
N10111_Comp = N10111_Comp.astype(int)
N10112_Comp = pd.to_numeric(final_compare['N10112']) != pd.to_numeric(final_compare['N10112g'])
N10112_Comp = N10112_Comp.astype(int)
N10350_Comp = pd.to_numeric(final_compare['N10350']) != pd.to_numeric(final_compare['N10350g'])
N10350_Comp = N10350_Comp.astype(int)
N10351_Comp = pd.to_numeric(final_compare['N10351']) != pd.to_numeric(final_compare['N10351g'])
N10351_Comp = N10351_Comp.astype(int)
N10352_Comp = pd.to_numeric(final_compare['N10352']) != pd.to_numeric(final_compare['N10352g'])
N10352_Comp = N10352_Comp.astype(int)
N10353_Comp = pd.to_numeric(final_compare['N10353']) != pd.to_numeric(final_compare['N10353g'])
N10353_Comp = N10353_Comp.astype(int)
N10574_Comp = pd.to_numeric(final_compare['N10574']) != pd.to_numeric(final_compare['N10574g'])
N10574_Comp = N10574_Comp.astype(int)
N10575_Comp = pd.to_numeric(final_compare['N10575']) != pd.to_numeric(final_compare['N10575g'])
N10575_Comp = N10575_Comp.astype(int)
N10576_Comp = pd.to_numeric(final_compare['N10576']) != pd.to_numeric(final_compare['N10576g'])
N10576_Comp = N10576_Comp.astype(int)
N10628_Comp = pd.to_numeric(final_compare['N10628']) != pd.to_numeric(final_compare['N10628g'])
N10628_Comp = N10628_Comp.astype(int)
N10632_Comp = pd.to_numeric(final_compare['N10632']) != pd.to_numeric(final_compare['N10632g'])
N10632_Comp = N10632_Comp.astype(int)
N10641_Comp = pd.to_numeric(final_compare['N10641']) != pd.to_numeric(final_compare['N10641g'])
N10641_Comp = N10641_Comp.astype(int)
N10704_Comp = pd.to_numeric(final_compare['N10704']) != pd.to_numeric(final_compare['N10704g'])
N10704_Comp = N10704_Comp.astype(int)
N10706_Comp = pd.to_numeric(final_compare['N10706']) != pd.to_numeric(final_compare['N10706g'])
N10706_Comp = N10706_Comp.astype(int)
N10711_Comp = pd.to_numeric(final_compare['N10711']) != pd.to_numeric(final_compare['N10711g'])
N10711_Comp = N10711_Comp.astype(int)
N10712_Comp = pd.to_numeric(final_compare['N10712']) != pd.to_numeric(final_compare['N10712g'])
N10712_Comp = N10712_Comp.astype(int)
N10713_Comp = pd.to_numeric(final_compare['N10713']) != pd.to_numeric(final_compare['N10713g'])
N10713_Comp = N10713_Comp.astype(int)
N10714_Comp = pd.to_numeric(final_compare['N10714']) != pd.to_numeric(final_compare['N10714g'])
N10714_Comp = N10714_Comp.astype(int)
N10715_Comp = pd.to_numeric(final_compare['N10715']) != pd.to_numeric(final_compare['N10715g'])
N10715_Comp = N10715_Comp.astype(int)
N10716_Comp = pd.to_numeric(final_compare['N10716']) != pd.to_numeric(final_compare['N10716g'])
N10716_Comp = N10716_Comp.astype(int)
N10717_Comp = pd.to_numeric(final_compare['N10717']) != pd.to_numeric(final_compare['N10717g'])
N10717_Comp = N10717_Comp.astype(int)
N10718_Comp = pd.to_numeric(final_compare['N10718']) != pd.to_numeric(final_compare['N10718g'])
N10718_Comp = N10718_Comp.astype(int)
N10729_Comp = pd.to_numeric(final_compare['N10729']) != pd.to_numeric(final_compare['N10729g'])
N10729_Comp = N10729_Comp.astype(int)
N10759_Comp = pd.to_numeric(final_compare['N10759']) != pd.to_numeric(final_compare['N10759g'])
N10759_Comp = N10759_Comp.astype(int)
N10760_Comp = pd.to_numeric(final_compare['N10760']) != pd.to_numeric(final_compare['N10760g'])
N10760_Comp = N10760_Comp.astype(int)
N10761_Comp = pd.to_numeric(final_compare['N10761']) != pd.to_numeric(final_compare['N10761g'])
N10761_Comp = N10761_Comp.astype(int)
N10762_Comp = pd.to_numeric(final_compare['N10762']) != pd.to_numeric(final_compare['N10762g'])
N10762_Comp = N10762_Comp.astype(int)
N10763_Comp = pd.to_numeric(final_compare['N10763']) != pd.to_numeric(final_compare['N10763g'])
N10763_Comp = N10763_Comp.astype(int)
N10827_Comp = pd.to_numeric(final_compare['N10827']) != pd.to_numeric(final_compare['N10827g'])
N10827_Comp = N10827_Comp.astype(int)
N10837_Comp = pd.to_numeric(final_compare['N10837']) != pd.to_numeric(final_compare['N10837g'])
N10837_Comp = N10837_Comp.astype(int)
N10838_Comp = pd.to_numeric(final_compare['N10838']) != pd.to_numeric(final_compare['N10838g'])
N10838_Comp = N10838_Comp.astype(int)
N10839_Comp = pd.to_numeric(final_compare['N10839']) != pd.to_numeric(final_compare['N10839g'])
N10839_Comp = N10839_Comp.astype(int)
N10840_Comp = pd.to_numeric(final_compare['N10840']) != pd.to_numeric(final_compare['N10840g'])
N10840_Comp = N10840_Comp.astype(int)
N10868_Comp = pd.to_numeric(final_compare['N10868']) != pd.to_numeric(final_compare['N10868g'])
N10868_Comp = N10868_Comp.astype(int)
N10869_Comp = pd.to_numeric(final_compare['N10869']) != pd.to_numeric(final_compare['N10869g'])
N10869_Comp = N10869_Comp.astype(int)
N10870_Comp = pd.to_numeric(final_compare['N10870']) != pd.to_numeric(final_compare['N10870g'])
N10870_Comp = N10870_Comp.astype(int)
N10871_Comp = pd.to_numeric(final_compare['N10871']) != pd.to_numeric(final_compare['N10871g'])
N10871_Comp = N10871_Comp.astype(int)
N10905_Comp = pd.to_numeric(final_compare['N10905']) != pd.to_numeric(final_compare['N10905g'])
N10905_Comp = N10905_Comp.astype(int)
N10906_Comp = pd.to_numeric(final_compare['N10906']) != pd.to_numeric(final_compare['N10906g'])
N10906_Comp = N10906_Comp.astype(int)
N10907_Comp = pd.to_numeric(final_compare['N10907']) != pd.to_numeric(final_compare['N10907g'])
N10907_Comp = N10907_Comp.astype(int)
N10908_Comp = pd.to_numeric(final_compare['N10908']) != pd.to_numeric(final_compare['N10908g'])
N10908_Comp = N10908_Comp.astype(int)
N11333_Comp = pd.to_numeric(final_compare['N11333']) != pd.to_numeric(final_compare['N11333g'])
N11333_Comp = N11333_Comp.astype(int)
N11334_Comp = pd.to_numeric(final_compare['N11334']) != pd.to_numeric(final_compare['N11334g'])
N11334_Comp = N11334_Comp.astype(int)
N11340_Comp = pd.to_numeric(final_compare['N11340']) != pd.to_numeric(final_compare['N11340g'])
N11340_Comp = N11340_Comp.astype(int)
N11342_Comp = pd.to_numeric(final_compare['N11342']) != pd.to_numeric(final_compare['N11342g'])
N11342_Comp = N11342_Comp.astype(int)
N241_O_Comp = pd.to_numeric(final_compare['N241_O']) != pd.to_numeric(final_compare['N241_Og'])
N241_O_Comp = N241_O_Comp.astype(int)

final_compare = final_compare.assign(N387_Comp = N387_Comp.values)
final_compare = final_compare.assign(N388_Comp = N388_Comp.values)
final_compare = final_compare.assign(N478_Comp = N478_Comp.values)
final_compare = final_compare.assign(N482_Comp = N482_Comp.values)
final_compare = final_compare.assign(N484_Comp = N484_Comp.values)
final_compare = final_compare.assign(N486_Comp = N486_Comp.values)
final_compare = final_compare.assign(N489_Comp = N489_Comp.values)
final_compare = final_compare.assign(N492_Comp = N492_Comp.values)
final_compare = final_compare.assign(N501_Comp = N501_Comp.values)
final_compare = final_compare.assign(N505_Comp = N505_Comp.values)
final_compare = final_compare.assign(N507_Comp = N507_Comp.values)
final_compare = final_compare.assign(N509_Comp = N509_Comp.values)
final_compare = final_compare.assign(N511_Comp = N511_Comp.values)
final_compare = final_compare.assign(N513_Comp = N513_Comp.values)
final_compare = final_compare.assign(N515_Comp = N515_Comp.values)
final_compare = final_compare.assign(N517_Comp = N517_Comp.values)
final_compare = final_compare.assign(N519_Comp = N519_Comp.values)
final_compare = final_compare.assign(N535_Comp = N535_Comp.values)
final_compare = final_compare.assign(N537_Comp = N537_Comp.values)
final_compare = final_compare.assign(N539_Comp = N539_Comp.values)
final_compare = final_compare.assign(N541_Comp = N541_Comp.values)
final_compare = final_compare.assign(N543_Comp = N543_Comp.values)
final_compare = final_compare.assign(N545_Comp = N545_Comp.values)
final_compare = final_compare.assign(N547_Comp = N547_Comp.values)
final_compare = final_compare.assign(N549_Comp = N549_Comp.values)
final_compare = final_compare.assign(N551_Comp = N551_Comp.values)
final_compare = final_compare.assign(N553_Comp = N553_Comp.values)
final_compare = final_compare.assign(N556_Comp = N556_Comp.values)
final_compare = final_compare.assign(N559_Comp = N559_Comp.values)
final_compare = final_compare.assign(N561_Comp = N561_Comp.values)
final_compare = final_compare.assign(N563_Comp = N563_Comp.values)
final_compare = final_compare.assign(N565_Comp = N565_Comp.values)
final_compare = final_compare.assign(N567_Comp = N567_Comp.values)
final_compare = final_compare.assign(N569_Comp = N569_Comp.values)
final_compare = final_compare.assign(N571_Comp = N571_Comp.values)
final_compare = final_compare.assign(N573_Comp = N573_Comp.values)
final_compare = final_compare.assign(N582_Comp = N582_Comp.values)
final_compare = final_compare.assign(N643_Comp = N643_Comp.values)
final_compare = final_compare.assign(N707_Comp = N707_Comp.values)
final_compare = final_compare.assign(N813_Comp = N813_Comp.values)
final_compare = final_compare.assign(N881_Comp = N881_Comp.values)
final_compare = final_compare.assign(N882_Comp = N882_Comp.values)
final_compare = final_compare.assign(N883_Comp = N883_Comp.values)
final_compare = final_compare.assign(N884_Comp = N884_Comp.values)
final_compare = final_compare.assign(N885_Comp = N885_Comp.values)
final_compare = final_compare.assign(N889_Comp = N889_Comp.values)
final_compare = final_compare.assign(N945_Comp = N945_Comp.values)
final_compare = final_compare.assign(N1110_Comp = N1110_Comp.values)
final_compare = final_compare.assign(N1111_Comp = N1111_Comp.values)
final_compare = final_compare.assign(N1112_Comp = N1112_Comp.values)
final_compare = final_compare.assign(N1113_Comp = N1113_Comp.values)
final_compare = final_compare.assign(N1114_Comp = N1114_Comp.values)
final_compare = final_compare.assign(N1489_Comp = N1489_Comp.values)
final_compare = final_compare.assign(N1490_Comp = N1490_Comp.values)
final_compare = final_compare.assign(N1781_Comp = N1781_Comp.values)
final_compare = final_compare.assign(N10025_Comp = N10025_Comp.values)
final_compare = final_compare.assign(N10101_Comp = N10101_Comp.values)
final_compare = final_compare.assign(N10102_Comp = N10102_Comp.values)
final_compare = final_compare.assign(N10103_Comp = N10103_Comp.values)
final_compare = final_compare.assign(N10104_Comp = N10104_Comp.values)
final_compare = final_compare.assign(N10109_Comp = N10109_Comp.values)
final_compare = final_compare.assign(N10110_Comp = N10110_Comp.values)
final_compare = final_compare.assign(N10111_Comp = N10111_Comp.values)
final_compare = final_compare.assign(N10112_Comp = N10112_Comp.values)
final_compare = final_compare.assign(N10350_Comp = N10350_Comp.values)
final_compare = final_compare.assign(N10351_Comp = N10351_Comp.values)
final_compare = final_compare.assign(N10352_Comp = N10352_Comp.values)
final_compare = final_compare.assign(N10353_Comp = N10353_Comp.values)
final_compare = final_compare.assign(N10574_Comp = N10574_Comp.values)
final_compare = final_compare.assign(N10575_Comp = N10575_Comp.values)
final_compare = final_compare.assign(N10576_Comp = N10576_Comp.values)
final_compare = final_compare.assign(N10628_Comp = N10628_Comp.values)
final_compare = final_compare.assign(N10632_Comp = N10632_Comp.values)
final_compare = final_compare.assign(N10641_Comp = N10641_Comp.values)
final_compare = final_compare.assign(N10704_Comp = N10704_Comp.values)
final_compare = final_compare.assign(N10706_Comp = N10706_Comp.values)
final_compare = final_compare.assign(N10711_Comp = N10711_Comp.values)
final_compare = final_compare.assign(N10712_Comp = N10712_Comp.values)
final_compare = final_compare.assign(N10713_Comp = N10713_Comp.values)
final_compare = final_compare.assign(N10714_Comp = N10714_Comp.values)
final_compare = final_compare.assign(N10715_Comp = N10715_Comp.values)
final_compare = final_compare.assign(N10716_Comp = N10716_Comp.values)
final_compare = final_compare.assign(N10717_Comp = N10717_Comp.values)
final_compare = final_compare.assign(N10718_Comp = N10718_Comp.values)
final_compare = final_compare.assign(N10729_Comp = N10729_Comp.values)
final_compare = final_compare.assign(N10759_Comp = N10759_Comp.values)
final_compare = final_compare.assign(N10760_Comp = N10760_Comp.values)
final_compare = final_compare.assign(N10761_Comp = N10761_Comp.values)
final_compare = final_compare.assign(N10762_Comp = N10762_Comp.values)
final_compare = final_compare.assign(N10763_Comp = N10763_Comp.values)
final_compare = final_compare.assign(N10827_Comp = N10827_Comp.values)
final_compare = final_compare.assign(N10837_Comp = N10837_Comp.values)
final_compare = final_compare.assign(N10838_Comp = N10838_Comp.values)
final_compare = final_compare.assign(N10839_Comp = N10839_Comp.values)
final_compare = final_compare.assign(N10840_Comp = N10840_Comp.values)
final_compare = final_compare.assign(N10868_Comp = N10868_Comp.values)
final_compare = final_compare.assign(N10869_Comp = N10869_Comp.values)
final_compare = final_compare.assign(N10870_Comp = N10870_Comp.values)
final_compare = final_compare.assign(N10871_Comp = N10871_Comp.values)
final_compare = final_compare.assign(N10905_Comp = N10905_Comp.values)
final_compare = final_compare.assign(N10906_Comp = N10906_Comp.values)
final_compare = final_compare.assign(N10907_Comp = N10907_Comp.values)
final_compare = final_compare.assign(N10908_Comp = N10908_Comp.values)
final_compare = final_compare.assign(N11333_Comp = N11333_Comp.values)
final_compare = final_compare.assign(N11334_Comp = N11334_Comp.values)
final_compare = final_compare.assign(N11340_Comp = N11340_Comp.values)
final_compare = final_compare.assign(N11342_Comp = N11342_Comp.values)
final_compare = final_compare.assign(N241_O_Comp = N241_O_Comp.values)

final_compare["M/S"] = final_compare["N387_Comp"] + final_compare["N388_Comp"] + final_compare["N478_Comp"] + final_compare["N482_Comp"] + final_compare["N484_Comp"] + final_compare["N486_Comp"] + final_compare["N489_Comp"] + final_compare["N492_Comp"] + final_compare["N501_Comp"] + final_compare["N505_Comp"] + final_compare["N507_Comp"] + final_compare["N509_Comp"] + final_compare["N511_Comp"] + final_compare["N513_Comp"] + final_compare["N515_Comp"] + final_compare["N517_Comp"] + final_compare["N519_Comp"] + final_compare["N535_Comp"] + final_compare["N537_Comp"] + final_compare["N539_Comp"] + final_compare["N541_Comp"] + final_compare["N543_Comp"] + final_compare["N545_Comp"] + final_compare["N547_Comp"] + final_compare["N549_Comp"] + final_compare["N551_Comp"] + final_compare["N553_Comp"] + final_compare["N556_Comp"] + final_compare["N559_Comp"] + final_compare["N561_Comp"] + final_compare["N563_Comp"] + final_compare["N565_Comp"] + final_compare["N567_Comp"] + final_compare["N569_Comp"] + final_compare["N571_Comp"] + final_compare["N573_Comp"] + final_compare["N582_Comp"] + final_compare["N643_Comp"] + final_compare["N707_Comp"] + final_compare["N813_Comp"] + final_compare["N881_Comp"] + final_compare["N882_Comp"] + final_compare["N883_Comp"] + final_compare["N884_Comp"] + final_compare["N885_Comp"] + final_compare["N889_Comp"] + final_compare["N945_Comp"] + final_compare["N1110_Comp"] + final_compare["N1111_Comp"] + final_compare["N1112_Comp"] + final_compare["N1113_Comp"] + final_compare["N1114_Comp"] + final_compare["N1489_Comp"] + final_compare["N1490_Comp"] + final_compare["N1781_Comp"] + final_compare["N10025_Comp"] + final_compare["N10101_Comp"] + final_compare["N10102_Comp"] + final_compare["N10103_Comp"] + final_compare["N10104_Comp"] + final_compare["N10109_Comp"] + final_compare["N10110_Comp"] + final_compare["N10111_Comp"] + final_compare["N10112_Comp"] + final_compare["N10350_Comp"] + final_compare["N10351_Comp"] + final_compare["N10352_Comp"] + final_compare["N10353_Comp"] + final_compare["N10574_Comp"] + final_compare["N10575_Comp"] + final_compare["N10576_Comp"] + final_compare["N10628_Comp"] + final_compare["N10632_Comp"] + final_compare["N10641_Comp"] + final_compare["N10704_Comp"] + final_compare["N10706_Comp"] + final_compare["N10711_Comp"] + final_compare["N10712_Comp"] + final_compare["N10713_Comp"] + final_compare["N10714_Comp"] + final_compare["N10715_Comp"] + final_compare["N10716_Comp"] + final_compare["N10717_Comp"] + final_compare["N10718_Comp"] + final_compare["N10729_Comp"] + final_compare["N10759_Comp"] + final_compare["N10760_Comp"] + final_compare["N10761_Comp"] + final_compare["N10762_Comp"] + final_compare["N10763_Comp"] + final_compare["N10827_Comp"] + final_compare["N10837_Comp"] + final_compare["N10838_Comp"] + final_compare["N10839_Comp"] + final_compare["N10840_Comp"] + final_compare["N10868_Comp"] + final_compare["N10869_Comp"] + final_compare["N10870_Comp"] + final_compare["N10871_Comp"] + final_compare["N10905_Comp"] + final_compare["N10906_Comp"] + final_compare["N10907_Comp"] + final_compare["N10908_Comp"] + final_compare["N11333_Comp"] + final_compare["N11334_Comp"] + final_compare["N11340_Comp"] + final_compare["N11342_Comp"] + final_compare["N241_O_Comp"]

final_compare.index.rename('Sr.No.', inplace=True)
final_compare.to_csv("compare_c7552.csv")

# final_compare = final_compare.loc[final_compare['M/S'] == 2]
# #print(final_compare)
# #Cri_Node = final_compare.iloc[:,1]
# #print(Cri_Node)
# #Multiple = final_compare.iloc[:,11]
# #print(Multiple)
# #final_compare = final_compare.assign(Multiple=Multiple.values)
# #final_compare = final_compare.assign(Cri_Node=Cri_Node.values)
# final_compare.to_csv("Critical.csv")
