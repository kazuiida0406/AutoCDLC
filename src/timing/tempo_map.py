from model.tempo import Tempo



class TempoMap:
    """
    Tempo Map

    tick
      ↓
    seconds

    Ver4.5 Final
    """



    PPQ = 960



    def __init__(
        self,
        song
    ):


        self.tempos = []


        if hasattr(
            song,
            "tempos"
        ):

            self.tempos = song.tempos



        if not self.tempos:

            self.tempos.append(

                Tempo(

                    time=0.0,

                    bpm=120.0

                )

            )



    # =================================================
    # Tick -> Time
    # =================================================

    def tick_to_time(
        self,
        tick
    ):


        bpm = (

            self.tempos[0].bpm

        )


        seconds_per_tick = (

            60.0
            /
            (
                bpm
                *
                self.PPQ
            )

        )


        return (

            tick
            *
            seconds_per_tick

        )



    # =================================================
    # Beat Time
    # =================================================

    def beat_to_time(
        self,
        beat
    ):


        bpm = (

            self.tempos[0].bpm

        )


        return (

            beat
            *
            60.0
            /
            bpm

        )



    # =================================================
    # BPM
    # =================================================

    def get_bpm(
        self,
        time=0.0
    ):


        for tempo in reversed(
            self.tempos
        ):


            if tempo.time <= time:

                return tempo.bpm



        return 120.0