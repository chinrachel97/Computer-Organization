import sys
import Parser
import Code
import SymbolTable

class Assembler(object):

	#create Assembler object
	def __init__(self, in_file):
		self.in_file = in_file
		self.out_file = self.get_out_file(in_file)
		self.symbol_table = SymbolTable.SymbolTable()
		self.symbol_address = 16
		
	#loop through file and add labels found to the symbol table
	def first_pass(self):
		parser = Parser.Parser(self.in_file)
		curr_address = 0
		while parser.has_more_commands():
			parser.advance()
			if(parser.command_type() == parser.A_COMMAND or parser.command_type() == parser.C_COMMAND):
				curr_address += 1
			elif parser.command_type() == parser.L_COMMAND:
				self.symbol_table.add_entry(parser.symbol(), curr_address)
				
	#loop through file and generate binary code
	def second_pass(self):
		parser = Parser.Parser(self.in_file)
		outf = open(self.out_file, 'w')
		code = Code.Code()
		while parser.has_more_commands():
			parser.advance()
			if parser.command_type() == parser.A_COMMAND:
				outf.write(code.gen_a_code(self.get_address(parser.symbol()))+ '\n')
			elif parser.command_type() == parser.C_COMMAND:
				outf.write(code.gen_c_code(parser.comp(), parser.dest(), parser.jump()) + '\n')
			elif parser.command_type == parser.L_COMMAND:
				pass
		outf.close()
		
	#get address from the symbol table
	def get_address(self, symbol):
		if symbol.isdigit():
			return symbol
		else:
			if not self.symbol_table.contains(symbol):
				self.symbol_table.add_entry(symbol, self.symbol_address)
				self.symbol_address += 1
			return self.symbol_table.get_address(symbol)
	
	#get the output file name
	@staticmethod
	def get_out_file(in_file):
		if in_file.endswith('.asm'):
			return in_file.replace('.asm', '.hack')
		else:
			return in_file + '.hack'
			
#main, makes sure a command line argument is given
def main():
	in_file = ""
	if len(sys.argv) != 2:
		print("Please use: Assembler.py file.asm")
	else:
		in_file = sys.argv[1]
		
	asm = Assembler(in_file)
	asm.first_pass()
	asm.second_pass()
	
main()
				