from gpiozero import CPUTemperature

class CpuTemp():
    def poll():
        cpu = CPUTemperature()
        return cpu.temperature