from dataclasses import dataclass, field



@dataclass
class Track:


    # -------------------------
    # Metadata
    # -------------------------

    name: str = ""



    # -------------------------
    # Tuning
    # -------------------------

    # 6弦→1弦
    tuning: list[int] = field(

        default_factory=lambda:

        [
            0,
            0,
            0,
            0,
            0,
            0
        ]

    )



    # -------------------------
    # Notes
    # -------------------------

    notes: list = field(
        default_factory=list
    )



    # -------------------------
    # Generated Data
    # -------------------------

    chords: list = field(
        default_factory=list
    )



    max_difficulty: int = 0