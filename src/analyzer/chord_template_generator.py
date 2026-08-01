from model.chord_template import ChordTemplate


class ChordTemplateGenerator:
    """
    Chord Template Generator

    ChordからRocksmith用コードフォームを生成
    """



    def __init__(self):

        self.templates = {}



    # =================================================
    # Generate
    # =================================================

    def generate(
        self,
        track
    ):

        result = []


        for chord in track.chords:


            template = (
                self.create_template(
                    chord
                )
            )


            if template.id == -1:

                continue


            result.append(
                template
            )


        return self.unique_templates(
            result
        )



    # =================================================
    # Create Template
    # =================================================

    def create_template(
        self,
        chord
    ):

        frets = [
            -1,
            -1,
            -1,
            -1,
            -1,
            -1
        ]


        fingers = [
            -1,
            -1,
            -1,
            -1,
            -1,
            -1
        ]



        for note in chord.notes:


            string = note.string


            if 0 <= string < 6:

                frets[string] = (
                    note.fret
                )



        key = tuple(
            frets
        )



        if key in self.templates:

            return self.templates[key]



        template = ChordTemplate()


        template.id = (
            len(
                self.templates
            )
        )


        template.name = (
            self.generate_name(
                frets
            )
        )


        template.frets = (
            tuple(
                frets
            )
        )


        template.fingers = (
            tuple(
                fingers
            )
        )



        self.templates[key] = template


        return template



    # =================================================
    # Name Generator
    # =================================================

    def generate_name(
        self,
        frets
    ):

        if all(
            f == -1
            for f in frets
        ):

            return "Mute"


        return (
            "Chord_"
            +
            "_".join(
                str(f)
                for f in frets
            )
        )



    # =================================================
    # Remove Duplicate
    # =================================================

    def unique_templates(
        self,
        templates
    ):

        result = []

        seen = set()


        for template in templates:

            key = (
                template.frets
            )


            if key in seen:

                continue


            seen.add(key)


            result.append(
                template
            )


        return result