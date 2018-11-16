# Program for Automata Theory
# Elementary Cellular Automata Simulation

import math, random

# 8 bit binary number seperated into elements in a list / try a different number (this example is 129 in decimal)
ruleset = [1, 0, 0, 0, 0, 0, 0, 1]
# row of a generation of cell
cells = []
for r in range(80):
	cells.append(random.randint(0, 1))
# amount of generations (rows) for the output
requested_generations = 30

# defines the rule of the 8 bit binary number
def rule(l, m, r, rbin):
	if l == 0 and m == 0 and r == 0:
		return rbin[7]
	elif l == 0 and m == 0 and r == 1:
		return rbin[6]
	elif l == 0 and m == 1 and r == 0:
		return rbin[5]
	elif l == 0 and m == 1 and r == 1:
		return rbin[4]
	elif l == 1 and m == 0 and r == 0:
		return rbin[3]
	elif l == 1 and m == 0 and r == 1:
		return rbin[2]
	elif l == 1 and m == 1 and r == 0:
		return rbin[1]
	elif l == 1 and m == 1 and r == 1:
		return rbin[0]

# prints generation 0
def first_line(c):
	s = ""
	for i in c:
		if i == 1:
			s = s + '●'
		else:
			s = s + ' '
	print(s)

# prints the following generations of 
def successive_generations(c, r, g):
	s = ""
	next_gen = c
	for j in range(g):
		i = 0
		for k in next_gen:
			m = next_gen[i]
			l = next_gen[i-1]
			if (i + 1) >= len(next_gen):
				r = next_gen[0]
			else:
				r = next_gen[i+1]
			value = rule(l, m, r, ruleset)
			if value == 1:
				s = s + '●'
			else:
				s = s + ' '
			i+=1
		next_gen = []
		for l, v in enumerate(s):
			if v == '●':
				next_gen.append(1)
			else:
				next_gen.append(0)
		print(s)
		s = ""

first_line(cells)
successive_generations(cells, ruleset, requested_generations)