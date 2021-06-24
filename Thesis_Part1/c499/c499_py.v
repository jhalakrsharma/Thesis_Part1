// c499
// Ninputs 41 // Noutputs 32
// NtotalGates= 202 // XOR2=104 // AND2=40 // NOT1=40 // AND4=8 // OR4=2 // AND5=8

module c499 (N1,N5,N9,N13,N17,N21,N25,N29,N33,N37,N41,N45,N49,N53,N57,N61,N65,N69,N73,N77,N81,N85,N89,N93,N97,N101,N105,N109,N113,N117,
             N121,N125,N129,N130,N131,N132,N133,N134,N135,N136,N137,N724,N725,N726,N727,N728,N729,N730,N731,N732,N733,N734,N735,N736,N737,
             N738,N739,N740,N741,N742,N743,N744,N745,N746,N747,N748,N749,N750,N751,N752,N753,N754,N755, clk, en);

input en, clk, N1, N5, N9, N13, N17, N21, N25, N29, N33, N37, N41, N45, N49, N53, N57, N61, N65, N69, N73, N77, N81, N85, N89, N93, N97, N101, N105, N109, N113, N117, N121, N125, N129, N130, N131, N132, N133, N134, N135, N136, N137;

output N724, N725, N726, N727, N728, N729, N730, N731, N732, N733, N734, N735, N736, N737, N738, N739, N740, N741, N742, N743, N744, N745, N746, N747, N748, N749, N750, N751, N752, N753, N754, N755;

wire error, N250, N251, N252, N253, N254, N255, N256, N257, N258, N259, N260, N261, N262, N263, N264, N265, N266, N267, N268, N269, N270, N271, N272, N273, N274, N275, N276, N277, N278, N279, N280, N281, N282, N283, N284, N285, N286, N287, N288, N289, N290, N293, N296, N299, N302, N305, N308, N311, N314, N315, N316, N317, N318, N319, N320, N321, N338, N339, N340, N341, N342, N343, N344, N345, N346, N347, N348, N349, N350, N351, N352, N353, N354, N367, N380, N393, N406, N419, N432, N445, N554, N555, N556, N557, N558, N559, N560, N561, N562, N563, N564, N565, N566, N567, N568, N569, N570, N571, N572, N573, N574, N575, N576, N577, N578, N579, N580, N581, N582, N583, N584, N585, N586, N587, N588, N589, N590, N591, N592, N593, N594, N595, N596, N597, N598, N599, N600, N601, N602, N607, N620, N625, N630, N635, N640, N645, N650, N655, N692, N693, N694, N695, N696, N697, N698, N699, N700, N701, N702, N703, N704, N705, N706, N707, N708, N709, N710, N711, N712, N713, N714, N715, N716, N717, N718, N719, N720, N721, N722, N723, d1, d5, d9, d13, d17, d21, d25, d29, d33, d37, d41, d45, d49, d53, d57, d61, d65, d69, d73, d77, d81, d85, d89, d93, d97, d101, d105, d109, d113, d117, d121, d125, d129, d130, d131, d132, d133, d134, d135, d136, d137, d724, d725, d726, d727, d728, d729, d730, d731, d732, d733, d734, d735, d736, d737, d738, d739, d740, d741, d742, d743, d744, d745, d746, d747, d748, d749, d750, d751, d752, d753, d754, d755;

xor XOR2_1 (N250, d1, d5);
xor XOR2_2 (N251, d9, d13);
xor XOR2_3 (N252, d17, d21);
xor XOR2_4 (N253, d25, d29);
xor XOR2_5 (N254, d33, d37);
xor XOR2_6 (N255, d41, d45);
xor XOR2_7 (N256, d49, d53);
xor XOR2_8 (N257, N57, N61);
xor XOR2_9 (N258, d65, d69);
xor XOR2_10 (N259, d73, d77);
xor XOR2_11 (N260, d81, d85);
xor XOR2_12 (N261, d89, d93);
xor XOR2_13 (N262, d97, d101);
xor XOR2_14 (N263, d105, d109);
xor XOR2_15 (N264, d113, d117);
xor XOR2_16 (N265, d121, d125);
and AND2_17 (N266, d129, d137);
and AND2_18 (N267, d130, d137);
and AND2_19 (N268, d131, d137);
and AND2_20 (N269, d132, d137);
and AND2_21 (N270, d133, d137);
and AND2_22 (N271, d134, d137);
and AND2_23 (N272, d135, d137);
and AND2_24 (N273, d136, d137);
xor XOR2_25 (N274, d1, d17);
xor XOR2_26 (N275, d33, d49);
xor XOR2_27 (N276, d5, d21);
xor XOR2_28 (N277, d37, d53);
xor XOR2_29 (N278, d9, d25);
xor XOR2_30 (N279, d41, d57);
xor XOR2_31 (N280, d13, d29);
xor XOR2_32 (N281, d45, d61);
xor XOR2_33 (N282, d65, d81);
xor XOR2_34 (N283, d97, d113);
xor XOR2_35 (N284, d69, d85);
xor XOR2_36 (N285, d101, d117);
xor XOR2_37 (N286, d73, d89);
xor XOR2_38 (N287, d105, d121);
xor XOR2_39 (N288, d77, d93);
xor XOR2_40 (N289, d109, d125);

xor XOR2_41 (N290, N250, N251);
xor XOR2_42 (N293, N252, N253);
xor XOR2_43 (N296, N254, N255);
xor XOR2_44 (N299, N256, N257);
xor XOR2_45 (N302, N258, N259);
xor XOR2_46 (N305, N260, N261);
xor XOR2_47 (N308, N262, N263);
xor XOR2_48 (N311, N264, N265);
xor XOR2_49 (N314, N274, N275);
xor XOR2_50 (N315, N276, N277);
xor XOR2_51 (N316, N278, N279);
xor XOR2_52 (N317, N280, N281);
xor XOR2_53 (N318, N282, N283);
xor XOR2_54 (N319, N284, N285);
xor XOR2_55 (N320, N286, N287);
xor XOR2_56 (N321, N288, N289);
xor XOR2_57 (N338, N290, N293);
xor XOR2_58 (N339, N296, N299);
xor XOR2_59 (N340, N290, N296);
xor XOR2_60 (N341, N293, N299);
xor XOR2_61 (N342, N302, N305);
xor XOR2_62 (N343, N308, N311);
xor XOR2_63 (N344, N302, N308);
xor XOR2_64 (N345, N305, N311);
xor XOR2_65 (N346, N266, N342);
xor XOR2_66 (N347, N267, N343);
xor XOR2_67 (N348, N268, N344);
xor XOR2_68 (N349, N269, N345);
xor XOR2_69 (N350, N270, N338);
xor XOR2_70 (N351, N271, N339);
xor XOR2_71 (N352, N272, N340);
xor XOR2_72 (N353, N273, N341);
xor XOR2_73 (N354, N314, N346);
xor XOR2_74 (N367, N315, N347);
xor XOR2_75 (N380, N316, N348);
xor XOR2_76 (N393, N317, N349);
xor XOR2_77 (N406, N318, N350);
xor XOR2_78 (N419, N319, N351);
xor XOR2_79 (N432, N320, N352);
xor XOR2_80 (N445, N321, N353);

not NOT1_81 (N554, N354);
not NOT1_82 (N555, N367);
not NOT1_83 (N556, N380);
not NOT1_84 (N557, N354);
not NOT1_85 (N558, N367);
not NOT1_86 (N559, N393);
not NOT1_87 (N560, N354);
not NOT1_88 (N561, N380);
not NOT1_89 (N562, N393);
not NOT1_90 (N563, N367);
not NOT1_91 (N564, N380);
not NOT1_92 (N565, N393);
not NOT1_93 (N566, N419);
not NOT1_94 (N567, N445);
not NOT1_95 (N568, N419);
not NOT1_96 (N569, N432);
not NOT1_97 (N570, N406);
not NOT1_98 (N571, N445);
not NOT1_99 (N572, N406);
not NOT1_100 (N573, N432);
not NOT1_101 (N574, N406);
not NOT1_102 (N575, N419);
not NOT1_103 (N576, N432);
not NOT1_104 (N577, N406);
not NOT1_105 (N578, N419);
not NOT1_106 (N579, N445);
not NOT1_107 (N580, N406);
not NOT1_108 (N581, N432);
not NOT1_109 (N582, N445);
not NOT1_110 (N583, N419);
not NOT1_111 (N584, N432);
not NOT1_112 (N585, N445);
not NOT1_113 (N586, N367);
not NOT1_114 (N587, N393);
not NOT1_115 (N588, N367);
not NOT1_116 (N589, N380);
not NOT1_117 (N590, N354);
not NOT1_118 (N591, N393);
not NOT1_119 (N592, N354);
not NOT1_120 (N593, N380);
and AND4_121 (N594, N554, N555, N556, N393);
and AND4_122 (N595, N557, N558, N380, N559);
and AND4_123 (N596, N560, N367, N561, N562);
and AND4_124 (N597, N354, N563, N564, N565);
and AND4_125 (N598, N574, N575, N576, N445);
and AND4_126 (N599, N577, N578, N432, N579);
and AND4_127 (N600, N580, N419, N581, N582);
and AND4_128 (N601, N406, N583, N584, N585);
or OR4_129 (N602, N594, N595, N596, N597);
or OR4_130 (N607, N598, N599, N600, N601);
and AND5_131 (N620, N406, N566, N432, N567, N602);
and AND5_132 (N625, N406, N568, N569, N445, N602);
and AND5_133 (N630, N570, N419, N432, N571, N602);
and AND5_134 (N635, N572, N419, N573, N445, N602);
and AND5_135 (N640, N354, N586, N380, N587, N607);
and AND5_136 (N645, N354, N588, N589, N393, N607);
and AND5_137 (N650, N590, N367, N380, N591, N607);
and AND5_138 (N655, N592, N367, N593, N393, N607);
and AND2_139 (N692, N354, N620);
and AND2_140 (N693, N367, N620);
and AND2_141 (N694, N380, N620);
and AND2_142 (N695, N393, N620);
and AND2_143 (N696, N354, N625);
and AND2_144 (N697, N367, N625);
and AND2_145 (N698, N380, N625);
and AND2_146 (N699, N393, N625);
and AND2_147 (N700, N354, N630);
and AND2_148 (N701, N367, N630);
and AND2_149 (N702, N380, N630);
and AND2_150 (N703, N393, N630);
and AND2_151 (N704, N354, N635);
and AND2_152 (N705, N367, N635);
and AND2_153 (N706, N380, N635);
and AND2_154 (N707, N393, N635);
and AND2_155 (N708, N406, N640);
and AND2_156 (N709, N419, N640);
and AND2_157 (N710, N432, N640);
and AND2_158 (N711, N445, N640);
and AND2_159 (N712, N406, N645);
and AND2_160 (N713, N419, N645);
and AND2_161 (N714, N432, N645);
and AND2_162 (N715, N445, N645);
and AND2_163 (N716, N406, N650);
and AND2_164 (N717, N419, N650);
and AND2_165 (N718, N432, N650);
and AND2_166 (N719, N445, N650);
and AND2_167 (N720, N406, N655);
and AND2_168 (N721, N419, N655);
and AND2_169 (N722, N432, N655);
and AND2_170 (N723, N445, N655);

xor XOR2_171 (d724, d1, N692);
xor XOR2_172 (d725, d5, N693);
xor XOR2_173 (d726, d9, N694);
xor XOR2_174 (d727, d13, N695);
xor XOR2_175 (d728, d17, N696);
xor XOR2_176 (d729, d21, N697);
xor XOR2_177 (d730, d25, N698);
xor XOR2_178 (d731, d29, N699);
xor XOR2_179 (d732, d33, N700);
xor XOR2_180 (d733, d37, N701);
xor XOR2_181 (d734, d41, N702);
xor XOR2_182 (d735, d45, N703);
xor XOR2_183 (d736, d49, N704);
xor XOR2_184 (d737, d53, N705);
xor XOR2_185 (d738, d57, N706);
xor XOR2_186 (d739, d61, N707);
xor XOR2_187 (d740, d65, N708);
xor XOR2_188 (d741, d69, N709);
xor XOR2_189 (d742, d73, N710);
xor XOR2_190 (d743, d77, N711);
xor XOR2_191 (d744, d81, N712);
xor XOR2_192 (d745, d85, N713);
xor XOR2_193 (d746, d89, N714);
xor XOR2_194 (d747, d93, N715);
xor XOR2_195 (d748, d97, N716);
xor XOR2_196 (d749, d101, N717);
xor XOR2_197 (d750, d105, N718);
xor XOR2_198 (d751, d109, N719);
xor XOR2_199 (d752, d113, N720);
xor XOR2_200 (d753, d117, N721);
xor XOR2_201 (d754, d121, N722);
xor XOR2_202 (d755, d125, N723);

//input Flip-flops
dff a1 (d1, N1, clk);
dff a2 (d5, N5, clk);
dff a3 (d9, N9, clk);
dff a4 (d13, N13, clk);
dff a5 (d17, N17, clk);
dff a6 (d21, N21, clk);
dff a7 (d25, N25, clk);
dff a8 (d29, N29, clk);
dff a9 (d33, N33, clk);
dff a10 (d37, N37, clk);
dff a11 (d41, N41, clk);
dff a12 (d45, N45, clk);
dff a13 (d49, N49, clk);
dff a14 (d53, N53, clk);
dff a15 (d57, N57, clk);
dff a16 (d61, N61, clk);
dff a17 (d65, N65, clk);
dff a18 (d69, N69, clk);
dff a19 (d73, N73, clk);
dff a20 (d77, N77, clk);
dff a21 (d81, N81, clk);
dff a22 (d85, N85, clk);
dff a23 (d89, N89, clk);
dff a24 (d93, N93, clk);
dff a25 (d97, N97, clk);
dff a26 (d101, N101, clk);
dff a27 (d105, N105, clk);
dff a28 (d109, N109, clk);
dff a29 (d113, N113, clk);
dff a30 (d117, N117, clk);
dff a31 (d121, N121, clk);
dff a32 (d125, N125, clk);
dff a33 (d129, N129, clk);
dff a34 (d130, N130, clk);
dff a35 (d131, N131, clk);
dff a36 (d132, N132, clk);
dff a37 (d133, N133, clk);
dff a38 (d134, N134, clk);
dff a39 (d135, N135, clk);
dff a40 (d136, N136, clk);
dff a41 (d137, N137, clk);
//output Flip-flops
dff o1 (N724, d724, clk);
dff o2 (N725, d725, clk);
dff o3 (N726, d726, clk);
dff o4 (N727, d727, clk);
dff o5 (N728, d728, clk);
dff o6 (N729, d729, clk);
dff o7 (N730, d730, clk);
dff o8 (N731, d731, clk);
dff o9 (N732, d732, clk);
dff o10 (N733, d733, clk);
dff o11 (N734, d734, clk);
dff o12 (N735, d735, clk);
dff o13 (N736, d736, clk);
dff o14 (N737, d737, clk);
dff o15 (N738, d738, clk);
dff o16 (N739, d739, clk);
dff o17 (N740, d740, clk);
dff o18 (N741, d741, clk);
dff o19 (N742, d742, clk);
dff o20 (N743, d743, clk);
dff o21 (N744, d744, clk);
dff o22 (N745, d745, clk);
dff o23 (N746, d746, clk);
dff o24 (N747, d747, clk);
dff o25 (N748, d748, clk);
dff o26 (N749, d749, clk);
dff o27 (N750, d750, clk);
dff o28 (N751, d751, clk);
dff o29 (N752, d752, clk);
dff o30 (N753, d753, clk);
dff o31 (N754, d754, clk);
dff o32 (N755, d755, clk);



endmodule

module dff(q, d, clk);
	input  d, clk;
	output reg q;

always @ (posedge clk)
	q <= d;
	
endmodule


`timescale 1ns/ 1ps

module Testbench_benchmark3();
 reg N1, N5, N9, N13, N17, N21, N25, N29, N33, N37, N41, N45, N49, N53, N57, N61, N65, N69, N73, N77, N81, N85,
	 N89, N93, N97, N101, N105, N109, N113, N117, N121, N125, N129, N130, N131, N132, N133, N134, N135, N136, N137, clk, en;
	 
 wire N724, N725, N726, N727, N728, N729, N730, N731, N732, N733, N734, N735, N736, N737, N738, N739, N740, N741, N742, N743,
	  N744, N745, N746, N747, N748, N749, N750, N751, N752, N753, N754, N755;

 //instantiation
c499 dut(
//input port mapping
    .N1(N1),
    .N5(N5),
    .N9(N9),
	.N13(N13),
    .N17(N17),
    .N21(N21),
	.N25(N25),
    .N29(N29),
    .N33(N33),
    .N37(N37),
	.N41(N41),
    .N45(N45),
    .N49(N49),
	.N53(N53),
    .N57(N57),
    .N61(N61),
    .N65(N65),
	.N69(N69),
    .N73(N73),
    .N77(N77),
	.N81(N81),
    .N85(N85),
    .N89(N89),
    .N93(N93),
	.N97(N97),
    .N101(N101),
    .N105(N105),
	.N109(N109),
    .N113(N113),
    .N117(N117),
    .N121(N121),
	.N125(N125),
    .N129(N129),
    .N130(N130),
	.N131(N131),
    .N132(N132),
    .N133(N133),
    .N134(N134),
	.N135(N135),
    .N136(N136),
    .N137(N137),
//output port mapping	
	.N724(N724),
    .N725(N725),
    .N726(N726),
    .N727(N727),
	.N728(N728),
    .N729(N729),
    .N730(N730),
	.N731(N731),
	.N732(N732),
    .N733(N733),
    .N734(N734),
    .N735(N735),
	.N736(N736),
    .N737(N737),
    .N738(N738),
	.N739(N739),
	.N740(N740),
    .N741(N741),
    .N742(N742),
    .N743(N743),
	.N744(N744),
    .N745(N745),
    .N746(N746),
	.N747(N747),
	.N748(N748),
    .N749(N749),
    .N750(N750),
    .N751(N751),
	.N752(N752),
    .N753(N753),
    .N754(N754),
	.N755(N755),	
	.clk(clk),
	.en(en)
   );
   
    initial begin
		clk = 0; N1=clk; N5=clk; N9=clk; N13=clk; N17=clk; N21=clk; N25=clk; N29=clk; N33=clk; N37=clk; 
		N41=clk; N45=clk; N49=clk; N53=clk; N57=clk; N61=clk; N65=clk; N69=clk; N73=clk; N77=clk; N81=clk; N85=clk; 
		N89=clk; N93=clk; N97=clk; N101=clk; N105=clk; N109=clk; N113=clk; N117=clk; N121=clk; N125=clk; N129=clk; 
		N130=clk; N131=clk; N132=clk; N133=clk; N134=clk; N135=clk; N136=clk; N137=clk; en = 0;
	 //$dumpfile ("goldenc17.vcd"); 
	 //$dumpvars(0,Testbench_benchmark1);
	end
	
	always @ (posedge clk)
		 $display(" %4d, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b,%1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b,%1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b",
             $time, N1, N5, N9, N13, N17, N21, N25, N29, N33, N37, N41, N45, N49, N53, N57, N61, N65, N69, N73, N77, N81, N85, N89, N93, N97, N101, N105, 
             N109, N113, N117, N121, N125, N129, N130, N131, N132, N133, N134, N135, N136, N137, en, N724, N725, N726, N727, N728, N729, N730, N731, 
             N732, N733, N734, N735, N736, N737, N738, N739, N740, N741, N742, N743, N744, N745, N746, N747, N748, N749, N750, N751, N752, N753, N754, 
             N755);
	initial begin
		#0.4 en = 0;
	end
	
	always
		#1 clk = ~clk;
	always 
		#4 N1 = ~N1;
	always 
		#3 N5 = ~N5;
	always 
		#5 N9 = ~N9;
	always 
		#2 N13 = ~N13;
	always 
		#1 N17 = ~N17;
	always 
		#4 N21 = ~N21;
	always 
		#3 N25 = ~N25;
	always 
		#2 N29 = ~N29;
	always 
		#6 N33 = ~N33;
	always 
		#1 N37 = ~N37;
	always 
		#7 N41 = ~N41;
	always 
		#3 N45 = ~N45;
	always 
		#5 N49 = ~N49;
	always 
		#2 N53 = ~N53;
	always 
		#9 N57 = ~N57;
	always 
		#1 N61 = ~N61;
	always 
		#6 N69 = ~N69;
	always 
		#9 N73 = ~N73;
	always 
		#2 N77 = ~N77;
	always 
		#5 N81 = ~N81;
	always 
		#4 N85 = ~N85;
	always 
		#3 N89 = ~N89;
	always 
		#1 N93 = ~N93;
	always 
		#5 N97 = ~N97;
	always 
		#1 N101 = ~N101;
	always 
		#8 N105 = ~N105;
	always 
		#3 N109 = ~N109;
	always 
		#6 N113 = ~N113;
	always 
		#2 N117 = ~N117;
	always 
		#5 N121 = ~N121;
	always 
		#9 N125 = ~N125;
	always 
		#3 N129 = ~N129;
	always 
		#8 N130 = ~N130;
	always 
		#2 N131 = ~N131;
	always 
		#7 N132 = ~N132;
	always 
		#2 N133 = ~N133;
	always 
		#6 N134 = ~N134;
	always 
		#3 N135 = ~N135;
	always 
		#1 N136 = ~N136;
	always 
		#5 N137 = ~N137;		

	initial #1024 $finish;
endmodule