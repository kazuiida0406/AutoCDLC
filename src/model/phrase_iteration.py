from dataclasses import dataclass



@dataclass
class PhraseIteration:
    """
    Rocksmith Phrase Iteration Model

    XML:
    <phraseIterations>
        <phraseIteration>
    """



    # ==========================================
    # Phrase Reference
    # ==========================================

    phrase_id: int = 0



    # ==========================================
    # Time
    # ==========================================

    time: float = 0.0



    # ==========================================
    # Variation
    # ==========================================

    variation: int = 0



    # ==========================================
    # Helper
    # ==========================================

    def __repr__(self):

        return (
            f"PhraseIteration("
            f"phrase_id={self.phrase_id}, "
            f"time={self.time}"
            f")"
        )