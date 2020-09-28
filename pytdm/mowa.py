"""speech"""

import pyttsx3
import os

# relative vs non relative import bs
try:
    from translacja import tłumacz
except ModuleNotFoundError:
    from .translacja import tłumacz

LANG = "en"
langs = {"en": "en_US", "fr": "fr_FR"}
engine = pyttsx3.init()


def change_lang(new_lang: str):
    "change current synthesiser and translator language"
    global LANG
    voices = ["en", "fr"]
    if new_lang not in voices:
        raise NotImplementedError(
            "Voice %s isn't among avalaible voices." % new_lang)
    LANG = new_lang
    new_lang = langs[new_lang]
    new_voice_id = "xd"
    vs = engine.getProperty("voices")
    for v in vs:
        if v.languages[0] == new_lang:
            new_voice_id = v.id
            break
    if new_voice_id == "xd":
        print("language not found in your built-in synthesiser")
    else:
        engine.setProperty("voice", new_voice_id)


def say(s):
    "pyttsx3 say function"
    engine.say(s)
    engine.runAndWait()


def mów(s: str, lang="en", show=True):
    """
    say given polish text then print it if show == True.
    Uses built-in synthesiser with language specified by
    `lang`. Avalaible languages: "en" & "fr".
    you can also call it with mow(s)
    """
    global LANG
    if lang != LANG:
        change_lang(lang)
    translated = tłumacz(s.lower(), LANG)
    if show:
        print(s)
    say(translated)


def zapisz(s: str, path_save: str, lang="en"):
    global LANG
    if lang != LANG:
        change_lang(lang)
    translated = tłumacz(s.lower(), LANG)
    path_save = os.path.join(os.getcwd(), path_save)
    print("Saving file to", path_save)
    engine.save_to_file(translated, path_save)
    engine.runAndWait()
