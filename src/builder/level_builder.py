from model.level import Level



class LevelBuilder:
    """
    Ver4.5 Final

    Difficulty Level Generator
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


        track = arrangement.track



        if track is None:

            return levels



        for difficulty in range(
            self.max_levels
        ):


            level = Level()



            level.difficulty = (
                difficulty
            )



            level.notes = (

                self.filter_notes(
                    track.notes,
                    difficulty
                )

            )



            level.chords = (

                self.filter_chords(
                    getattr(
                        track,
                        "chords",
                        []
                    ),
                    difficulty
                )

            )



            level.anchors = list(
                arrangement.anchors
            )



            level.hand_shapes = list(
                arrangement.hand_shapes
            )



            levels.append(
                level
            )



        return levels



    # =================================================
    # Notes
    # =================================================

    def filter_notes(
        self,
        notes,
        difficulty
    ):


        result = []



        for note in notes:


            if getattr(
                note,
                "difficulty",
                0
            ) <= difficulty:


                result.append(
                    note
                )



        return result



    # =================================================
    # Chords
    # =================================================

    def filter_chords(
        self,
        chords,
        difficulty
    ):


        return list(
            chords
        )