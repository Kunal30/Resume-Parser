''' methods to extract information for a given para of text '''


import regex as re
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk import RegexpParser

def InfoExtractor(text):

	### Regex Expressions ###
	#########################
	regex_email = re.compile(r'([a-zA-Z0-9._-]+@[a-zA-z0-9._-]+\.[^\s]*)',re.IGNORECASE | re.UNICODE)
	regex_phone = re.compile(r'(\d+[\-\+\(]?\d+[\)\-\s]?\d+[\-\s]?\d+)', re.UNICODE)
	
	regex_DOB = re.compile(r'([0-3]?[0-9](?:\.|\/|\-|\s)[0-3]?(?:[0-9]|' + 
		r'(?:Feb|Jan|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January' +
		r'|February|March|April|May|June|July|August|September|October|' +
		r'November|December))(?:\.|\/|\-|\s)(?:[0-9]{2})?[0-9]{2})',re.IGNORECASE | re.UNICODE)

	#regex_phone = re.compile(r'\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)$',re.IGNORECASE | re.UNICODE)
	
	info = dict()

	regex = {
	'email':regex_email,
	'phone':regex_phone,
	'DOB':regex_DOB
	}

	for exp in regex.keys():
		info[exp] = regex[exp].findall(text)

	#Filtering phone numbers
	info['phone'] = [x for x in info['phone'] if len(x)>5]

	print text

	### Sent Tokenize ###
	######################
	
	sent = sent_tokenize(text.decode("utf8"))
	print sent
	print
	### Word Tokenize ###  
	#####################

	sent = [ word_tokenize(word) for word in sent ]
	#print words

	sent = [pos_tag(word) for word in sent]
	#print sent[0]
	#print sent
	#print sent[1]

	grammar = "NP: {<DT>?<JJ>*<NN>}"

	cp = RegexpParser(grammar)
	result = cp.parse(sent[0])
	#print result
	#result.draw()

	#print sent
	'''
	raw_tuples = sent[0].split('\n')

	for line in raw_tuples:
		try:
			key, value = line.split('\t')
			print key, value
			print
		except:
			pass 

	'''

	#return None
	return info