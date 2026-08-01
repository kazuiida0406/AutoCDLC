import xml.etree.ElementTree as ET


from exporter.xml_sections import XMLSections
from exporter.xml_levels import XMLLevels



class XMLWriter(
    XMLSections,
    XMLLevels
):
    """
    Rocksmith XML Writer

    Arrangement
        ↓
    song.xml
    """



    def __init__(self):

        self.arrangement = None



    # =====================================================
    # Write
    # =====================================================

    def write(
        self,
        arrangement,
        output_path
    ):


        self.arrangement = (
            arrangement
        )



        root = ET.Element(
            "song",
            {
                "version":
                    str(
                        arrangement.version
                    )
            }
        )



        # -----------------------------
        # Metadata
        # -----------------------------

        self.write_metadata(
            root
        )



        # -----------------------------
        # Structure
        # -----------------------------

        self.write_ebeats(
            root
        )


        self.write_phrases(
            root
        )


        self.write_phrase_iterations(
            root
        )


        self.write_new_linked_diffs(
            root
        )


        self.write_linked_diffs(
            root
        )



        # -----------------------------
        # Musical Data
        # -----------------------------

        self.write_chord_templates(
            root
        )


        self.write_anchors(
            root,
            arrangement.anchors
        )


        self.write_hand_shapes(
            root,
            arrangement.hand_shapes
        )


        self.write_events(
            root
        )


        self.write_tone_changes(
            root
        )


        self.write_sections(
            root
        )



        # -----------------------------
        # Levels
        # -----------------------------

        self.write_levels(
            root
        )



        tree = ET.ElementTree(
            root
        )


        ET.indent(
            tree,
            space="    "
        )


        tree.write(
            output_path,
            encoding="utf-8",
            xml_declaration=True
        )



    # =====================================================
    # Chord Templates
    # =====================================================

    def write_chord_templates(
        self,
        root
    ):


        parent = ET.SubElement(
            root,
            "chordTemplates",
            {
                "count":
                    str(
                        len(
                            self.arrangement.chord_templates
                        )
                    )
            }
        )


        for template in (
            self.arrangement.chord_templates
        ):


            ET.SubElement(
                parent,
                "chordTemplate",
                {

                    "id":
                        str(
                            template.id
                        ),


                    "displayName":
                        getattr(
                            template,
                            "display_name",
                            getattr(
                                template,
                                "name",
                                ""
                            )
                        )

                }
            )



    # =====================================================
    # Tone Changes
    # =====================================================

    def write_tone_changes(
        self,
        root
    ):


        parent = ET.SubElement(
            root,
            "toneChanges",
            {
                "count":
                    str(
                        len(
                            self.arrangement.tone_changes
                        )
                    )
            }
        )



        for tone in (
            self.arrangement.tone_changes
        ):


            ET.SubElement(
                parent,
                "toneChange",
                {

                    "time":
                        f"{tone.time:.3f}",


                    "tone":
                        tone.tone

                }
            )



    # =====================================================
    # Events
    # =====================================================

    def write_events(
        self,
        root
    ):


        parent = ET.SubElement(
            root,
            "events",
            {
                "count":
                    str(
                        len(
                            self.arrangement.events
                        )
                    )
            }
        )



        for event in (
            self.arrangement.events
        ):


            ET.SubElement(
                parent,
                "event",
                {

                    "time":
                        f"{event.time:.3f}",


                    "code":
                        event.code

                }
            )



    # =====================================================
    # Sections
    # =====================================================

    def write_sections(
        self,
        root
    ):


        sections = getattr(
            self.arrangement,
            "sections",
            []
        )


        parent = ET.SubElement(
            root,
            "sections",
            {
                "count":
                    str(
                        len(
                            sections
                        )
                    )
            }
        )



        for section in sections:


            ET.SubElement(
                parent,
                "section",
                {

                    "name":
                        section.name,


                    "number":
                        str(
                            section.number
                        )

                }
            )