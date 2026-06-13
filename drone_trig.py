import math
def thrust_components(total_thrust, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    vertical = total_thrust * math.cos(angle_radians)
    horizontal = total_thrust * math.sin(angle_radians)
    return vertical, horizontal
v, h = thrust_components(100, 30)
print(f"Thrust: 100N at 30°")
print(f"Vertical: {v: .2f}N")
print(f"Horizontal {h: .2f}N")

def thrust_components(total_thrust, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    vertical = total_thrust * math.cos(angle_radians)
    horizontal = total_thrust * math.sin(angle_radians)
    return vertical, horizontal
v, h = thrust_components(80, 45)
print(f"Thrust: 80N at 45°")
print(f"Vertical: {v: .2f}N")
print(f"Horizontal {h: .2f}N")

def required_thrust(vertical_force, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    return vertical_force / math.cos(angle_radians)
t = required_thrust(60, 30)
print(f"Required thrust: {t:.2f}N")

