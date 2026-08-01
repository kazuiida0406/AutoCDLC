from dataclasses import dataclass, field


@dataclass
class Level:
    """
    Rocksmith Level Model

    Difficultyごとの譜面データ
    """


    # ==========================================
    # Difficulty
    #
    # 0-3
    # ==========================================

    difficulty: int = 0


    # ==========================================
    # Notes
    # ==========================================

    notes: list = field(
        default_factory=list
    )


    # ==========================================
    # Chords
    # ==========================================

    chords: list = field(
        default_factory=list
    )


    # ==========================================
    # Anchors
    # ==========================================

    anchors: list = field(
        default_factory=list
    )


    # ==========================================
    # Hand Shapes
    # ==========================================

    hand_shapes: list = field(
        default_factory=list
    )


    # ==========================================
    # Helpers
    # ==========================================

    def add_note(
        self,
        note
    ):

        self.notes.append(
            note
        )


    def add_chord(
        self,
        chord
    ):

        self.chords.append(
            chord
        )


    @property
    def note_count(self) -> int:

        return len(
            self.notes
        )


    @property
    def chord_count(self) -> int:

        return len(
            self.chords
        )