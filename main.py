import time

class SmartHomeEnergyManagementSystem:
    def __init__(self):
        self.devices = {}
        self.energy_data = {}

    def add_device(self, device_name):
        if device_name not in self.devices:
            self.devices[device_name] = {'power_usage': 0, 'status': 'off'}
            self.energy_data[device_name] = []

    def remove_device(self, device_name):
        if device_name in self.devices:
            del self.devices[device_name]
            del self.energy_data[device_name]

    def toggle_device(self, device_name):
        if device_name in self.devices:
            device = self.devices[device_name]
            device['status'] = 'on' if device['status'] == 'off' else 'off'

    def record_energy_usage(self):
        for device_name, device in self.devices.items():
            if device['status'] == 'on':
                device['power_usage'] += 1
                self.energy_data[device_name].append((time.time(), device['power_usage']))

    def get_energy_usage(self, device_name):
        return self.energy_data[device_name]

    def optimize_energy_usage(self):
        # Implement energy optimization logic here
        pass

    def generate_recommendations(self):
        # Implement recommendation generation logic here
        pass

    def set_energy_budget(self, device_name, budget):
        if device_name in self.devices:
            self.devices[device_name]['budget'] = budget

    def send_alerts(self):
        for device_name, device in self.devices.items():
            if 'budget' in device and device['power_usage'] > device['budget']:
                print(f"Alert: {device_name} exceeded energy budget!")

# Usage example
system = SmartHomeEnergyManagementSystem()

# Add devices
system.add_device('Refrigerator')
system.add_device('Lights')
system.add_device('Television')

# Toggle devices
system.toggle_device('Refrigerator')
system.toggle_device('Lights')

# Record energy usage every second
for _ in range(10):
    system.record_energy_usage()
    time.sleep(1)

# Check energy usage
print(system.get_energy_usage('Refrigerator'))
print(system.get_energy_usage('Lights'))

# Set energy budget
system.set_energy_budget('Lights', 50)

# Send alerts
system.send_alerts()