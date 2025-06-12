# modules/app_state.py

class AppState:
    def __init__(self):
        self.bluetooth_inputs = []
        self.bluetooth_outputs = [None, None, None]  # Sorties 1, 2, 3
        self.volumes = [70, 70, 70]  # Volumes des sorties
        self.eq_settings = [
            {"bass": 0, "mid": 0, "treble": 0},
            {"bass": 0, "mid": 0, "treble": 0},
            {"bass": 0, "mid": 0, "treble": 0}
        ]
        self.theme = "day"  # day / night
        self.battery_level = 100
        self.connected = [False, False, False]
        self.split_mode = ["stereo", "stereo", "stereo"]  # par sortie

    def reset(self):
        self.__init__()

# Singleton
app_state = AppState()
