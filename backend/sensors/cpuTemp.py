from gpiozero import CPUTemperature

class CpuTemp():
    def poll():
        cpu = CPUTemperature()
        res = {"name": "temp_cpu", "value": cpu.temperature}
        return res