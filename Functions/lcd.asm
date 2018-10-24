//Using Euclidean algorithm to find the largest common divisor of two non-negative integers
//Assuming RAM[R0] stores the first integer and RAM[R1] stores the second integer
//RAM[R2] stores the result
//Write your code here

//get the larger/smaller integer
	@R0
	D = M	//get R0
	@temp
	M = D	//set temp to R0
	@R1
	D = M	//get R1
	@temp	//use temp so R0 and R1 is not altered
	M = M - D	//R0-R1
	D = M	//get R0-R1
	@FIRST
	D; JGT	//if D is positive, that means R0>R1, go to FIRST
	
	@R1
	D = M	//get R1 (larger)
	@a	//otherwise, 
	M = D	//set a to R1
	@larger
	M = D	//store larger
	@R0
	D = M	//get R0 (smaller)
	@c
	M = D	//set c to R0 
	@R2
	M = D	//set R2 to R0 
	@ALTEND
	D; JEQ	//go to alt end if the smaller value is zero; skip computation
	@TOMOD
	0; JMP
(FIRST)
	@R0
	D = M	//get R0 (larger)
	@a
	M = D	//set a to R0 (the larger int)
	@larger
	M = D	//store larger
	@R1
	D = M	//get R1 (smaller)
	@c
	M = D	//set c to R1 (the smaller int)
	@R2
	M = D	//set R2 TO R1 (in case smaller divides larger)
	@ALTEND
	D; JEQ	//go to alt end if the smaller value is zero; skip computation
//a mod c
(TOMOD)
	@a
	D = M	//get a
	@c
	D = D - M	//a-c
	@MODDED
	D; JLT	//jump to end if D<c
	@a
	M = D	//otherwise, set a=a-c
	@TOMOD
	0; JMP
//change a to c and c to remainder
(MODDED)
	@a
	D = M	//get a
	@END
	D; JEQ	//jump to END if remainder is 0
	@R2
	M = D	//set result to be the remainder
	@c
	D = M	//get c
	@ctemp
	M = D	//store c in ctemp
	@a
	D = M	//get a
	@c
	M = D	//set c to a(the remainder)
	@ctemp
	D = M	//get ctemp
	@a
	M = D	//set a to ctemp
	@TOMOD
	0; JMP
//if any one of the given values was 0, just return the larger value
(ALTEND)
	@larger
	D = M	//get larger value
	@R2
	M = D	//return larger int as the result
(END)
	0; JMP