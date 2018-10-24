// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.

	@8192	//(256*512) pixels/16; there are this many sections on the screen
	D = A 
	@count
	M = D	//"count" keeps # of bytes
(SET)
	@index	//set current position to 0
	M = 0
(LOOP)
	@KBD
	D = M	//get KBD value
	@WHITE
	D; JEQ	//go to WHITE if KBD has no input, else go to BLACK
(BLACK)
	@index
	D = M	//get current position 
	@SCREEN
	A = A + D	//go to memory location + current position
	M = -1		//change 16 pixels to black
	@END
	0; JMP
(WHITE)
	@index
	D = M		//get currentposition
	@SCREEN
	A = A + D	//go to screen memory location + current position
	M = 0		//change to white
(END)
	@index
	MD = M + 1	//increment current position
	@count
	D = D - M	//current position - # of bytes
	@SET		
	D; JEQ		//go to LOOP if current position = # of bytes to reset position
	@LOOP
	0; JMP		//else go to INNER