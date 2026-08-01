from model.song import Song
from model.track import Track
from model.note import Note
from model.tempo import Tempo



class GPReader:
    """
    GuitarPro Reader

    Ver4.5 Final

    GP5
      ↓
    Internal Model
    """



    def __init__(
        self,
        filepath
    ):

        self.filepath = filepath

        self.gp_song = None

        self.song = Song()



        self.load()



    # =================================================
    # Load GP
    # =================================================

    def load(self):

        import guitarpro



        self.gp_song = (

            guitarpro.parse(
                self.filepath
            )

        )



    # =================================================
    # Public
    # =================================================

    def get_song(
        self
    ):


        self.read_metadata()

        self.read_tempos()

        self.read_tracks()


        return self.song



    # =================================================
    # Metadata
    # =================================================

    def read_metadata(
        self
    ):


        self.song.title = (

            getattr(
                self.gp_song,
                "title",
                "Unknown"
            )

        )


        self.song.artist = (

            getattr(
                self.gp_song,
                "artist",
                ""
            )

        )


        self.song.album = (

            getattr(
                self.gp_song,
                "album",
                ""
            )

        )



    # =================================================
    # Tempo
    # =================================================

    def read_tempos(
        self
    ):


        self.song.tempos = []



        bpm = 120



        if hasattr(
            self.gp_song,
            "tempo"
        ):


            bpm = (

                self.gp_song.tempo

            )



        self.song.tempos.append(

            Tempo(

                time=0.0,

                bpm=float(
                    bpm
                )

            )

        )



    # =================================================
    # Tracks
    # =================================================

    def read_tracks(
        self
    ):


        self.song.tracks = []



        for gp_track in self.gp_song.tracks:



            track = Track()



            track.name = (

                getattr(
                    gp_track,
                    "name",
                    "Guitar"
                )

            )



            track.notes = []



            self.read_notes(

                gp_track,

                track

            )



            self.song.tracks.append(

                track

            )



    # =================================================
    # Notes
    # =================================================

    def read_notes(
        self,
        gp_track,
        track
    ):


        for measure in gp_track.measures:


            for voice in measure.voices:


                for beat in voice.beats:


                    for gp_note in beat.notes:



                        note = Note()



                        note.time = (

                            self.convert_time(
                                beat.start
                            )

                        )



                        note.duration = (

                            self.convert_time(
                                beat.duration
                            )

                        )



                        note.string = (

                            getattr(
                                gp_note,
                                "string",
                                1
                            )
                            -
                            1

                        )



                        note.fret = (

                            getattr(
                                gp_note,
                                "value",
                                0
                            )

                        )



                        note.difficulty = 0



                        track.notes.append(

                            note

                        )



    # =================================================
    # Time Convert
    # =================================================

    def convert_time(
        self,
        value
    ):


        try:

            return float(
                value
            )

        except:


            return 0.0