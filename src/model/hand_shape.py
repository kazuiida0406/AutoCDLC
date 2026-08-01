from dataclasses import dataclass


@dataclass
class HandShape:
    """
    Rocksmith Hand Shape Model

    左手フォーム情報
    """


    # ==========================================
    # Time Range
    # ==========================================

    start_time: float = 0.0

    end_time: float = 0.0


    # ==========================================
    # Chord Reference
    # ==========================================

    chord_id: int = 0


    # ==========================================
    # Difficulty
    # ==========================================

    difficulty: int = 0


    # ==========================================
    # Helpers
    # ==========================================

    @property
    def duration(self) -> float:

        return (
            self.end_time
            - self.start_time
        )