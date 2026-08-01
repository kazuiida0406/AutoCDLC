from model.level import Level



class LevelBuilder:
    """
    Level Builder

    Difficulty別に譜面を構築
    """



    def __init__(self):

        self.max_levels = 4



    # =================================================
    # Generate
    # =================================================

    def generate(
        self,
        arrangement
    ):

        levels = []


        track = (
            arrangement.track
        )


        # ---------------------------------
        # Difficulty 0-3生成
        # ---------------------------------

        for difficulty in range(
            self.max_levels
        ):


            level = Level()


            level.difficulty = (
                difficulty
            )


            # Notes

            level.notes = (

                self.filter_notes(
                    track.notes,
                    difficulty
                )

            )


            # Chords

            level.chords = (

                self.filter_chords(
                    track.chords,
                    difficulty
                )

            )


            # Anchors

            level.anchors = (

                arrangement.anchors

            )


            # HandShapes

            level.hand_shapes = (

                arrangement.hand_shapes

            )


            levels.append(
                level
            )


        return levels



    # =================================================
    # Note Filter
    # =================================================

    def filter_notes(
        self,
        notes,
        difficulty
    ):

        result = []


        for note in notes:


            if note.difficulty <= difficulty:

                result.append(
                    note
                )


        return result



    # =================================================
    # Chord Filter
    # =================================================

    def filter_chords(
        self,
        chords,
        difficulty
    ):

        result = []


        for chord in chords:


            result.append(
                chord
            )


        return result