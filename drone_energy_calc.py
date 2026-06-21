flight_time = input("Flight time:")
t = float(flight_time)
total_energy = 2 * t**2
if total_energy > 100:
    print("Warning battery insufficient")
else:
    print("Keep flying")
