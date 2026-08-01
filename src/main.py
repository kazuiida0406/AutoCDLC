import os
import sys



# ==========================================
# Path
# ==========================================

SRC_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


if SRC_DIR not in sys.path:

    sys.path.insert(
        0,
        SRC_DIR
    )



# ==========================================
# Imports
# ==========================================

from parser.gp_reader import GPReader

from builder.arrangement_builder import ArrangementBuilder

from exporter.xml_writer import XMLWriter



# ==========================================
# Config
# ==========================================

ROOT_DIR = os.path.dirname(
    SRC_DIR
)


INPUT_DIR = os.path.join(
    ROOT_DIR,
    "input"
)


OUTPUT_XML = os.path.join(
    ROOT_DIR,
    "output.xml"
)



# ==========================================
# Find GP File
# ==========================================

def find_gp_file():


    if not os.path.exists(
        INPUT_DIR
    ):

        raise FileNotFoundError(
            "input folder not found"
        )



    for file in os.listdir(
        INPUT_DIR
    ):


        if file.lower().endswith(
            (
                ".gp3",
                ".gp4",
                ".gp5",
                ".gpx"
            )
        ):

            return os.path.join(
                INPUT_DIR,
                file
            )



    raise FileNotFoundError(
        "No GuitarPro file found"
    )



# ==========================================
# Main
# ==========================================

def main():


    print(
        "=== AutoCDLC Ver4.5 Final ==="
    )



    # --------------------------------------
    # GuitarPro
    # --------------------------------------

    print(
        "Reading GuitarPro..."
    )


    gp_file = find_gp_file()


    reader = GPReader(
        gp_file
    )


    song = reader.get_song()


    print(
        "GuitarPro Loaded"
    )



    # --------------------------------------
    # Arrangement
    # --------------------------------------

    print(
        "Building Arrangement..."
    )


    builder = ArrangementBuilder()


    arrangement = builder.build(
        song
    )


    print(
        "Arrangement Ready"
    )



    # --------------------------------------
    # XML
    # --------------------------------------

    print(
        "Writing XML..."
    )


    writer = XMLWriter()


    writer.write(
        arrangement,
        OUTPUT_XML
    )


    print(
        "XML Complete:",
        OUTPUT_XML
    )



# ==========================================
# Entry
# ==========================================

if __name__ == "__main__":

    main()