from model.tone_change import ToneChange



class ToneGenerator:
    """
    Tone Change Generator

    Rocksmith Tone情報生成
    """



    def __init__(self):

        pass



    # =================================================
    # Generate
    # =================================================

    def generate(
        self,
        arrangement
    ):

        tones = []


        # ---------------------------------
        # Default Tone
        # ---------------------------------

        base = ToneChange()


        base.time = 0.0


        base.tone = (
            "tone_base"
        )


        tones.append(
            base
        )



        # ---------------------------------
        # Section Based Tone
        # ---------------------------------

        for section in arrangement.sections:


            name = (
                section.name.lower()
            )


            if (
                "solo" in name
                or
                "lead" in name
            ):


                tone = ToneChange()


                tone.time = (
                    section.start_time
                )


                tone.tone = (
                    "tone_lead"
                )


                tones.append(
                    tone
                )



        return tones