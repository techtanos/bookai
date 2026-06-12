m = input("Enter Drone mass: ")
a = input("Enter desired upward acceleration: ")
force = float(m) * (9.8 + float(a))

if force >= 100:
    print(f"Motors are strong!  {force:.1f} Newtons")
else:
    print(f"Motors are weak! Force needed: {force:.1f} Newtons")


