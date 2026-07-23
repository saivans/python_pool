def ft_helper(day: int, n: int):
    if (day == n):
        print("Harvest time!")
    else:
        print("Day ", day + 1)
        ft_helper(day + 1, n)


def ft_count_harvest_recursive():
    day = 0
    n = int(input("Days until harvest: "))
    ft_helper(day, n)
