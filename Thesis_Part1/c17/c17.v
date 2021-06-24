module c17 (N1, N2, N3, N6, N7, N22, N23, clk, en);

input N1, N2, N3, N6, N7, clk, en;

output N22, N23;

wire N10, N11, N16, N19, d1, d2, d3, d6, d7, d22, d23, error;

nand NAND2_1 (N10, d1, d3);
nand NAND2_2 (N11, d3, d6);
nand NAND2_3 (N16, d2, N11);
nand NAND2_4 (N19, N11, d7);
nand NAND2_5 (d22, N10, N16);
nand NAND2_6 (d23, N16, N19);

dff a1 (d1, N1, clk);
dff a2 (d2, N2, clk);
dff a3 (d3, N3, clk);
dff a4 (d6, N6, clk);
dff a5 (d7, N7, clk);
dff a6 (N22, d22, clk);
dff a7 (N23, d23, clk);


endmodule

module dff(q, d, clk);
	input  d, clk;
	output reg q;

always @ (posedge clk)
	q <= d;
endmodule


`timescale 1ns/ 1ps

module Testbench_benchmark1();
 reg N1, N2, N3, N6, N7, clk, en;
 wire N22, N23;

 //instantiation
c17 dut(
    .N1(N1),
    .N2(N2),
    .N3(N3),
	.N6(N6),
    .N7(N7),
    .N22(N22),
	.N23(N23),
	.clk(clk),
	.en(en)
   );
   
    initial begin
	 clk = 0; N1 = clk; N2 = clk; N3 = clk; N6 = clk; N7 = clk; en = 0;
	 //$dumpfile ("goldenc17.vcd"); 
	 //$dumpvars(0,Testbench_benchmark1);
	end
	
	always @ (posedge clk)
		$display("%3d, %1b, %1b, %1b, %1b, %1b, %1b, %1b, %1b", $time, N1, N2, N3, N6, N7, en, N22, N23);
		
	initial begin
		#0.4 en = 0;
	end
	
		always
		#1 clk = ~clk;
	always 
		#5 N1 = ~N1;
	always 
		#4 N2 = ~N2;
	always
		#3 N3 = ~N3;
	always 
		#2 N6 = ~N6;
	always
		#1 N7 = ~N7;		

	initial #16384 $finish;
endmodule