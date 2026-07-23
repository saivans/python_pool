def ft_count_harvest_iterative():
    until_harvest = int(input("Days until harvest: "))

    for i in range(until_harvest):
        print("Day ", i + 1)
    print("Harvest time!")
