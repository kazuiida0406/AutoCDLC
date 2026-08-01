from model.hand_shape import HandShape



class HandShapeGenerator:
    """
    Hand Shape Generator

    ChordからHandShapeを生成
    """



    def __init__(self):

        pass



    # =================================================
    # Generate
    # =================================================

    def generate(
        self,
        track
    ):

        shapes = []


        if not track.chords:

            return shapes



        for chord in track.chords:


            shape = (
                self.create_shape(
                    chord
                )
            )


            shapes.append(
                shape
            )



        return shapes



    # =================================================
    # Create
    # =================================================

    def create_shape(
        self,
        chord
    ):

        shape = HandShape()


        # ---------------------------------
        # Start Time
        # ---------------------------------

        shape.start_time = (
            chord.time
        )



        # ---------------------------------
        # End Time
        # ---------------------------------

        shape.end_time = (
            self.calculate_end_time(
                chord
            )
        )



        # ---------------------------------
        # Chord Reference
        # ---------------------------------

        shape.chord_id = (
            getattr(
                chord,
                "chord_id",
                0
            )
        )


        return shape



    # =================================================
    # Calculate End
    # =================================================

    def calculate_end_time(
        self,
        chord
    ):

        end = (
            chord.time
        )


        for note in chord.notes:


            note_end = (
                note.time
                +
                note.sustain
            )


            if note_end > end:

                end = note_end



        return end