matrix = [
    ["7", "i", "3"],
    ["T", "s", "i"],
    ["h", "%", "x"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"]
]

string = ''
columns = len(matrix[0])
rows = len(matrix)
for a in range(columns):
	for b in range(rows):
		if matrix[b][a].isalpha():
			 string += matrix[b][a]
		elif string and string[-1] != ' ':  
			string += ' '

print(string)