import pyttsx3
# relative vs non relative import bs
try:
	from translacja import tłumacz
except ModuleNotFoundError:
	from .translacja import tłumacz



engine = pyttsx3.init()

def say(s):
	engine.say(s)
	engine.runAndWait()


def mów(s, show=True):
	translated = tłumacz(s.lower())
	if show:
		print(s)
	say(translated)
