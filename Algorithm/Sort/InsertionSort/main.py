def insertSortASC(list):
    for i in range(1, len(list)):
        item = list[i]

        j = i - 1
        while(j >= 0 and item < list[j]):
            list[j+1] = list[j]
            j -= 1

        list[j+1] = item
            
    return list

def insertSortDESC(list):
    for i in range(1, len(list)):
        item = list[i]

        j = i - 1
        while(j >= 0 and item > list[j]):
            list[j+1] = list[j]
            j -= 1

        list[j+1] = item
            
    return list

def main():
    input = [2, 4, 5, 6, 1, 3]
    print(insertSortASC(input.copy()))
    print(insertSortDESC(input.copy()))

main()