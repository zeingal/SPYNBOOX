# modules/config_utils.py

from modules import config

_config_data = config.load_config()

def get_setting(key, default=None):
    return _config_data.get(key, default)

def set_setting(key, value):
    _config_data[key] = value
    config.save_config(_config_data)

def get_output_status(output_name):
    return _config_data["bluetooth_outputs"].get(output_name, {}).get("status", False)

def set_output_status(output_name, status):
    if output_name in _config_data["bluetooth_outputs"]:
        _config_data["bluetooth_outputs"][output_name]["status"] = status
        config.save_config(_config_data)

def get_output_mode(output_name):
    return _config_data["bluetooth_outputs"].get(output_name, {}).get("mode", "stereo")

def set_output_mode(output_name, mode):
    if output_name in _config_data["bluetooth_outputs"]:
        _config_data["bluetooth_outputs"][output_name]["mode"] = mode
        config.save_config(_config_data)

def get_equalizer_value(band):
    return _config_data["equalizer"].get(band, 0)

def set_equalizer_value(band, value):
    _config_data["equalizer"][band] = value
    config.save_config(_config_data)
