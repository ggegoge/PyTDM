'''speech'''

import pyttsx3
# relative vs non relative import bs
try:
	from translacja import tłumacz
except ModuleNotFoundError:
	from .translacja import tłumacz



engine = pyttsx3.init()

def say(s):
	'pyttsx3 say function'
	engine.say(s)
	engine.runAndWait()


def mów(s : str, show=True):
	'''
	say given polish text then print it if show == True.
	you can also call it with mow(s)
	'''
	translated = tłumacz(s.lower())
	if show:
		print(s)
	say(translated)
