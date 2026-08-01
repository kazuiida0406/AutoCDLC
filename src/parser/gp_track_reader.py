from model.track import Track
from model.note import Note
from model.song import Tempo
from timing.tempo_map import TempoMap


class GPTrackReader:
    """
    GuitarPro Track Reader

    GP5 Track
        ↓
    Track Model
    """


    def __init__(self):

        pass



    # =================================================
    # Read Track
    # =================================================

    def read_track(
        self,
        gp_track,
        song
    ):

        track = Track()


        # -------------------------------
        # Basic Info
        # -------------------------------

        track.name = (
            gp_track.name
            if gp_track.name
            else "Guitar"
        )


        track.instrument = (
            getattr(
                gp_track,
                "instrument",
                "Guitar"
            )
        )


        # -------------------------------
        # Tuning
        # -------------------------------

        if hasattr(
            gp_track,
            "strings"
        ):

            tuning = []

            for string in gp_track.strings:

                tuning.append(
                    string.value
                )

            track.tuning = tuning



        # -------------------------------
        # Tempo
        # -------------------------------

        tempo_map = TempoMap(
            song
        )



        # -------------------------------
        # Measures
        # -------------------------------

        for measure in gp_track.measures:

            for voice in measure.voices:

                for beat in voice.beats:


                    beat_time = (
                        tempo_map.tick_to_time(
                            beat.start
                        )
                    )


                    for gp_note in beat.notes:


                        note = self.convert_note(
                            gp_note,
                            beat_time,
                            tempo_map
                        )


                        track.notes.append(
                            note
                        )



        track.sort_notes()


        return track



    # =================================================
    # Convert Note
    # =================================================

    def convert_note(
        self,
        gp_note,
        time,
        tempo_map
    ):

        note = Note()


        # -------------------------------
        # Position
        # -------------------------------

        note.time = time


        note.string = (
            gp_note.string - 1
        )


        note.fret = (
            gp_note.value
        )



        # -------------------------------
        # Sustain
        # -------------------------------

        duration = (
            getattr(
                gp_note,
                "duration",
                0
            )
        )


        note.sustain = (
            duration
        )



        # -------------------------------
        # Techniques
        # -------------------------------

        effect = (
            getattr(
                gp_note,
                "effect",
                None
            )
        )


        if effect:

            note.hammer_on = (
                getattr(
                    effect,
                    "hammer",
                    False
                )
            )

            note.pull_off = (
                getattr(
                    effect,
                    "pullOff",
                    False
                )
            )

            note.vibrato = (
                getattr(
                    effect,
                    "vibrato",
                    False
                )
            )



        return note