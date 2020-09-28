from pytdm import mów, tłumacz
from termcolor import colored

hymn = """Jeszcze Polska nie zginęła,
Kiedy my żyjemy. 
Co nam obca przemoc wzięła,
Szablą odbierzemy.

Marsz, marsz, Dąbrowski,
Z ziemi włoskiej do Polski.
Za twoim przewodem
Złączym się z narodem.

Przejdziem Wisłę, przejdziem Wartę,
Będziem Polakami.
Dał nam przykład Bonaparte,
Jak zwyciężać mamy.

Marsz, marsz, Dąbrowski...

Jak Czarniecki do Poznania
Po szwedzkim zaborze,
Dla ojczyzny ratowania
Wrócim się przez morze.

Marsz, marsz, Dąbrowski...

Już tam ojciec do swej Basi
Mówi zapłakany –
Słuchaj jeno, pono nasi
Biją w tarabany.

Marsz, marsz, Dąbrowski..."""

zwrotki = hymn.split("\n\n")

print(colored(tłumacz("Zaśpiewam hymn Rzeczpospolitej Polski!", "fr"), "yellow"))
mów("Zaśpiewam hymn Rzeczpospolitej Polski!\n", lang="fr")
for zwrotka in zwrotki:
    print(colored(tłumacz(zwrotka, "fr"), "yellow"))
    mów(zwrotka, lang="fr")
    print("\n\n")
