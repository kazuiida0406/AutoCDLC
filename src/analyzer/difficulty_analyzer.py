class DifficultyAnalyzer:
    """
    Difficulty Analyzer

    Noteごとの難易度を計算する
    """



    def __init__(self):

        pass



    # =================================================
    # Analyze
    # =================================================

    def analyze(
        self,
        track
    ):

        if not track.notes:

            return



        for note in track.notes:


            difficulty = (
                self.calculate(
                    note
                )
            )


            note.difficulty = (
                difficulty
            )



        track.max_difficulty = max(

            note.difficulty

            for note in track.notes

        )



    # =================================================
    # Calculate Difficulty
    # =================================================

    def calculate(
        self,
        note
    ):

        score = 0



        # -------------------------
        # Fret Position
        # -------------------------

        if note.fret >= 12:

            score += 1


        if note.fret >= 17:

            score += 1



        # -------------------------
        # Techniques
        # -------------------------

        if note.hammer_on:

            score += 1


        if note.pull_off:

            score += 1


        if note.slide_to >= 0:

            score += 1


        if note.bend > 0:

            score += 1


        if note.vibrato:

            score += 1



        # -------------------------
        # Sustain
        # -------------------------

        if note.sustain > 2.0:

            score += 1



        # -------------------------
        # Convert
        # -------------------------

        if score <= 1:

            return 0


        elif score <= 3:

            return 1


        elif score <= 5:

            return 2


        else:

            return 3