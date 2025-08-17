# Interperter for NEMO



# Variables
global y_size
global x_size
global x_pointer
global y_pointer
global y_tape
global x_tape
global xy_tape
global codet
y_size = 10
x_size = 10
x_pointer = 0
y_pointer = 0
y_tape = [0] * y_size
x_tape = [0] * x_size
xy_tape = [x_tape, y_tape]
codet = ""

class NEMO:

	__version__ = "1.0.0"
	__name__ = f"NEMO Interperter: {__version__}"

	def __init__(self, y, x, pr=True):
		self.code = ""
		self.y = y
		self.x = x
		self.pr = pr
		y_size = self.y
		x_size = self.x
		y_tape = [0] * y_size
		x_tape = [0] * x_size
		xy_tape = [x_tape, y_tape]
		self.save = 0
		self.ysave = 0
		self.comment_mode = False
		self.x_pointer = x_pointer
		self.y_pointer = y_pointer



	def add(self, codes):
		self.code = self.code + codes



	def run(self):
		codep = self.code
		if self.pr == True:
			print(self.__name__)
		if codep.startswith("I") != True:
			raise SyntaxError("Code not initilized with SoF identifier 'I'.")
		if codep.endswith("$") != True:
			raise SyntaxError("Code not closed properly with EoF marker '$'")

		for char in codep:
			if self.x_pointer > len(xy_tape[0]):
				raise MemoryError("X_pointer out of bounds of x_tape.")
			elif self.y_pointer > len(xy_tape[1]):
				raise MemoryError("Y_pointer out of bounds of y_tape.")
			elif "A" in char:
				if self.comment_mode == True:
					continue
				else:
					xy_tape[0][self.x_pointer] += 1
			elif "I" in char:
				continue
			elif "$" in char:
				continue
			elif "!" in char:
				if self.comment_mode == True:
					continue
				else:
					xy_tape[0][self.x_pointer] = 0
			elif "%" in char:
				if self.comment_mode == True:
					continue
				else:
					xy_tape[0][self.x_pointer] = input(">> ")
			elif "#" in char:
				if self.comment_mode == True:
					continue
				else:
					xy_tape[1][self.y_pointer] = input(">> ")
			elif ":" in char:
				if self.comment_mode == True:
					continue
				else:
					u = int(codep[codep.index(char) + 1])
					xy_tape[0][self.x_pointer] = u
			elif ";" in char:
				if self.comment_mode == True:
					continue
				else:
					c = codep[codep.index(char) + 1]
					xy_tape[1][self.y_pointer] = c
			elif "c" in char:
				if self.comment_mode == True:
					continue
				else:
					xy_tape[1][self.y_pointer] = 0
			elif "a" in char:
				if self.comment_mode == True:
					continue
				else:
					xy_tape[1][self.y_pointer] += 1
			elif "M" in char:
				if self.comment_mode == True:
					continue
				else:
					xy_tape[0][self.x_pointer] -= 1
			elif "m" in char:
				if self.comment_mode == True:
					continue
				else:
					xy_tape[1][self.y_pointer] -= 1
			elif ">" in char:
				if self.comment_mode == True:
					continue
				else:
					self.x_pointer += 1
			elif "<" in char:
				if self.comment_mode == True:
					continue
				else:
					self.x_pointer -= 1
			elif "^" in char:
				if self.comment_mode == True:
					continue
				else:
					self.y_pointer += 1
			elif "~" in char:
				if self.comment_mode == True:
					continue
				else:
					self.y_pointer -= 1
			elif "*" in char:
				if self.comment_mode == True:
					continue
				else:
					xy_tape[0][self.x_pointer] = xy_tape[0][self.x_pointer] * xy_tape[0][self.x_pointer]
			elif "8" in char:
				if self.comment_mode == True:
					continue
				else:
					xy_tape[1][self.y_pointer] = xy_tape[1][self.y_pointer] * xy_tape[1][self.y_pointer]
			elif "S" in char:
				if self.comment_mode == True:
					continue
				else:
					self.save = xy_tape[0][self.x_pointer]
			elif "s" in char:
				if self.comment_mode == True:
					continue
				else:
					self.ysave = xy_tape[1][self.y_pointer]
			elif "L" in char:
				if self.comment_mode == True:
					continue
				else:
					xy_tape[0][self.x_pointer] = self.save
					self.save = 0
			elif "l" in char:
				if self.comment_mode == True:
					continue
				else:
					xy_tape[1][self.y_pointer] = self.ysave
					self.ysave = 0
			elif "&" in char:
				if self.comment_mode == True:
					continue
				else:
					self.comment_mode == True
			elif "+" in char:
				if self.comment_mode == True:
					continue
				else:
					a = int(codep[codep.index(char) -1])
					b = int(codep[codep.index(char) +1])
					xy_tape[0][self.x_pointer] = a + b
			elif "-" in char:
				if self.comment_mode == True:
					continue
				else:
					a = int(codep[codep.index(char) -1])
					b = int(codep[codep.index(char) +1])
					xy_tape[0][self.x_pointer] = a-b
			elif "X" in char:
				if self.comment_mode == True:
					continue
				else:
					a = int(codep[codep.index(char) -1])
					b = int(codep[codep.index(char) +1])
					xy_tape[0][self.x_pointer] = a*b
			elif "D" in char:
				if self.comment_mode == True:
					continue
				else:
					a = int(codep[codep.index(char) -1])
					b = int(codep[codep.index(char) +1])
					xy_tape[0][self.x_pointer] = a/b

			elif "/" in char:
				self.comment_mode == False
			elif "P" in char:
				if self.comment_mode == True:
					continue
				else:
					print(chr(xy_tape[0][self.x_pointer]), end='')
			elif "p" in char:
				if self.comment_mode == True:
					continue
				else:
					print(chr(xy_tape[1][self.y_pointer]), end='')
			elif "V" in char:
				if self.comment_mode == True:
					continue
				else:
					print(xy_tape[0][self.x_pointer])
			elif "v" in char:
				if self.comment_mode == True:
					continue
				else:
					print(xy_tape[1][self.y_pointer])
			elif "F" in char:
				if self.comment_mode == True:
					continue
				else:
					i = codep[codep.index(char) + 1]
					if xy_tape[0][self.x_pointer] == 0:
						if i.isdigit():
							self.x_pointer = int(i)
						else:
							raise SyntaxError(f"cannot go to xcell {i} as it is not a valid inttype")
					else:
						continue
			elif "f" in char:
				if self.comment_mode == True:
					continue
				else:
					i = codep[codep.index(char) + 1]
					if xy_tape[1][self.y_pointer] == 0:
						if i.isdigit():
							self.y_pointer = int(i)
						else:
							raise SyntaxError(f"cannot go to ycell {i} as it is not a valid inttype")
					else:
						continue

			elif "r" in char:
				if self.comment_mode == True:
					continue
				else:
					return xy_tape[0][self.x_pointer]
			elif "R" in char:
				if self.comment_mode == True:
					continue
				else:
					return xy_tape[1][self.y_pointer]
			elif "t" in char:
				if self.comment_mode == True:
					continue
				else:
					return xy_tape[1]
			elif "T" in char:
				if self.comment_mode == True:
					continue
				else:
					return xy_tape[0]

			else:
				if char.isdigit():
					continue
				raise SyntaxError(f"'{char}' is not a valid argument.")
		print("\n")




