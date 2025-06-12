import subprocess

class BluetoothOutput:
    def __init__(self, adapter):
        self.adapter = adapter

    def power_on(self):
        subprocess.run(f"bluetoothctl --adapter={self.adapter} power on", shell=True)

    def power_off(self):
        subprocess.run(f"bluetoothctl --adapter={self.adapter} power off", shell=True)

    def pair_device(self):
        subprocess.run(f"bluetoothctl --adapter={self.adapter} pairable on", shell=True)
        subprocess.run(f"bluetoothctl --adapter={self.adapter} discoverable on", shell=True)
        subprocess.run(f"bluetoothctl --adapter={self.adapter} agent NoInputNoOutput", shell=True)
        subprocess.run(f"bluetoothctl --adapter={self.adapter} default-agent", shell=True)

    def connect(self, device_mac):
        subprocess.run(f"bluetoothctl --adapter={self.adapter} connect {device_mac}", shell=True)

    def disconnect(self, device_mac):
        subprocess.run(f"bluetoothctl --adapter={self.adapter} disconnect {device_mac}", shell=True)

    def remove_device(self, device_mac):
        subprocess.run(f"bluetoothctl --adapter={self.adapter} remove {device_mac}", shell=True)
