# PyTDM
ie. __Pytońska treść do mowy__ which is Polish for _Python Text to Speech_. Package for turning text written in Polish into speech.

Both for standard Python3 and for iOS.

### ok but why 
This lil library was designed in order to assure that people programming for Pollacks have some sort of an offline-working _text to speech_ python software.
For English speaking people there already is the [`pyttsx3`](https://pypi.org/project/pyttsx3/) library which provides such functionalities.
If you want your programme to _talk_ you simply run few commands

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

### how it's made
It's based on the `pyttsx3` package I've just mentioned. The thing is that contrary to what many English speaking people think (looking at u americans) Polish actually __is__ pronounceable for someone knowing English. 

What `PyTDM` does is 

* first it _translates*_ the given polish string/text into english
* then it gets pronounced with the `pyttsx3` 

The asterisk above next to the word "translates" is there for a reason – it's not exactly translation. More like transcription or transliteration.
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
and then you can happily listen to the sweet sound of the polish language spoken by the `pyttsx3` synthesiser voice. Isn't that great?

###### little disclaimer
the functions have Polish names like `mów` or `tłumacz` with those funny strange letter but if you want you can use them without the diacritics eg. write `mow` or `tlumacz`. They will work just fine.

In general if have any problems first you can type eg. `help(pytdm.mow)` and read the info provided there.


##### examples
An example for how well does the software work with approxima... _translation_ of polish words is to be seen in the `demo.py` file (avalaible on [my github](https://github.com/test0wanie/PyTDM)). You just can run it and then see how well it handles the most sacred polish song (actually the second sacred-est. For the most sacred one see `barka.py`. Both demo files are in the __[`demos`](https://github.com/test0wanie/PyTDM/tree/master/demos)__ github directory) – the anthem of the Third Polish Republic. 

There is a video showing how the `demo.py` file works (recorded in low quality by me and posted on youtube) [here](https://youtu.be/bHWxwoAm0OE).


### dependencies

all you need are built-in packages like `re` and apart from that the `pyttsx3` package (`v>=2.7`). It is [avalaible on pypi](https://pypi.org/project/pyttsx3/) so you can just do the classic:

```
pip install pyttsx3
```
### what OS? 
The only problem is it's different for every OS. 

* For all I know it works really well on __macOS__ – I use this OS myself therefore I can easily test that there and adjust it respectively. 

For other OS I have only some feedback from other people:

* __Windows__ is stoopid _(per usual)_ and reads 'ch' as /k/ and not /t͡ʃ/. Apart from that and _maybe_ some other mistakes it is fine. 
* it's not bad on __Linux__ but it has problems with eg. consonant clusters like _szcz_. When it tries to pronounce them as _shtch_ it spells (_es aitch tee cee aitch..._) the cluster instead of just just saying /ʃt͡ʃ/ as other versions tend to do. Also it sounds robotic which is _w e i r d_

__In conclusion:__ it works ok for all of them but some sounds are realised differently on different OSs.

###### mobile versions – iOS
for __iOS__ see the __`pythonista`__ [directory on github](https://github.com/test0wanie/PyTDM/blob/master/pythonista/README_iOS.md). Everything there is the iOS version of `PyTDM`.


#### Function names are weird?
As a cautious reader might have noticed the main speaking function is `mów` (fyi it means _say_ just like in the `pyttsx3`). One could ask _wthell?_ or more properly __co do diabła?__ but that is exactly how the package was intended to be: the functions have polish names. __Deal with it.__

##### behind the scenes
Now for some calrification about how the so called _translation_ process actually works. 

For every word passed to the `mów` function it is first _tanslated_ by another polish-named func `tłumacz` (ie. __translate__) and it calls 2 more functions first:

* `repolonizuj` ie. __repolonise__ – it deals with all the weird polish ortographic stuff like the diagraphs, some consonants being devoiced etc. **_[Futuryści](https://pl.wikisource.org/wiki/Mańifest_w_sprawie_ortografji_fonetycznej)_** inspired
 
* `anglicyzuj` ie. __anglicise__ – it takes the __repolonised__ text and tries to find the closest approximations for all the sounds that are to be found. It's doingit's best.

only then `mów` gives the anglicised repolonised text to the `engine.say` as shown above.

So when you do something like `mów('czuję, że będzie dziś dość średni dzień')` it first calls `tłumacz` which calls `repolonizuj`
that returns this simplified polish text:
`'czuje, że bendźe dźiś dość średni dźen'`
and it is passed to the `anglicyzuj` which gives the final result to be said by `pyttsx3`:

`'choo yeah, zshehh behnjehh jeesh dawshtch shrehdnee jehn'`

it sure is amazing.

##### TO DO
* saving mp3s (to do before `v0.1.0`)
* polish the Polish
	* implement pronouncing numbers above 199
	* better handling of numbers mixed-in with words
	* no hardcoded words is the goal
	* better handling of syllables, diphtongs and other strange edgecases eg. _je, ej, aj, świe_ etc
* a good idea would be to provide alternative rules of _translation_ for different operating systems in the future
* some proper documentation for functions and the _translation_ process
* optional [`gTTS`](https://pypi.org/project/gTTS/) mode
* extend this list

feel free to fork the github repo and provide some videos:)
