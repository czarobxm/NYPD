
from .gminy import czyt_pit_gminy
from .gminy import czyt_ludnosc_gminy

from .powiaty import czyt_pit_powiaty
from .powiaty import czyt_ludnosc_powiaty
from .powiaty import czyt_pit_powiaty_miasta_npp

from .wojewodztwa import czyt_pit_wojewodztwa
from .wojewodztwa import czyt_ludnosc_wojewodztwa

from .testy import testy_czyt_pit





__all__ = ("czyt_pit_gminy", "czyt_ludnosc_gminy",
            "czyt_pit_powiaty", "czyt_ludnosc_powiaty", "czyt_pit_powiaty_miasta_npp",
            "czyt_pit_wojewodztwa", "czyt_ludnosc_wojewodztwa",
            "testy_czyt_pit"
            )