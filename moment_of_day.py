from enum import Enum

class MomentOfDay(Enum):
    START_MORNING = "débutMatin"
    END_MORNING = "finMatin"
    START_AFTERNOON = "débutAprèsMidi"
    END_AFTERNOON = "finAprèsMidi"
    START_MORNING_FULL = "Début matin"
    END_MORNING_FULL = "Fin matin"
    START_AFTERNOON_FULL = "Début après-midi"
    END_AFTERNOON_FULL = "Fin après-midi"