class EOFWriter:

    def write(self, filename, notes):

        with open(filename, "w", encoding="utf-8") as f:

            f.write("# AutoCDLC\n\n")

            for note in notes:

                f.write(
                    f"{note.time:.3f},"
                    f"{note.string},"
                    f"{note.fret}\n"
                )

        print(f"Saved : {filename}")