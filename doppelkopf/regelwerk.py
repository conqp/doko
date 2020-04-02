"""Regelwerk."""

from typing import Callable, NamedTuple


class Regelwerk(NamedTuple):
    """Eine Regelvariante."""

    ist_trumpf: Callable
    ist_fehl: Callable
    schlägt: Callable
    test: Callable
