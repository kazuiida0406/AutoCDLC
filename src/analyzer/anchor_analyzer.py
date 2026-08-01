from model.anchor import Anchor



class AnchorAnalyzer:
    """
    Anchor Generator

    Noteから左手位置を解析
    """



    def __init__(
        self,
        width=4
    ):

        self.width = width



    # =================================================
    # Analyze
    # =================================================

    def analyze(
        self,
        track
    ):

        anchors = []


        notes = sorted(
            track.notes,
            key=lambda n: n.time
        )


        if not notes:

            return anchors



        current_anchor = None



        for note in notes:


            fret = note.fret


            # Open弦は除外

            if fret <= 0:

                continue



            if current_anchor is None:


                current_anchor = (
                    self.create_anchor(
                        note
                    )
                )

                anchors.append(
                    current_anchor
                )

                continue



            # ---------------------------------
            # 現在Anchor範囲内
            # ---------------------------------

            if self.in_range(
                fret,
                current_anchor
            ):

                continue



            # ---------------------------------
            # 範囲外 → 新Anchor
            # ---------------------------------

            current_anchor = (
                self.create_anchor(
                    note
                )
            )


            anchors.append(
                current_anchor
            )



        return anchors



    # =================================================
    # Create Anchor
    # =================================================

    def create_anchor(
        self,
        note
    ):

        anchor = Anchor()


        anchor.time = (
            note.time
        )


        anchor.fret = (
            max(
                0,
                note.fret
            )
        )


        anchor.width = (
            self.width
        )


        return anchor



    # =================================================
    # Range Check
    # =================================================

    def in_range(
        self,
        fret,
        anchor
    ):

        return (
            anchor.fret
            <= fret
            <=
            anchor.fret
            +
            anchor.width
        )