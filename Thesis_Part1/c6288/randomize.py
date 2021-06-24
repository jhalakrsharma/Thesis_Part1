import glob, os
import subprocess
import random
import csv
import datetime
#print(str(datetime.datetime.now().time()))

#Critical nodes extracted from the golden code.
parameter = ['N1', 'N18', 'N35', 'N52', 'N69', 'N86', 'N103', 'N120', 'N137', 'N154', 'N171', 'N188', 'N205', 'N222', 'N239', 'N256', 'N273', 'N290', 'N307', 'N324', 'N341', 'N358', 'N375', 'N392', 'N409', 'N426', 'N443', 'N460', 'N477', 'N494', 'N511', 'N528', 'd1', 'd18', 'd35', 'd52', 'd69', 'd86', 'd103', 'd120', 'd137', 'd154', 'd171', 'd188', 'd205', 'd222', 'd239', 'd256', 'd273', 'd290', 'd307', 'd324', 'd341', 'd358', 'd375', 'd392', 'd409', 'd426', 'd443', 'd460', 'd477', 'd494', 'd511', 'd528', 'd545', 'd1581', 'd1901', 'd2223', 'd2548', 'd2877', 'd3211', 'd3552', 'd3895', 'd4241', 'd4591', 'd4946', 'd5308', 'd5672', 'd5971', 'd6123', 'd6150', 'd6160', 'd6170', 'd6180', 'd6190', 'd6200', 'd6210', 'd6220', 'd6230', 'd6240', 'd6250', 'd6260', 'd6270', 'd6280', 'd6287', 'd6288', 'N546', 'N549', 'N552', 'N555', 'N558', 'N561', 'N564', 'N567', 'N570', 'N573', 'N576', 'N579', 'N582', 'N585', 'N588', 'N591', 'N594', 'N597', 'N600', 'N603', 'N606', 'N609', 'N612', 'N615', 'N618', 'N621', 'N624', 'N627', 'N630', 'N633', 'N636', 'N639', 'N642', 'N645', 'N648', 'N651', 'N654', 'N657', 'N660', 'N663', 'N666', 'N669', 'N672', 'N675', 'N678', 'N681', 'N684', 'N687', 'N690', 'N693', 'N696', 'N699', 'N702', 'N705', 'N708', 'N711', 'N714', 'N717', 'N720', 'N723', 'N726', 'N729', 'N732', 'N735', 'N738', 'N741', 'N744', 'N747', 'N750', 'N753', 'N756', 'N759', 'N762', 'N765', 
            'N768', 'N771', 'N774', 'N777', 'N780', 'N783', 'N786', 'N789', 'N792', 'N795', 'N798', 'N801', 'N804', 'N807', 'N810', 'N813', 'N816', 'N819', 'N822', 'N825', 'N828', 'N831', 'N834', 'N837', 'N840', 'N843', 'N846', 'N849', 'N852', 'N855', 'N858', 'N861', 'N864', 'N867', 'N870', 'N873', 'N876', 'N879', 'N882', 'N885', 'N888', 'N891', 'N894', 'N897', 'N900', 'N903', 'N906', 'N909', 'N912', 'N915', 'N918', 'N921', 'N924', 'N927', 'N930', 'N933', 'N936', 'N939', 'N942', 'N945', 'N948', 'N951', 'N954', 'N957', 'N960', 'N963', 'N966', 'N969', 'N972', 'N975', 'N978', 'N981', 'N984', 'N987', 'N990', 'N993', 'N996', 'N999', 'N1002', 'N1005', 'N1008', 'N1011', 'N1014', 'N1017', 'N1020', 'N1023', 
            'N1026', 'N1029', 'N1032', 'N1035', 'N1038', 'N1041', 'N1044', 'N1047', 'N1050', 'N1053', 'N1056', 'N1059', 'N1062', 'N1065', 'N1068', 'N1071', 'N1074', 'N1077', 'N1080', 'N1083', 'N1086', 'N1089', 'N1092', 'N1095', 'N1098', 'N1101', 'N1104', 'N1107', 'N1110', 'N1113', 'N1116', 'N1119', 'N1122', 'N1125', 'N1128', 'N1131', 'N1134', 'N1137', 'N1140', 'N1143', 'N1146', 'N1149', 'N1152', 'N1155', 'N1158', 'N1161', 'N1164', 'N1167', 'N1170', 'N1173', 'N1176', 'N1179', 'N1182', 'N1185', 'N1188', 'N1191', 'N1194', 'N1197', 
            'N1200', 'N1203', 'N1206', 'N1209', 'N1212', 'N1215', 'N1218', 'N1221', 'N1224', 'N1227', 'N1230', 'N1233', 'N1236', 'N1239', 'N1242', 'N1245', 'N1248', 'N1251', 'N1254', 'N1257', 'N1260', 'N1263', 'N1266', 'N1269', 'N1272', 'N1275', 'N1278', 'N1281', 'N1284', 'N1287', 'N1290', 'N1293', 'N1296', 'N1299', 'N1302', 'N1305', 'N1308', 'N1311', 'N1315', 'N1319', 'N1323', 'N1327', 'N1331', 'N1335', 'N1339', 'N1343', 'N1347', 'N1351', 'N1355', 'N1359', 'N1363', 'N1367', 'N1371', 'N1372', 'N1373', 'N1374', 'N1375', 'N1376', 
            'N1377', 'N1378', 'N1379', 'N1380', 'N1381', 'N1382', 'N1383', 'N1384', 'N1385', 'N1386', 'N1387', 'N1388', 'N1389', 'N1390', 'N1391', 'N1392', 'N1393', 'N1394', 'N1395', 'N1396', 'N1397', 'N1398', 'N1399', 'N1400', 'N1401', 'N1404', 'N1407', 'N1410', 'N1413', 'N1416', 'N1419', 'N1422', 'N1425', 'N1428', 'N1431', 'N1434', 'N1437', 'N1440', 'N1443', 'N1446', 'N1450', 'N1454', 'N1458', 'N1462', 'N1466', 'N1470', 'N1474', 'N1478', 'N1482', 'N1486', 'N1490', 'N1494', 'N1498', 'N1502', 'N1506', 'N1507', 'N1508', 'N1511', 
            'N1512', 'N1513', 'N1516', 'N1517', 'N1518', 'N1521', 'N1522', 'N1523', 'N1526', 'N1527', 'N1528', 'N1531', 'N1532', 'N1533', 'N1536', 'N1537', 'N1538', 'N1541', 'N1542', 'N1543', 'N1546', 'N1547', 'N1548', 'N1551', 'N1552', 'N1553', 'N1556', 'N1557', 'N1558', 'N1561', 'N1562', 'N1563', 'N1566', 'N1567', 'N1568', 'N1571', 'N1572', 'N1573', 'N1576', 'N1577', 'N1578', 'N1582', 'N1585', 'N1588', 'N1591', 'N1594', 'N1597', 'N1600', 'N1603', 'N1606', 'N1609', 'N1612', 'N1615', 'N1618', 'N1621', 'N1624', 'N1628', 'N1632', 
            'N1636', 'N1640', 'N1644', 'N1648', 'N1652', 'N1656', 'N1660', 'N1664', 'N1668', 'N1672', 'N1676', 'N1680', 'N1684', 'N1685', 'N1686', 'N1687', 'N1688', 'N1689', 'N1690', 'N1691', 'N1692', 'N1693', 'N1694', 'N1695', 'N1696', 'N1697', 'N1698', 'N1699', 'N1700', 'N1701', 'N1702', 'N1703', 'N1704', 'N1705', 'N1706', 'N1707', 'N1708', 'N1709', 'N1710', 'N1711', 'N1712', 'N1713', 'N1714', 'N1717', 'N1720', 'N1723', 'N1726', 'N1729', 'N1732', 'N1735', 'N1738', 'N1741', 'N1744', 'N1747', 'N1750', 'N1753', 'N1756', 'N1759', 
            'N1763', 'N1767', 'N1771', 'N1775', 'N1779', 'N1783', 'N1787', 'N1791', 'N1795', 'N1799', 'N1803', 'N1807', 'N1811', 'N1815', 'N1819', 'N1820', 'N1821', 'N1824', 'N1825', 'N1826', 'N1829', 'N1830', 'N1831', 'N1834', 'N1835', 'N1836', 'N1839', 'N1840', 'N1841', 'N1844', 'N1845', 'N1846', 'N1849', 'N1850', 'N1851', 'N1854', 'N1855', 'N1856', 'N1859', 'N1860', 'N1861', 'N1864', 'N1865', 'N1866', 'N1869', 'N1870', 'N1871', 'N1874', 'N1875', 'N1876', 'N1879', 'N1880', 'N1881', 'N1884', 'N1885', 'N1886', 'N1889', 'N1890', 
            'N1891', 'N1894', 'N1897', 'N1902', 'N1905', 'N1908', 'N1911', 'N1914', 'N1917', 'N1920', 'N1923', 'N1926', 'N1929', 'N1932', 'N1935', 'N1938', 'N1941', 'N1945', 'N1946', 'N1947', 'N1951', 'N1955', 'N1959', 'N1963', 'N1967', 'N1971', 'N1975', 'N1979', 'N1983', 'N1987', 'N1991', 'N1995', 'N1999', 'N2000', 'N2001', 'N2004', 'N2005', 'N2006', 'N2007', 'N2008', 'N2009', 'N2010', 'N2011', 'N2012', 'N2013', 'N2014', 'N2015', 'N2016', 'N2017', 'N2018', 'N2019', 'N2020', 'N2021', 'N2022', 'N2023', 'N2024', 'N2025', 'N2026', 
            'N2027', 'N2028', 'N2029', 'N2030', 'N2033', 'N2037', 'N2040', 'N2043', 'N2046', 'N2049', 'N2052', 'N2055', 'N2058', 'N2061', 'N2064', 'N2067', 'N2070', 'N2073', 'N2076', 'N2080', 'N2081', 'N2082', 'N2085', 'N2089', 'N2093', 'N2097', 'N2101', 'N2105', 'N2109', 'N2113', 'N2117', 'N2121', 'N2125', 'N2129', 'N2133', 'N2137', 'N2138', 'N2139', 'N2142', 'N2145', 'N2149', 'N2150', 'N2151', 'N2154', 'N2155', 'N2156', 'N2159', 'N2160', 'N2161', 'N2164', 'N2165', 'N2166', 'N2169', 'N2170', 'N2171', 'N2174', 'N2175', 'N2176', 
            'N2179', 'N2180', 'N2181', 'N2184', 'N2185', 'N2186', 'N2189', 'N2190', 'N2191', 'N2194', 'N2195', 'N2196', 'N2199', 'N2200', 'N2201', 'N2204', 'N2205', 'N2206', 'N2209', 'N2210', 'N2211', 'N2214', 'N2217', 'N2221', 'N2222', 'N2224', 'N2227', 'N2230', 'N2233', 'N2236', 'N2239', 'N2242', 'N2245', 'N2248', 'N2251', 'N2254', 'N2257', 'N2260', 'N2264', 'N2265', 'N2266', 'N2269', 'N2273', 'N2277', 'N2281', 'N2285', 'N2289', 'N2293', 'N2297', 'N2301', 'N2305', 'N2309', 'N2313', 'N2317', 'N2318', 'N2319', 'N2322', 'N2326', 
            'N2327', 'N2328', 'N2329', 'N2330', 'N2331', 'N2332', 'N2333', 'N2334', 'N2335', 'N2336', 'N2337', 'N2338', 'N2339', 'N2340', 'N2341', 'N2342', 'N2343', 'N2344', 'N2345', 'N2346', 'N2347', 'N2348', 'N2349', 'N2350', 'N2353', 'N2357', 'N2358', 'N2359', 'N2362', 'N2365', 'N2368', 'N2371', 'N2374', 'N2377', 'N2380', 'N2383', 'N2386', 'N2389', 'N2392', 'N2395', 'N2398', 'N2402', 'N2403', 'N2404', 'N2407', 'N2410', 'N2414', 'N2418', 'N2422', 'N2426', 'N2430', 'N2434', 'N2438', 'N2442', 'N2446', 'N2450', 'N2454', 'N2458', 
            'N2462', 'N2463', 'N2464', 'N2467', 'N2470', 'N2474', 'N2475', 'N2476', 'N2477', 'N2478', 'N2481', 'N2482', 'N2483', 'N2486', 'N2487', 'N2488', 'N2491', 'N2492', 'N2493', 'N2496', 'N2497', 'N2498', 'N2501', 'N2502', 'N2503', 'N2506', 'N2507', 'N2508', 'N2511', 'N2512', 'N2513', 'N2516', 'N2517', 'N2518', 'N2521', 'N2522', 'N2523', 'N2526', 'N2527', 'N2528', 'N2531', 'N2532', 'N2533', 'N2536', 'N2539', 'N2543', 'N2544', 'N2545', 'N2549', 'N2552', 'N2555', 'N2558', 'N2561', 'N2564', 'N2567', 'N2570', 'N2573', 'N2576', 
            'N2579', 'N2582', 'N2586', 'N2587', 'N2588', 'N2591', 'N2595', 'N2599', 'N2603', 'N2607', 'N2611', 'N2615', 'N2619', 'N2623', 'N2627', 'N2631', 'N2635', 'N2639', 'N2640', 'N2641', 'N2644', 'N2648', 'N2649', 'N2650', 'N2653', 'N2654', 'N2655', 'N2656', 'N2657', 'N2658', 'N2659', 'N2660', 'N2661', 'N2662', 'N2663', 'N2664', 'N2665', 'N2666', 'N2667', 'N2668', 'N2669', 'N2670', 'N2671', 'N2672', 'N2673', 'N2674', 'N2675', 'N2678', 'N2682', 'N2683', 'N2684', 'N2687', 'N2690', 'N2694', 'N2697', 'N2700', 'N2703', 'N2706', 
            'N2709', 'N2712', 'N2715', 'N2718', 'N2721', 'N2724', 'N2727', 'N2731', 'N2732', 'N2733', 'N2736', 'N2739', 'N2743', 'N2744', 'N2745', 'N2749', 'N2753', 'N2757', 'N2761', 'N2765', 'N2769', 'N2773', 'N2777', 'N2781', 'N2785', 'N2789', 'N2790', 'N2791', 'N2794', 'N2797', 'N2801', 'N2802', 'N2803', 'N2806', 'N2807', 'N2808', 'N2811', 'N2812', 'N2813', 'N2816', 'N2817', 'N2818', 'N2821', 'N2822', 'N2823', 'N2826', 'N2827', 'N2828', 'N2831', 'N2832', 'N2833', 'N2836', 'N2837', 'N2838', 'N2841', 'N2842', 'N2843', 'N2846', 
            'N2847', 'N2848', 'N2851', 'N2852', 'N2853', 'N2856', 'N2857', 'N2858', 'N2861', 'N2864', 'N2868', 'N2869', 'N2870', 'N2873', 'N2878', 'N2881', 'N2884', 'N2887', 'N2890', 'N2893', 'N2896', 'N2899', 'N2902', 'N2905', 'N2908', 'N2912', 'N2913', 'N2914', 'N2917', 'N2921', 'N2922', 'N2923', 'N2926', 'N2930', 'N2934', 'N2938', 'N2942', 'N2946', 'N2950', 'N2954', 'N2958', 'N2962', 'N2966', 'N2967', 'N2968', 'N2971', 'N2975', 'N2976', 'N2977', 'N2980', 'N2983', 'N2987', 'N2988', 'N2989', 'N2990', 'N2991', 'N2992', 'N2993', 
            'N2994', 'N2995', 'N2996', 'N2997', 'N2998', 'N2999', 'N3000', 'N3001', 'N3002', 'N3003', 'N3004', 'N3005', 'N3006', 'N3007', 'N3010', 'N3014', 'N3015', 'N3016', 'N3019', 'N3022', 'N3026', 'N3027', 'N3028', 'N3031', 'N3034', 'N3037', 'N3040', 'N3043', 'N3046', 'N3049', 'N3052', 'N3055', 'N3058', 'N3062', 'N3063', 'N3064', 'N3067', 'N3070', 'N3074', 'N3075', 'N3076', 'N3079', 'N3083', 'N3087', 'N3091', 'N3095', 'N3099', 'N3103', 'N3107', 'N3111', 'N3115', 'N3119', 'N3120', 'N3121', 'N3124', 'N3127', 'N3131', 'N3132', 
            'N3133', 'N3136', 'N3140', 'N3141', 'N3142', 'N3145', 'N3146', 'N3147', 'N3150', 'N3151', 'N3152', 'N3155', 'N3156', 'N3157', 'N3160', 'N3161', 'N3162', 'N3165', 'N3166', 'N3167', 'N3170', 'N3171', 'N3172', 'N3175', 'N3176', 'N3177', 'N3180', 'N3181', 'N3182', 'N3185', 'N3186', 'N3187', 'N3190', 'N3193', 'N3197', 'N3198', 'N3199', 'N3202', 'N3206', 'N3207', 'N3208', 'N3212', 'N3215', 'N3218', 'N3221', 'N3224', 'N3227', 'N3230', 'N3233', 'N3236', 'N3239', 'N3243', 'N3244', 'N3245', 'N3248', 'N3252', 'N3253', 'N3254', 
            'N3257', 'N3260', 'N3264', 'N3268', 'N3272', 'N3276', 'N3280', 'N3284', 'N3288', 'N3292', 'N3296', 'N3300', 'N3301', 'N3302', 'N3305', 'N3309', 'N3310', 'N3311', 'N3314', 'N3317', 'N3321', 'N3322', 'N3323', 'N3324', 'N3325', 'N3326', 'N3327', 'N3328', 'N3329', 'N3330', 'N3331', 'N3332', 'N3333', 'N3334', 'N3335', 'N3336', 'N3337', 'N3338', 'N3339', 'N3340', 'N3341', 'N3344', 'N3348', 'N3349', 'N3350', 'N3353', 'N3356', 'N3360', 'N3361', 'N3362', 'N3365', 'N3368', 'N3371', 'N3374', 'N3377', 'N3380', 'N3383', 'N3386', 
            'N3389', 'N3392', 'N3396', 'N3397', 'N3398', 'N3401', 'N3404', 'N3408', 'N3409', 'N3410', 'N3413', 'N3417', 'N3421', 'N3425', 'N3429', 'N3433', 'N3437', 'N3441', 'N3445', 'N3449', 'N3453', 'N3454', 'N3455', 'N3458', 'N3461', 'N3465', 'N3466', 'N3467', 'N3470', 'N3474', 'N3475', 'N3476', 'N3479', 'N3480', 'N3481', 'N3484', 'N3485', 'N3486', 'N3489', 'N3490', 'N3491', 'N3494', 'N3495', 'N3496', 'N3499', 'N3500', 'N3501', 'N3504', 'N3505', 'N3506', 'N3509', 'N3510', 'N3511', 'N3514', 'N3515', 'N3516', 'N3519', 'N3520', 
            'N3521', 'N3524', 'N3527', 'N3531', 'N3532', 'N3533', 'N3536', 'N3540', 'N3541', 'N3542', 'N3545', 'N3548', 'N3553', 'N3556', 'N3559', 'N3562', 'N3565', 'N3568', 'N3571', 'N3574', 'N3577', 'N3581', 'N3582', 'N3583', 'N3586', 'N3590', 'N3591', 'N3592', 'N3595', 'N3598', 'N3602', 'N3603', 'N3604', 'N3608', 'N3612', 'N3616', 'N3620', 'N3624', 'N3628', 'N3632', 'N3636', 'N3637', 'N3638', 'N3641', 'N3645', 'N3646', 'N3647', 'N3650', 'N3653', 'N3657', 'N3658', 'N3659', 'N3662', 'N3663', 'N3664', 'N3665', 'N3666', 'N3667', 
            'N3668', 'N3669', 'N3670', 'N3671', 'N3672', 'N3673', 'N3674', 'N3675', 'N3676', 'N3677', 'N3678', 'N3681', 'N3685', 'N3686', 'N3687', 'N3690', 'N3693', 'N3697', 'N3698', 'N3699', 'N3702', 'N3706', 'N3709', 'N3712', 'N3715', 'N3718', 'N3721', 'N3724', 'N3727', 'N3730', 'N3734', 'N3735', 'N3736', 'N3739', 'N3742', 'N3746', 'N3747', 'N3748', 'N3751', 'N3755', 'N3756', 'N3757', 'N3760', 'N3764', 'N3768', 'N3772', 'N3776', 'N3780', 'N3784', 'N3788', 'N3792', 'N3793', 'N3794', 'N3797', 'N3800', 'N3804', 'N3805', 'N3806', 
            'N3809', 'N3813', 'N3814', 'N3815', 'N3818', 'N3821', 'N3825', 'N3826', 'N3827', 'N3830', 'N3831', 'N3832', 'N3835', 'N3836', 'N3837', 'N3840', 'N3841', 'N3842', 'N3845', 'N3846', 'N3847', 'N3850', 'N3851', 'N3852', 'N3855', 'N3856', 'N3857', 'N3860', 'N3861', 'N3862', 'N3865', 'N3868', 'N3872', 'N3873', 'N3874', 'N3877', 'N3881', 'N3882', 'N3883', 'N3886', 'N3889', 'N3893', 'N3894', 'N3896', 'N3899', 'N3902', 'N3905', 'N3908', 'N3911', 'N3914', 'N3917', 'N3921', 'N3922', 'N3923', 'N3926', 'N3930', 'N3931', 'N3932', 
            'N3935', 'N3938', 'N3942', 'N3943', 'N3944', 'N3947', 'N3951', 'N3955', 'N3959', 'N3963', 'N3967', 'N3971', 'N3975', 'N3976', 'N3977', 'N3980', 'N3984', 'N3985', 'N3986', 'N3989', 'N3992', 'N3996', 'N3997', 'N3998', 'N4001', 'N4005', 'N4006', 'N4007', 'N4008', 'N4009', 'N4010', 'N4011', 'N4012', 'N4013', 'N4014', 'N4015', 'N4016', 'N4017', 'N4018', 'N4019', 'N4022', 'N4026', 'N4027', 'N4028', 'N4031', 'N4034', 'N4038', 'N4039', 'N4040', 'N4043', 'N4047', 'N4048', 'N4049', 'N4052', 'N4055', 'N4058', 'N4061', 'N4064', 
            'N4067', 'N4070', 'N4073', 'N4077', 'N4078', 'N4079', 'N4082', 'N4085', 'N4089', 'N4090', 'N4091', 'N4094', 'N4098', 'N4099', 'N4100', 'N4103', 'N4106', 'N4110', 'N4114', 'N4118', 'N4122', 'N4126', 'N4130', 'N4134', 'N4138', 'N4139', 'N4140', 'N4143', 'N4146', 'N4150', 'N4151', 'N4152', 'N4155', 'N4159', 'N4160', 'N4161', 'N4164', 'N4167', 'N4171', 'N4172', 'N4173', 'N4174', 'N4175', 'N4178', 'N4179', 'N4180', 'N4183', 'N4184', 'N4185', 'N4188', 'N4189', 'N4190', 'N4193', 'N4194', 'N4195', 'N4198', 'N4199', 'N4200', 
            'N4203', 'N4204', 'N4205', 'N4208', 'N4211', 'N4215', 'N4216', 'N4217', 'N4220', 'N4224', 'N4225', 'N4226', 'N4229', 'N4232', 'N4236', 'N4237', 'N4238', 'N4242', 'N4245', 'N4248', 'N4251', 'N4254', 'N4257', 'N4260', 'N4264', 'N4265', 'N4266', 'N4269', 'N4273', 'N4274', 'N4275', 'N4278', 'N4281', 'N4285', 'N4286', 'N4287', 'N4290', 'N4294', 'N4298', 'N4302', 'N4306', 'N4310', 'N4314', 'N4318', 'N4319', 'N4320', 'N4323', 'N4327', 'N4328', 'N4329', 'N4332', 'N4335', 'N4339', 'N4340', 'N4341', 'N4344', 'N4348', 'N4349', 
            'N4350', 'N4353', 'N4354', 'N4355', 'N4356', 'N4357', 'N4358', 'N4359', 'N4360', 'N4361', 'N4362', 'N4363', 'N4364', 'N4365', 'N4368', 'N4372', 'N4373', 'N4374', 'N4377', 'N4380', 'N4384', 'N4385', 'N4386', 'N4389', 'N4393', 'N4394', 'N4395', 'N4398', 'N4401', 'N4405', 'N4408', 'N4411', 'N4414', 'N4417', 'N4420', 'N4423', 'N4427', 'N4428', 'N4429', 'N4432', 'N4435', 'N4439', 'N4440', 'N4441', 'N4444', 'N4448', 'N4449', 'N4450', 'N4453', 'N4456', 'N4460', 'N4461', 'N4462', 'N4466', 'N4470', 'N4474', 'N4478', 'N4482', 
            'N4486', 'N4487', 'N4488', 'N4491', 'N4494', 'N4498', 'N4499', 'N4500', 'N4503', 'N4507', 'N4508', 'N4509', 'N4512', 'N4515', 'N4519', 'N4520', 'N4521', 'N4524', 'N4525', 'N4526', 'N4529', 'N4530', 'N4531', 'N4534', 'N4535', 'N4536', 'N4539', 'N4540', 'N4541', 'N4544', 'N4545', 'N4546', 'N4549', 'N4550', 'N4551', 'N4554', 'N4557', 'N4561', 'N4562', 'N4563', 'N4566', 'N4570', 'N4571', 'N4572', 'N4575', 'N4578', 'N4582', 'N4583', 'N4584', 'N4587', 'N4592', 'N4595', 'N4598', 'N4601', 'N4604', 'N4607', 'N4611', 'N4612', 
            'N4613', 'N4616', 'N4620', 'N4621', 'N4622', 'N4625', 'N4628', 'N4632', 'N4633', 'N4634', 'N4637', 'N4641', 'N4642', 'N4643', 'N4646', 'N4650', 'N4654', 'N4658', 'N4662', 'N4666', 'N4667', 'N4668', 'N4671', 'N4675', 'N4676', 'N4677', 'N4680', 'N4683', 'N4687', 'N4688', 'N4689', 'N4692', 'N4696', 'N4697', 'N4698', 'N4701', 'N4704', 'N4708', 'N4709', 'N4710', 'N4711', 'N4712', 'N4713', 'N4714', 'N4715', 'N4716', 'N4717', 'N4718', 'N4721', 'N4725', 'N4726', 'N4727', 'N4730', 'N4733', 'N4737', 'N4738', 'N4739', 'N4742', 
            'N4746', 'N4747', 'N4748', 'N4751', 'N4754', 'N4758', 'N4759', 'N4760', 'N4763', 'N4766', 'N4769', 'N4772', 'N4775', 'N4779', 'N4780', 'N4781', 'N4784', 'N4787', 'N4791', 'N4792', 'N4793', 'N4796', 'N4800', 'N4801', 'N4802', 'N4805', 'N4808', 'N4812', 'N4813', 'N4814', 'N4817', 'N4821', 'N4825', 'N4829', 'N4833', 'N4837', 'N4838', 'N4839', 'N4842', 'N4845', 'N4849', 'N4850', 'N4851', 'N4854', 'N4858', 'N4859', 'N4860', 'N4863', 'N4866', 'N4870', 'N4871', 'N4872', 'N4875', 'N4879', 'N4880', 'N4881', 'N4884', 'N4885', 
            'N4886', 'N4889', 'N4890', 'N4891', 'N4894', 'N4895', 'N4896', 'N4899', 'N4900', 'N4901', 'N4904', 'N4907', 'N4911', 'N4912', 'N4913', 'N4916', 'N4920', 'N4921', 'N4922', 'N4925', 'N4928', 'N4932', 'N4933', 'N4934', 'N4937', 'N4941', 'N4942', 'N4943', 'N4947', 'N4950', 'N4953', 'N4956', 'N4959', 'N4963', 'N4964', 'N4965', 'N4968', 'N4972', 'N4973', 'N4974', 'N4977', 'N4980', 'N4984', 'N4985', 'N4986', 'N4989', 'N4993', 'N4994', 'N4995', 'N4998', 'N5001', 'N5005', 'N5009', 'N5013', 'N5017', 'N5021', 'N5022', 'N5023', 
            'N5026', 'N5030', 'N5031', 'N5032', 'N5035', 'N5038', 'N5042', 'N5043', 'N5044', 'N5047', 'N5051', 'N5052', 'N5053', 'N5056', 'N5059', 'N5063', 'N5064', 'N5065', 'N5066', 'N5067', 'N5068', 'N5069', 'N5070', 'N5071', 'N5072', 'N5073', 'N5076', 'N5080', 'N5081', 'N5082', 'N5085', 'N5088', 'N5092', 'N5093', 'N5094', 'N5097', 'N5101', 'N5102', 'N5103', 'N5106', 'N5109', 'N5113', 'N5114', 'N5115', 'N5118', 'N5121', 'N5124', 'N5127', 'N5130', 'N5134', 'N5135', 'N5136', 'N5139', 'N5142', 'N5146', 'N5147', 'N5148', 'N5151', 
            'N5155', 'N5156', 'N5157', 'N5160', 'N5163', 'N5167', 'N5168', 'N5169', 'N5172', 'N5176', 'N5180', 'N5184', 'N5188', 'N5192', 'N5193', 'N5194', 'N5197', 'N5200', 'N5204', 'N5205', 'N5206', 'N5209', 'N5213', 'N5214', 'N5215', 'N5218', 'N5221', 'N5225', 'N5226', 'N5227', 'N5230', 'N5234', 'N5235', 'N5236', 'N5239', 'N5240', 'N5241', 'N5244', 'N5245', 'N5246', 'N5249', 'N5250', 'N5251', 'N5254', 'N5255', 'N5256', 'N5259', 'N5262', 'N5266', 'N5267', 'N5268', 'N5271', 'N5275', 'N5276', 'N5277', 'N5280', 'N5283', 'N5287', 
            'N5288', 'N5289', 'N5292', 'N5296', 'N5297', 'N5298', 'N5301', 'N5304', 'N5309', 'N5312', 'N5315', 'N5318', 'N5322', 'N5323', 'N5324', 'N5327', 'N5331', 'N5332', 'N5333', 'N5336', 'N5339', 'N5343', 'N5344', 'N5345', 'N5348', 'N5352', 'N5353', 'N5354', 'N5357', 'N5360', 'N5364', 'N5365', 'N5366', 'N5370', 'N5374', 'N5378', 'N5379', 'N5380', 'N5383', 'N5387', 'N5388', 'N5389', 'N5392', 'N5395', 'N5399', 'N5400', 'N5401', 'N5404', 'N5408', 'N5409', 'N5410', 'N5413', 'N5416', 'N5420', 'N5421', 'N5422', 'N5425', 'N5426', 
            'N5427', 'N5428', 'N5429', 'N5430', 'N5431', 'N5434', 'N5438', 'N5439', 'N5440', 'N5443', 'N5446', 'N5450', 'N5451', 'N5452', 'N5455', 'N5459', 'N5460', 'N5461', 'N5464', 'N5467', 'N5471', 'N5472', 'N5473', 'N5476', 'N5480', 'N5483', 'N5486', 'N5489', 'N5493', 'N5494', 'N5495', 'N5498', 'N5501', 'N5505', 'N5506', 'N5507', 'N5510', 'N5514', 'N5515', 'N5516', 'N5519', 'N5522', 'N5526', 'N5527', 'N5528', 'N5531', 'N5535', 'N5536', 'N5537', 'N5540', 'N5544', 'N5548', 'N5552', 'N5553', 'N5554', 'N5557', 'N5560', 'N5564', 
            'N5565', 'N5566', 'N5569', 'N5573', 'N5574', 'N5575', 'N5578', 'N5581', 'N5585', 'N5586', 'N5587', 'N5590', 'N5594', 'N5595', 'N5596', 'N5599', 'N5602', 'N5606', 'N5607', 'N5608', 'N5611', 'N5612', 'N5613', 'N5616', 'N5617', 'N5618', 'N5621', 'N5624', 'N5628', 'N5629', 'N5630', 'N5633', 'N5637', 'N5638', 'N5639', 'N5642', 'N5645', 'N5649', 'N5650', 'N5651', 'N5654', 'N5658', 'N5659', 'N5660', 'N5663', 'N5666', 'N5670', 'N5671', 'N5673', 'N5676', 'N5679', 'N5683', 'N5684', 'N5685', 'N5688', 'N5692', 'N5693', 'N5694', 
            'N5697', 'N5700', 'N5704', 'N5705', 'N5706', 'N5709', 'N5713', 'N5714', 'N5715', 'N5718', 'N5721', 'N5725', 'N5726', 'N5727', 'N5730', 'N5734', 'N5738', 'N5739', 'N5740', 'N5743', 'N5747', 'N5748', 'N5749', 'N5752', 'N5755', 'N5759', 'N5760', 'N5761', 'N5764', 'N5768', 'N5769', 'N5770', 'N5773', 'N5776', 'N5780', 'N5781', 'N5782', 'N5785', 'N5786', 'N5787', 'N5788', 'N5789', 'N5792', 'N5796', 'N5797', 'N5798', 'N5801', 'N5804', 'N5808', 'N5809', 'N5810', 'N5813', 'N5817', 'N5818', 'N5819', 'N5822', 'N5825', 'N5829', 
            'N5830', 'N5831', 'N5834', 'N5837', 'N5840', 'N5844', 'N5845', 'N5846', 'N5849', 'N5852', 'N5856', 'N5857', 'N5858', 'N5861', 'N5865', 'N5866', 'N5867', 'N5870', 'N5873', 'N5877', 'N5878', 'N5879', 'N5882', 'N5886', 'N5890', 'N5891', 'N5892', 'N5895', 'N5898', 'N5902', 'N5903', 'N5904', 'N5907', 'N5911', 'N5912', 'N5913', 'N5916', 'N5919', 'N5923', 'N5924', 'N5925', 'N5928', 'N5929', 'N5930', 'N5933', 'N5934', 'N5935', 'N5938', 'N5941', 'N5945', 'N5946', 'N5947', 'N5950', 'N5954', 'N5955', 'N5956', 'N5959', 'N5962', 
            'N5966', 'N5967', 'N5968', 'N5972', 'N5975', 'N5979', 'N5980', 'N5981', 'N5984', 'N5988', 'N5989', 'N5990', 'N5993', 'N5996', 'N6000', 'N6001', 'N6002', 'N6005', 'N6009', 'N6010', 'N6011', 'N6014', 'N6018', 'N6019', 'N6020', 'N6023', 'N6026', 'N6030', 'N6031', 'N6032', 'N6035', 'N6036', 'N6037', 'N6040', 'N6044', 'N6045', 'N6046', 'N6049', 'N6052', 'N6056', 'N6057', 'N6058', 'N6061', 'N6064', 'N6068', 'N6069', 'N6070', 'N6073', 'N6076', 'N6080', 'N6081', 'N6082', 'N6085', 'N6089', 'N6090', 'N6091', 'N6094', 'N6097', 
            'N6101', 'N6102', 'N6103', 'N6106', 'N6107', 'N6108', 'N6111', 'N6114', 'N6118', 'N6119', 'N6120', 'N6124', 'N6128', 'N6129', 'N6130', 'N6133', 'N6134', 'N6135', 'N6138', 'N6141', 'N6145', 'N6146', 'N6147', 'N6151', 'N6155', 'N6156', 'N6157', 'N6161', 'N6165', 'N6166', 'N6167', 'N6171', 'N6175', 'N6176', 'N6177', 'N6181', 'N6185', 'N6186', 'N6187', 'N6191', 'N6195', 'N6196', 'N6197', 'N6201', 'N6205', 'N6206', 'N6207', 'N6211', 'N6215', 'N6216', 'N6217', 'N6221', 'N6225', 'N6226', 'N6227', 'N6231', 'N6235', 'N6236', 
            'N6237', 'N6241', 'N6245', 'N6246', 'N6247', 'N6251', 'N6255', 'N6256', 'N6257', 'N6261', 'N6265', 'N6266', 'N6267', 'N6271', 'N6275', 'N6276', 'N6277', 'N6281', 'N6285', 'N6286']

lookup = 'en = 0'
linenumber = []
rows = []
toAdd = ["Clk", "N1", "N18", "N35", "N52", "N69", "N86", "N103", "N120", "N137", "N154", "N171", "N188", "N205", "N222", "N239", "N256", "N273", "N290", "N307", "N324", "N341", "N358", "N375", "N392", "N409", "N426", "N443", "N460", "N477", "N494", "N511", "N528", "en", "N545", "N1581", "N1901", "N2223", "N2548", "N2877", "N3211", "N3552", "N3895", "N4241", "N4591", "N4946", "N5308", "N5672", "N5971", "N6123", "N6150", "N6160", "N6170", "N6180", "N6190", "N6200", "N6210", "N6220", "N6230", "N6240", "N6250", "N6260", "N6270", "N6280", "N6287", "N6288"]
# Generating a random number, to randomly select one of the parameters
randpara = random.randint(0, 2479)
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