from dataclasses import dataclass, field



@dataclass
class Tempo:

    time: float = 0.0

    bpm: float = 120.0




@dataclass
class Song:

    # -------------------------
    # Metadata
    # -------------------------

    title: str = ""

    artist: str = ""

    album: str = ""

    year: int = 0



    # -------------------------
    # Timing
    # -------------------------

    tempos: list[Tempo] = field(
        default_factory=list
    )



    # -------------------------
    # Tracks
    # -------------------------

    tracks: list = field(
        default_factory=list
    )