
class BowlingGame:
	def __init__(self):
		self.roll_l = []

	def roll(self, n):
		self.roll_l.append(n)

	def score(self):
		s = 0
		n = len(self.roll_l)
		roll_index = 0
		while roll_index < n:
			if self.roll_l[roll_index] == 10:
				s += 10
				if roll_index + 1 < n:
					s += self.roll_l[roll_index + 1]
				if roll_index + 2 < n:
					s += self.roll_l[roll_index + 2]
				roll_index += 1
			elif self.roll_l[roll_index] + self.roll_l[roll_index + 1] == 10: ## Spare
				s += 10
				if roll_index + 2 < n:
					s += self.roll_l[roll_index + 2]
				roll_index += 2
			else:
				s += self.roll_l[roll_index] + self.roll_l[roll_index + 1]
				roll_index += 2

		return s
