from dataclasses import dataclass


@dataclass
class ToneChange:
    """
    Rocksmith Tone Change Model

    Toneの切替イベント
    """


    # ==========================================
    # Position
    # ==========================================

    time: float = 0.0


    # ==========================================
    # Tone Name
    # ==========================================

    tone: str = "tone_base"


    # ==========================================
    # Helpers
    # ==========================================

    def get_id(self) -> int:
        """
        XML用Tone ID取得
        """

        tone_table = {

            "tone_base": 0,

            "tone_a": 1,

            "tone_b": 2,

            "tone_c": 3,

            "tone_d": 4,
        }


        return tone_table.get(
            self.tone,
            0
        )