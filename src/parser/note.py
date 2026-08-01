from dataclasses import dataclass

@dataclass
class Note:

    tick: int
    time: float

    string: int
    fret: int
    duration: int

    # ---------- Techniques ----------
    hammer_on: bool = False
    pull_off: bool = False

    slide_to: int = -1

    bend: float = 0.0

    vibrato: bool = False

    harmonic: bool = False

    palm_mute: bool = False

    tremolo: bool = False

    dead_note: bool = False

    ghost_note: bool = False

    accent: bool = False

    tie: bool = False