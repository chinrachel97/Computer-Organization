// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/div.asm

// Divides R0 by R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

	@R2
	M = 0	//initialize R2=0
(WHILE)
	@R1
	D = M	//get R1
	@R0	
	M=M-D	//R0=R0-R1
	D = M	//get R0
	@END	
	D; JLT	//jump to END if R0<0, don't increment
	@R2
	M = M+1	//otherwise ++R2 and continue the loop
	@WHILE
	0; JMP
(END)
	@END
	0; JMP