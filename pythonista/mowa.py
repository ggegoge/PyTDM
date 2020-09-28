"""PyTDM's version for Pythonista ie. iOS"""

import speech

# relative vs non relative import bs
try:
    from translacja import tłumacz
except ModuleNotFoundError:
    from .translacja import tłumacz


def say(s):
    speech.say(s)


def mów(s, lang="en", show=True):
    # apple's text to speech doesn't handle all those signs apart from commas too well
    s_corrected = (
        s.replace(".", ",").replace("!", ",").replace(
            ":", ",").replace("?", ",")
    )
    translated = tłumacz(s_corrected.lower(), lang)
    if show:
        print(s)
    say(translated)


# english keyboardz
mow = mów
tlumacz = tłumacz
