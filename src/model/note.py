from dataclasses import dataclass



@dataclass
class Note:
    """
    Guitar Note Model

    GP5/GuitarPro
    ↓
    Rocksmith Note
    """



    # =================================================
    # Position
    # =================================================

    tick: int = 0


    time: float = 0.0


    # 0=6弦
    # 5=1弦

    string: int = 0


    fret: int = 0



    # =================================================
    # Duration
    # =================================================

    sustain: float = 0.0



    # GP互換用

    duration: float = 0.0



    # =================================================
    # Difficulty
    # =================================================

    difficulty: int = 0


    priority: int = 0



    # =================================================
    # Techniques
    # =================================================

    hammer_on: bool = False


    pull_off: bool = False


    slide_to: int = -1


    slide_unpitch_to: int = -1


    bend: float = 0.0


    vibrato: bool = False


    harmonic: bool = False


    harmonic_pinch: bool = False


    palm_mute: bool = False


    mute: bool = False


    tremolo: bool = False


    tap: bool = False


    slap: bool = False


    pluck: bool = False


    accent: bool = False


    link_next: bool = False


    ignore: bool = False



    # =================================================
    # Hand
    # =================================================

    left_hand: int = -1


    finger: int = -1



    # =================================================
    # Picking
    # =================================================

    pick_direction: int = 0



    # =================================================
    # Pitch
    # =================================================

    pitch: int = 0



    # =================================================
    # Post Init
    # =================================================

    def __post_init__(self):

        """
        GP形式 duration
        Rocksmith形式 sustain
        の同期
        """


        if self.sustain == 0.0:

            self.sustain = (
                self.duration
            )


        elif self.duration == 0.0:

            self.duration = (
                self.sustain
            )