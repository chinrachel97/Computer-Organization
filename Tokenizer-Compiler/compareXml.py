#compare two .xml files

import sys

class comp(object):

	def __init__(self, file1, file2):
		self.file1 = file1
		self.file2 = file2
		
	def compare(self):
		with open(self.file1, 'r') as read_file:
			self.lines1 = read_file.readlines()
		with open(self.file2, 'r') as read_file:
			self.lines2 = read_file.readlines()
		line_no = 0
		
		if len(self.lines1) != len(self.lines2):
			print('.xml files have different number of lines')
		
		while(line_no < len(self.lines1)):
			outline = line_no + 1
			if self.lines1[line_no] != self.lines2[line_no]:
				print(str(outline)+': not the same')
			else:
				print(str(outline)+': ok')
			line_no += 1

def main():
	in_file1 = ""
	in_file2 = ""
	if len(sys.argv) != 3:
		print("Please use: compareXml.py file1.xml file2.xml")
	else:
		in_file1 = sys.argv[1]
		in_file2 = sys.argv[2]
	
	c = comp(in_file1, in_file2)
	c.compare()
	
main()