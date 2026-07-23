def ft_plant_age():
    age_d = int(input("Enter plant age in days: "))

    if age_d <= 60:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
