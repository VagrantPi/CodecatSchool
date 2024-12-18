def quickSortASC(list):
    if len(list) <= 1: # 如果list只有一個元素，直接return
        return list
    
    pivot = list[0] # 選擇pivot
    left = [] # pivot左邊的元素
    right = [] # pivot右邊的元素
    for i in range(1, len(list)): # loop所有元素
        if list[i] < pivot: # 如果元素小於pivot
            left.append(list[i]) # 加入left
        else: # 如果元素大於或等於pivot
            right.append(list[i]) # 加入right
    return quickSortASC(left) + [pivot] + quickSortASC(right) #遞迴呼叫

def quickSortDESC(list):
    if len(list) <= 1: # 如果list只有一個元素，直接return
        return list
    
    pivot = list[0] # 選擇pivot
    left = [] # pivot左邊的元素
    right = [] # pivot右邊的元素
    for i in range(1, len(list)): # loop所有元素
        if list[i] > pivot: # 如果元素大於pivot
            left.append(list[i]) # 加入left
        else: # 如果元素小於或等於pivot
            right.append(list[i]) # 加入right
    return quickSortDESC(left) + [pivot] + quickSortDESC(right) #遞迴呼叫

def main():
    input = [2, 4, 5, 6, 1, 3]
    print(quickSortASC(input.copy())) # 複製input，避免改變原本的list
    print(quickSortDESC(input.copy()))

main()