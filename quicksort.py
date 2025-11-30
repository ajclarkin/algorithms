values_to_sort = [2, 9, 1, 6, 7, 4, 8, 3, 5]


def quicksort(values):
    if len(values) < 2:
        return values
    else:
        pivot = values[0]

        less = [v for v in values[1:] if v <= pivot]
        greater = [v for v in values[1:] if v > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort(values_to_sort))
