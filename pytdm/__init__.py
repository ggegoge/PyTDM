from .mowa import mów, tłumacz
from .translacja import repolonizuj, anglicyzuj

# to make it no-polish-keyboard friendly:

def mow(s, show=True):
	mów(s, show)

def tlumacz(s):
	return tłumacz(s)
