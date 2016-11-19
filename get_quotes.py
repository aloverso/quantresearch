import xml.etree.ElementTree
import re

filename = 'hu_interviewz_111516.txt'
#Atlas -> export...
#cleaned by changing all ["] within q names to [']
#removed bracketed transcriptor notes
#and some manual stuff
filename2 = 'allcodes.txt'
#Atlas -> codes ...
#cleaned by changing all ["] to [']
#and removing quotes entirely around passion
#removed bracketed transcriptor notes
#and some othe small manual stuff, to be automated eventually


def get_quotes(filename, cq_dict,codelist):
	"""gets a list of dictionaries from a file
	each dictionary named after a person containing 
	codes as keys. each code points to a list of tuples,
	each tuple represents a quote,
	first member is (start_line_number, start_line_character)
	second member is (end_line_number, end_line_character)

	"""

	e = xml.etree.ElementTree.parse(filename).getroot()

	quote_dict = {}

	for pds in e.findall('primDocs'):
		for pd in pds.findall('primDoc'):
			name = pd.attrib["name"]
			quote_dict[name] = {c:[] for c in codelist}
			for quotations in pd.findall('quotations'):
				for quote in quotations.findall('q'):
					trunc = quote.attrib["name"]
					for code in cq_dict[trunc]:
						loc = quote.attrib["loc"]
						loc = loc.split()
						start_tup = (loc[0],loc[2][0:-1])
						end_tup = (loc[3], loc[5][0:-1])
						quote_dict[name][code].append((start_tup,end_tup))

	return quote_dict

def get_cq_dict (filename, codelist):
	"""given a file (like "allcodes.txt")
	returns a dictionary where keys are truncated quotes'
	items are list of codes
	"""

	f = open(filename)
	cq_dict = {}

	line = f.readline()

	while line:
		p_num = line[1:3]

		try:
			int(p_num)
			quote_name = re.split("\[|\]",line)[1]
			line = f.readline()
			dirty_codes = re.split("\[|\]",line)
			cq_dict[quote_name] = [code for code in dirty_codes if code in codelist]
		except:
			pass

		line = f.readline()

	return cq_dict 


codelist = ["passion","accident", "always inclined", "badness/frustration", "Candidate's Weekend","career","confidence/empowerment","constant dialogue","content/skill learning","cultural norms", "decision", "decision pressure","diverse perspectives","don't think it affects me","encouragement", "environment expectations","excitement","faculty connection","feeling of value" , "fun", "good fit", "I'll do it myself", "identity", "interest/learning combo", "learning goals", "learning in context", "limited opportunity","losing interest","only woman", "peer teaching", "perspective learning", "reflections on wanting", "repitition", "responsibility", "responsiveness/empathy", "self-direction", "success/failure", "teaching model - delta", "teaching model - enact", "teaching model - express", "things they call teachers" ]
cq_dict = get_cq_dict(filename2,codelist)
quote_dict = get_quotes(filename, cq_dict, codelist)

# Fred and his codes
print(quote_dict.keys()[1])
print(quote_dict[quote_dict.keys()[1]])

def get_quote(address, subject):
	#i = open("interviews/" + subject * '.txt')
	pass

def strict_cooccurences(subject_dict, codes):
	quotes = subject_dict[codes.pop()]
	while codes:
		quotes = list(set(quotes) & set(subject_dict[codes.pop()]))
	return quotes

s = strict_cooccurences(quote_dict[quote_dict.keys()[0]], ['learning in context', 'responsiveness/empathy'])
print(s)