//c432, input = 36, output = 7

module c432 (en, clk, N1, N4, N8, N11, N14, N17, N21, N24, N27, N30, N34, N37, N40, N43, N47, N50, N53, N56, N60, N63, N66, N69, N73, N76, N79, N82, N86, N89, 
			 N92, N95, N99, N102, N105, N108, N112, N115,N223, N329, N370, N421, N430, N431, N432);

input en, clk, N1, N4, N8, N11, N14, N17, N21, N24, N27, N30, N34, N37, N40, N43, N47, N50, N53, N56, N60, N63, N66, N69, N73, N76, N79, N82, N86, N89, N92, N95, N99, N102, N105, N108, N112, N115;

output N223, N329, N370, N421, N430, N431, N432;

wire error, d223, d329, d370, d421, d430, d431, d432, d1, d4, d8, d11, d14, d17, d21, d24, d27, d30, d34, d37, d40, d43, d47, d50, d53, d56, d60, d63, 
d66, d69, d73, d76, d79, d82, d86, d89, d92, d95, d99, d102, d105, d108, d112, d115, N118, N119, N122, N123, N126, N127, N130, N131, N134, N135, N138, 
N139, N142, N143, N146, N147, N150, N151, N154, N157, N158, N159, N162, N165, N168, N171, N174, N177, N180, N183, N184, N185, N186, N187, N188, N189, 
N190, N191, N192, N193, N194, N195, N196, N197, N198, N199, N203, N213, N224, N227, N230, N233, N236, N239, N242, N243, N246, N247, N250, N251, N254, 
N255, N256, N257, N258, N259, N260, N263, N264, N267, N270, N273, N276, N279, N282, N285, N288, N289, N290, N291, N292, N293, N294, N295, N296, N300, 
N301, N302, N303, N304, N305, N306, N307, N308, N309, N319, N330, N331, N332, N333, N334, N335, N336, N337, N338, N339, N340, N341, N342, N343, N344, 
N345, N346, N347, N348, N349, N350, N351, N352, N353, N354, N355, N356, N357, N360, N371, N372, N373, N374, N375, N376, N377, N378, N379, N380, N381, 
N386, N393, N399, N404, N407, N411, N414, N415, N416, N417, N418, N419, N420, N422, N425, N428, N429;

not NOT1_1 (N118, d1);
not NOT1_2 (N119, d4);
not NOT1_3 (N122, d11);
not NOT1_4 (N123, d17);
not NOT1_5 (N126, d24);
not NOT1_6 (N127, d30);
not NOT1_7 (N130, d37);
not NOT1_8 (N131, d43);
not NOT1_9 (N134, d50);
not NOT1_10 (N135, d56);
not NOT1_11 (N138, d63);
not NOT1_12 (N139, d69);
not NOT1_13 (N142, d76);
not NOT1_14 (N143, d82);
not NOT1_15 (N146, d89);
not NOT1_16 (N147, d95);
not NOT1_17 (N150, d102);
not NOT1_18 (N151, d108);
nand NAND2_19 (N154, N118, d4);
nor NOR2_20 (N157, d8, N119);
nor NOR2_21 (N158, d14, N119);
nand NAND2_22 (N159, N122, d17);
nand NAND2_23 (N162, N126, d30);
nand NAND2_24 (N165, N130, d43);
nand NAND2_25 (N168, N134, d56);
nand NAND2_26 (N171, N138, d69);
nand NAND2_27 (N174, N142, d82);
nand NAND2_28 (N177, N146, d95);
nand NAND2_29 (N180, N150, d108);
nor NOR2_30 (N183, d21, N123);
nor NOR2_31 (N184, d27, N123);
nor NOR2_32 (N185, d34, N127);
nor NOR2_33 (N186, d40, N127);
nor NOR2_34 (N187, d47, N131);
nor NOR2_35 (N188, d53, N131);
nor NOR2_36 (N189, d60, N135);
nor NOR2_37 (N190, d66, N135);
nor NOR2_38 (N191, d73, N139);
nor NOR2_39 (N192, d79, N139);
nor NOR2_40 (N193, d86, N143);
nor NOR2_41 (N194, d92, N143);
nor NOR2_42 (N195, d99, N147);
nor NOR2_43 (N196, d105, N147);
nor NOR2_44 (N197, d112, N151);
nor NOR2_45 (N198, d115, N151);
and AND9_46 (N199, N154, N159, N162, N165, N168, N171, N174, N177, N180);
not NOT1_47 (N203, N199);
not NOT1_48 (N213, N199);
not NOT1_49 (d223, N199);
xor XOR2_50 (N224, N203, N154);
xor XOR2_51 (N227, N203, N159);
xor XOR2_52 (N230, N203, N162);
xor XOR2_53 (N233, N203, N165);
xor XOR2_54 (N236, N203, N168);
xor XOR2_55 (N239, N203, N171);
nand NAND2_56 (N242, d1, N213);
xor XOR2_57 (N243, N203, N174);
nand NAND2_58 (N246, N213, d11);
xor XOR2_59 (N247, N203, N177);
nand NAND2_60 (N250, N213, d24);
xor XOR2_61 (N251, N203, N180);
nand NAND2_62 (N254, N213, d37);
nand NAND2_63 (N255, N213, d50);
nand NAND2_64 (N256, N213, d63);
nand NAND2_65 (N257, N213, d76);
nand NAND2_66 (N258, N213, d89);
nand NAND2_67 (N259, N213, d102);
nand NAND2_68 (N260, N224, N157);
nand NAND2_69 (N263, N224, N158);
nand NAND2_70 (N264, N227, N183);
nand NAND2_71 (N267, N230, N185);
nand NAND2_72 (N270, N233, N187);
nand NAND2_73 (N273, N236, N189);
nand NAND2_74 (N276, N239, N191);
nand NAND2_75 (N279, N243, N193);
nand NAND2_76 (N282, N247, N195);
nand NAND2_77 (N285, N251, N197);
nand NAND2_78 (N288, N227, N184);
nand NAND2_79 (N289, N230, N186);
nand NAND2_80 (N290, N233, N188);
nand NAND2_81 (N291, N236, N190);
nand NAND2_82 (N292, N239, N192);
nand NAND2_83 (N293, N243, N194);
nand NAND2_84 (N294, N247, N196);
nand NAND2_85 (N295, N251, N198);
and AND9_86 (N296, N260, N264, N267, N270, N273, N276, N279, N282, N285);
not NOT1_87 (N300, N263);
not NOT1_88 (N301, N288);
not NOT1_89 (N302, N289);
not NOT1_90 (N303, N290);
not NOT1_91 (N304, N291);
not NOT1_92 (N305, N292);
not NOT1_93 (N306, N293);
not NOT1_94 (N307, N294);
not NOT1_95 (N308, N295);
not NOT1_96 (N309, N296);
not NOT1_97 (N319, N296);
not NOT1_98 (d329, N296);
xor XOR2_99 (N330, N309, N260);
xor XOR2_100 (N331, N309, N264);
xor XOR2_101 (N332, N309, N267);
xor XOR2_102 (N333, N309, N270);
nand NAND2_103 (N334, d8, N319);
xor XOR2_104 (N335, N309, N273);
nand NAND2_105 (N336, N319, d21);
xor XOR2_106 (N337, N309, N276);
nand NAND2_107 (N338, N319, d34);
xor XOR2_108 (N339, N309, N279);
nand NAND2_109 (N340, N319, d47);
xor XOR2_110 (N341, N309, N282);
nand NAND2_111 (N342, N319, d60);
xor XOR2_112 (N343, N309, N285);
nand NAND2_113 (N344, N319, d73);
nand NAND2_114 (N345, N319, d86);
nand NAND2_115 (N346, N319, d99);
nand NAND2_116 (N347, N319, d112);
nand NAND2_117 (N348, N330, N300);
nand NAND2_118 (N349, N331, N301);
nand NAND2_119 (N350, N332, N302);
nand NAND2_120 (N351, N333, N303);
nand NAND2_121 (N352, N335, N304);
nand NAND2_122 (N353, N337, N305);
nand NAND2_123 (N354, N339, N306);
nand NAND2_124 (N355, N341, N307);
nand NAND2_125 (N356, N343, N308);
and AND9_126 (N357, N348, N349, N350, N351, N352, N353, N354, N355, N356);
not NOT1_127 (N360, N357);
not NOT1_128 (d370, N357);
nand NAND2_129 (N371, d14, N360);
nand NAND2_130 (N372, N360, d27);
nand NAND2_131 (N373, N360, d40);
nand NAND2_132 (N374, N360, d53);
nand NAND2_133 (N375, N360, d66);
nand NAND2_134 (N376, N360, d79);
nand NAND2_135 (N377, N360, d92);
nand NAND2_136 (N378, N360, d105);
nand NAND2_137 (N379, N360, d115);
nand NAND4_138 (N380, d4, N242, N334, N371);
nand NAND4_139 (N381, N246, N336, N372, d17);
nand NAND4_140 (N386, N250, N338, N373, d30);
nand NAND4_141 (N393, N254, N340, N374, d43);
nand NAND4_142 (N399, N255, N342, N375, d56);
nand NAND4_143 (N404, N256, N344, N376, d69);
nand NAND4_144 (N407, N257, N345, N377, d82);
nand NAND4_145 (N411, N258, N346, N378, d95);
nand NAND4_146 (N414, N259, N347, N379, d108);
not NOT1_147 (N415, N380);
and AND8_148 (N416, N381, N386, N393, N399, N404, N407, N411, N414);
not NOT1_149 (N417, N393);
not NOT1_150 (N418, N404);
not NOT1_151 (N419, N407);
not NOT1_152 (N420, N411);
nor NOR2_153 (d421, N415, N416);
nand NAND2_154 (N422, N386, N417);
nand NAND4_155 (N425, N386, N393, N418, N399);
nand NAND3_156 (N428, N399, N393, N419);
nand NAND4_157 (N429, N386, N393, N407, N420);
nand NAND4_158 (d430, N381, N386, N422, N399);
nand NAND4_159 (d431, N381, N386, N425, N428);
nand NAND4_160 (d432, N381, N422, N425, N429);

// D Flip-Flops in front of input	
	dff a1  (d1,  N1,  clk);
	dff a2  (d4,  N4,  clk);
	dff a3  (d8,  N8,  clk);
	dff a4  (d11, N11, clk);
	dff a5  (d14, N14, clk);
	dff a6  (d17, N17, clk);
	dff a7  (d21, N21, clk);
	dff a8  (d24, N24, clk);
	dff a9  (d27, N27, clk);
	dff a10 (d30, N30, clk); 	
	dff a11 (d34, N34, clk);	
	dff a12 (d37, N37, clk);
	dff a13 (d40, N40, clk);
	dff a14 (d43, N43, clk);
	dff a15 (d47, N47, clk);
	dff a16 (d50, N50, clk);
	dff a17 (d53, N53, clk);
	dff a18 (d56, N56, clk);
	dff a19 (d60, N60, clk);	
	dff a20 (d63, N63, clk);
	dff a21 (d66, N66, clk);
	dff a22 (d69, N69, clk);
	dff a23 (d73, N73, clk);
	dff a24 (d76, N76, clk);
	dff a25 (d79, N79, clk);	
	dff a26 (d82, N82, clk); 	
	dff a27 (d86, N86, clk);	
	dff a28 (d89, N89, clk);
	dff a29 (d92, N92, clk);	
	dff a30 (d95, N95, clk); 	
	dff a31 (d99, N99, clk);	
	dff a32 (d102, N102, clk);
	dff a33 (d105, N105, clk);	
	dff a34 (d108, N108, clk); 	
	dff a35 (d112, N112, clk);	
	dff a36 (d115, N115, clk);	

// D Flip-Flops after output
	dff b1 (N223, d223, clk);	
	dff b2 (N329, d329, clk);
	dff b3 (N370, d370, clk);
	dff b4 (N421, d421, clk);
	dff b5 (N430, d430, clk); 
	dff b6 (N431, d431, clk);
	dff b7 (N432, d432, clk);
	
endmodule

module dff(q, d, clk);
	input  d, clk;
	output reg q;

always @ (posedge clk)
	q <= d;
	
endmodule

//-------------------------------------------------------------------------------
//write test bench here

`timescale 1ns/ 1ps

module Testbench_c432();

reg clk, en, N1, N4, N8, N11, N14, N17, N21, N24, N27, N30, N34, N37, N40, N43, N47, N50, N53, N56, N60, N63, N66, N69, N73, N76, N79, N82, N86, N89, N92, N95, N99, N102, N105, N108, N112, N115;
wire N223, N329, N370, N421, N430, N431, N432;
 
 //instantiation
 c432 dut(
	.N1(N1),	
	.N4(N4),
	.N8(N8),
	.N11(N11),
	.N14(N14),
	.N17(N17),
	.N21(N21),
	.N24(N24),
	.N27(N27),
	.N30(N30),
	.N34(N34),
	.N37(N37),
	.N40(N40),
	.N43(N43),
	.N47(N47),
	.N50(N50),
	.N53(N53),
	.N56(N56),
	.N60(N60),
	.N63(N63),
	.N66(N66),
	.N69(N69),
	.N73(N73),
	.N76(N76),
	.N79(N79),
	.N82(N82),
	.N86(N86),
	.N89(N89),
	.N92(N92),
	.N95(N95),
	.N99(N99),
	.N102(N102),
	.N105(N105),
	.N108(N108),
	.N112(N112),	
	.N115(N115),
	.clk(clk),
	.en(en),	
//output port mapping	

	.N223(N223),
	.N329(N329),
	.N370(N370),
	.N421(N421),
	.N430(N430),
	.N431(N431),
	.N432(N432)
);

initial begin
	clk = 0; en = 0; N1=clk; N4=clk; N8=clk; N11=clk; N14=clk; N17=clk; N21=clk; N24=clk; N27=clk; N30=clk; N34=clk; N37=clk; N40=clk; N43=clk; 
	N47=clk; N50=clk; N53=clk; N56=clk; N60=clk; N63=clk; N66=clk; N69=clk; N73=clk; N76=clk; N79=clk; N82=clk; N86=clk; N89=clk; N92=clk; N95=clk; 
	N99=clk; N102=clk; N105=clk; N108=clk; N112=clk; N115=clk;

	//$dumpfile ("c432.vcd"); 
	//$dumpvars(0,Testbench_c432);
end

initial begin
	#0.4 en = 0;

end
	
always @ (posedge clk)
	$display("%3d, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b", $time, N1, N4, N8, N11, N14, N17, N21, N24, N27, N30, N34, N37, N40, N43, N47, N50, N53, N56, N60, N63, N66, N69, N73, N76, N79, N82, N86, N89, N92, N95, N99, N102, N105, N108, N112, N115, en, N223, N329, N370, N421, N430, N431, N432);
	
	always		#1 clk = ~clk;
	always		#36 N1 = ~N1;
	always		#35 N4 = ~N4;	
	always		#34 N8 = ~N8;
	always		#33 N11 = ~N11;
	always		#32 N14 = ~N14;
	always		#31 N17 = ~N17;
	always		#30 N21 = ~N21;
	always		#29 N24 = ~N24;
	always		#28 N27 = ~N27;
	always		#27 N30 = ~N30;
	always		#26 N34 = ~N34;
	always 
		#25 N37 = ~N37;
	always 
		#24 N40 = ~N40;
	always 
		#23 N43 = ~N43;
	always 
		#22 N47 = ~N47;
	always 
		#21 N50 = ~N50;
	always 
		#20 N53 = ~N53;
	always 
		#19 N56 = ~N56; 
	always 
		#18 N60 = ~N60;
	always 
		#17 N63 = ~N63;
	always 
		#16 N66 = ~N66;
	always 
		#15 N69 = ~N69;
	always 
		#14 N73 = ~N73;
	always 
		#13 N76 = ~N76;
	always 
		#12 N79 = ~N79;
	always 
		#11 N82 = ~N82;
	always 
		#10 N86 = ~N86;
	always 
		#9  N89 = ~N89;
	always 
		#8  N92 = ~N92;
	always 
		#7  N95 = ~N95;
	always 
		#6  N99 = ~N99;
	always 
		#5 N102 = ~N102;
	always 
		#4 N105 = ~N105;
	always 
		#3 N108 = ~N108;
	always 
		#2 N112 = ~N112;
	always 
		#1 N115 = ~N115;

initial #4096 $finish;

endmodule