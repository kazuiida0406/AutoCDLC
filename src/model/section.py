from dataclasses import dataclass


@dataclass
class Section:
    """
    Rocksmith Section Model

    曲構成情報

    Example:

    Intro
    Verse
    Chorus
    Solo
    Outro
    """


    # ==========================================
    # Section Number
    # ==========================================

    number: int = 0


    # ==========================================
    # Section Name
    # ==========================================

    name: str = ""


    # ==========================================
    # Start Position
    # ==========================================

    start_time: float = 0.0


    # ==========================================
    # Difficulty
    # ==========================================

    difficulty: int = 0


    # ==========================================
    # Helpers
    # ==========================================

    def is_empty(self) -> bool:

        return self.name == ""