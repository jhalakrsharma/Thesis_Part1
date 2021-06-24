// c880						// NAND4 13
// Ninputs 60				// AND3 12
// Noutputs 26				// NAND2 60
// NtotalGates 383			// NAND3 14
// AND2 105					// OR2 29
// NOT1 63					// NOR2 61
// BUFF1 26

module c880 (en, clk, N1, N8, N13, N17, N26, N29, N36, N42, N51, N55, N59, N68, N72, N73, N74, N75, N80, N85, N86, N87, N88, N89, N90, N91, N96, N101, N106, N111, 
			 N116, N121, N126, N130, N135, N138, N143, N146, N149, N152, N153, N156, N159, N165, N171, N177, N183, N189, N195, N201, N207, N210, N219, N228, N237, 
			 N246, N255, N259, N260, N261, N267, N268, N388, N389, N390, N391, N418, N419, N420, N421, N422, N423, N446, N447, N448, N449, N450, N767, N768, N850, 
			 N863, N864, N865, N866, N874, N878, N879, N880);

input en, clk, N1, N8, N13, N17, N26, N29, N36, N42, N51, N55, N59, N68, N72, N73, N74, N75, N80, N85, N86, N87, N88, N89, N90, N91, N96, N101, N106, N111, N116, N121, N126, N130, N135, N138, N143, N146, N149, N152, N153, N156, N159, N165, N171, N177, N183, N189, N195, N201, N207, N210, N219, N228, N237, N246, N255, N259, N260, N261, N267, N268;

output N388, N389, N390, N391, N418, N419, N420, N421, N422, N423, N446, N447, N448, N449, N450, N767, N768, N850, N863, N864, N865, N866, N874, N878, N879, N880;

wire error, d1, d8, d13, d17, d26, d29, d36, d42, d51, d55, d59, d68, d72, d73, d74, d75, d80, d85, d86, d87, d88, d89, d90, d91, d96, d101, d106, d111, d116, d121, d126, d130, d135, d138, d143, d146, d149, d152, d153, d156, d159, d165, d171, d177, d183, d189, d195, d201, d207, d210, d219, d228, d237, d246, d255, d259, d260, d261, d267, d268, d388, d389, d390, d391, d418, d419, d420, d421, d422, d423, d446, d447, d448, d449, d450, d767, d768, d850, d863, d864, d865, d866, d874, d878, d879, d880, N269, N270, N273, N276, N279, N280, N284, N285, N286, N287, N290, N291, N292, N293, N294, N295, N296, N297, N298, N301, N302, N303, N304, N305, N306, N307, N308, N309, N310, N316, N317, N318, N319, N322, N323, N324, N325, N326, N327, N328,  N329, N330, N331, N332, N333, N334, N335, N336, N337, N338, N339, N340, N341, N342, N343, N344, N345, N346, N347, N348,  N349, N350, N351, N352, N353, N354, N355, N356, N357, N360, N363, N366, N369, N375, N376, N379, N382, N385, N392, N393, N399, N400, N401, N402, N403, N404, N405, N406, N407, N408, N409, N410, N411, N412, N413, N414, N415, N416, N417, N424, N425, N426, N427, N432, N437, N442, N443, N444, N445, N451, N460, N463, N466, N475, N476, N477, N478, N479, N480, N481,  N482, N483, N488, N489, N490, N491, N492, N495, N498, N499, N500, N501, N502, N503, N504, N505, N506, N507, N508, N509,  N510, N511, N512, N513, N514, N515, N516, N517, N518, N519, N520, N521, N522, N523, N524, N525, N526, N527, N528, N529,  N530, N533, N536, N537, N538, N539, N540, N541, N542, N543, N544, N547, N550, N551, N552, N553, N557, N561, N565, N569,  N573, N577, N581, N585, N586, N587, N588, N589, N590, N593, N596, N597, N600, N605, N606, N609, N615, N616, N619, N624,  N625, N628, N631, N632, N635, N640, N641, N644, N650, N651, N654, N659, N660, N661, N662, N665, N669, N670, N673, N677,  N678, N682, N686, N687, N692, N696, N697, N700, N704, N705, N708, N712, N713, N717, N721, N722, N727, N731, N732, N733,  N734, N735, N736, N737, N738, N739, N740, N741, N742, N743, N744, N745, N746, N747, N748, N749, N750, N751, N752, N753,  N754, N755, N756, N757, N758, N759, N760, N761, N762, N763, N764, N765, N766, N769, N770, N771, N772, N773, N777, N778, N781, N782, N785, N786, N787, N788, N789, N790, N791, N792, N793, N794, N795, N796, N802, N803, N804, N805, N806, N807,  N808, N809, N810, N811, N812, N813, N814, N815, N819, N822, N825, N826, N827, N828, N829, N830, N831, N832, N833, N834,  N835, N836, N837, N838, N839, N840, N841, N842, N843, N844, N845, N846, N847, N848, N849, N851, N852, N853, N854, N855,  N856, N857, N858, N859, N860, N861, N862, N867, N868, N869, N870, N871, N872, N873, N875, N876, N877;	 

nand NAND4_1 (N269, d1, d8, d13, d17);
nand NAND4_2 (N270, d1, d26, d13, d17);
and AND3_3 (N273, d29, d36, d42);
and AND3_4 (N276, d1, d26, d51);
nand NAND4_5 (N279, d1, d8, d51, d17);
nand NAND4_6 (N280, d1, d8, d13, d55);
nand NAND4_7 (N284, d59, d42, d68, d72);
nand NAND2_8 (N285, d29, d68);
nand NAND3_9 (N286, d59, d68, d74);
and AND3_10 (N287, d29, d75, d80);
and AND3_11 (N290, d29, d75, d42);
and AND3_12 (N291, d29, d36, d80);
and AND3_13 (N292, d29, d36, d42);
and AND3_14 (N293, d59, d75, d80);
and AND3_15 (N294, d59, d75, d42);
and AND3_16 (N295, d59, d36, d80);
and AND3_17 (N296, d59, d36, d42);
and AND2_18 (N297, d85, d86);
or OR2_19 (N298, d87, d88);
nand NAND2_20 (N301, d91, d96);
or OR2_21 (N302, d91, d96);
nand NAND2_22 (N303, d101, d106);
or OR2_23 (N304, d101, d106);
nand NAND2_24 (N305, d111, d116);
or OR2_25 (N306, d111, d116);
nand NAND2_26 (N307, d121, d126);
or OR2_27 (N308, d121, d126);
and AND2_28 (N309, d8, d138);
not NOT1_29 (N310, d268);
and AND2_30 (N316, d51, d138);
and AND2_31 (N317, d17,  d138);
and AND2_32 (N318, d152, d138);
nand NAND2_33 (N319, d59, d156);
nor NOR2_34 (N322, d17,  d42);
and AND2_35 (N323, d17,  d42);
nand NAND2_36 (N324, d159, d165);
or OR2_37 (N325, d159, d165);
nand NAND2_38 (N326, d171, d177);
or OR2_39 (N327, d171, d177);
nand NAND2_40 (N328, d183, d189);
or OR2_41 (N329, d183, d189);
nand NAND2_42 (N330, d195, d201);
or OR2_43 (N331, d195, d201);
and AND2_44 (N332, d210, d91);
and AND2_45 (N333, d210, d96);
and AND2_46 (N334, d210, d101);
and AND2_47 (N335, d210, d106);
and AND2_48 (N336, d210, d111);
and AND2_49 (N337, d255, d259);
and AND2_50 (N338, d210, d116);
and AND2_51 (N339, d255, d260);
and AND2_52 (N340, d210, d121);
and AND2_53 (N341, d255, d267);
not NOT1_54 (N342, N269);
not NOT1_55 (N343, N273);
or OR2_56 (N344, N270, N273);
not NOT1_57 (N345, N276);
not NOT1_58 (N346, N276);
not NOT1_59 (N347, N279);
nor NOR2_60 (N348, N280, N284);
or OR2_61 (N349, N280, N285);
or OR2_62 (N350, N280, N286);
not NOT1_63 (N351, N293);
not NOT1_64 (N352, N294);
not NOT1_65 (N353, N295);
not NOT1_66 (N354, N296);
nand NAND2_67 (N355, d89, N298);
and AND2_68 (N356, d90, N298);
nand NAND2_69 (N357, N301, N302);
nand NAND2_70 (N360, N303, N304);
nand NAND2_71 (N363, N305, N306);
nand NAND2_72 (N366, N307, N308);
not NOT1_73 (N369, N310);
nor NOR2_74 (N375, N322, N323);
nand NAND2_75 (N376, N324, N325);
nand NAND2_76 (N379, N326, N327);
nand NAND2_77 (N382, N328, N329);
nand NAND2_78 (N385, N330, N331);
buf BUFF1_79 (d388, N290);
buf BUFF1_80 (d389, N291);
buf BUFF1_81 (d390, N292);
buf BUFF1_82 (d391, N297);
or OR2_83 (N392, N270, N343);
not NOT1_84 (N393, N345);
not NOT1_85 (N399, N346);
and AND2_86 (N400, N348, d73);
not NOT1_87 (N401, N349);
not NOT1_88 (N402, N350);
not NOT1_89 (N403, N355);
not NOT1_90 (N404, N357);
not NOT1_91 (N405, N360);
and AND2_92 (N406, N357, N360);
not NOT1_93 (N407, N363);
not NOT1_94 (N408, N366);
and AND2_95 (N409, N363, N366);
nand NAND2_96 (N410, N347, N352);
not NOT1_97 (N411, N376);
not NOT1_98 (N412, N379);
and AND2_99 (N413, N376, N379);
not NOT1_100 (N414, N382);
not NOT1_101 (N415, N385);
and AND2_102 (N416, N382, N385);
and AND2_103 (N417, d210, N369);
buf BUFF1_104 (d418, N342);
buf BUFF1_105 (d419, N344);
buf BUFF1_106 (d420, N351);
buf BUFF1_107 (d421, N353);
buf BUFF1_108 (d422, N354);
buf BUFF1_109 (d423, N356);
not NOT1_110 (N424, N400);
and AND2_111 (N425, N404, N405);
and AND2_112 (N426, N407, N408);
and AND3_113 (N427, N319, N393, d55);
and AND3_114 (N432, N393, d17,  N287);
nand NAND3_115 (N437, N393, N287, d55);
nand NAND4_116 (N442, N375, d59, d156, N393);
nand NAND3_117 (N443, N393, N319, d17) ;
and AND2_118 (N444, N411, N412);
and AND2_119 (N445, N414, N415);
buf BUFF1_120 (d446, N392);
buf BUFF1_121 (d447, N399);
buf BUFF1_122 (d448, N401);
buf BUFF1_123 (d449, N402);
buf BUFF1_124 (d450, N403);
not NOT1_125 (N451, N424);
nor NOR2_126 (N460, N406, N425);
nor NOR2_127 (N463, N409, N426);
nand NAND2_128 (N466, N442, N410);
and AND2_129 (N475, d143, N427);
and AND2_130 (N476, N310, N432);
and AND2_131 (N477, d146, N427);
and AND2_132 (N478, N310, N432);
and AND2_133 (N479, d149, N427);
and AND2_134 (N480, N310, N432);
and AND2_135 (N481, d153, N427);
and AND2_136 (N482, N310, N432);
nand NAND2_137 (N483, N443, d1);
or OR2_138 (N488, N369, N437);
or OR2_139 (N489, N369, N437);
or OR2_140 (N490, N369, N437);
or OR2_141 (N491, N369, N437);
nor NOR2_142 (N492, N413, N444);
nor NOR2_143 (N495, N416, N445);
nand NAND2_144 (N498, d130, N460);
or OR2_145 (N499, d130, N460);
nand NAND2_146 (N500, N463, d135);
or OR2_147 (N501, N463, d135);
and AND2_148 (N502, d91, N466);
nor NOR2_149 (N503, N475, N476);
and AND2_150 (N504, d96, N466);
nor NOR2_151 (N505, N477, N478);
and AND2_152 (N506, d101, N466);
nor NOR2_153 (N507, N479, N480);
and AND2_154 (N508, d106, N466);
nor NOR2_155 (N509, N481, N482);
and AND2_156 (N510, d143, N483);
and AND2_157 (N511, d111, N466);
and AND2_158 (N512, d146, N483);
and AND2_159 (N513, d116, N466);
and AND2_160 (N514, d149, N483);
and AND2_161 (N515, d121, N466);
and AND2_162 (N516, d153, N483);
and AND2_163 (N517, d126, N466);
nand NAND2_164 (N518, d130, N492);
or OR2_165 (N519, d130, N492);
nand NAND2_166 (N520, N495, d207);
or OR2_167 (N521, N495, d207);
and AND2_168 (N522, N451, d159);
and AND2_169 (N523, N451, d165);
and AND2_170 (N524, N451, d171);
and AND2_171 (N525, N451, d177);
and AND2_172 (N526, N451, d183);
nand NAND2_173 (N527, N451, d189);
nand NAND2_174 (N528, N451, d195);
nand NAND2_175 (N529, N451, d201);
nand NAND2_176 (N530, N498, N499);
nand NAND2_177 (N533, N500, N501);
nor NOR2_178 (N536, N309, N502);
nor NOR2_179 (N537, N316, N504);
nor NOR2_180 (N538, N317, N506);
nor NOR2_181 (N539, N318, N508);
nor NOR2_182 (N540, N510, N511);
nor NOR2_183 (N541, N512, N513);
nor NOR2_184 (N542, N514, N515);
nor NOR2_185 (N543, N516, N517);
nand NAND2_186 (N544, N518, N519);
nand NAND2_187 (N547, N520, N521);
not NOT1_188 (N550, N530);
not NOT1_189 (N551, N533);
and AND2_190 (N552, N530, N533);
nand NAND2_191 (N553, N536, N503);
nand NAND2_192 (N557, N537, N505);
nand NAND2_193 (N561, N538, N507);
nand NAND2_194 (N565, N539, N509);
nand NAND2_195 (N569, N488, N540);
nand NAND2_196 (N573, N489, N541);
nand NAND2_197 (N577, N490, N542);
nand NAND2_198 (N581, N491, N543);
not NOT1_199 (N585, N544);
not NOT1_200 (N586, N547);
and AND2_201 (N587, N544, N547);
and AND2_202 (N588, N550, N551);
and AND2_203 (N589, N585, N586);
nand NAND2_204 (N590, N553, d159);
or OR2_205 (N593, N553, d159);
and AND2_206 (N596, d246, N553);
nand NAND2_207 (N597, N557, d165);
or OR2_208 (N600, N557, d165);
and AND2_209 (N605, d246, N557);
nand NAND2_210 (N606, N561, d171);
or OR2_211 (N609, N561, d171);
and AND2_212 (N615, d246, N561);
nand NAND2_213 (N616, N565, d177);
or OR2_214 (N619, N565, d177);
and AND2_215 (N624, d246, N565);
nand NAND2_216 (N625, N569, d183);
or OR2_217 (N628, N569, d183);
and AND2_218 (N631, d246, N569);
nand NAND2_219 (N632, N573, d189);
or OR2_220 (N635, N573, d189);
and AND2_221 (N640, d246, N573);
nand NAND2_222 (N641, N577, d195);
or OR2_223 (N644, N577, d195);
and AND2_224 (N650, d246, N577);
nand NAND2_225 (N651, N581, d201);
or OR2_226 (N654, N581, d201);
and AND2_227 (N659, d246, N581);
nor NOR2_228 (N660, N552, N588);
nor NOR2_229 (N661, N587, N589);
not NOT1_230 (N662, N590);
and AND2_231 (N665, N593, N590);
nor NOR2_232 (N669, N596, N522);
not NOT1_233 (N670, N597);
and AND2_234 (N673, N600, N597);
nor NOR2_235 (N677, N605, N523);
not NOT1_236 (N678, N606);
and AND2_237 (N682, N609, N606);
nor NOR2_238 (N686, N615, N524);
not NOT1_239 (N687, N616);
and AND2_240 (N692, N619, N616);
nor NOR2_241 (N696, N624, N525);
not NOT1_242 (N697, N625);
and AND2_243 (N700, N628, N625);
nor NOR2_244 (N704, N631, N526);
not NOT1_245 (N705, N632);
and AND2_246 (N708, N635, N632);
nor NOR2_247 (N712, N337, N640);
not NOT1_248 (N713, N641);
and AND2_249 (N717, N644, N641);
nor NOR2_250 (N721, N339, N650);
not NOT1_251 (N722, N651);
and AND2_252 (N727, N654, N651);
nor NOR2_253 (N731, N341, N659);
nand NAND2_254 (N732, N654, d261);
nand NAND3_255 (N733, N644, N654, d261);
nand NAND4_256 (N734, N635, N644, N654, d261);
not NOT1_257 (N735, N662);
and AND2_258 (N736, d228, N665);
and AND2_259 (N737, d237, N662);
not NOT1_260 (N738, N670);
and AND2_261 (N739, d228, N673);
and AND2_262 (N740, d237, N670);
not NOT1_263 (N741, N678);
and AND2_264 (N742, d228, N682);
and AND2_265 (N743, d237, N678);
not NOT1_266 (N744, N687);
and AND2_267 (N745, d228, N692);
and AND2_268 (N746, d237, N687);
not NOT1_269 (N747, N697);
and AND2_270 (N748, d228, N700);
and AND2_271 (N749, d237, N697);
not NOT1_272 (N750, N705);
and AND2_273 (N751, d228, N708);
and AND2_274 (N752, d237, N705);
not NOT1_275 (N753, N713);
and AND2_276 (N754, d228, N717);
and AND2_277 (N755, d237, N713);
not NOT1_278 (N756, N722);
nor NOR2_279 (N757, N727, d261);
and AND2_280 (N758, N727, d261);
and AND2_281 (N759, d228, N727);
and AND2_282 (N760, d237, N722);
nand NAND2_283 (N761, N644, N722);
nand NAND2_284 (N762, N635, N713);
nand NAND3_285 (N763, N635, N644, N722);
nand NAND2_286 (N764, N609, N687);
nand NAND2_287 (N765, N600, N678);
nand NAND3_288 (N766, N600, N609, N687);
buf BUFF1_289 (d767, N660);
buf BUFF1_290 (d768, N661);
nor NOR2_291 (N769, N736, N737);
nor NOR2_292 (N770, N739, N740);
nor NOR2_293 (N771, N742, N743);
nor NOR2_294 (N772, N745, N746);
nand NAND4_295 (N773, N750, N762, N763, N734);
nor NOR2_296 (N777, N748, N749);
nand NAND3_297 (N778, N753, N761, N733);
nor NOR2_298 (N781, N751, N752);
nand NAND2_299 (N782, N756, N732);
nor NOR2_300 (N785, N754, N755);
nor NOR2_301 (N786, N757, N758);
nor NOR2_302 (N787, N759, N760);
nor NOR2_303 (N788, N700, N773);
and AND2_304 (N789, N700, N773);
nor NOR2_305 (N790, N708, N778);
and AND2_306 (N791, N708, N778);
nor NOR2_307 (N792, N717, N782);
and AND2_308 (N793, N717, N782);
and AND2_309 (N794, d219, N786);
nand NAND2_310 (N795, N628, N773);
nand NAND2_311 (N796, N795, N747);
nor NOR2_312 (N802, N788, N789);
nor NOR2_313 (N803, N790, N791);
nor NOR2_314 (N804, N792, N793);
nor NOR2_315 (N805, N340, N794);
nor NOR2_316 (N806, N692, N796);
and AND2_317 (N807, N692, N796);
and AND2_318 (N808, d219, N802);
and AND2_319 (N809, d219, N803);
and AND2_320 (N810, d219, N804);
nand NAND4_321 (N811, N805, N787, N731, N529);
nand NAND2_322 (N812, N619, N796);
nand NAND3_323 (N813, N609, N619, N796);
nand NAND4_324 (N814, N600, N609, N619, N796);
nand NAND4_325 (N815, N738, N765, N766, N814);
nand NAND3_326 (N819, N741, N764, N813);
nand NAND2_327 (N822, N744, N812);
nor NOR2_328 (N825, N806, N807);
nor NOR2_329 (N826, N335, N808);
nor NOR2_330 (N827, N336, N809);
nor NOR2_331 (N828, N338, N810);
not NOT1_332 (N829, N811);
nor NOR2_333 (N830, N665, N815);
and AND2_334 (N831, N665, N815);
nor NOR2_335 (N832, N673, N819);
and AND2_336 (N833, N673, N819);
nor NOR2_337 (N834, N682, N822);
and AND2_338 (N835, N682, N822);
and AND2_339 (N836, d219, N825);
nand NAND3_340 (N837, N826, N777, N704);
nand NAND4_341 (N838, N827, N781, N712, N527);
nand NAND4_342 (N839, N828, N785, N721, N528);
not NOT1_343 (N840, N829);
nand NAND2_344 (N841, N815, N593);
nor NOR2_345 (N842, N830, N831);
nor NOR2_346 (N843, N832, N833);
nor NOR2_347 (N844, N834, N835);
nor NOR2_348 (N845, N334, N836);
not NOT1_349 (N846, N837);
not NOT1_350 (N847, N838);
not NOT1_351 (N848, N839);
and AND2_352 (N849, N735, N841);
buf BUFF1_353 (d850, N840);
and AND2_354 (N851, d219, N842);
and AND2_355 (N852, d219, N843);
and AND2_356 (N853, d219, N844);
nand NAND3_357 (N854, N845, N772, N696);
not NOT1_358 (N855, N846);
not NOT1_359 (N856, N847);
not NOT1_360 (N857, N848);
not NOT1_361 (N858, N849);
nor NOR2_362 (N859, N417, N851);
nor NOR2_363 (N860, N332, N852);
nor NOR2_364 (N861, N333, N853);
not NOT1_365 (N862, N854);
buf BUFF1_366 (d863, N855);
buf BUFF1_367 (d864, N856);
buf BUFF1_368 (d865, N857);
buf BUFF1_369 (d866, N858);
nand NAND3_370 (N867, N859, N769, N669);
nand NAND3_371 (N868, N860, N770, N677);
nand NAND3_372 (N869, N861, N771, N686);
not NOT1_373 (N870, N862);
not NOT1_374 (N871, N867);
not NOT1_375 (N872, N868);
not NOT1_376 (N873, N869);
buf BUFF1_377 (d874, N870);
not NOT1_378 (N875, N871);
not NOT1_379 (N876, N872);
not NOT1_380 (N877, N873);
buf BUFF1_381 (d878, N875);
buf BUFF1_382 (d879, N876);
buf BUFF1_383 (d880, N877);


// D Flip-Flops in front of input	
	dff a1  (d1, N1, clk);
	dff a2  (d8, N8, clk);
	dff a3  (d13, N13, clk);
	dff a4  (d17, N17, clk);
	dff a5  (d26, N26, clk);
	dff a6  (d29, N29, clk);
	dff a7  (d36, N36, clk);
	dff a8  (d42, N42, clk);
	dff a9  (d51, N51, clk);
	dff a10 (d55, N55, clk);
	dff a11 (d59, N59, clk);
	dff a12 (d68, N68, clk);
	dff a13 (d72, N72, clk);
	dff a14 (d73, N73, clk);
	dff a15 (d74, N74, clk);
	dff a16 (d75, N75, clk);
	dff a17 (d80, N80, clk);
	dff a18 (d85, N85, clk);
	dff a19 (d86, N86, clk);	
	dff a20 (d87, N87, clk);
	dff a21 (d88, N88, clk);
	dff a22 (d89, N89, clk);
	dff a23 (d90, N90, clk);
	dff a24 (d91, N91, clk);
	dff a25 (d96, N96, clk);	
	dff a26 (d101, N101, clk); 	
	dff a27 (d106, N106, clk);	
	dff a28 (d111, N111, clk);
	dff a29 (d116, N116, clk);	
	dff a30 (d121, N121, clk); 	
	dff a31 (d126, N126, clk);	
	dff a32 (d130, N130, clk);
	dff a33 (d135, N135, clk);	
	dff a34 (d138, N138, clk);
	dff a35 (d143, N143, clk);	
	dff a36 (d146, N146, clk); 	
	dff a37 (d149, N149, clk);	
	dff a38 (d152, N152, clk);
	dff a39 (d153, N153, clk);	
	dff a40 (d156, N156, clk);
	dff a41 (d159, N159, clk);
	dff a42 (d165, N165, clk);
	dff a43 (d171, N171, clk);	
	dff a44 (d177, N177, clk); 	
	dff a45 (d183, N183, clk);	
	dff a46 (d189, N189, clk);
	dff a47 (d195, N195, clk);	
	dff a48 (d201, N201, clk); 
	dff a49 (d207, N207, clk);	
	dff a50 (d210, N210, clk);
	dff a51 (d219, N219, clk);
	dff a52 (d228, N228, clk);
	dff a53 (d237, N237, clk);	
	dff a54 (d246, N246, clk); 	
	dff a55 (d255, N255, clk);	
	dff a56 (d259, N259, clk);
	dff a57 (d260, N260, clk);	
	dff a58 (d261, N261, clk); 
	dff a59 (d267, N267, clk);	
	dff a60 (d268, N268, clk);
	
	
// D Flip-Flops after output
	dff b1  (N388, d388, clk);
	dff b2  (N389, d389, clk);
	dff b3  (N390, d390, clk);
	dff b4  (N391, d391, clk);
	dff b5  (N418, d418, clk); 
	dff b6  (N419, d419, clk);
	dff b7  (N420, d420, clk);
	dff b8  (N421, d421, clk);
	dff b9  (N422, d422, clk);
	dff b10 (N423, d423, clk);
	dff b11 (N446, d446, clk);
	dff b12 (N447, d447, clk);
	dff b13 (N448, d448, clk);
	dff b14 (N449, d449, clk);
	dff b15 (N450, d450, clk);
	dff b16 (N767, d767, clk);
	dff b17 (N768, d768, clk);
	dff b18 (N850, d850, clk);
	dff b19 (N863, d863, clk);	
	dff b20 (N864, d864, clk);
	dff b21 (N865, d865, clk);
	dff b22 (N866, d866, clk);
	dff b23 (N874, d874, clk);
	dff b24 (N878, d878, clk);
	dff b25 (N879, d879, clk);	
	dff b26 (N880, d880, clk);
endmodule

module dff(q, d, clk);
	input  d, clk;
	output reg q;

always @ (posedge clk)
	q <= d;
	
endmodule

//------------------------------------------------------------------------------------------------------------------------------------------------------
//---------------------------------------------------------------------------------------------------------------------------------------------------
`timescale 1ns/ 1ps

module Testbench_benchmarkc880();

reg en, clk, N1, N8, N13, N17, N26, N29, N36, N42, N51, N55, N59, N68, N72, N73, N74, N75, N80, N85, N86, N87, N88, N89, N90, N91, N96, N101, N106, N111, N116, N121, N126, N130, N135, N138, N143, N146, N149, N152, N153, N156, N159, N165, N171, N177, N183, N189, N195, N201, N207, N210, N219, N228, N237, N246, N255, N259, N260, N261, N267, N268;

wire N388, N389, N390, N391, N418, N419, N420, N421, N422, N423, N446, N447, N448, N449, N450, N767, N768, N850, N863, N864, N865, N866, N874, N878, N879, N880;
 
 //instantiation
c880 dut(
//input port mapping
	.clk(clk),
	.en(en),
	.N1(N1), 
	.N8(N8),
	.N13(N13),
	.N17(N17),
	.N26(N26), 
	.N29(N29),
	.N36(N36),
	.N42(N42),
	.N51(N51),
	.N55(N55),
	.N59(N59),
	.N68(N68),
	.N72(N72),
	.N73(N73),
	.N74(N74), 
	.N75(N75),
	.N80(N80),
	.N85(N85),
	.N86(N86),
	.N87(N87),
	.N88(N88),
	.N89(N89),
	.N90(N90),
	.N91(N91),
	.N96(N96),
	.N101(N101),
	.N106(N106),
	.N111(N111),
	.N116(N116),
	.N121(N121),
	.N126(N126),
	.N130(N130),
	.N135(N135),
	.N138(N138),
	.N143(N143),
	.N146(N146),
	.N149(N149),
	.N152(N152),
	.N153(N153),
	.N156(N156),
	.N159(N159),
	.N165(N165),
	.N171(N171),
	.N177(N177),
	.N183(N183),
	.N189(N189),
	.N195(N195),
	.N201(N201),
	.N207(N207),
	.N210(N210),
	.N219(N219),
	.N228(N228),
	.N237(N237),
	.N246(N246),
	.N255(N255),
	.N259(N259),
	.N260(N260),
	.N261(N261),
	.N267(N267),
	.N268(N268),
	
//output port mapping	
	.N388(N388),  
	.N389(N389),
	.N390(N390),
	.N391(N391),
	.N418(N418),
	.N419(N419),
	.N420(N420),
	.N421(N421),
	.N422(N422),
	.N423(N423),
	.N446(N446),
	.N447(N447),
	.N448(N448),
	.N449(N449),
	.N450(N450),
	.N767(N767),
	.N768(N768),
	.N850(N850),
	.N863(N863),
	.N864(N864),
	.N865(N865),
	.N866(N866),
	.N874(N874),
	.N878(N878),
	.N879(N879),
	.N880(N880)
);
   

initial begin
	clk = 0; en = 0; 
	//COMBINATION
   N1=1; N8=1; N13=1; N17=1; N26=1; N29=0; N36=1; N42=1; N51=0; N55=1; N59=0; N68=1; N72=1; N73=1; N74=1; N75=1; N80=1; N85=0; N86=1; N87=0; N88=1; N89=1; N90=1; N91=1; N96=1; N101=1; N106=1; N111=1; N116=1; N121=1; N126=1; N130=1; N135=1; N138=1; N143=1; N146=0; N149=1; N152=1; N153=0; N156=1; N159=0; N165=0; N171=0; N177=0; N183=1; N189=0; N195=1; N201=1; N207=0; N210=0; N219=1; N228=0; N237=1; N246=0; N255=0; N259=1; N260=0; N261=1; N267=0; N268=1;
	//$dumpfile ("c880.vcd"); 
	//$dumpvars(0,Testbench_benchmarkc880);

end

	always @ (posedge clk)
		$display("%3d,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b,%1b", $time,N1,N8,N13,N17,N26,N29,N36,N42,N51,N55,N59,N68,N72,N73,N74,N75,N80,N85,N86,N87,N88,N89,N90,N91,N96,N101,N106,N111,N116,N121,N126,N130,N135,N138,N143,N146,N149,N152,N153,N156,N159,N165,N171,N177,N183,N189,N195,N201,N207,N210,N219,N228,N237,N246,N255,N259,N260,N261,N267,N268,en,N388,N389,N390,N391,N418,N419,N420,N421,N422,N423,N446,N447,N448,N449,N450,N767,N768,N850,N863,N864,N865,N866,N874,N878,N879,N880);
		
	initial begin
		#0.4 en = 0;
	end

	always
		#1 clk = ~clk;
	always
		#524288 N1 = ~N1;
	always
		#524288 N8 = ~N8;
	always
		#1048576 N13 = ~N13;
	always
		#2097152 N17 = ~N17;
	always
		#4194304 N26 = ~N26;
	always 
		#8388608 N29 = ~N29;
	always
		#16777216 N36 = ~N36;
	always
		#33554432 N42 = ~N42;
	always
		#67108864 N51 = ~N51;
	always
		#134217728 N55 = ~N55;
	always
		#268435456 N59 = ~N59;
	always
		#268435456 N68 = ~N68;
	always
		#536870912 N72 = ~N72;
	always
		#1073741824 N73 = ~N73;
	always
		#2147483648 N74 = ~N74; 
	always
		#4294967296 N75 = ~N75;
	always
		#8589934592 N80 = ~N80;
	always
		#17179869184 N85 = ~N85;
	always
		#34359738368 N86 = ~N86;
	always
		#68719476735 N87 = ~N87;
	always
		#137438953470 N88 = ~N88;
	always
		#274877906940 N89 = ~N89;
	always
		#274877906940 N90 = ~N90;
	always
		#137438953470 N91 = ~N91;
	always
		#68719476735 N96 = ~N96;
	always
		#34359738368 N101 = ~N101;
	always
		#17179869184 N106 = ~N106;
	always
		#8589934592 N111 = ~N111;
	always
		#4294967296 N116 = ~N116;
	always
		#2147483648 N121 = ~N121;
	always
		#1073741824 N126 = ~N126;
	always
		#536870912 N130 = ~N130;
	always
		#268435456 N135 = ~N135;
	always
		#134217728 N138 = ~N138;
	always
		#67108864 N143 = ~N143;
	always
		#33554432 N146 = ~N146;
	always
		#16777216 N149 = ~N149;
	always
		#8388608 N152 = ~N152;
	always
		#4194304 N153 = ~N153;
	always
		#2097152 N156 = ~N156;
	always
		#1048576 N159 = ~N159;
	always
		#524288 N165 = ~N165;
	always
		#262144 N171 = ~N171;
	always
		#131072 N177 = ~N177;
	always
		#65536 N183 = ~N183;
	always
		#32768 N189 = ~N189;
	always
		#16384 N195 = ~N195;
	always
		#8192 N201 = ~N201;
	always
		#4096 N207 = ~N207;
	always
		#2048 N210 = ~N210;
	always
		#1024 N219 = ~N219;
	always
		#512 N228 = ~N228;
	always
		#256 N237 = ~N237;
	always
		#128 N246 = ~N246;
	always
		#64 N255 = ~N255;
	always
		#32 N259 = ~N259;
	always
		#16 N260 = ~N260;
	always
		#8 N261 = ~N261;
	always
		#4 N267 = ~N267;
	always
		#2 N268 = ~N268;		

	initial #1024 $finish;
endmodule