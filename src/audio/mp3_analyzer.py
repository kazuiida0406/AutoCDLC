import librosa


class MP3Analyzer:

    def __init__(self, filename):
        self.filename = filename
        self.y, self.sr = librosa.load(filename, sr=None)

    def print_info(self):
        print(f"Sample Rate : {self.sr}")
        print(f"Samples     : {len(self.y)}")
        print(f"Length(sec) : {len(self.y) / self.sr:.2f}")

        import librosa

class MP3Analyzer:

    def __init__(self, filename):
        self.filename = filename
        self.y, self.sr = librosa.load(filename, sr=None)

    def print_info(self):
        print(f"Sample Rate : {self.sr}")
        print(f"Samples     : {len(self.y)}")
        print(f"Length(sec) : {len(self.y) / self.sr:.2f}")

    def detect_onsets(self):
        onset_frames = librosa.onset.onset_detect(
            y=self.y,
            sr=self.sr
        )

        onset_times = librosa.frames_to_time(
            onset_frames,
            sr=self.sr
        )

        return onset_times