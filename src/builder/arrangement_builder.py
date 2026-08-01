from datetime import datetime


from model.arrangement import Arrangement


from analyzer.anchor_analyzer import AnchorAnalyzer
from analyzer.chord_analyzer import ChordAnalyzer
from analyzer.chord_template_generator import ChordTemplateGenerator
from analyzer.difficulty_analyzer import DifficultyAnalyzer
from analyzer.event_generator import EventGenerator
from analyzer.handshape_generator import HandShapeGenerator
from analyzer.phrase_generator import PhraseGenerator
from analyzer.tone_generator import ToneGenerator


from timing.tempo_map import TempoMap
from timing.beat_generator import BeatGenerator


from builder.level_builder import LevelBuilder




class ArrangementBuilder:
    """
    Arrangement Builder

    Song
      ↓
    Arrangement
      ↓
    Rocksmith XML Data
    """



    def __init__(self):


        self.chord_analyzer = (
            ChordAnalyzer()
        )


        self.anchor_analyzer = (
            AnchorAnalyzer()
        )


        self.template_generator = (
            ChordTemplateGenerator()
        )


        self.handshape_generator = (
            HandShapeGenerator()
        )


        self.difficulty_analyzer = (
            DifficultyAnalyzer()
        )


        self.event_generator = (
            EventGenerator()
        )


        self.tone_generator = (
            ToneGenerator()
        )


        self.phrase_generator = (
            PhraseGenerator()
        )


        self.level_builder = (
            LevelBuilder()
        )


        self.beat_generator = (
            BeatGenerator()
        )



    # =================================================
    # Build
    # =================================================

    def build(
        self,
        song,
        track_index=0
    ):


 


        arrangement = Arrangement()



        # ------------------------------------------------
        # Source
        # ------------------------------------------------

        arrangement.song = song



        if not song.tracks:

            raise ValueError(
                "No tracks found"
            )



        arrangement.track = (

            song.tracks[
                track_index
            ]

        )



        track = arrangement.track



        # ------------------------------------------------
        # Metadata
        # ------------------------------------------------

        arrangement.arrangement_name = (
            "Lead"
        )


        arrangement.average_tempo = (

            song.tempos[0].bpm

            if song.tempos

            else 120.0

        )


        arrangement.capo = 0


        arrangement.offset = 0.0


        arrangement.last_conversion_time = (

            datetime.now()
            .strftime(
                "%m-%d-%Y %H:%M"
            )

        )



        # ------------------------------------------------
        # Length
        # ------------------------------------------------

        arrangement.song_length = (

            self.get_length(
                track
            )

        )



        # ------------------------------------------------
        # Timing
        # ------------------------------------------------

        tempo_map = TempoMap(
            song
        )


        arrangement.ebeats = (

            self.beat_generator.generate(
                song,
                tempo_map
            )

        )



        # ------------------------------------------------
        # Analyze
        # ------------------------------------------------


        track.chords = (

            self.chord_analyzer.analyze(
                track
            )

        )



        arrangement.anchors = (

            self.anchor_analyzer.analyze(
                track
            )

        )



        self.difficulty_analyzer.analyze(
            track
        )



        # ------------------------------------------------
        # Generate
        # ------------------------------------------------


        arrangement.chord_templates = (

            self.template_generator.generate(
                track
            )

        )



        arrangement.hand_shapes = (

            self.handshape_generator.generate(
                track
            )

        )



        arrangement.phrases = (

            self.phrase_generator.generate_iterations(
                arrangement
            )

        )



        arrangement.phrase_iterations = []



        arrangement.events = (

            self.event_generator.generate(
                arrangement
            )

        )



        arrangement.tone_changes = (

            self.tone_generator.generate(
                arrangement
            )

        )



        # ------------------------------------------------
        # Levels
        # ------------------------------------------------


        arrangement.levels = (

            self.level_builder.generate(
                arrangement
            )

        )





        return arrangement




    # =================================================
    # Song Length
    # =================================================

    def get_length(
        self,
        track
    ):


        length = 0.0



        for note in track.notes:


            end = (

                note.time

                +
                note.sustain

            )


            if end > length:

                length = end



        return length