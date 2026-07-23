def ft_water_reminder():
    water_d = int(input("Days since last watering: "))

    if water_d > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
