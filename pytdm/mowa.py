"""speech"""

import pyttsx3
import os

# relative vs non relative import bs
try:
    from translacja import tłumacz, langs
except ModuleNotFoundError:
    from .translacja import tłumacz, langs

LANG = "en"

engine = pyttsx3.init()


def change_lang(new_lang: str):
    "change current synthesiser and translator language"
    global LANG
    if new_lang not in langs:
        raise NotImplementedError(
            "Language '%s' not found among avalaible languages, which are:" % new_lang,
            list(langs.keys()),
        )
    _LANG = new_lang
    new_lang = langs[new_lang]
    new_voice_id = "xd"
    vs = engine.getProperty("voices")
    for v in vs:
        if v.languages:
            if v.languages[0] == new_lang:
                new_voice_id = v.id
                break
    if new_voice_id == "xd":
        print("language not found in your built-in synthesiser")
    else:
        LANG = _LANG
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
    """
    tries to save an audio file generated from polish text.
    s - polish text to be speechised
    path_save - file name
    lang - language for the synthesiser
    """
    global LANG
    if lang != LANG:
        change_lang(lang)
    translated = tłumacz(s.lower(), LANG)
    path_save = os.path.join(os.getcwd(), path_save)
    # ok well. it doesn't work properly for one simple
    # reason - pyttsx3 seems to be breaking each time
    # it tries to save another new file with the same engine
    # idk why, it works for first zapisz, but not for more
    # tried to fix that but with no luck
    # seems like the problem is on pytttsx3's side

    print("Saving file to", path_save)
    engine.save_to_file(translated, path_save)
    engine.runAndWait()
