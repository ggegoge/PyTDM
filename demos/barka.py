from pytdm import mów

hymn = """Pan kiedyś stanął nad brzegiem, 
Szukał ludzi gotowych pójść za Nim; 
By łowić serca 
Słów Bożych prawdą.

 
O Panie, to Ty na mnie spojrzałeś, 
Twoje usta dziś wyrzekły me imię. 
Swoją barkę pozostawiam na brzegu, 
Razem z Tobą nowy zacznę dziś łów. 


Jestem ubogim człowiekiem, 
Moim skarbem są ręce gotowe 
Do pracy z Tobą, 
I czyste serce. 


O Panie, to Ty na mnie spojrzałeś, 
Twoje usta dziś wyrzekły me imię. 
Swoją barkę pozostawiam na brzegu, 
Razem z Tobą nowy zacznę dziś łów. 


Ty, potrzebujesz mych dłoni, 
Mego serca młodego zapałem 
Mych kropli potu, 
I samotności. 


O Panie, to Ty na mnie spojrzałeś, 
Twoje usta dziś wyrzekły me imię. 
Swoją barkę pozostawiam na brzegu, 
Razem z Tobą nowy zacznę dziś łów. 


Dziś wypłyniemy już razem, 
Łowić serca na morzach dusz ludzkich 
Twej prawdy siecią, 
I słowem życia. 
"""

zwrotki = hymn.split('\n\n')

mów('Zaśpiewam ulubioną pieśń ojca świętego Jana Pawła drugiego!\n')
for zwrotka in zwrotki:
	mów(zwrotka)
	print('\n\n')
