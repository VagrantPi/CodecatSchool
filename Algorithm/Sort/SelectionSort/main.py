def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

def selectionSortASC(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j
        swap(list, i, min)
    return list

def selectionSortDESC(list):
    for i in range(len(list)):
        max = i
        for j in range(i+1, len(list)):
            if list[j] > list[max]:
                max = j
        swap(list, i, max)
    return list


def main():
    input = [2, 4, 5, 6, 1, 3]
    print(selectionSortASC(input.copy()))
    print(selectionSortDESC(input.copy()))

main()