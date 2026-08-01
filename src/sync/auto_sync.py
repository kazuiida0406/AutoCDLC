class SmartAutoSync:
    """
    GPノート列とMP3のOnset列を比較して、
    最も一致するオフセットを求めるクラス
    """

    def calculate_offset(self, notes, onsets, compare_notes=20, search_limit=200):

        # データが無い場合
        if len(notes) == 0 or len(onsets) == 0:
            return 0.0, float("inf")

        # 比較するノート数を調整
        compare_notes = min(compare_notes, len(notes))

        # 探索範囲を制限
        search_limit = min(search_limit, len(onsets) - compare_notes)

        best_offset = 0.0
        best_error = float("inf")

        # Onset候補を順番に試す
        for onset_start in range(search_limit):

            # GP1音目とOnset候補との差
            offset = onsets[onset_start] - notes[0].time

            error = 0.0

            # compare_notes個比較
            for i in range(compare_notes):

                predicted = notes[i].time + offset
                actual = onsets[onset_start + i]

                error += abs(predicted - actual)

            # 最小誤差なら更新
            if error < best_error:
                best_error = error
                best_offset = offset

        return best_offset, best_error

    def apply_offset(self, notes, offset):
        """
        全ノートへオフセットを適用
        """
        for note in notes:
            note.time += offset