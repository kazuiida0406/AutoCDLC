import xml.etree.ElementTree as ET



class XMLSections:
    """
    Rocksmith XML Sections

    Metadata
    Song Structure
    """



    # =====================================================
    # Metadata
    # =====================================================

    def write_metadata(
        self,
        root
    ):


        song = self.arrangement.song

        track = self.arrangement.track



        ET.SubElement(
            root,
            "title"
        ).text = song.title



        ET.SubElement(
            root,
            "arrangement"
        ).text = (
            self.arrangement.arrangement_name
        )



        ET.SubElement(
            root,
            "part"
        ).text = "1"



        ET.SubElement(
            root,
            "offset"
        ).text = (
            f"{self.arrangement.offset:.3f}"
        )



        ET.SubElement(
            root,
            "centOffset"
        ).text = "0"



        length = 0.0


        if track.notes:

            length = max(

                note.time
                +
                note.sustain

                for note in track.notes

            )



        ET.SubElement(
            root,
            "songLength"
        ).text = (
            f"{length:.3f}"
        )



        ET.SubElement(
            root,
            "internalName"
        ).text = song.title



        ET.SubElement(
            root,
            "songNameSort"
        ).text = song.title



        ET.SubElement(
            root,
            "startBeat"
        ).text = "0"



        ET.SubElement(
            root,
            "averageTempo"
        ).text = (

            f"{self.arrangement.average_tempo:.3f}"

        )



        # Tuning

        tuning = ET.SubElement(
            root,
            "tuning"
        )


        for i, value in enumerate(
            track.tuning
        ):

            tuning.set(
                f"string{i}",
                str(value)
            )



        ET.SubElement(
            root,
            "capo"
        ).text = str(
            self.arrangement.capo
        )



        ET.SubElement(
            root,
            "artistName"
        ).text = song.artist



        ET.SubElement(
            root,
            "albumName"
        ).text = song.album



        ET.SubElement(
            root,
            "albumYear"
        ).text = str(
            song.year
        )



        ET.SubElement(
            root,
            "crowdSpeed"
        ).text = str(
            self.arrangement.crowd_speed
        )



        ET.SubElement(
            root,
            "lastConversionDateTime"
        ).text = (
            self.arrangement.last_conversion_time
        )



    # =====================================================
    # EBeats
    # =====================================================

    def write_ebeats(
        self,
        root
    ):


        parent = ET.SubElement(
            root,
            "ebeats",
            {
                "count":
                    str(
                        len(
                            self.arrangement.ebeats
                        )
                    )
            }
        )



        for beat in self.arrangement.ebeats:


            attrs = {

                "time":
                    f"{beat.time:.3f}"

            }


            if beat.measure:

                attrs["measure"] = str(
                    beat.measure
                )


            ET.SubElement(
                parent,
                "ebeat",
                attrs
            )



    # =====================================================
    # Phrases
    # =====================================================

    def write_phrases(
        self,
        root
    ):


        parent = ET.SubElement(
            root,
            "phrases",
            {
                "count":
                    str(
                        len(
                            self.arrangement.phrases
                        )
                    )
            }
        )



        for phrase in self.arrangement.phrases:


            ET.SubElement(
                parent,
                "phrase",
                {

                    "name":
                        phrase.name,


                    "maxDifficulty":
                        str(
                            phrase.max_difficulty
                        ),


                    "disparity":
                        "0",


                    "ignore":
                        "0",


                    "solo":
                        "0"

                }
            )



    # =====================================================
    # Phrase Iterations
    # =====================================================

    def write_phrase_iterations(
        self,
        root
    ):


        parent = ET.SubElement(
            root,
            "phraseIterations",
            {
                "count":
                    str(
                        len(
                            self.arrangement.phrase_iterations
                        )
                    )
            }
        )



        for item in (
            self.arrangement.phrase_iterations
        ):


            ET.SubElement(
                parent,
                "phraseIteration",
                {

                    "time":
                        f"{item.time:.3f}",


                    "phraseId":
                        str(
                            item.phrase_id
                        ),


                    "variation":
                        str(
                            item.variation
                        )

                }
            )



    # =====================================================
    # Linked Diff
    # =====================================================

    def write_new_linked_diffs(
        self,
        root
    ):

        ET.SubElement(
            root,
            "newLinkedDiffs",
            {
                "count":"0"
            }
        )



    def write_linked_diffs(
        self,
        root
    ):

        ET.SubElement(
            root,
            "linkedDiffs",
            {
                "count":"0"
            }
        )