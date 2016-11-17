import xml.etree.ElementTree

filename = 'hu_interviewz_111516.txt'

def get_quotes(filename):
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
			quote_dict[name] = {}
			for quotations in pd.findall('quotations'):
				for quote in quotations.findall('q'):
					quote_dict[name][]


get_quotes(filename)