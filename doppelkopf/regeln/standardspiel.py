"""Spielregeln."""

from itertools import permutations
from typing import List

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


def ist_trumpf(karte: Karte) -> bool:
    """Prüft, ob die Karte ein Trumpf ist."""

    return karte in TRUMPFFOLGE


def ist_fehl(karte: Karte) -> bool:
    """Prüft, ob die Karte eine Fehlfarbe ist."""#

    return not ist_trumpf(karte)


def schlaegt(zweite: Karte, erste: Karte) -> bool:
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


def bedient(karte: Karte, hand: List[Karte], liegt: Karte) -> bool:
    """Prüft ob die Karte bei den gegebenen Karten auf
    der Hand, die bereits liegende Karte bedient.
    """

    if ist_trumpf(liegt):
        if ist_trumpf(karte):
            return True     # Trumpf bedient Trumpf.

        # Fehl kann abgeworfen werden, wenn alle Karten auf der Hand Fehl sind.
        return all(ist_fehl(karte) for karte in hand)

    if ist_fehl(karte) and karte.farbe == liegt.farbe:
        return True     # Gleiche Fehlfarbe bedient Fehlfarbe.

    # Wenn keine Karte auf der Hand die gleiche Fehlfarbe hat, die liegt, kann
    # eine andere Fehlfarbe abgeworfen werden oder mit Trumpf gestochen werden.
    return all(k.farbe != liegt.farbe for k in filter(ist_fehl, hand))


def test():
    """Testet das Regelwerk."""

    karten = set(get_deck(neunen=True))

    for erste, zweite in permutations(karten, 2):
        if schlaegt(zweite, erste):
            print(zweite, 'schlägt', erste)
        else:
            print(zweite, 'schlägt nicht', erste)


STANDARDSPIEL = Regelwerk(ist_trumpf, ist_fehl, schlaegt, bedient, test)
