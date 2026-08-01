from dataclasses import dataclass, field



@dataclass
class Chord:
    """
    Chord Model

    Notesをまとめたコード情報
    """



    # ---------------------------------
    # Position
    # ---------------------------------

    time: float = 0.0



    # ---------------------------------
    # Notes
    # ---------------------------------

    notes: list = field(
        default_factory=list
    )



    # ---------------------------------
    # Generated Data
    # ---------------------------------

    chord_id: int = 0



    template_id: int = 0



    # ---------------------------------
    # Difficulty
    # ---------------------------------

    difficulty: int = 0



    # ---------------------------------
    # Helper
    # ---------------------------------

    def add_note(
        self,
        note
    ):

        self.notes.append(
            note
        )