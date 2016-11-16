people = ['alexander', 'greg', 'shawn', 'tricia', 'christine', 'steph', 'michelle', 'fred', 'grace', 'ellie', 'betty', 'nate', 'karen']

for p in people:
	filename = 'interviews/' + p + '.txt'
	f = open(filename)
	text = f.read()
	text = text.replace("\xe2\x80\x99", "'") # replace apostrophes
	text = text.replace("\xe2\x80\x9d", '"')  #replace close quotes
	text = text.replace("\xe2\x80\x9c", '"')  #replace open quotes
	text = text.replace("\xe2\x80\xa6", '...')  #replace ellipses
	nf = open(filename, 'w')
	nf.write(text)

