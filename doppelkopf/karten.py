"""Spielkarten."""

from enum import Enum
from itertools import product, repeat
from typing import NamedTuple


__all__ = ['Farbe', 'Bild', 'Karte']


class Farbe(Enum):
    """Farben der Spielkarten."""

    KARO = 'Karo'
    HERZ = 'Herz'
    PIK = 'Pik'
    KREUZ = 'Kreuz'

    def __str__(self):
        return self.value


class Bild(Enum):
    """Bilder der Karten."""

    ASS = 'Ass'
    KÖNIG = 'König'
    DAME = 'Dame'
    BUBE = 'Bube'
    ZEHN = 10
    NEUN = 9

    def __str__(self):
        return str(self.value)


class Karte(NamedTuple):
    """Eine Spielkarte."""

    farbe: Farbe
    bild: Bild

    def __str__(self):
        return f'{self.farbe} {self.bild}'


def get_deck(neunen=True):
    """Gibt ein Kartendeck zurück."""

    if neunen:
        bilder = set(Bild)
    else:
        bilder = {Bild.ASS, Bild.KÖNIG, Bild.DAME, Bild.BUBE, Bild.ZEHN}

    for farbe, bild in product(Farbe, bilder):
        for karte in repeat(Karte(farbe, bild), 2):
            yield karte
