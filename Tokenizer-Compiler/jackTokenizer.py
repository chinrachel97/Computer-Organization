#removes all comments and white space from the input stream and breaks it 
#into Jack-language tokens, as specified by the Jack grammar

import re
import sys

class JackTokenizer(object):
	
	#comment regex
	comment = re.compile(r'//.*')
	multi_comment1 = re.compile(r'/\*.*\*/')
	multi_comment2 = re.compile(r'/\*.*')
	multi_comment3 = re.compile(r'.*\*/')
	
	#opens the input file/stream and gets ready to tokenize it
	def __init__(self, infile):
		with open(infile, 'r') as read_file:
			self.lines = read_file.readlines()
		newName = infile.replace('.jack', '')
		newName += 'Ttest.xml'
		self.outfile = newName
		self.curr_line = 0
		self.pos = -1
		self.curr_token = ''
		self.keyword = ['class', 'constructor', 'function', 'method', 'field',
				'static', 'var', 'int', 'char', 'boolean', 'void', 'true',
				'false', 'null', 'this', 'let', 'do', 'if', 'else',
				'while', 'return']
		self.symbol = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*',
				'/', '&', '|', '<', '>', '=', '~', '"']
		self.delimiter = [' ', '\n', '\t']
		self.string_constant = []
		self.integer_constant = []
		self.identifier = []
		self.comm_switch = False
	
	#check if there are more tokens in the input
	def hasMoreTokens(self):
		if (self.pos+1<len(self.lines[self.curr_line])) or (self.curr_line+1 < len(self.lines)):
			return True
		else:
			return False
		
	#gets the next token from the input and makes it the current token
	#should only be called if hasMoreTokens() is true
	#initially there is no current token
	def advance(self):
		self.curr_token = ''
		
		self.lines[self.curr_line] = self.removeComments()
		if(self.pos+1<len(self.lines[self.curr_line])):
			self.pos += 1
		elif (self.curr_line + 1) < len(self.lines) or self.lines[self.curr_line][self.pos] == '\n':
			self.pos = 0
			self.curr_line += 1
			self.lines[self.curr_line] = self.removeComments()

		self.curr_token = self.lines[self.curr_line][self.pos].strip()
		print(self.curr_token)
		if self.lines[self.curr_line][self.pos] == '"':
			self.curr_token = ''
			self.pos += 1
			while(self.lines[self.curr_line][self.pos] != '"'):
				self.curr_token += self.lines[self.curr_line][self.pos]
				self.pos += 1
			self.string_constant.append(self.curr_token)
			
		elif self.curr_token not in self.symbol:
			self.groupToken()
			
	def removeComments(self):
		noComments = self.comment.sub('', self.lines[self.curr_line])

		if bool(self.multi_comment1.search(noComments)):
			noComments = self.multi_comment1.sub('', noComments)
		elif bool(self.multi_comment3.search(noComments)) and self.comm_switch:
			noComments = self.multi_comment3.sub('', noComments)
			self.comm_switch = False
		elif bool(self.multi_comment2.search(noComments)):
			noComments = self.multi_comment2.sub('', noComments)
			self.comm_switch = True
		elif self.comm_switch:
			noComments = '\n'
		return noComments
		
	def groupToken(self):
		while ((self.pos+1<len(self.lines[self.curr_line])) 
			and self.lines[self.curr_line][self.pos+1] not in self.symbol 
			and self.lines[self.curr_line][self.pos+1] not in self.delimiter):
			self.pos += 1
			self.curr_token += self.lines[self.curr_line][self.pos].strip()
		if self.curr_token.isdigit():
			self.integer_constant.append(self.curr_token)
		elif self.curr_token == '':
			pass
		else:
			self.identifier.append(self.curr_token)
			
	#test
	def printTokens(self):
		file = open(self.outfile, "w")
		file.write('<tokens>\n')
		while(self.hasMoreTokens()):
			self.advance()
			if self.tokenType() != 'unknown type':
				file.write('<'+self.tokenTypePrint()+'> '+self.curr_token+' </'+self.tokenTypePrint()+'>'+'\n')
		file.write('</tokens>\n')
		file.close()
	
	def tokenTypePrint(self):
		if self.curr_token in self.keyword:
			return 'keyword'
		elif self.curr_token in self.symbol:
			return 'symbol'
		elif self.curr_token in self.string_constant:
			return 'stringConstant'
		elif self.curr_token in self.identifier:
			return 'identifier'
		elif self.curr_token in self.integer_constant:
			return 'integerConstant'
		else:
			return 'unknown type'
	
	#return the type of the current token
	def tokenType(self):
		if self.curr_token in self.keyword:
			return 'KEYWORD'
		elif self.curr_token in self.symbol:
			return 'SYMBOL'
		elif self.curr_token in self.string_constant:
			return 'STRING_CONST'
		elif self.curr_token in self.identifier:
			return 'IDENTIFIER'
		elif self.curr_token in self.integer_constant:
			return 'INT_CONST'
		else:
			return 'unknown type'
		
	#returns the keyword which is the current token
	#should be called only when tokenType() is KEYWORD
	def keyWord(self):
		if self.keyWord() == 'KEYWORD':
			return self.curr_token
		
	#returns the character which is the current token
	#should be called only when tokenType() is SYMBOL
	def symbol(self):
		if self.keyWord() == 'SYMBOL':
			return self.curr_token
		
	#returns the identifier which is the current token
	#should be called only when tokenType() is IDENTIFIER
	def identifier(self):
		if self.keyWord() == 'IDENTIFIER':
			return self.curr_token
		
	#returns the integer value of the current token
	#should be called only when tokenType() is INT_CONST
	def intVal(self):
		if self.keyWord() == 'INT_CONST':
			return self.curr_token
		
	#returns the string value of the current token, without the double quotes
	#should be called only when tokenType() is STRING_CONST
	def stringVal(self):
		if self.keyWord() == 'STRING_CONST':
			return self.curr_token

def main():
	in_file = ""
	if len(sys.argv) != 2:
		print("Please use: JackTokenizer.py file.jack")
	else:
		in_file = sys.argv[1]
	
	jack = JackTokenizer(in_file)
	jack.printTokens()

main()