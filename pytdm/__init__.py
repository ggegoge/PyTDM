'''Pytońska treść do mowy - Python Text to Speech library for Polish'''
__version__ = '0.0.9'


from .mowa import mów, tłumacz
from .translacja import repolonizuj, anglicyzuj

# to make it no-polish-keyboard friendly:
mow = mów
tlumacz = tłumacz
