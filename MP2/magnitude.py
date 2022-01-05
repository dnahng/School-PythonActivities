magnitude = float(input("Enter an earthquake magnitude: "))


if magnitude < 2:
    desc = "Micro"
elif magnitude < 3:
    desc = "Very Minor"
elif magnitude < 4:
    desc = "Minor"
elif magnitude < 5:
    desc = "Light"
elif magnitude < 6:
    desc = "Moderate"
elif magnitude < 7:
    desc = "Strong"
elif magnitude < 8:
    desc = "Major"
elif magnitude < 10:
    desc = "Great"
elif magnitude >= 10:
    desc = "Meteoric"

print("This earthquake is classified as", desc)