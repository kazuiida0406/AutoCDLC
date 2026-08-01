from pathlib import Path
import zipfile



class PSARCWriter:
    """
    PSARC Package Writer

    Ver4.5 Final
    """



    def __init__(self):

        pass



    # =================================================
    # Write
    # =================================================

    def write(
        self,
        package_dir,
        output_file
    ):


        package_dir = Path(
            package_dir
        )


        output_file = Path(
            output_file
        )



        if not package_dir.exists():

            raise FileNotFoundError(
                package_dir
            )



        with zipfile.ZipFile(

            output_file,

            "w",

            compression=
            zipfile.ZIP_DEFLATED

        ) as archive:



            for file in package_dir.rglob("*"):


                if file.is_file():


                    archive.write(

                        file,

                        file.relative_to(
                            package_dir
                        )

                    )



        return output_file