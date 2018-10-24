//This asm computes the modulo of two numbers
//Assuming R0 stores the number a and R1 stores the number b (b can not be 0)
//so in normal programming language, the goal is to compute RAM[R0]%RAM[R1]
//The result will be put to RAM[R2]
//Assuming RAM[R1] is positive integer and RAM[R0] is non-negative integer
//write your code here.

//get R0

//set x = R0
//get R1

//keep doing x-R1 until x<R1

//return x

	@R0
	D = M	//get R0
	@x
	M = D	//set x to R0
(LOOP)
	@x
	D = M	//get x
	@R1
	D = D - M	//x-R1
	@END
	D; JLT	//jump to end if D<R1
	@x
	M = D	//otherwise, set x=x-R1
	@LOOP
	0; JMP
(END)
	@x
	D = M	//get x
	@R2
	M = D	//set result to x
	0; JMP