def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

def bubbleSortASC(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                swap(list, i, j)
    return list

def bubbleSortDESC(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] < list[j]:
                swap(list, i, j)
    return list

def main():
    input = [2, 4, 5, 6, 1, 3]
    print(bubbleSortASC(input.copy()))
    print(bubbleSortDESC(input.copy()))

main()