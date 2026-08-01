import json



class ManifestBuilder:
    """
    Rocksmith Manifest Generator
    """



    def __init__(self):

        pass



    # =========================================
    # Build
    # =========================================

    def build(
        self,
        arrangement,
        output_path
    ):


        song = (
            arrangement.song
        )


        data = {


            "Entries": [

                {

                    "Key":

                    "songs/" +
                    song.title.lower()
                    +
                    "/manifest.json",


                    "Value":

                    {

                        "SongName":

                            song.title,


                        "ArtistName":

                            song.artist,


                        "AlbumName":

                            song.album,


                        "Arrangement":

                            arrangement.arrangement_name,


                        "AverageTempo":

                            arrangement.average_tempo

                    }

                }

            ]

        }



        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as f:


            json.dump(

                data,

                f,

                indent=4,

                ensure_ascii=False

            )