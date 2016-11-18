from pattern.en import sentiment

class Interview:
	def __init__(self, name):
		self.name = name
		self.filename = "interviews/"+self.name+".txt"
		self.lines = self.find_lines()
		self.interviewer = self.find_interviewer()
		self.participant = self.find_participant()
		self.participant_lines = self.all_participant_lines()
		self.interviewer_lines = self.all_interviewer_lines()
		self.question_lines = self.all_questions()

	def find_lines(self):
		f = open(self.filename)
		lines = []
		for x in f.readlines():
			lines.append(unicode(x, 'utf-8'))
		return lines

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

	def all_questions(self):
		question_lines = []
		for line in self.interviewer_lines:
			if line.find('?') > 0:
				question_lines.append(line)
		return question_lines

	def length_per_question(self):
		d = dict((x,0) for x in self.question_lines)
		current_question = ''
		for line in self.lines:
			if line in self.question_lines:
				current_question = line
			elif line in self.participant_lines and current_question != '':
				d[current_question] += len(line.split(' '))
		for key in d.keys():
			d[key] = str(d[key]) + ' ' + '|'*d[key]
		return d

	def sentiment_per_question(self):
		d = dict((x,(0,0)) for x in self.question_lines)
		current_question = ''
		for line in self.lines:
			if line in self.question_lines:
				current_question = line
			elif line in self.participant_lines and current_question != '':
				if sentiment(line)[0] == 0.0 and len(line) < 12:
					continue
				if d[current_question] == (0,0):
					d[current_question] = (sentiment(line)[0], sentiment(line)[1])
				else:
					d[current_question] = (avg(d[current_question][0],sentiment(line)[0]), avg(d[current_question][1], sentiment(line)[1]))
		
		most_neg = {}
		most_pos = {}
		for key in d.keys():
			if d[key][0] < 0:
				most_neg[key] = d[key]
			if d[key][0] > .4:
				most_pos[key] = d[key]
		
		pos_subj = 0
		neg_subj = 0

		if len(most_pos) > 0: 		
			pos_subjs = [x[1] for x in most_pos.values()]
			pos_subj = sum(pos_subjs)/len(pos_subjs)

		if len(most_neg) > 0:
			neg_subjs = [x[1] for x in most_neg.values()]
			neg_subj = sum(neg_subjs)/len(neg_subjs)

		print pos_subj, neg_subj


		for key in d.keys():
			if d[key][0] < 0:
				d[key] = str(d[key]) + '\n' + 'X'*int(d[key][0]*-100)
			else:
				d[key] = str(d[key]) + '\n' + '|'*int(d[key][0]*100)

		return d

def avg(x, y):
	return (x + y)/2.0

if __name__ == "__main__":
	people = ['alexander', 'greg', 'shawn', 'tricia', 'christine', 'steph', 'michelle', 'fred', 'grace', 'ellie', 'betty', 'nate', 'karen']

	for p in people:
		i = Interview(p)
		d = i.sentiment_per_question()
		# d = i.length_per_question()
		# f = open(p+'responselens.txt', 'w')
		# for key in d.keys():
		# 	f.write(key)
		# 	f.write('\n')
		# 	f.write(d[key])
		# 	f.write('\n\n')
		f = open(p+'sentiment.txt', 'w')
		for key in d.keys():
			f.write(key.encode('utf-8'))
			f.write('\n')
			f.write(d[key].encode('utf-8'))	
			f.write('\n\n')