from dataclasses import dataclass


@dataclass
class Event:
    """
    Rocksmith Event Model

    XML events section用
    """


    # ==========================================
    # Position
    # ==========================================

    time: float = 0.0


    # ==========================================
    # Event Code
    # ==========================================

    code: str = ""


    # ==========================================
    # Optional Parameters
    # ==========================================

    value: str = ""


    # ==========================================
    # Helpers
    # ==========================================

    def is_empty(self) -> bool:

        return self.code == ""