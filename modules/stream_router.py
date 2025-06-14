# modules/stream_router.py

import subprocess
from modules.config import load_config

TEST_AUDIO_PATH = "assets/sounds/test_audio.wav"

def get_output_modes():
    config = load_config()
    bt_outputs = config.get("bluetooth_outputs", {})

    return {
        1: bt_outputs.get("output1", {}).get("mode", "stereo"),
        2: bt_outputs.get("output2", {}).get("mode", "stereo"),
        3: bt_outputs.get("output3", {}).get("mode", "stereo")
    }

def get_pan_filter(mode):
    mode = mode.lower()
    if mode == "gauche" or mode == "g":
        return "pan=stereo|c0=FL|c1=FL"
    elif mode == "droite" or mode == "d":
        return "pan=stereo|c0=FR|c1=FR"
    else:
        return "pan=stereo|c0=FL|c1=FR"

def launch_streams():
    modes = get_output_modes()

    outputs = {
        1: "bluealsa:DEV=00:11:22:33:AA:BB",  # USB 3.0 n°1
        2: "bluealsa:DEV=00:11:22:33:CC:DD",  # USB 3.0 n°2
        3: "bluealsa:DEV=00:11:22:33:EE:FF"   # USB 2.0
    }

    processes = []

    for i in range(1, 4):
        pan_filter = get_pan_filter(modes[i])
        cmd = [
            "ffmpeg",
            "-i", TEST_AUDIO_PATH,
            "-af", pan_filter,
            "-f", "wav",
            "-"
        ]

        p_ffmpeg = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        p_play = subprocess.Popen(
            ["aplay", "-D", outputs[i]], stdin=p_ffmpeg.stdout,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        processes.append((p_ffmpeg, p_play))

    return processes

def stop_streams(processes):
    for p_ffmpeg, p_play in processes:
        p_ffmpeg.terminate()
        p_play.terminate()
