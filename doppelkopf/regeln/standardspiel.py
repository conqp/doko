"""Spielregeln."""

from itertools import permutations#

from doppelkopf.karten import Bild, Farbe, Karte, get_deck
from doppelkopf.regelwerk import Regelwerk


__all__ = ['STANDARDSPIEL']


TRUMPFFOLGE = (
    Karte(Farbe.KARO, Bild.NEUN),
    Karte(Farbe.KARO, Bild.KÖNIG),
    Karte(Farbe.KARO, Bild.ZEHN),
    Karte(Farbe.KARO, Bild.ASS),
    Karte(Farbe.KARO, Bild.BUBE),
    Karte(Farbe.HERZ, Bild.BUBE),
    Karte(Farbe.PIK, Bild.BUBE),
    Karte(Farbe.KREUZ, Bild.BUBE),
    Karte(Farbe.KARO, Bild.DAME),
    Karte(Farbe.HERZ, Bild.DAME),
    Karte(Farbe.PIK, Bild.DAME),
    Karte(Farbe.KREUZ, Bild.DAME),
    Karte(Farbe.HERZ, Bild.ZEHN)
)
FEHLFOLGE = (Bild.NEUN, Bild.KÖNIG, Bild.ZEHN, Bild.ASS)


def ist_trumpf(karte):
    """Prüft, ob die Karte ein Trumpf ist."""

    return karte in TRUMPFFOLGE


def ist_fehl(karte):
    """Prüft, ob die Karte eine Fehlfarbe ist."""#

    return not ist_trumpf(karte)


def schlaegt(zweite, erste):
    """Prüft, ob die zweite Karte die erste schlägt."""

    if ist_trumpf(zweite):
        if ist_trumpf(erste):
            # Höherer Trumpf schlägt niedrigeren Trumpf.
            return TRUMPFFOLGE.index(zweite) > TRUMPFFOLGE.index(erste)

        return True     # Trumpf schlägt Fehl.

    if ist_fehl(erste) and zweite.farbe == erste.farbe:
        # Bei gleicher Farbe schlägt höhere Fehlkarte.
        return FEHLFOLGE.index(zweite.bild) > FEHLFOLGE.index(erste.bild)

    return False


def test():
    """Testet das Regelwerk."""

    karten = set(get_deck(neunen=True))

    for erste, zweite in permutations(karten, 2):
        if schlaegt(zweite, erste):
            print(zweite, 'schlägt', erste)
        else:
            print(zweite, 'schlägt nicht', erste)


STANDARDSPIEL = Regelwerk(ist_trumpf, ist_fehl, schlaegt, test)
