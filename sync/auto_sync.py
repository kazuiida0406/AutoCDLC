class SmartAutoSync:

    def calculate_offset(self, notes, onsets, compare_notes=20):

        if len(notes) == 0 or len(onsets) == 0:
            return 0.0

        compare_notes = min(compare_notes, len(notes))

        best_offset = 0.0
        best_error = float("inf")

        for onset_start in range(len(onsets) - compare_notes):

            offset = onsets[onset_start] - notes[0].time

            error = 0.0

            for i in range(compare_notes):

                predicted = notes[i].time + offset
                actual = onsets[onset_start + i]

                error += abs(predicted - actual)

            if error < best_error:
                best_error = error
                best_offset = offset

        return best_offset