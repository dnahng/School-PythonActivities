month = int(input("Please enter your month of birth as a number: "))
day = int(input("Please enter your day of birth as a number: "))

if month == 1:
    if day >= 1 and day <= 19:
        print("You are a Capricorn")
    elif day >= 20 and day <= 31:
        print("You are a Aquarius")
elif month == 2:
    if day >= 1 and day <= 18:
        print("You are a Aquarius")
    elif day >= 19 and day <= 29:
        print("You are a Pisces")
elif month == 3:
    if day >= 1 and day <= 20:
        print("You are a Pisces")
    elif day >= 21 and day <= 31:
        print("You are a Aries")
elif month == 4:
    if day >= 1 and day <= 19:
        print("You are a Aries")
    elif day >= 20 and day <= 30:
        print("You are a Taurus")
elif month == 5:
    if day >= 1 and day <= 20:
        print("You are a Taurus")
    elif day >= 21 and day <= 31:
        print("You are a Gemini")
elif month == 6:
    if day >= 1 and day <= 20:
        print("You are a Gemini")
    elif day >= 21 and day <= 30:
        print("You are a Cancer")
elif month == 7:
    if day >= 1 and day <= 22:
        print("You are a Cancer")
    elif day >= 23 and day <= 31:
        print("You are a Leo")
elif month == 8:
    if day >= 1 and day <= 22:
        print("You are a Leo")
    elif day >= 23 and day <= 31:
        print("You are a Virgo")
elif month == 9:
    if day >= 1 and day <= 22:
        print("You are a Virgo")
    elif day >= 23 and day <= 30:
        print("You are a Libra")
elif month == 10:
    if day >= 1 and day <= 22:
        print("You are a Libra")
    elif day >= 23 and day <= 31:
        print("You are a Scorpio")
elif month == 11:
    if day >= 1 and day <= 21:
        print("You are a Scorpio")
    elif day >= 22 and day <= 30:
        print("You are a Sagittarius")
elif month == 12:
    if day >= 1 and day <= 21:
        print("You are a Sagittarius")
    elif day >= 22 and day <= 31:
        print("You are a Capricorn")
else:
    print("Invalid Input")