from model.chord import Chord



class ChordAnalyzer:
    """
    Chord Analyzer

    Note群からChordを生成する
    """



    def __init__(
        self,
        tolerance=0.05
    ):

        # 同時演奏判定時間差
        self.tolerance = tolerance



    # =================================================
    # Analyze
    # =================================================

    def analyze(
        self,
        track
    ):

        chords = []


        notes = sorted(
            track.notes,
            key=lambda n: n.time
        )


        used = set()



        for i, note in enumerate(notes):

            if i in used:
                continue


            group = [
                note
            ]


            used.add(i)



            # -------------------------
            # 同時発音ノートを収集
            # -------------------------

            for j in range(
                i + 1,
                len(notes)
            ):

                if j in used:
                    continue


                other = notes[j]


                if abs(
                    other.time
                    -
                    note.time
                ) <= self.tolerance:

                    group.append(
                        other
                    )

                    used.add(j)


                else:

                    break



            # 1音はChordにしない

            if len(group) < 2:

                continue



            chord = Chord()

            chord.time = (
                note.time
            )

            chord.notes = (
                group
            )


            chords.append(
                chord
            )



        return chords