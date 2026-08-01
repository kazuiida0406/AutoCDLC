from dataclasses import dataclass



@dataclass
class ChordTemplate:
    """
    Rocksmith Chord Template
    """



    # ---------------------------------
    # ID
    # ---------------------------------

    id: int = 0



    # ---------------------------------
    # Name
    # ---------------------------------

    display_name: str = ""


    # 互換用

    name: str = ""



    # ---------------------------------
    # Frets
    # ---------------------------------

    # 6弦→1弦

    frets: tuple[int, ...] = ()



    # ---------------------------------
    # Fingers
    # ---------------------------------

    fingers: tuple[int, ...] = (
        -1,
        -1,
        -1,
        -1,
        -1,
        -1
    )



    # ---------------------------------
    # Sync
    # ---------------------------------

    def __post_init__(self):

        if (
            self.display_name
            and
            not self.name
        ):

            self.name = (
                self.display_name
            )


        elif (
            self.name
            and
            not self.display_name
        ):

            self.display_name = (
                self.name
            )