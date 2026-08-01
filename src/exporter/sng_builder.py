import subprocess


class SNGBuilder:

    def build(self, xml_file):

        subprocess.run(

            [

                "ToolkitCLI.exe",

                "-build",

                xml_file

            ],

            check=True

        )