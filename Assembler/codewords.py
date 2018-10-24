'''
Translates Hack assembly language mnemonics into binary codes
'''

class Code(object):
	destination_codes = ['', 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD']
	comparison_codes = {
		'0':'0101010', '1':'0111111', '-1':'0111010', 'D':'0001100',
		'A':'0110000', '!D':'0001101', '!A':'0110001', '-D':'0001111',
		'-A':'0110011', 'D+1':'0011111','A+1':'0110111','D-1':'0001110',
		'A-1':'0110010','D+A':'0000010','D-A':'0010011','A-D':'0000111',
		'D&A':'0000000','D|A':'0010101',
		'':'xxxxxxx',
		'M':'1110000', '!M':'1110001', '-M':'1110011', 'M+1':'1110111',
		'M-1':'1110010','D+M':'1000010','D-M':'1010011','M-D':'1000111',
		'D&M':'1000000', 'D|M':'1010101'
	}
	jump_codes = ['', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']
	
	#creates a Code object
	def __init__(self):
		pass
		
	#generate binary A-instruction
	def gen_a_code(self, address):
		return '0' + self.bits(address).zfill(15)
		
	#generate binary C-instruction
	def gen_c_code(self, comp, dest, jump):
		return '111' + self.comp(comp) + self.dest(dest) + self.jump(jump)
		
	#returns the binary code of the dest mnemonic
	def dest(self, mnemonic):
		return self.bits(self.destination_codes.index(mnemonic)).zfill(3)
		
	#returns the binary code of the comp mnemonic
	def comp(self, mnemonic):
		return self.comparison_codes[mnemonic]
		
	#returns the binary code of the jump mnemonic
	def jump(self, mnemonic):
		return self.bits(self.jump_codes.index(mnemonic)).zfill(3)
		
	@staticmethod
	#convert index to binary, using [2:] to leave out '0b' at the beginning
	def bits(num):
		return bin(int(num))[2:]