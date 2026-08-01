from model.ebeat import EBeat


class BeatGenerator:
    """
    Rocksmith EBeat Generator

    GPの拍情報から
    Rocksmith用ebeatを生成
    """


    def __init__(
        self,
        ticks_per_beat=960
    ):

        self.ticks_per_beat = (
            ticks_per_beat
        )


    # =================================================
    # Generate
    # =================================================

    def generate(
        self,
        song,
        tempo_map
    ):

        ebeats = []


        max_tick = (
            self.get_end_tick(song)
        )


        tick = 0

        beat_index = 0

        measure = 0


        while tick <= max_tick:


            time = (
                tempo_map.tick_to_time(
                    tick
                )
            )


            # 4拍ごとに小節更新

            if beat_index % 4 == 0:

                measure += 1


            ebeats.append(
                EBeat(
                    time=time,
                    measure=measure
                )
            )


            beat_index += 1


            tick += (
                self.ticks_per_beat
            )


        return ebeats



    # =================================================
    # End Tick
    # =================================================

    def get_end_tick(
        self,
        song
    ):

        end_tick = 0


        for track in song.tracks:

            for note in track.notes:

                if note.tick > end_tick:

                    end_tick = note.tick


        return end_tick