import xml.etree.ElementTree

filename = 'hu_interviewz_111516.txt'

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
						quote_dict[name][code].append((start_tup,end_tup))

def get_cq_dict (filename):
	"""given a file (like "allcodes.txt")
	returns a dictionary where keys are truncated quotes
	items are list of codes
	"""

	f = open(allcodes.txt)
	cq_dict = {}

	#walk through lines
	#if starting starting with P## or P[space]# 
		#quote_name = [regex isolation of truncated quote]
		#codes = [regex isoltaion of list of quotes]
		#cq_dict[quote_name] = codes

	return cq_dict 

codelist = ["passion","accident", "always inclined", "badness/frustration", "Candidate's Weekend","career","confidence/empowerment","constant dialogue","content/skill learning","cultural norms", "decision", "decision pressure","diverse perspectives","don't think it affects me","encouragement", "environment expectations","excitement","faculty connection","feeling of value" , "fun", "good fit", "I'll do it myself", "identity", "interest/learning combo", "learning goals", "learning in context", "limited opportunity","losing interest","only woman", "peer teaching", "perspective learning", "reflections on wanting", "repitition", "responsibility", "responsiveness/empathy", "self-direction", "success/failure", "teaching model - delta", "teaching model - enact", "teaching model - express", "things they call teachers" ]
cq_dict = get_cq_dict('allcodes.txt')
get_quotes(filename, cq_dict)