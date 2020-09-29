"""PyTDM - Pytońska treść do mowy. Pythonista iOS version."""
from .translacja import repolonizuj, anglicyzuj
from .mowa import mów, tłumacz

__version__ = "0.1.0"

# to make it non-polish-keyboard friendly:
mow = mów
tlumacz = tłumacz
