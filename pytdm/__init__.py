"""Pytońska treść do mowy - Python Text to Speech library for Polish"""
from .translacja import repolonizuj, anglicyzuj
from .mowa import mów, zapisz, tłumacz

__version__ = "0.1.0"

# to make it no-polish-keyboard friendly:
mow = mów
tlumacz = tłumacz
