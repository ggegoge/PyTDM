# PyTDM for Pythonista

the same thing but designed for
__[Pythonista](http://omz-software.com/pythonista/)__ 
ie. for __iOS__.

Only slight changes. No need for `pyttsx3` here since you have the
built-in `speech` module.

Also the `zapisz` function is not implemented since there is no easy
way to save an audio file with the `speech` module.

### set up
save this __whole directory__ (preferably under the name __pytdm__)
in your pythonista `site-packages-3` directory. Then you can import it
anywhere using the `import pytdm` command and
