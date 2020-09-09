# patterns najpierw

import re
# relative vs non relative import bs
try:
	from nums import num_to_speech
except:
	from .nums import num_to_speech

repolon = {
	r'(\b[wz])(\s)': r'\1',    # lone letters
	
	'rz': 'ż',
	r'([^p])ch': r'\1h',     # upraszczam polski
	'ó': 'u',
	'ęł': 'eł',
	'ął': 'oł',
	r'([ea])u': r'\1ł',
	
	r'ci(\b|[^eaouęą])': r'ći\1',
	r'ci([^e])': r'ć\1',
	r'ci': r'ć',
	
	r'si(\b|[^eaouęą])': r'śi\1',
	r'si([^e])': r'ś\1',
	r'si': r'ś',
	
	r'dzi(\b|[^eaouęą])': r'dźi\1',
	r'dzi([^e])': r'dź\1',
	r'dzi': r'dź',
	
	r'zi(\b|[^eaouęą])': r'źi\1',
	r'zi([^e])': r'ź\1',
	r'zi': r'ź',
	

	r'([śptkh])ż(\w+)': r'\1sz\2',    # ubezdźwięcznienie
	r'([śptksh])w(\w+)': r'\1f\2',
	r'([śptkh])d(\w+)': r'\1t\2',
	r'([^cs])z([kptf])': r'\1s\2',
	r'w([kptf])': r'f\1',
	r'ż\b': 'sz',
	r'(\S)w\b': r'\1f',
	r'b\b': 'p',
	r'g\b': 'k',
	r'd\b': 't',
	r'([^cs\s])z\b': r'\1s',
	r'ź\b': 'ś',
	r'dź\b': 'ć',
	r'dż\b': 'cz',
	'ń': 'n',

	r'ą\b': 'om',                       # nasals
	r'ę\b': 'e',      
	r'ę([zscśćtdkgż]|cz|sz)': r'en\1',
	r'ą([zscśćtdgkż]|cz|sz)': r'on\1',
	r'ą([pb])': r'om\1',
	r'ę([pb])': r'em\1'
}



angl = {
	'ch': 'kh',
	r'([fk])i(e)': r'\1\2',
	r'\bnie\b': 'ne',
	r'w': 'v',
	'ś': 'sz',
	'ź': 'ż',
	'ć': 'cz',
	'dź': 'dż',
	r's([^z]|\b)': r'ss\1',
	r'([^cs]|\b)z': r'\1s',
	r'(\b)cz': r'\1ch',     # to do
	'cz': 'tch',
	'sz': 'sh',
	'dż': 'J',
	'ż': 'zsh',
	r'c([^h]|\b)': r'ts\1',
	                             # 'a' 'i' 'e' samotne 
	r'a([^jłr]|\b)': r'ah\1',
	r'([^ji])e([^j]|\b)': r'\1eh\2',
	r'\bi\b': r'e', 
	
	r'y': 'I',                     # igrek na razie pod placeholderem takim
	r'(\w{2,})iej': r'\1 yay',
	r'(\w{2,})[ij]e': r'\1 yeah',     # końcówka -ie zależnie od sylabowości
	r'\bje(\w+)([eioua])': r'yeah \1\2',
	r'(\w+)je(\w+)': r'\1yeh\2',
	r'(\w{1})ie': r'\1ieh',
	r'i([^ea]|\b)': r'EE\1',   # EE by ominąć zmiany na małych e
	r'ej\b': 'ei',
	r'ej\B': 'ay',   
	r'EE': 'ee',        # i powrót ee
	r'I': 'ih',                    # igrek wraca
	r'ał': 'ow',
	r'([aeoi])(\w+)oł': r'\1\2 oh',
	'oł': 'ow',
	'ł': 'w',
	r'(\b\w{1})aj': r'\1ie',
	r'(\w+)(\w{1})aj(\w+)': r'\1 \2igh\3',
	r'(\w+)(\w{1})aj': r'\1 \2ie',	
	r'aj': ' i',
	'j': 'y',
	r'J': 'j',
	r'o([^whym]|\b)': r'aw\1',
	r'u': 'oo',
	r'g([ei])': r'gh\1'
}


def repolonizuj(s):
	subbed = s
	for key in repolon:
		subbed = re.sub(re.compile(key), repolon[key], subbed)
	return subbed

	
def anglicyzuj(s):
	subbed = []
	for w in s.split():
		sub = w
		if re.match(r'\d+', w):
			sub = num_to_speech(int(re.match(r'\d+', w).group(0))) + ''.join(re.findall(r'\D+', w))
		else:
			for key in angl:
				sub = re.sub(re.compile(key), angl[key], sub)
		subbed.append(sub)
	return ' '.join(subbed)
	


def tłumacz(s):
	s = repolonizuj(s)
	return anglicyzuj(s)