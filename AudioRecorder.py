import sounddevice
import wavio

class Audio():
    def __init__(self) -> None:
        self.frequency = 44100 # Audio
        self.duration = 10 # Seconds

    def record(self):
        try:
            recording = sounddevice.rec(int(self.duration * self.frequency), samplerate = self.frequency, channels = 2)

            sounddevice.wait()

            wavio.write("audio.wav",recording, self.frequency, sampwidth = 2)

            return True
        except Exception as e:
            print(e)
            return False

