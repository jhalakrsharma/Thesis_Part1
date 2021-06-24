import glob, os
import subprocess
import random
import csv
import datetime
#print(str(datetime.datetime.now().time()))

#Critical nodes extracted from the golden code.
parameter = ['N1', 'N4', 'N7', 'N10', 'N13', 'N16', 'N19', 'N22', 'N25', 'N28', 'N31', 'N34', 'N37', 'N40', 'N43', 'N46', 'N49', 'N53', 'N56', 'N60', 'N63', 'N66', 'N69', 'N72', 'N76', 'N79', 'N82', 'N85', 'N88', 'N91', 'N94', 'N99', 'N104', 'd1', 'd4', 'd7', 'd10', 'd13', 'd16', 'd19', 'd22', 'd25', 'd28', 'd31', 'd34', 'd37', 'd40', 'd43', 'd46', 'd49', 'd53', 'd56', 'd60', 'd63', 'd66', 'd69', 'd72', 'd76', 'd79', 'd82', 'd85', 'd88', 'd91', 'd94', 'd99', 'd104', 'd2753', 'd2754', 'd2755', 'd2756', 'd2762', 'd2767', 'd2768', 'd2779', 'd2780', 'd2781', 'd2782', 'd2783', 'd2784', 'd2785', 'd2786', 'd2787', 'd2811', 'd2886', 'd2887', 'd2888', 'd2889', 'd2890', 'd2891', 'd2892', 'd2899', 'N190', 'N194', 'N197', 'N201', 'N206', 'N209', 'N212', 'N216', 'N220', 'N225', 'N229', 'N232', 'N235', 'N239', 
'N243', 'N247', 'N251', 'N252', 'N253', 'N256', 'N257', 'N260', 'N263', 'N266', 'N269', 'N272', 'N275', 'N276', 'N277', 'N280', 'N283', 'N290', 'N297', 'N300', 'N303', 'N306', 'N313', 'N316', 'N319', 'N326', 'N331', 'N338', 'N343', 'N346', 'N349', 'N352', 'N355', 'N358', 'N361', 'N364', 'N367', 'N370', 'N373', 'N376', 'N379', 'N382', 'N385', 'N388', 'N534', 'N535', 'N536', 'N537', 'N538', 'N539', 'N540', 'N541', 'N542', 'N543', 'N544', 'N545', 'N546', 'N547', 'N548', 'N549', 'N550', 'N551', 'N552', 'N553', 'N554', 'N555', 'N556', 'N559', 'N562', 'N565', 'N568', 'N571', 'N574', 'N577', 'N580', 'N583', 'N586', 'N589', 'N592', 'N595', 'N598', 
'N601', 'N602', 'N603', 'N608', 'N612', 'N616', 'N619', 'N622', 'N625', 'N628', 'N631', 'N634', 'N637', 'N640', 'N643', 'N646', 'N649', 'N652', 'N655', 'N658', 'N661', 'N664', 'N667', 'N670', 'N673', 'N676', 'N679', 'N682', 'N685', 'N688', 'N691', 'N694', 'N697', 'N700', 'N703', 'N706', 'N709', 'N712', 'N715', 'N718', 'N721', 'N724', 'N727', 'N730', 'N733', 'N736', 'N739', 'N742', 'N745', 'N748', 'N751', 'N886', 'N887', 'N888', 'N889', 'N890', 'N891', 'N892', 'N893', 'N894', 'N895', 'N896', 'N897', 'N898', 'N899', 'N903', 'N907', 'N910', 'N913', 'N914', 'N915', 'N916', 'N917', 'N918', 'N919', 'N920', 'N921', 'N922', 'N923', 'N926', 'N935', 
'N938', 'N939', 'N942', 'N943', 'N946', 'N947', 'N950', 'N951', 'N954', 'N955', 'N958', 'N959', 'N962', 'N965', 'N968', 'N969', 'N972', 'N973', 'N976', 'N977', 'N980', 'N981', 'N984', 'N985', 'N988', 'N989', 'N990', 'N991', 'N992', 'N993', 'N994', 'N997', 'N998', 'N1001', 'N1002', 'N1003', 'N1004', 'N1005', 'N1006', 'N1007', 'N1008', 'N1009', 'N1010', 'N1013', 'N1016', 'N1019', 'N1022', 'N1025', 'N1028', 'N1031', 'N1034', 'N1037', 'N1040', 'N1043', 'N1046', 'N1049', 'N1054', 'N1055', 'N1063', 'N1064', 'N1067', 'N1068', 'N1119', 'N1120', 'N1121', 'N1122', 'N1128', 'N1129', 'N1130', 'N1131', 'N1132', 'N1133', 'N1148', 'N1149', 'N1150', 'N1151', 'N1152', 'N1153', 'N1154', 'N1155', 'N1156', 'N1157', 'N1158', 'N1159', 'N1160', 'N1161', 'N1162', 'N1163', 'N1164', 'N1167', 'N1168', 'N1171', 'N1188', 'N1205', 'N1206', 'N1207', 'N1208', 'N1209', 'N1210', 'N1211', 'N1212', 'N1213', 'N1214', 'N1215', 'N1216', 'N1217', 'N1218', 'N1219', 'N1220', 'N1221', 'N1222', 'N1223', 'N1224', 'N1225', 'N1226', 'N1227', 'N1228', 'N1229', 'N1230', 'N1231', 'N1232', 'N1235', 'N1238', 'N1239', 'N1240', 'N1241', 'N1242', 'N1243', 'N1246', 'N1249', 'N1252', 'N1255', 'N1258', 'N1261', 'N1264', 'N1267', 'N1309', 'N1310', 'N1311', 'N1312', 'N1313', 'N1314', 'N1315', 'N1316', 'N1317', 'N1318', 'N1319', 'N1322', 'N1327', 'N1328', 'N1334', 'N1344', 'N1345', 'N1346', 'N1348', 'N1349', 'N1350', 'N1351', 'N1352', 'N1355', 'N1358', 'N1361', 'N1364', 'N1367', 'N1370', 'N1373', 'N1376', 'N1379', 'N1383', 'N1386', 'N1387', 'N1388', 'N1389', 'N1390', 'N1393', 'N1396', 'N1397', 'N1398', 'N1399', 'N1409', 'N1412', 'N1413', 'N1416', 'N1419', 'N1433', 'N1434', 'N1438', 'N1439', 'N1440', 'N1443', 'N1444', 'N1445', 'N1446', 'N1447', 'N1448', 'N1451', 'N1452', 'N1453', 'N1454', 'N1455', 'N1456', 'N1457', 'N1458', 'N1459', 'N1460', 'N1461', 'N1462', 'N1463', 'N1464', 'N1468', 'N1469', 'N1470', 'N1471', 'N1472', 'N1475', 'N1476', 'N1478', 'N1481', 'N1484', 'N1487', 'N1488', 'N1489', 'N1490', 'N1491', 'N1492', 'N1493', 'N1494', 'N1495', 'N1496', 'N1498', 'N1499', 'N1500', 'N1501', 'N1504', 'N1510', 'N1513', 'N1514', 'N1517', 'N1520', 'N1521', 'N1522', 'N1526', 'N1527', 'N1528', 'N1529', 'N1530', 'N1531', 'N1532', 'N1534', 'N1537', 'N1540', 'N1546', 'N1554', 'N1557', 'N1561', 'N1567', 'N1568', 'N1569', 'N1571', 'N1576', 'N1588', 'N1591', 'N1593', 'N1594', 'N1595', 'N1596', 'N1600', 'N1603', 'N1606', 'N1609', 'N1612', 'N1615', 'N1620', 'N1623', 'N1635', 'N1636', 'N1638', 'N1639', 'N1640', 'N1643', 'N1647', 'N1651', 'N1658', 'N1661', 'N1664', 'N1671', 'N1672', 'N1675', 'N1677', 'N1678', 'N1679', 'N1680', 'N1681', 'N1682', 'N1683', 'N1685', 'N1688', 'N1697', 'N1701', 'N1706', 'N1707', 'N1708', 'N1709', 'N1710', 'N1711', 'N1712', 'N1713', 'N1714', 'N1717', 'N1720', 'N1721', 'N1723', 'N1727', 'N1728', 'N1730', 'N1731', 'N1734', 'N1740', 'N1741', 'N1742', 'N1746', 'N1747', 'N1748', 'N1751', 'N1759', 'N1761', 'N1762', 'N1763', 'N1764', 'N1768', 'N1769', 'N1772', 'N1773', 'N1774', 'N1777', 'N1783', 'N1784', 'N1785', 'N1786', 'N1787', 'N1788', 'N1791', 'N1792', 'N1795', 'N1796', 'N1798', 'N1801', 'N1802', 'N1807', 'N1808', 'N1809', 'N1810', 'N1812', 'N1815', 'N1818', 'N1821', 'N1822', 'N1823', 'N1824', 'N1825', 'N1826', 'N1827', 'N1830', 'N1837', 'N1838', 'N1841', 'N1848', 'N1849', 'N1850', 'N1852', 'N1855', 'N1856', 'N1857', 'N1858', 'N1864', 'N1865', 'N1866', 'N1869', 'N1872', 'N1875', 'N1878', 'N1879', 'N1882', 'N1883', 'N1884', 'N1885', 'N1889', 'N1895', 'N1896', 'N1897', 'N1898', 'N1902', 'N1910', 'N1911', 'N1912', 'N1913', 'N1915', 'N1919', 'N1920', 'N1921', 'N1922', 'N1923', 'N1924', 'N1927', 'N1930', 'N1933', 'N1936', 'N1937', 'N1938', 'N1941', 'N1942', 'N1944', 'N1947', 'N1950', 'N1953', 'N1958', 'N1961', 'N1965', 'N1968', 'N1975', 'N1976', 'N1977', 'N1978', 'N1979', 'N1980', 'N1985', 'N1987', 'N1999', 'N2000', 'N2002', 'N2003', 'N2004', 'N2005', 'N2006', 'N2007', 'N2008', 'N2009', 'N2012', 'N2013', 'N2014', 'N2015', 'N2016', 'N2018', 'N2019', 'N2020', 'N2021', 'N2022', 'N2023', 'N2024', 'N2025', 'N2026', 'N2027', 'N2030', 'N2033', 'N2036', 'N2037', 'N2038', 'N2039', 'N2040', 'N2041', 'N2042', 'N2047', 'N2052', 'N2055', 'N2060', 'N2061', 'N2062', 'N2067', 'N2068', 'N2071', 'N2076', 'N2077', 'N2078', 'N2081', 'N2086', 'N2089', 'N2104', 'N2119', 'N2129', 'N2143', 'N2148', 'N2151', 'N2196', 'N2199', 'N2202', 'N2205', 'N2214', 'N2215', 'N2216', 'N2217', 'N2222', 'N2223', 'N2224', 'N2225', 'N2226', 'N2227', 'N2228', 'N2229', 'N2230', 'N2231', 'N2232', 'N2233', 'N2234', 'N2235', 'N2236', 'N2237', 'N2240', 'N2241', 'N2244', 'N2245', 'N2250', 'N2253', 'N2256', 'N2257', 'N2260', 'N2263', 'N2266', 'N2269', 'N2272', 'N2279', 'N2286', 'N2297', 'N2315', 'N2326', 'N2340', 'N2353', 'N2361', 'N2375', 'N2384', 'N2385', 'N2386', 'N2426', 'N2427', 'N2537', 'N2540', 'N2543', 'N2546', 'N2549', 'N2552', 'N2555', 'N2558', 'N2561', 'N2564', 'N2567', 'N2570', 'N2573', 'N2576', 'N2594', 'N2597', 'N2600', 'N2603', 'N2606', 'N2611', 'N2614', 'N2617', 'N2620', 'N2627', 'N2628', 'N2629', 'N2630', 'N2631', 'N2632', 'N2633', 'N2634', 'N2639', 'N2642', 'N2645', 'N2648', 'N2651', 'N2655', 'N2658', 'N2661', 'N2664', 'N2669', 'N2670', 'N2671', 'N2672', 'N2673', 'N2674', 'N2675', 'N2676', 'N2682', 'N2683', 'N2688', 'N2689', 'N2690', 'N2691', 'N2710', 'N2720', 'N2721', 'N2722', 'N2723', 'N2724', 'N2725', 'N2726', 'N2727', 'N2728', 'N2729', 'N2730', 'N2731', 'N2732', 'N2733', 'N2734', 'N2735', 'N2736', 'N2737', 'N2738', 'N2739', 'N2740', 'N2741', 'N2742', 'N2743', 'N2744', 'N2745', 'N2746', 'N2747', 'N2750', 'N2757', 'N2758', 'N2759', 'N2760', 'N2761', 'N2763', 'N2764', 'N2765', 'N2766', 'N2773', 'N2776', 'N2788', 'N2789', 'N2800', 'N2807', 'N2808', 'N2809', 'N2810', 'N2812', 'N2815', 'N2818', 'N2821', 'N2824', 'N2827', 'N2828', 'N2829', 'N2843', 'N2846', 'N2850', 'N2851', 'N2852', 'N2853', 'N2854', 'N2857', 'N2858', 'N2859', 'N2860', 'N2861', 'N2862', 'N2863', 'N2866', 'N2867', 'N2868', 'N2869', 'N2870', 'N2871', 'N2872', 'N2873', 'N2874', 'N2875', 'N2876', 'N2877', 'N2878', 'N2879', 'N2880', 'N2881', 'N2882', 'N2883', 'N2895', 'N2896', 'N2897', 'N2898', 'N2753', 'N2754', 'N2755', 'N2756', 'N2762', 'N2767', 'N2768', 'N2779', 'N2780', 'N2781', 'N2782', 'N2783', 'N2784', 'N2785', 'N2786', 'N2787', 'N2811', 'N2886', 'N2887', 'N2888', 'N2889', 'N2890', 'N2891', 'N2892', 'N2899']

lookup = 'en = 0'
linenumber = []
rows = []

toAdd = ["Clk", "N1", "N4", "N7", "N10", "N13", "N16", "N19", "N22", "N25", "N28", "N31", "N34", "N37", "N40", "N43", "N46", "N49", "N53", "N56", "N60", "N63", "N66", "N69", "N72", "N76", "N79", "N82", "N85", "N88", "N91", "N94", "N99", "N104", "en", "N2753", "N2754", "N2755", "N2756", "N2762", "N2767", "N2768", "N2779", "N2780", "N2781", "N2782", "N2783", "N2784", "N2785", "N2786", "N2787", "N2811", "N2886", "N2887", "N2888", "N2889", "N2890", "N2891", "N2892", "N2899"]
# Generating a random number, to randomly select one of the parameters
randpara = random.randint(0, 970)
#print ("Random number = ",randpara)
para = parameter[randpara]
#print("Random Parameter = ", para);
#print(str(datetime.datetime.now().time()))
# Generating a random number, to randomly select one of the clock cycle to inject fault
# After generating random number, print the index
#randrange ([start,] stop [,step])
randcycle = random.randrange(2, 998, 2)
randcycle  = randcycle + 0.8
#print ("Random clock cycle = ",randcycle)
randomize = repr(randcycle) + "_" + para
print(randomize)
#print(str(datetime.datetime.now().time()) + "test 2")
for param in parameter:
    with open('fault{}.v'.format(randomize), "w") as f:
        with open('fault{}.v'.format(para), 'r') as h:
            for num, line in enumerate(h, 1):
                if lookup in line:
                    linenumber.append(num)

        change = "\t\t#" + repr(randcycle) + " " + "en = 1;\n"
        		
        with open('fault{}.v'.format(para), 'r') as k:
            lines = k.readlines()

        with open('fault{}.v'.format(randomize), "w") as m:
            for i, line in enumerate(lines):
                if i == linenumber[1]-1:
                    m.write(change)
                m.write(line)
#print(str(datetime.datetime.now().time()) + "test 3")
# creating csv file to store the output of this faulty file
#for para in parameter:
with open('fault{}.v'.format(randomize), "r") as f:
	cmd1 = 'iverilog -o fault' + randomize + " " + 'fault' + randomize + '.v'
	#print(cmd1)
	#print(str(datetime.datetime.now().time()) + "test 4")
	cmd2 = 'vvp fault' + randomize + " " + '> fault' + randomize + '.csv'
	os.system(cmd1)
	#print(str(datetime.datetime.now().time()) + "test 4.1")
	os.system(cmd2)
#print(str(datetime.datetime.now().time()) + "test 5")
with open('fault{}.csv'.format(randomize), "r") as infile:
	reader = list(csv.reader(infile))
	reader.insert(0, toAdd)
#print(str(datetime.datetime.now().time()) + "test 5")
with open('fault{}.csv'.format(randomize), "w", newline = '') as outfile:
	writer = csv.writer(outfile)
	for line in reader:
		writer.writerow(line)

#print(str(datetime.datetime.now().time()) + "test 3")