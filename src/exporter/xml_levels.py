import xml.etree.ElementTree as ET



class XMLLevels:
    """
    Rocksmith XML Levels

    Notes / Chords / Anchors
    """



    # =====================================================
    # Levels
    # =====================================================

    def write_levels(
        self,
        root
    ):


        levels = ET.SubElement(
            root,
            "levels",
            {
                "count":
                    str(
                        len(
                            self.arrangement.levels
                        )
                    )
            }
        )



        for level in (
            self.arrangement.levels
        ):


            node = ET.SubElement(
                levels,
                "level",
                {

                    "difficulty":
                        str(
                            level.difficulty
                        )

                }
            )


            self.write_notes(
                node,
                level.notes
            )


            self.write_chords(
                node,
                level.chords
            )


            self.write_anchors(
                node,
                level.anchors
            )


            self.write_hand_shapes(
                node,
                level.hand_shapes
            )



    # =====================================================
    # Notes
    # =====================================================

    def write_notes(
        self,
        root,
        notes
    ):


        parent = ET.SubElement(
            root,
            "notes",
            {
                "count":
                    str(
                        len(notes)
                    )
            }
        )



        for note in notes:


            attrs = {

                "time":
                    f"{note.time:.3f}",


                "string":
                    str(
                        note.string
                    ),


                "fret":
                    str(
                        note.fret
                    ),


                "sustain":
                    f"{note.sustain:.3f}"

            }



            if note.hammer_on:

                attrs["hammerOn"] = "1"


            if note.pull_off:

                attrs["pullOff"] = "1"



            if note.slide_to >= 0:

                attrs["slideTo"] = (
                    str(
                        note.slide_to
                    )
                )


            if note.bend > 0:

                attrs["bend"] = (
                    str(
                        note.bend
                    )
                )


            ET.SubElement(
                parent,
                "note",
                attrs
            )



    # =====================================================
    # Chords
    # =====================================================

    def write_chords(
        self,
        root,
        chords
    ):


        parent = ET.SubElement(
            root,
            "chords",
            {
                "count":
                    str(
                        len(chords)
                    )
            }
        )



        for chord in chords:


            ET.SubElement(
                parent,
                "chord",
                {

                    "time":
                        f"{chord.time:.3f}",


                    "chordId":
                        str(
                            getattr(
                                chord,
                                "chord_id",
                                0
                            )
                        )

                }
            )



    # =====================================================
    # Anchors
    # =====================================================

    def write_anchors(
        self,
        root,
        anchors
    ):


        parent = ET.SubElement(
            root,
            "anchors",
            {
                "count":
                    str(
                        len(anchors)
                    )
            }
        )



        for anchor in anchors:


            ET.SubElement(
                parent,
                "anchor",
                {

                    "time":
                        f"{anchor.time:.3f}",


                    "fret":
                        str(
                            anchor.fret
                        ),


                    "width":
                        str(
                            anchor.width
                        )

                }
            )



    # =====================================================
    # Hand Shapes
    # =====================================================

    def write_hand_shapes(
        self,
        root,
        shapes
    ):


        parent = ET.SubElement(
            root,
            "handShapes",
            {
                "count":
                    str(
                        len(shapes)
                    )
            }
        )



        for shape in shapes:


            ET.SubElement(
                parent,
                "handShape",
                {

                    "startTime":
                        f"{shape.start_time:.3f}",


                    "endTime":
                        f"{shape.end_time:.3f}",


                    "chordId":
                        str(
                            shape.chord_id
                        )

                }
            )