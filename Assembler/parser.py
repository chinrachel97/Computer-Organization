import re

'''
Encapsulates access to the input code.
Reads an assembly language command, parses it, and provides
convenient access to the command's components (fields and symbols).
In addition, removes all white space and comments.
'''

class Parser(object):
	
	A_COMMAND = 0
	C_COMMAND = 1
	L_COMMAND = 2
	
	#comment regex
	comment = re.compile(r'//.*')
	
	#opens the input file/stream and gets ready to parse it
	def __init__(self, in_file):
		with open(in_file, 'r') as read_file:
			self.lines = read_file.readlines()
		self.command = ''
		self.curr_line = 0
		
	#checks if there are more commands in the input
	def has_more_commands(self):
		if(self.curr_line + 1) < len(self.lines):
			return True
		else:
			return False
			
	#reads the next command from the input and
	#makes it the current command. Should be called only if
	#has_more_commands() is true. Initially there is no current command
	def advance(self):
		self.curr_line += 1
		line = self.lines[self.curr_line]
		
		#take out comments
		line = self.comment.sub('', line)
		if line == '\n':
			self.advance()
		else:
			self.command = line.strip()
			
	#returns the type of the current command
	def command_type(self):
		#look for @
		if re.match(r'^@.*', self.command):
			return Parser.A_COMMAND
		#look for (
		elif re.match(r'^\(.*', self.command):
			return Parser.L_COMMAND
		else:
			return Parser.C_COMMAND
			
	#returns the symbol or decimal of the current command
	def symbol(self):
		matching = re.match(r'^[@\(](.*?)\)?$', self.command)
		symbol = matching.group(1)
		return symbol
		
	#returns the dest mnemonic in the current C-COMMAND (8 possibilities)
	def dest(self):
		matching = re.match(r'^(.*?)=.*$', self.command)
		if not matching:
			dest = ''
		else:
			dest = matching.group(1)
		return dest
	
	#returns the comp mnemonic in the current C-command (28 possibilities)
	def comp(self):
		#take out = and anything before it
		comp = re.sub(r'^.*?=', '', self.command)
		#take out ; and anything after it
		comp = re.sub(r';\w+$', '', comp)
		return comp.strip()
		
	#returns the jump mnemonic in the current C-command (8 possibilities)
	def jump(self):
		matching = re.match(r'^.*;(\w+)$', self.command)
		if not matching:
			jump = ''
		else:
			jump = matching.group(1)
		return jump