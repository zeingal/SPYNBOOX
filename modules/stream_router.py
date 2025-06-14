import subprocess
import json

CONFIG_PATH = "config/config.json"
TEST_AUDIO_PATH = "assets/sounds/test_audio.wav"

def get_output_modes():
    try:
        with open(CONFIG_PATH, "r") as f:
            config = json.load(f)
        return {
            1: config.get("output_1_mode", "ST"),
            2: config.get("output_2_mode", "ST"),
            3: config.get("output_3_mode", "ST")
        }
    except Exception as e:
        print(f"[SPYNBOOX][ERROR] Unable to read config: {e}")
        return {1: "ST", 2: "ST", 3: "ST"}

def get_pan_filter(mode):
    if mode == "G":
        return "pan=stereo|c0=FL|c1=FL"
    elif mode == "D":
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
