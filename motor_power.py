import math
rpm = float(input("Enter RPM:"))
torque = float(input("Enter torque (Nm): "))
omega = 2 * math.pi * rpm /60
power = torque * omega
print(f"Angular velocity: {omega:.2f} rad/s")
print(f"Power consumed: {power:.2f} W")
