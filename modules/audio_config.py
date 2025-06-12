# modules/audio_config.py

audio_settings = {
    "output_1": {
        "volume": 70,
        "mode": "stereo"  # Options: stereo, left, right
    },
    "output_2": {
        "volume": 70,
        "mode": "stereo"
    },
    "output_3": {
        "volume": 70,
        "mode": "stereo"
    }
}

def get_audio_settings():
    return audio_settings

def set_output_config(output_key, volume=None, mode=None):
    if output_key in audio_settings:
        if volume is not None:
            audio_settings[output_key]["volume"] = volume
        if mode is not None:
            audio_settings[output_key]["mode"] = mode

def get_output_config(output_key):
    return audio_settings.get(output_key, {})
