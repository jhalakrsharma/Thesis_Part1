module c1355(G1, G10, G11, G12, G13, G1324, G1325, G1326, G1327, G1328, G1329, G1330, G1331, G1332, G1333, G1334, G1335, G1336, G1337, G1338,G1339,G1340,G1341,G1342,
  G1343,G1344,G1345,G1346,G1347,G1348,G1349,G1350,G1351,G1352,G1353,G1354,
  G1355,G14,G15,G16,G17,G18,G19,G2,G20,G21,G22,G23,G24,G25,G26,G27,G28,G29,G3,
  G30,G31,G32,G33,G34,G35,G36,G37,G38,G39,G4,G40,G41,G5,G6,G7,G8,G9, clk,en);
  
input G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20, G21, G22, G23, G24, G25, G26, G27, G28, G29, G30, G31, G32, G33, G34, G35, G36, G37, G38, G39, G40, G41, clk ,en;

output G1324, G1325, G1326, G1327, G1328, G1329, G1330, G1331, G1332, G1333, G1334, G1335, G1336, G1337, G1338, G1339, G1340, G1341, G1342, G1343, G1344, G1345, G1346, G1347, G1348, G1349, G1350, G1351, G1352, G1353, G1354, G1355;

wire d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27, d28, d29, d30, d31, d32, d33, d34, d35, d36, d37, d38, d39, d40, d41, d1324, d1325, d1326, d1327, d1328, d1329, d1330, d1331, d1332, d1333, d1334, d1335, d1336, d1337, d1338, d1339, d1340, d1341, d1342, d1343, d1344, d1345, d1346, d1347, d1348, d1349, d1350, d1351, d1352, d1353, d1354, d1355, G242, G245, G248, G251, G254, G257, G260, G263, G266, G269, G272, G275, G278, G281, G284, G287, G290, G293, G296, G299, G302, G305, G308, G311, G314, G317, G320, G323, G326, G329, G332, G335, G338, G341, G344, G347, G350, G353, G356, G359, G362, G363, G364, G365, G366, G367, G368, G369, G370, G371, G372, G373, G374, G375, G376, G377, G378, G379, G380, G381, G382, G383, G384, G385, G386, G387, G388, G389, G390, G391, G392, G393, G394, G395, G396, G397, G398, G399, G400, G401, G402, G403, G404, G405, G406, G407, G408, G409, G410, G411, G412, G413, G414, G415, G416, G417, G418, G419, G420, G421, G422, G423, G424, G425, G426, G429, G432, G435, G438, G441, G444, G447, G450, G453, G456, G459, G462, G465, G468, G471, G474, G477, G480, G483, G486, G489, G492, G495, G498, G501, G504, G507, G510, G513, G516, G519, G522, G525, G528, G531, G534, G537, G540, G543, G546, G549, G552, G555, G558, G561, G564, G567, G570, G571, G572, G573, G574, G575, G576, G577, G578, G579, G580, G581, G582, G583, G584, G585, G586, G587, G588, G589, G590, G591, G592, G593, G594, G595, G596, G597, G598, G599, G600, G601, G602, G607, G612, G617, G622, G627, G632, G637, G642, G645, G648, G651, G654, G657, G660, G663, G666, G669, G672, G675, G678, G681, G684, G687, G690, G691, G692, G693, G694, G695, G696, G697, G698, G699, G700, G701, G702, G703, G704, G705, G706, G709, G712, G715, G718, G721, G724, G727, G730, G733, G736, G739, G742, G745, G748, G751, G754, G755, G756, G757, G758, G759, G760, G761, G762, G763, G764, G765, G766, G767, G768, G769, G770, G773, G776, G779, G782, G785, G788, G791, G794, G797, G800, G803, G806,     G809, G812, G815, G818, G819, G820, G821, G822, G823, G824, G825, G826, G827, G828, G829, G830, G831, G832, G833, G834, G847, G860, G873, G886, G899, G912, G925, G938, G939, G940, G941, G942, G943, G944, G945, G946, G947, G948, G949, G950, G951, G952, G953, G954, G955, G956, G957, G958, G959, G960, G961, G962, G963, G964, G965, G966, G967, G968, G969, G970, G971, G972, G973, G974, G975, G976, G977, G978, G979, G980, G981, G982, G983, G984, G985, G986, G991, G996, G1001, G1006, G1011, G1016, G1021, G1026, G1031, G1036, G1039, G1042, G1045, G1048, G1051, G1054, G1057, G1060, G1063, G1066, G1069, G1072, G1075, G1078, G1081, G1084, G1087, G1090, G1093, G1096, G1099, G1102, G1105, G1108, G1111, G1114, G1117, G1120, G1123, G1126, G1129, G1132, G1135, G1138, G1141, G1144, G1147, G1150, G1153, G1156, G1159, G1162, G1165, G1168, G1171, G1174, G1177, G1180, G1183, G1186, G1189, G1192, G1195, G1198, G1201, G1204, G1207, G1210, G1213, G1216, G1219, G1222, G1225, G1228, G1229, G1230, G1231, G1232, G1233, G1234, G1235, G1236, G1237, G1238, G1239, G1240, G1241, G1242, G1243, G1244, G1245, G1246, G1247, G1248, G1249, G1250, G1251, G1252, G1253, G1254, G1255, G1256, G1257, G1258, G1259, G1260, G1261, G1262, G1263, G1264, G1265, G1266, G1267, G1268, G1269, G1270, G1271, G1272, G1273, G1274, G1275, G1276, G1277, G1278, G1279, G1280, G1281, G1282, G1283, G1284, G1285, G1286, G1287, G1288, G1289, G1290, G1291, G1292, G1293, G1294, G1295, G1296, G1297, G1298, G1299, G1300, G1301, G1302, G1303, G1304, G1305, G1306, G1307, G1308, G1309, G1310, G1311, G1312, G1313, G1314, G1315, G1316, G1317, G1318, G1319, G1320, G1321, G1322, G1323;
  
  and AND2_0(G242, d33, d41);
  and AND2_1(G245, d34, d41);
  and AND2_2(G248, d35, d41);
  and AND2_3(G251, d36, d41);
  and AND2_4(G254, d37, d41);
  and AND2_5(G257, d38, d41);
  and AND2_6(G260, d39, d41);
  and AND2_7(G263, d40, d41);
  nand NAND2_0(G266, d1, d2);
  nand NAND2_1(G269, d3, d4);
  nand NAND2_2(G272, d5, d6);
  nand NAND2_3(G275, d7, d8);
  nand NAND2_4(G278, d9, d10);
  nand NAND2_5(G281, d11, d12);
  nand NAND2_6(G284, d13, d14);
  nand NAND2_7(G287, d15, d16);
  nand NAND2_8(G290, d17, d18);
  nand NAND2_9(G293, d19, d20);
  nand NAND2_10(G296, d21, d22);
  nand NAND2_11(G299, d23, d24);
  nand NAND2_12(G302, d25, d26);
  nand NAND2_13(G305, d27, d28);
  nand NAND2_14(G308, d29, d30);
  nand NAND2_15(G311, d31, d32);
  nand NAND2_16(G314, d1, d5);
  nand NAND2_17(G317, d9, d13);
  nand NAND2_18(G320, d2, d6);
  nand NAND2_19(G323, d10, d14);
  nand NAND2_20(G326, d3, d7);
  nand NAND2_21(G329, d11, d15);
  nand NAND2_22(G332, d4, d8);
  nand NAND2_23(G335, d12, d16);
  nand NAND2_24(G338, d17, d21);
  nand NAND2_25(G341, d25, d29);
  nand NAND2_26(G344, d18, d22);
  nand NAND2_27(G347, d26, d30);
  nand NAND2_28(G350, d19, d23);
  nand NAND2_29(G353, d27, d31);
  nand NAND2_30(G356, d20, d24);
  nand NAND2_31(G359, d28, d32);
  nand NAND2_32(G362, d1, G266);
  nand NAND2_33(G363, d2, G266);
  nand NAND2_34(G364, d3, G269);
  nand NAND2_35(G365, d4, G269);
  nand NAND2_36(G366, d5, G272);
  nand NAND2_37(G367, d6, G272);
  nand NAND2_38(G368, d7, G275);
  nand NAND2_39(G369, d8, G275);
  nand NAND2_40(G370, d9, G278);
  nand NAND2_41(G371, d10, G278);
  nand NAND2_42(G372, d11, G281);
  nand NAND2_43(G373, d12, G281);
  nand NAND2_44(G374, d13, G284);
  nand NAND2_45(G375, d14, G284);
  nand NAND2_46(G376, d15, G287);
  nand NAND2_47(G377, d16, G287);
  nand NAND2_48(G378, d17, G290);
  nand NAND2_49(G379, d18, G290);
  nand NAND2_50(G380, d19, G293);
  nand NAND2_51(G381, d20, G293);
  nand NAND2_52(G382, d21, G296);
  nand NAND2_53(G383, d22, G296);
  nand NAND2_54(G384, d23, G299);
  nand NAND2_55(G385, d24, G299);
  nand NAND2_56(G386, d25, G302);
  nand NAND2_57(G387, d26, G302);
  nand NAND2_58(G388, d27, G305);
  nand NAND2_59(G389, d28, G305);
  nand NAND2_60(G390, d29, G308);
  nand NAND2_61(G391, d30, G308);
  nand NAND2_62(G392, d31, G311);
  nand NAND2_63(G393, d32, G311);
  nand NAND2_64(G394, d1, G314);
  nand NAND2_65(G395, d5, G314);
  nand NAND2_66(G396, d9, G317);
  nand NAND2_67(G397, d13, G317);
  nand NAND2_68(G398, d2, G320);
  nand NAND2_69(G399, d6, G320);
  nand NAND2_70(G400, d10, G323);
  nand NAND2_71(G401, d14, G323);
  nand NAND2_72(G402, d3, G326);
  nand NAND2_73(G403, d7, G326);
  nand NAND2_74(G404, d11, G329);
  nand NAND2_75(G405, d15, G329);
  nand NAND2_76(G406, d4, G332);
  nand NAND2_77(G407, d8, G332);
  nand NAND2_78(G408, d12, G335);
  nand NAND2_79(G409, d16, G335);
  nand NAND2_80(G410, d17, G338);
  nand NAND2_81(G411, d21, G338);
  nand NAND2_82(G412, d25, G341);
  nand NAND2_83(G413, d29, G341);
  nand NAND2_84(G414, d18, G344);
  nand NAND2_85(G415, d22, G344);
  nand NAND2_86(G416, d26, G347);
  nand NAND2_87(G417, d30, G347);
  nand NAND2_88(G418, d19, G350);
  nand NAND2_89(G419, d23, G350);
  nand NAND2_90(G420, d27, G353);
  nand NAND2_91(G421, d31, G353);
  nand NAND2_92(G422, d20, G356);
  nand NAND2_93(G423, d24, G356);
  nand NAND2_94(G424, d28, G359);
  nand NAND2_95(G425, d32, G359);
  nand NAND2_96(G426, G362, G363);
  nand NAND2_97(G429, G364, G365);
  nand NAND2_98(G432, G366, G367);
  nand NAND2_99(G435, G368, G369);
  nand NAND2_100(G438, G370, G371);
  nand NAND2_101(G441, G372, G373);
  nand NAND2_102(G444, G374, G375);
  nand NAND2_103(G447, G376, G377);
  nand NAND2_104(G450, G378, G379);
  nand NAND2_105(G453, G380, G381);
  nand NAND2_106(G456, G382, G383);
  nand NAND2_107(G459, G384, G385);
  nand NAND2_108(G462, G386, G387);
  nand NAND2_109(G465, G388, G389);
  nand NAND2_110(G468, G390, G391);
  nand NAND2_111(G471, G392, G393);
  nand NAND2_112(G474, G394, G395);
  nand NAND2_113(G477, G396, G397);
  nand NAND2_114(G480, G398, G399);
  nand NAND2_115(G483, G400, G401);
  nand NAND2_116(G486, G402, G403);
  nand NAND2_117(G489, G404, G405);
  nand NAND2_118(G492, G406, G407);
  nand NAND2_119(G495, G408, G409);
  nand NAND2_120(G498, G410, G411);
  nand NAND2_121(G501, G412, G413);
  nand NAND2_122(G504, G414, G415);
  nand NAND2_123(G507, G416, G417);
  nand NAND2_124(G510, G418, G419);
  nand NAND2_125(G513, G420, G421);
  nand NAND2_126(G516, G422, G423);
  nand NAND2_127(G519, G424, G425);
  nand NAND2_128(G522, G426, G429);
  nand NAND2_129(G525, G432, G435);
  nand NAND2_130(G528, G438, G441);
  nand NAND2_131(G531, G444, G447);
  nand NAND2_132(G534, G450, G453);
  nand NAND2_133(G537, G456, G459);
  nand NAND2_134(G540, G462, G465);
  nand NAND2_135(G543, G468, G471);
  nand NAND2_136(G546, G474, G477);
  nand NAND2_137(G549, G480, G483);
  nand NAND2_138(G552, G486, G489);
  nand NAND2_139(G555, G492, G495);
  nand NAND2_140(G558, G498, G501);
  nand NAND2_141(G561, G504, G507);
  nand NAND2_142(G564, G510, G513);
  nand NAND2_143(G567, G516, G519);
  nand NAND2_144(G570, G426, G522);
  nand NAND2_145(G571, G429, G522);
  nand NAND2_146(G572, G432, G525);
  nand NAND2_147(G573, G435, G525);
  nand NAND2_148(G574, G438, G528);
  nand NAND2_149(G575, G441, G528);
  nand NAND2_150(G576, G444, G531);
  nand NAND2_151(G577, G447, G531);
  nand NAND2_152(G578, G450, G534);
  nand NAND2_153(G579, G453, G534);
  nand NAND2_154(G580, G456, G537);
  nand NAND2_155(G581, G459, G537);
  nand NAND2_156(G582, G462, G540);
  nand NAND2_157(G583, G465, G540);
  nand NAND2_158(G584, G468, G543);
  nand NAND2_159(G585, G471, G543);
  nand NAND2_160(G586, G474, G546);
  nand NAND2_161(G587, G477, G546);
  nand NAND2_162(G588, G480, G549);
  nand NAND2_163(G589, G483, G549);
  nand NAND2_164(G590, G486, G552);
  nand NAND2_165(G591, G489, G552);
  nand NAND2_166(G592, G492, G555);
  nand NAND2_167(G593, G495, G555);
  nand NAND2_168(G594, G498, G558);
  nand NAND2_169(G595, G501, G558);
  nand NAND2_170(G596, G504, G561);
  nand NAND2_171(G597, G507, G561);
  nand NAND2_172(G598, G510, G564);
  nand NAND2_173(G599, G513, G564);
  nand NAND2_174(G600, G516, G567);
  nand NAND2_175(G601, G519, G567);
  nand NAND2_176(G602, G570, G571);
  nand NAND2_177(G607, G572, G573);
  nand NAND2_178(G612, G574, G575);
  nand NAND2_179(G617, G576, G577);
  nand NAND2_180(G622, G578, G579);
  nand NAND2_181(G627, G580, G581);
  nand NAND2_182(G632, G582, G583);
  nand NAND2_183(G637, G584, G585);
  nand NAND2_184(G642, G586, G587);
  nand NAND2_185(G645, G588, G589);
  nand NAND2_186(G648, G590, G591);
  nand NAND2_187(G651, G592, G593);
  nand NAND2_188(G654, G594, G595);
  nand NAND2_189(G657, G596, G597);
  nand NAND2_190(G660, G598, G599);
  nand NAND2_191(G663, G600, G601);
  nand NAND2_192(G666, G602, G607);
  nand NAND2_193(G669, G612, G617);
  nand NAND2_194(G672, G602, G612);
  nand NAND2_195(G675, G607, G617);
  nand NAND2_196(G678, G622, G627);
  nand NAND2_197(G681, G632, G637);
  nand NAND2_198(G684, G622, G632);
  nand NAND2_199(G687, G627, G637);
  nand NAND2_200(G690, G602, G666);
  nand NAND2_201(G691, G607, G666);
  nand NAND2_202(G692, G612, G669);
  nand NAND2_203(G693, G617, G669);
  nand NAND2_204(G694, G602, G672);
  nand NAND2_205(G695, G612, G672);
  nand NAND2_206(G696, G607, G675);
  nand NAND2_207(G697, G617, G675);
  nand NAND2_208(G698, G622, G678);
  nand NAND2_209(G699, G627, G678);
  nand NAND2_210(G700, G632, G681);
  nand NAND2_211(G701, G637, G681);
  nand NAND2_212(G702, G622, G684);
  nand NAND2_213(G703, G632, G684);
  nand NAND2_214(G704, G627, G687);
  nand NAND2_215(G705, G637, G687);
  nand NAND2_216(G706, G690, G691);
  nand NAND2_217(G709, G692, G693);
  nand NAND2_218(G712, G694, G695);
  nand NAND2_219(G715, G696, G697);
  nand NAND2_220(G718, G698, G699);
  nand NAND2_221(G721, G700, G701);
  nand NAND2_222(G724, G702, G703);
  nand NAND2_223(G727, G704, G705);
  nand NAND2_224(G730, G242, G718);
  nand NAND2_225(G733, G245, G721);
  nand NAND2_226(G736, G248, G724);
  nand NAND2_227(G739, G251, G727);
  nand NAND2_228(G742, G254, G706);
  nand NAND2_229(G745, G257, G709);
  nand NAND2_230(G748, G260, G712);
  nand NAND2_231(G751, G263, G715);
  nand NAND2_232(G754, G242, G730);
  nand NAND2_233(G755, G718, G730);
  nand NAND2_234(G756, G245, G733);
  nand NAND2_235(G757, G721, G733);
  nand NAND2_236(G758, G248, G736);
  nand NAND2_237(G759, G724, G736);
  nand NAND2_238(G760, G251, G739);
  nand NAND2_239(G761, G727, G739);
  nand NAND2_240(G762, G254, G742);
  nand NAND2_241(G763, G706, G742);
  nand NAND2_242(G764, G257, G745);
  nand NAND2_243(G765, G709, G745);
  nand NAND2_244(G766, G260, G748);
  nand NAND2_245(G767, G712, G748);
  nand NAND2_246(G768, G263, G751);
  nand NAND2_247(G769, G715, G751);
  nand NAND2_248(G770, G754, G755);
  nand NAND2_249(G773, G756, G757);
  nand NAND2_250(G776, G758, G759);
  nand NAND2_251(G779, G760, G761);
  nand NAND2_252(G782, G762, G763);
  nand NAND2_253(G785, G764, G765);
  nand NAND2_254(G788, G766, G767);
  nand NAND2_255(G791, G768, G769);
  nand NAND2_256(G794, G642, G770);
  nand NAND2_257(G797, G645, G773);
  nand NAND2_258(G800, G648, G776);
  nand NAND2_259(G803, G651, G779);
  nand NAND2_260(G806, G654, G782);
  nand NAND2_261(G809, G657, G785);
  nand NAND2_262(G812, G660, G788);
  nand NAND2_263(G815, G663, G791);
  nand NAND2_264(G818, G642, G794);
  nand NAND2_265(G819, G770, G794);
  nand NAND2_266(G820, G645, G797);
  nand NAND2_267(G821, G773, G797);
  nand NAND2_268(G822, G648, G800);
  nand NAND2_269(G823, G776, G800);
  nand NAND2_270(G824, G651, G803);
  nand NAND2_271(G825, G779, G803);
  nand NAND2_272(G826, G654, G806);
  nand NAND2_273(G827, G782, G806);
  nand NAND2_274(G828, G657, G809);
  nand NAND2_275(G829, G785, G809);
  nand NAND2_276(G830, G660, G812);
  nand NAND2_277(G831, G788, G812);
  nand NAND2_278(G832, G663, G815);
  nand NAND2_279(G833, G791, G815);
  nand NAND2_280(G834, G818, G819);
  nand NAND2_281(G847, G820, G821);
  nand NAND2_282(G860, G822, G823);
  nand NAND2_283(G873, G824, G825);
  nand NAND2_284(G886, G828, G829);
  nand NAND2_285(G899, G832, G833);
  nand NAND2_286(G912, G830, G831);
  nand NAND2_287(G925, G826, G827);
  not NOT_0(G938, G834);
  not NOT_1(G939, G847);
  not NOT_2(G940, G860);
  not NOT_3(G941, G834);
  not NOT_4(G942, G847);
  not NOT_5(G943, G873);
  not NOT_6(G944, G834);
  not NOT_7(G945, G860);
  not NOT_8(G946, G873);
  not NOT_9(G947, G847);
  not NOT_10(G948, G860);
  not NOT_11(G949, G873);
  not NOT_12(G950, G886);
  not NOT_13(G951, G899);
  not NOT_14(G952, G886);
  not NOT_15(G953, G912);
  not NOT_16(G954, G925);
  not NOT_17(G955, G899);
  not NOT_18(G956, G925);
  not NOT_19(G957, G912);
  not NOT_20(G958, G925);
  not NOT_21(G959, G886);
  not NOT_22(G960, G912);
  not NOT_23(G961, G925);
  not NOT_24(G962, G886);
  not NOT_25(G963, G899);
  not NOT_26(G964, G925);
  not NOT_27(G965, G912);
  not NOT_28(G966, G899);
  not NOT_29(G967, G886);
  not NOT_30(G968, G912);
  not NOT_31(G969, G899);
  not NOT_32(G970, G847);
  not NOT_33(G971, G873);
  not NOT_34(G972, G847);
  not NOT_35(G973, G860);
  not NOT_36(G974, G834);
  not NOT_37(G975, G873);
  not NOT_38(G976, G834);
  not NOT_39(G977, G860);
  and AND4_0(G978, G938, G939, G940, G873);
  and AND4_1(G979, G941, G942, G860, G943);
  and AND4_2(G980, G944, G847, G945, G946);
  and AND4_3(G981, G834, G947, G948, G949);
  and AND4_4(G982, G958, G959, G960, G899);
  and AND4_5(G983, G961, G962, G912, G963);
  and AND4_6(G984, G964, G886, G965, G966);
  and AND4_7(G985, G925, G967, G968, G969);
  or OR4_0(G986, G978, G979, G980, G981);
  or OR4_1(G991, G982, G983, G984, G985);
  and AND5_0(G996, G925,G950, G912, G951, G986);
  and AND5_1(G1001, G925, G952, G953, G899, G986);
  and AND5_2(G1006, G954, G886, G912, G955, G986);
  and AND5_3(G1011, G956, G886, G957, G899, G986);
  and AND5_4(G1016, G834, G970, G860, G971, G991);
  and AND5_5(G1021, G834, G972, G973, G873, G991);
  and AND5_6(G1026, G974, G847, G860, G975, G991);
  and AND5_7(G1031, G976, G847, G977, G873, G991);
  and AND2_8(G1036, G834, G996);
  and AND2_9(G1039, G847, G996);
  and AND2_10(G1042, G860, G996);
  and AND2_11(G1045, G873, G996);
  and AND2_12(G1048, G834, G1001);
  and AND2_13(G1051, G847, G1001);
  and AND2_14(G1054, G860, G1001);
  and AND2_15(G1057, G873, G1001);
  and AND2_16(G1060, G834, G1006);
  and AND2_17(G1063, G847, G1006);
  and AND2_18(G1066, G860, G1006);
  and AND2_19(G1069, G873, G1006);
  and AND2_20(G1072, G834, G1011);
  and AND2_21(G1075, G847, G1011);
  and AND2_22(G1078, G860, G1011);
  and AND2_23(G1081, G873, G1011);
  and AND2_24(G1084, G925, G1016);
  and AND2_25(G1087, G886, G1016);
  and AND2_26(G1090, G912, G1016);
  and AND2_27(G1093, G899, G1016);
  and AND2_28(G1096, G925, G1021);
  and AND2_29(G1099, G886, G1021);
  and AND2_30(G1102, G912, G1021);
  and AND2_31(G1105, G899, G1021);
  and AND2_32(G1108, G925, G1026);
  and AND2_33(G1111, G886, G1026);
  and AND2_34(G1114, G912, G1026);
  and AND2_35(G1117, G899, G1026);
  and AND2_36(G1120, G925, G1031);
  and AND2_37(G1123, G886, G1031);
  and AND2_38(G1126, G912, G1031);
  and AND2_39(G1129, G899, G1031);
  nand NAND2_288(G1132, d1, G1036);
  nand NAND2_289(G1135, d2, G1039);
  nand NAND2_290(G1138, d3, G1042);
  nand NAND2_291(G1141, d4, G1045);
  nand NAND2_292(G1144, d5, G1048);
  nand NAND2_293(G1147, d6, G1051);
  nand NAND2_294(G1150, d7, G1054);
  nand NAND2_295(G1153, d8, G1057);
  nand NAND2_296(G1156, d9, G1060);
  nand NAND2_297(G1159, d10, G1063);
  nand NAND2_298(G1162, d11, G1066);
  nand NAND2_299(G1165, d12, G1069);
  nand NAND2_300(G1168, d13, G1072);
  nand NAND2_301(G1171, d14, G1075);
  nand NAND2_302(G1174, d15, G1078);
  nand NAND2_303(G1177, d16, G1081);
  nand NAND2_304(G1180, d17, G1084);
  nand NAND2_305(G1183, d18, G1087);
  nand NAND2_306(G1186, d19, G1090);
  nand NAND2_307(G1189, d20, G1093);
  nand NAND2_308(G1192, d21, G1096);
  nand NAND2_309(G1195, d22, G1099);
  nand NAND2_310(G1198, d23, G1102);
  nand NAND2_311(G1201, d24, G1105);
  nand NAND2_312(G1204, d25, G1108);
  nand NAND2_313(G1207, d26, G1111);
  nand NAND2_314(G1210, d27, G1114);
  nand NAND2_315(G1213, d28, G1117);
  nand NAND2_316(G1216, d29, G1120);
  nand NAND2_317(G1219, d30, G1123);
  nand NAND2_318(G1222, d31, G1126);
  nand NAND2_319(G1225, d32, G1129);
  nand NAND2_321(G1229, G1036, G1132);
  nand NAND2_323(G1231, G1039, G1135);
  nand NAND2_325(G1233, G1042, G1138);
  nand NAND2_327(G1235, G1045, G1141);
  nand NAND2_329(G1237, G1048, G1144);
  nand NAND2_331(G1239, G1051, G1147);
  nand NAND2_333(G1241, G1054, G1150);
  nand NAND2_335(G1243, G1057, G1153);
  nand NAND2_337(G1245, G1060, G1156);
  nand NAND2_339(G1247, G1063, G1159);
  nand NAND2_341(G1249, G1066, G1162);
  nand NAND2_343(G1251, G1069, G1165);
  nand NAND2_345(G1253, G1072, G1168);
  nand NAND2_347(G1255, G1075, G1171);
  nand NAND2_349(G1257, G1078, G1174);
  nand NAND2_351(G1259, G1081, G1177);
  nand NAND2_353(G1261, G1084, G1180);
  nand NAND2_355(G1263, G1087, G1183);
  nand NAND2_357(G1265, G1090, G1186);
  nand NAND2_359(G1267, G1093, G1189);
  nand NAND2_361(G1269, G1096, G1192);
  nand NAND2_363(G1271, G1099, G1195);
  nand NAND2_365(G1273, G1102, G1198);
  nand NAND2_367(G1275, G1105, G1201);
  nand NAND2_369(G1277, G1108, G1204);
  nand NAND2_371(G1279, G1111, G1207);
  nand NAND2_373(G1281, G1114, G1210);
  nand NAND2_375(G1283, G1117, G1213);
  nand NAND2_377(G1285, G1120, G1216);
  nand NAND2_379(G1287, G1123, G1219);
  nand NAND2_381(G1289, G1126, G1222);
  nand NAND2_320(G1228, d1, G1132);
  nand NAND2_322(G1230, d2, G1135);
  nand NAND2_324(G1232, d3, G1138);
  nand NAND2_326(G1234, d4, G1141);
  nand NAND2_328(G1236, d5, G1144);
  nand NAND2_330(G1238, d6, G1147);
  nand NAND2_332(G1240, d7, G1150);
  nand NAND2_334(G1242, d8, G1153);
  nand NAND2_336(G1244, d9, G1156);
  nand NAND2_338(G1246, d10, G1159);
  nand NAND2_340(G1248, d11, G1162);
  nand NAND2_342(G1250, d12, G1165);
  nand NAND2_344(G1252, d13, G1168);
  nand NAND2_346(G1254, d14, G1171);
  nand NAND2_348(G1256, d15, G1174);
  nand NAND2_350(G1258, d16, G1177);
  nand NAND2_352(G1260, d17, G1180);
  nand NAND2_354(G1262, d18, G1183);
  nand NAND2_356(G1264, d19, G1186);
  nand NAND2_358(G1266, d20, G1189);
  nand NAND2_360(G1268, d21, G1192);
  nand NAND2_362(G1270, d22, G1195);
  nand NAND2_364(G1272, d23, G1198);
  nand NAND2_366(G1274, d24, G1201);
  nand NAND2_368(G1276, d25, G1204);
  nand NAND2_370(G1278, d26, G1207);
  nand NAND2_372(G1280, d27, G1210);
  nand NAND2_374(G1282, d28, G1213);
  nand NAND2_376(G1284, d29, G1216);
  nand NAND2_378(G1286, d30, G1219);
  nand NAND2_380(G1288, d31, G1222);
  nand NAND2_382(G1290, d32, G1225);
  nand NAND2_383(G1291, G1129, G1225);
  nand NAND2_384(G1292, G1228, G1229);
  nand NAND2_385(G1293, G1230, G1231);
  nand NAND2_386(G1294, G1232, G1233);
  nand NAND2_387(G1295, G1234, G1235);
  nand NAND2_388(G1296, G1236, G1237);
  nand NAND2_389(G1297, G1238, G1239);
  nand NAND2_390(G1298, G1240, G1241);
  nand NAND2_391(G1299, G1242, G1243);
  nand NAND2_392(G1300, G1244, G1245);
  nand NAND2_393(G1301, G1246, G1247);
  nand NAND2_394(G1302, G1248, G1249);
  nand NAND2_395(G1303, G1250, G1251);
  nand NAND2_396(G1304, G1252, G1253);
  nand NAND2_397(G1305, G1254, G1255);
  nand NAND2_398(G1306, G1256, G1257);
  nand NAND2_399(G1307, G1258, G1259);
  nand NAND2_400(G1308, G1260, G1261);
  nand NAND2_401(G1309, G1262, G1263);
  nand NAND2_402(G1310, G1264, G1265);
  nand NAND2_403(G1311, G1266, G1267);
  nand NAND2_404(G1312, G1268, G1269);
  nand NAND2_405(G1313, G1270, G1271);
  nand NAND2_406(G1314, G1272, G1273);
  nand NAND2_407(G1315, G1274, G1275);
  nand NAND2_408(G1316, G1276, G1277);
  nand NAND2_409(G1317, G1278, G1279);
  nand NAND2_410(G1318, G1280, G1281);
  nand NAND2_411(G1319, G1282, G1283);
  nand NAND2_412(G1320, G1284, G1285);
  nand NAND2_413(G1321, G1286, G1287);
  nand NAND2_414(G1322, G1288, G1289);
  nand NAND2_415(G1323, G1290, G1291);
  not NOT_40(d1324, G1292);
  not NOT_41(d1325, G1293);
  not NOT_42(d1326, G1294);
  not NOT_43(d1327, G1295);
  not NOT_44(d1328, G1296);
  not NOT_45(d1329, G1297);
  not NOT_46(d1330, G1298);
  not NOT_47(d1331, G1299);
  not NOT_48(d1332, G1300);
  not NOT_49(d1333, G1301);
  not NOT_50(d1334, G1302);
  not NOT_51(d1335, G1303);
  not NOT_52(d1336, G1304);
  not NOT_53(d1337, G1305);
  not NOT_54(d1338, G1306);
  not NOT_55(d1339, G1307);
  not NOT_56(d1340, G1308);
  not NOT_57(d1341, G1309);
  not NOT_58(d1342, G1310);
  not NOT_59(d1343, G1311);
  not NOT_60(d1344, G1312);
  not NOT_61(d1345, G1313);
  not NOT_62(d1346, G1314);
  not NOT_63(d1347, G1315);
  not NOT_64(d1348, G1316);
  not NOT_65(d1349, G1317);
  not NOT_66(d1350, G1318);
  not NOT_67(d1351, G1319);
  not NOT_68(d1352, G1320);
  not NOT_69(d1353, G1321);
  not NOT_70(d1354, G1322);
  not NOT_71(d1355, G1323);

//input Flip-flops
dff a1 (d1, G1, clk);
dff a2 (d2, G2, clk);
dff a3 (d3, G3, clk);
dff a4 (d4, G4, clk);
dff a5 (d5, G5, clk);
dff a6 (d6, G6, clk);
dff a7 (d7, G7, clk);
dff a8 (d8, G8, clk);
dff a9 (d9, G9, clk);
dff a10 (d10, G10, clk);
dff a11 (d11, G11, clk);
dff a12 (d12, G12, clk);
dff a13 (d13, G13, clk);
dff a14 (d14, G14, clk);
dff a15 (d15, G15, clk);
dff a16 (d16, G16, clk);
dff a17 (d17, G17, clk);
dff a18 (d18, G18, clk);
dff a19 (d19, G19, clk);
dff a20 (d20, G20, clk);
dff a21 (d21, G21, clk);
dff a22 (d22, G22, clk);
dff a23 (d23, G23, clk);
dff a24 (d24, G24, clk);
dff a25 (d25, G25, clk);
dff a26 (d26, G26, clk);
dff a27 (d27, G27, clk);
dff a28 (d28, G28, clk);
dff a29 (d29, G29, clk);
dff a30 (d30, G30, clk);
dff a31 (d31, G31, clk);
dff a32 (d32, G32, clk);
dff a33 (d33, G33, clk);
dff a34 (d34, G34, clk);
dff a35 (d35, G35, clk);
dff a36 (d36, G36, clk);
dff a37 (d37, G37, clk);
dff a38 (d38, G38, clk);
dff a39 (d39, G39, clk);
dff a40 (d40, G40, clk);
dff a41 (d41, G41, clk);
//output Flip-flops
dff o1 (G1324, d1324, clk);
dff o2 (G1325, d1325, clk);
dff o3 (G1326, d1326, clk);
dff o4 (G1327, d1327, clk);
dff o5 (G1328, d1328, clk);
dff o6 (G1329, d1329, clk);
dff o7 (G1330, d1330, clk);
dff o8 (G1331, d1331, clk);
dff o9 (G1332, d1332, clk);
dff o10 (G1333, d1333, clk);
dff o11 (G1334, d1334, clk);
dff o12 (G1335, d1335, clk);
dff o13 (G1336, d1336, clk);
dff o14 (G1337, d1337, clk);
dff o15 (G1338, d1338, clk);
dff o16 (G1339, d1339, clk);
dff o17 (G1340, d1340, clk);
dff o18 (G1341, d1341, clk);
dff o19 (G1342, d1342, clk);
dff o20 (G1343, d1343, clk);
dff o21 (G1344, d1344, clk);
dff o22 (G1345, d1345, clk);
dff o23 (G1346, d1346, clk);
dff o24 (G1347, d1347, clk);
dff o25 (G1348, d1348, clk);
dff o26 (G1349, d1349, clk);
dff o27 (G1350, d1350, clk);
dff o28 (G1351, d1351, clk);
dff o29 (G1352, d1352, clk);
dff o30 (G1353, d1353, clk);
dff o31 (G1354, d1354, clk);
dff o32 (G1355, d1355, clk);

endmodule
//---------------------------------------------------------------------------------------------------------------------------------------------------
module dff(q, d, clk);
	input  d, clk;
	output reg q;

always @ (posedge clk)
	q <= d;
	
endmodule

//---------------------------------------------------------------------------------------------------------------------------------------------------
`timescale 1ns/ 1ps

module Testbench_benchmark3();
 reg G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20, G21, G22, G23, G24, G25, G26, G27, G28, G29, G30, G31, G32, G33, G34, G35, G36, G37, G38, G39, G40, G41, clk, en;
	 
 wire G1324, G1325, G1326, G1327, G1328, G1329, G1330, G1331, G1332, G1333, G1334, G1335, G1336, G1337, G1338, G1339, G1340, G1341, G1342, G1343, G1344, G1345, G1346, G1347, G1348, G1349, G1350, G1351, G1352, G1353, G1354, G1355;

 //instantiation
c1355 dut(
//input port mapping
    .G1(G1),
    .G2(G2),
    .G3(G3),
	.G4(G4),
    .G5(G5),
    .G6(G6),
	.G7(G7),
    .G8(G8),
    .G9(G9),
    .G10(G10),
	.G11(G11),
    .G12(G12),
    .G13(G13),
	.G14(G14),
    .G15(G15),
    .G16(G16),
    .G17(G17),
	.G18(G18),
    .G19(G19),
    .G20(G20),
	.G21(G21),
    .G22(G22),
    .G23(G23),
	.G24(G24),
    .G25(G25),
    .G26(G26),
    .G27(G27),
	.G28(G28),
    .G29(G29),
    .G30(G30),
	.G31(G31),
    .G32(G32),
    .G33(G33),
	.G34(G34),
    .G35(G35),
    .G36(G36),
    .G37(G37),
	.G38(G38),
    .G39(G39),
    .G40(G40),
	.G41(G41),
	
//output port mapping	
	.G1324(G1324),
	.G1325(G1325),
	.G1326(G1326),
	.G1327(G1327),
	.G1328(G1328),
	.G1329(G1329),
	.G1330(G1330),
	.G1331(G1331),
	.G1332(G1332),
	.G1333(G1333),
	.G1334(G1334),
	.G1335(G1335),
	.G1336(G1336),
	.G1337(G1337),
	.G1338(G1338),
	.G1339(G1339),
	.G1340(G1340),
	.G1341(G1341),
	.G1342(G1342),
	.G1343(G1343),
	.G1344(G1344),
	.G1345(G1345),
	.G1346(G1346),
	.G1347(G1347),
	.G1348(G1348),
	.G1349(G1349),
	.G1350(G1350),
	.G1351(G1351),
	.G1352(G1352),
	.G1353(G1353),
	.G1354(G1354),
	.G1355(G1355),	
	.clk(clk),
	.en(en)
   );
   
    initial begin
		clk = 0; G1=clk; G2=clk; G3=clk; G4=clk; G5=clk; G6=clk; G7=clk; G8=clk; G9=clk; G10=clk; G21=clk;
		G11=clk; G12=clk; G13=clk; G14=clk; G15=clk; G16=clk; G17=clk; G18=clk; G19=clk; G20=clk; G22=clk; 
		G23=clk; G24=clk; G25=clk; G26=clk; G27=clk; G28=clk; G29=clk; G30=clk; G31=clk; G32=clk; G33=clk; 
		G34=clk; G35=clk; G36=clk; G37=clk; G38=clk; G39=clk; G40=clk; G41=clk; en = 0;
	 //$dumpfile ("goldenc17.vcd"); 
	 //$dumpvars(0,Testbench_benchmark1);
	end
	
	always @ (posedge clk)
		 $display(" %4d, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b,%1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b,%1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b",
             $time, G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20, G21, G22, G23, G24, G25, G26, G27, G28, G29, G30, G31,
			 G32, G33, G34, G35, G36, G37, G38, G39, G40, G41, en, G1324, G1325, G1326, G1327, G1328, G1329, G1330, G1331, G1332, G1333, G1334, G1335, G1336, G1337, 
			 G1338, G1339, G1340, G1341, G1342, G1343, G1344, G1345, G1346, G1347, G1348, G1349, G1350, G1351, G1352, G1353, G1354, G1355);
	initial begin
		#0.4 en = 0;
	end
	
	always
		#1 clk = ~clk;
	always 
		#4 G1 = ~G1;
	always 
		#40 G2 = ~G2;
	always 
		#3 G3 = ~G3;
	always 
		#23 G4 = ~G4;
	always 
		#1 G5 = ~G5;
	always 
		#2 G6 = ~G6;
	always 
		#21 G7 = ~G7;
	always 
		#38 G8 = ~G8;
	always 
		#7 G9 = ~G9;
	always 
		#14 G10 = ~G10;
	always 
		#39 G11 = ~G11;
	always 
		#24 G12 = ~G12;
	always 
		#5 G13 = ~G13;
	always 
		#22 G14 = ~G14;
	always 
		#8 G15 = ~G15;
	always 
		#15 G16 = ~G16;
	always 
		#6 G17 = ~G17;
	always 
		#13 G18 = ~G18;
	always 
		#36 G19 = ~G19;
	always 
		#20 G20 = ~G20;
	always 
		#9 G21 = ~G21;
	always 
		#26 G22 = ~G22;
	always 
		#19 G23 = ~G23;
	always 
		#10 G24 = ~G24;
	always 
		#16 G25 = ~G25;
	always 
		#37 G26 = ~G26;
	always 
		#18 G27 = ~G27;
	always 
		#30 G28 = ~G28;
	always 
		#25 G29 = ~G29;
	always 
		#12 G30 = ~G30;
	always 
		#34 G31 = ~G31;
	always 
		#28 G32 = ~G32;
	always 
		#32 G33 = ~G33;
	always 
		#17 G34 = ~G34;
	always 
		#35 G35 = ~G35;
	always 
		#11 G36 = ~G36;
	always 
		#29 G37 = ~G37;
	always 
		#3 G38 = ~G38;
	always 
		#27 G39 = ~G39;
	always 
		#33 G40 = ~G40;	
	always 
		#31 G41 = ~G41;			

	initial #1000 $finish;
endmodule