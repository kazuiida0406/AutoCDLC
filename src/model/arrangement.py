from dataclasses import dataclass, field



@dataclass
class Arrangement:
    """
    Rocksmith Arrangement Model

    Ver4.5 Final Core

    Song
      ↓
    Arrangement
      ↓
    XML Writer
    """



    # ==========================================
    # Source
    # ==========================================

    song: object = None


    track: object = None



    # ==========================================
    # Metadata
    # ==========================================

    arrangement_name: str = "Lead"


    arrangement_type: str = "Lead"


    average_tempo: float = 120.0


    capo: int = 0


    offset: float = 0.0


    last_conversion_time: str = ""



    # ==========================================
    # Song Info
    # ==========================================

    song_length: float = 0.0



    # ==========================================
    # Song Structure
    # ==========================================

    ebeats: list = field(
        default_factory=list
    )


    phrases: list = field(
        default_factory=list
    )


    phrase_iterations: list = field(
        default_factory=list
    )


    sections: list = field(
        default_factory=list
    )



    # ==========================================
    # Musical Data
    # ==========================================

    chord_templates: list = field(
        default_factory=list
    )


    anchors: list = field(
        default_factory=list
    )


    hand_shapes: list = field(
        default_factory=list
    )


    events: list = field(
        default_factory=list
    )


    tone_changes: list = field(
        default_factory=list
    )


    fret_hand_mutes: list = field(
        default_factory=list
    )



    # ==========================================
    # Difficulty
    # ==========================================

    levels: list = field(
        default_factory=list
    )



    # ==========================================
    # XML
    # ==========================================

    version: int = 7


    persistent_id: str = ""


    master_id: int = 0


    crowd_speed: int = 1



    # ==========================================
    # Helper
    # ==========================================

    def add_level(
        self,
        level
    ):

        self.levels.append(
            level
        )



    def add_event(
        self,
        event
    ):

        self.events.append(
            event
        )