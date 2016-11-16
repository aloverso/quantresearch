class Interview:
	def __init__(self, name):
		self.name = name
		self.filename = "interviews/"+self.name+".txt"
		self.lines = self.find_lines()
		self.interviewer = self.find_interviewer()
		self.participant = self.find_participant()

	def find_lines(self):
		f = open(self.filename)
		return f.readlines()

	def find_interviewer(self):
		for line in self.lines:
			if ':' in line:
				ind = line.index(':')
				return line[0:ind]

	def find_participant(self):
		for line in self.lines:
			if ':' in line:
				ind = line.index(':')
				participant = line[0:ind]
				if participant == self.interviewer:
					continue
				return participant

	def all_interviewer_lines(self):
		return self.all_lines_helper(self.interviewer, self.participant)

	def all_participant_lines(self):
		return self.all_lines_helper(self.participant, self.interviewer)

	def all_lines_helper(self, subject, other):
		all_lines = []
		currently_subject = 0
		for line in self.lines:
			if line[0:len(subject)] == subject:
				currently_subject = 1
			elif line[0:len(other)] == other:
				currently_subject = 0

			if currently_subject:
				all_lines.append(line)
		return all_lines

if __name__ == "__main__":
	people = ['alexander', 'greg', 'shawn', 'tricia', 'christine', 'steph', 'michelle', 'fred', 'grace', 'ellie', 'betty', 'nate', 'karen']

	for p in ['alexander']:
		i = Interview(p)
		print i.all_participant_lines()