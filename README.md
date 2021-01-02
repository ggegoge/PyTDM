# PyTDM
ie. __Pytońska treść do mowy__ which is Polish for _Python Text to
Speech_. Package for turning text written in Polish into speech.

Both for standard Python3 and for iOS.

### ok but why 
This lil library was designed in order to assure that people
programming for Pollacks have some sort of an offline-working _text to
speech_ python software.
For English speaking people there already is
the [`pyttsx3`](https://pypi.org/project/pyttsx3/) library which
provides such functionalities.
If you want your program to _talk_ you simply run few commands

```python
import pyttsx3
engine = pyttsx3.init()
engine.say("now we're talkin'")
engine.runAndWait()
```
and it's literally that easy! But for Polish there was no such thing. Until now.

### installation
it is avalaible on [PyPI](https://pypi.org/project/pytdm/)!
you can just run:

```python
pip install pytdm
```
and you can use it just like that!

###### iOS
for the iOS version see
the
[pythonista directory on github](https://github.com/test0wanie/PyTDM/blob/master/pythonista/README_iOS.md),
do not use `pip` there – just put this file in the `Python
Modules/site-packages-3` directory and restart the app. The module will
be added to the path and then you can simply import it. 

### how it's made
It's based on the `pyttsx3` package I've mentioned. The thing is
that contrary to what many English speaking people think (looking at u
americans) Polish actually __is__ pronounceable for someone knowing
English (or French – see below).

What `PyTDM` does is

* first it _translates*_ the given polish string/text into english
* then it gets pronounced with the `pyttsx3` 

The asterisk above next to the word "translates" is there for a reason
– it's not exactly translation. More like transcription or
transliteration. Anglicises or francises depending on the language one
has choosen.
We shall get back to that later

### usage
For simple basic stuff you should do it as follows:

```python
import pytdm
pytdm.mów("dzień dobry, dobranoc")
```
or the second way:

```python
from pytdm import mowa
mowa.mów("dzień dobry, dobranoc")
```
and then you can happily listen to the sweet sound of the polish
language spoken by the `pyttsx3` synthesiser voice. Isn't that great?

You don't have to start the engine as one does with `pyttsx3` hence it
takes some time for python to import the package (the `pytdm` modulw performs the
`pyttsx3.init()` command itself when imported).

##### saving files
With version `0.1.0` came the functionality of saving spoken text in
files! It is similar to simply making the computer say stuff:

```python
pytdm.zapisz("dzień dobry świecie!", "example.mp3")
```
and your file will be saved in your cwd under the name
`"example.mp3"`. **It isn't working 100% correctly though.** For some
reason `pyttsx3` seems to break when trying to save a second file in
the same session. Or rather the file does indeed get saved but the command
doesn't stop executing itself. I suppose the issue is at `pyttsx3` part.

###### little disclaimer
the functions have Polish names like `mów` or `tłumacz` with those
funny strange letter but if you want you can use them without the
diacritics eg. write `mow` or `tlumacz`. They will work just fine.

In general if you have any problems first you can type
eg. `help(pytdm.mow)` and read the info provided there.


##### examples
An example for how well does the software work with
approxima... _translation_ of polish words is to be seen in the
`demo.py` file (avalaible
on [my github](https://github.com/test0wanie/PyTDM)). You just can run
it and then see how well it handles the most sacred polish song
(actually the second sacred-est. For the most sacred one see
`barka.py`) – the anthem of the Third Polish Republic.

There is a video showing how the `demo.py` file works (recorded in low
quality by me and posted on
youtube) [here](https://youtu.be/bHWxwoAm0OE).

Also with version `0.1.0` the french mode has been introduced
therefore there's another demo file `demo_fr.py`. A video of it being
run is [here](https://youtu.be/ti8CjUXVVpo).

All demo files are in the
__[`demos`](https://github.com/test0wanie/PyTDM/tree/master/demos)__
github directory.

### dependencies
all you need are built-in packages like `re` and apart from that the
`pyttsx3` package (version `>=2.7`). It
is [avalaible on pypi](https://pypi.org/project/pyttsx3/) so you can
just do the classic: 

```
pip install pyttsx3
```
### what OS? 
The only problem is it's different for every OS.

* For all I know it works really well on __macOS__ – I use this OS
  myself therefore I can easily test it there and adjust it
  respectively. The built-in synthesisers are some of _really_ high quality
  ones and it comes with many languages avalaible which are easily
  managable for the user.

For other OS I have only some feedback from other people:

* __Windows__ is stoopid _(per usual)_ and reads 'ch' as /k/ and not
  /t͡ʃ/. Apart from that and _maybe_ some other mistakes it is
  fine. Using `pytdm` with other languages is problematic though -
  windows' built-in synthesiser comes without necessary language
  marking flags for the `pyttsx3` to detect hence trying to change the
  language may often fail.
* the English one it's not bad on __Linux__ (of course it depends on what synthesiser
  do you use and on which distribution of linux) but it has problems
  with eg. consonant
  clusters like _szcz_. When it tries to pronounce them as _shtch_ it
  spells (_es aitch tee cee aitch..._) the cluster instead of just
  just saying /ʃt͡ʃ/ as other versions tend to do. Also it sounds
  robotic which is _w e i r d_. I do not know how does it work with
  the language set to french.

__In conclusion:__ it works ok for all of them but some sounds are
realised differently on different OSs.

###### mobile versions – iOS
for __iOS__ see the
__`pythonista`__
[directory on github](https://github.com/test0wanie/PyTDM/blob/master/pythonista/README_iOS.md). 
Everything there is the iOS version of `PyTDM`.


#### Function names are weird?
As a cautious reader might have already noticed the main speaking function is
`mów` (fyi it means _say_ just like in the `pyttsx3`). One could ask
_wthell?_ or more properly __co do diabła?__ but that is exactly how
the package was intended to be: the functions have polish
names. __Deal with it.__ Or use the same name without the diacritics
if you really need to.
##### behind the scenes
Now for some calrification about how the so called _translation_
process actually works. 

For every word passed to the `mów` function it is first _tanslated_ by
another polish-named func `tłumacz` (ie. __translate__) and it calls 2
more functions first:

* `repolonizuj` ie. __repolonise__ – it deals with all the weird
  polish ortographic stuff like the diagraphs, some consonants being
  devoiced
  etc. **_[Futuryści](https://pl.wikisource.org/wiki/Mańifest_w_sprawie_ortografji_fonetycznej)_**
  inspired
 
* `anglicyzuj` ie. __anglicise__ – it takes the __repolonised__ text
  and tries to find the closest approximations for all the sounds that
  are to be found. It's doing its best.

only then `mów` gives the anglicised repolonised text to the
`engine.say` as shown above.

So when you do something like `mów('czuję, że będzie dziś dość średni
dzień')` it first calls `tłumacz` which calls `repolonizuj`
that returns this simplified polish text:
`'czuje, że bendźe dźiś dość średni dźen'`
and it is passed to the `anglicyzuj` which gives the final result to
be said by `pyttsx3`:

`'choo yeah, zshehh behnjehh jeesh dawshtch shrehdnee jehn'`

it sure is amazing.

#### French 
As you may have known the `pyttsx3` library offers any speech
synthesiser avalaible to the system. Therefore it may happen one does
also have the french one and now it is possible to use it with `pytdm`
too.

It is a relatively new feature so you shouldn't expect it to be
flawless. As for now pronouncing numbers is not even implemented
here. Also it hasn't been tested anywhere apart from macOS yet.

The good thing is it is actually easier to transcribe Polish into
French than into English. Why? Well despite what many people think
about the French language it is actually pretty logical and much more
regular than English. Its reading rules are not that messy and there
are not as many strange edge cases. 



##### How to use the french mode?
You must have the `pytdm` version `0.1.0` or higher installed. 

just add the `lang="fr"` argument or simply `fr` when calling
functions like `mów` or `tłumacz`. To set it back to english set
`lang="en"`.

```python
>>> import pytdm
>>> pytdm.tłumacz("czuję, że będzie dziś dość średni dzień", "fr")
'tchouyé, jé baindjé djich dochtch chrédgni djègn'
>>> pytdm.mów("czuję, że będzie dziś dość średni dzień", "fr")
czuję, że będzie dziś dość średni dzień
```
And there is the function `francyzuj` that works the same as
`anglicyzuj` mentioned before but for French.

---


##### TO DO
* polish the Polish
	* implement pronouncing numbers above 199
	* better handling of numbers mixed-in with words
	* no hardcoded words is the goal
	* better handling of syllables, diphtongs and other strange
      edgecases eg. _je, ej, aj, świe_ etc
* make french mode as good as the standard english one. right now
  there is no pronounciation for numbers implemented in the french mode
* a good idea would be to provide alternative rules of _translation_
  for different operating systems in the future 
* add numbers to the french variant
* some proper documentation for functions and the _translation_
  process. Regexp is [famously](http://regex.info/blog/2006-09-15/247)
  complicated as hell so an entire file
  explaining each of all those patterns etc is not a bad
  idea. 
* optional [`gTTS`](https://pypi.org/project/gTTS/) mode
* extend this list

feel free to fork the github repo and provide some videos:)
