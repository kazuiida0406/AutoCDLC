from pathlib import Path
import shutil



class PackageBuilder:
    """
    PSARC Working Folder Builder
    """



    def build(
        self,
        xml_file,
        audio_file,
        manifest_file,
        output_dir
    ):


        root = Path(
            output_dir
        )


        root.mkdir(
            exist_ok=True
        )



        # XML

        shutil.copy(

            xml_file,

            root /
            "arrangement.xml"

        )



        # Audio

        shutil.copy(

            audio_file,

            root /
            "audio.mp3"

        )



        # Manifest

        shutil.copy(

            manifest_file,

            root /
            "manifest.json"

        )


        return root