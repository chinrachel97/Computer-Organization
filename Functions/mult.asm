// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Do multiplication of R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

	@R2
	M = 0	//initialize result to 0
	@R0
	D = M	//get R0
	@counter
	M = D	//initialize counter to R0
	D = M	//get value of counter
	@END
	D; JLT	//jump to END if it's lesser than zero
(LOOP)
	@temp
	M = 1	//set temp to 1
	@counter
	D = M	//get value of counter
	@temp
	M = M < D	//shift temp by that many bits
	@R1
	D = M	//get R1
	@temp
	D = M & D	//set D to (R1 & temp)
	@DECREMENT
	D; JLE
(GETRS)
	@counter
	D = M	//get value of counter
	@R0
	D = M < D	//shift R0 by that many bitsS
	@R2
	M = M + D	
(DECREMENT)
	@counter
	M = M - 1	//decrement counter
	D = M	//get value of counter
	@LOOP
	D; JGE	//loop of counter >= 0
(END)
	0; JMP