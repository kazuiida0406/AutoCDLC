from model.event import Event



class EventGenerator:
    """
    Event Generator

    Arrangement用イベント生成
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

        events = []


        # ---------------------------------
        # Sectionsからイベント生成
        # ---------------------------------

        for section in arrangement.sections:


            event = Event()


            event.time = (
                section.start_time
            )


            event.code = (
                "section"
            )


            event.value = (
                section.name
            )


            events.append(
                event
            )



        return events