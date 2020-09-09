# PyTDM
ie. __Pytońska treść do mowy__ which is Polish for _Python Text To Speech_. Both for standard python and for iOS (iOS version is in the `pythonista` [directory](https://github.com/TichyProgs/PyTDM/blob/master/pythonista/pythonista_README.md))

### ok but why 
This lil library was designed in order to assure that people programming for Pollacks have some sort of a offline-working _text to speech_ python software.
For english speaking people there already is the `pyttsx3` library which provides such functionalities.
If you want your programme to _talk_ you simply run few commands

```python
import pyttsx3
engine = pyttsx3.init()
engine.say("now we're talkin'")
engine.runAndWait()
```
and it's literally that easy! But for Polish there was no such thing until now.

### how it's made
It's based on the same `pyttsx3` package I've just mentioned. The thing is that contrary to what many English speaking people think (looking at u americans) Polish actually __is__ pronounceable for someone knowing English. 

What `PyTDM` does is 

* first it _translates*_ the given polish string/text into english
* then it gets pronounced with the `pyttsx3` 

The asterisk above next to the word "translates" is there for a reason – it's not exactly translation. More like transcription or transliteration.
We shall get back to that later

### usage
An example for how well does the software work with approxima... _translation_ of polish words is to be seen in the `demo.py` file. You just can run it and then see how well it handles the most sacred polish song (actually the second sacred-est. For the most sacred one see `barka.py` (both demo files are in the `demo` directory but you should run them in the same directory `mowa.py` is)) – the anthem of the third republic of Poland. 

But just for simple basic stuff you should do it as follows:

```python
from PyTDM import mowa
mowa.mów("dzień dobry, dobranoc")
```
and then you can happily listen to the sweet sound of the polish language spoken by the `pyttsx3` synthesiser guy. Isn't that great?

### dependencies

all you need are built-in packages like `re` and apart from that the `pyttsx3` package [avalaible on pypi](https://pypi.org/project/pyttsx3/).

###### what OS? 
The only problem is it's different for every OS. Eg windows is stoopid _(per usual)_ and reads 'ch' as /k/ and not /t͡ʃ/. For all I know it works best on iOS but I lack enough feedback to know whether it is fine on Linux and what other issues are there when using windows (+ I highly discourage everyone from using windows. like at all).
###### iOS
for iOS see the `pythonista` directory. Everything there is the iOS version of `PyTDM`

##### Function names are weird?
As a cautious reader might have noticed the main speaking function is `mów` (fyi it means _say_ just like in the `pyttsx3`). One could ask _wthell?_ or more properly __co do diabła?__ but that is exactly how the package was intended to be: the functions have polish names. __Deal with it.__

##### behind the scenes
Now for some calrification about how the so called _translation_ process actually works. 

For every word passed to the `mów` function it is first _tanslated_ by another polish-named func `tłumacz` (ie. __translate__) and it calls 2 more functions first:

* `repolonizuj` ie. __repolonise__ – it deals with all the weird polish ortographic stuff like the diagraphs, some consonants being devoiced etc
* `anglicyzuj` ie. __anglicise__ – it takes the __repolonised__ text and tries to find the closes approximations for all the sounds that are to be found.

only then `mów` gives the anglicised repolonised text to the `engine.say` as shown above.

So when you do something like `mów('czuję, że będzie dziś dość średni dzień')` it first calls `tłumacz` which calls `repolonise`
that returns this simplified polish text:
`'czuje, że bendźe dźiś dość średni dźen'`
and it is passed to the `anglicyzuj` which gives the final result to be said by `pyttsx3`:
`'choo yeah, zsheh behnjeh jeesh dawshtch shrehdnee jehn'`

it sure is amazing



##### TO DO
* saving mp3
* polish the Polish
* implement pronouncing numbers above 199
* extend this list
