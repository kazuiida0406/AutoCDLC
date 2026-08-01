class TimeConverter:

    def __init__(self, tempo):
        self.tempo = tempo
        self.ticks_per_quarter = 960

    def tick_to_seconds(self, tick):
        beats = tick / self.ticks_per_quarter
        return beats * 60 / self.tempo