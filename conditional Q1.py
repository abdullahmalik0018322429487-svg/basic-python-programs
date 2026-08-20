# input dalein
light = input("Enter traffic light color (Red, Yellow, Green): ")

# Traffic signal ke hisaab se action
if light.lower() == "red":
    print("Stop your vehicle")
elif light.lower() == "yellow":
    print("Slow Down")
elif light.lower() == "green":
    print("Go")
else:
    print("Invalid traffic light color")