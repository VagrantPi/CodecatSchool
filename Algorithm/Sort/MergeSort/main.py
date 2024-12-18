def mergeSortASC(list):
    # 如果list只有一個元素，直接return
    if len(list) <= 1:
        return list
    
    # 分成左邊和右邊
    mid = len(list) // 2
    left = list[:mid] # 左邊
    right = list[mid:] # 右邊
    
    #遞迴呼叫
    left = mergeSortASC(left)
    right = mergeSortASC(right)
    
    # 合成
    return mergeASC(left, right)

def mergeASC(left, right):
    result = [] # 儲存合成的結果
    i, j = 0, 0 # 分別是左邊和右邊的index
    while i < len(left) and j < len(right): # 如果左邊和右邊都還有元素
        if left[i] < right[j]: # 如果左邊的元素小於右邊的元素
            result.append(left[i]) # 就將左邊的元素加入結果
            i += 1 # 並且左邊的index+1
        else: # 如果左邊的元素大於或等於右邊的元素
            result.append(right[j]) # 就將右邊的元素加入結果
            j += 1 # 並且右邊的index+1
    result += left[i:] # 將左邊剩下的元素加入結果
    result += right[j:] # 將右邊剩下的元素加入結果
    return result # 回傳合成的結果

def mergeSortDESC(list):
    # 如果list只有一個元素，直接return
    if len(list) <= 1:
        return list
    
    # 分成左邊和右邊
    mid = len(list) // 2
    left = list[:mid] # 左邊
    right = list[mid:] # 右邊
    
    #遞迴呼叫
    left = mergeSortDESC(left)
    right = mergeSortDESC(right)
    
    # 合成
    return mergeDESC(left, right)

def mergeDESC(left, right):
    result = [] # 儲存合成的結果
    i, j = 0, 0 # 分別是左邊和右邊的index
    while i < len(left) and j < len(right): # 如果左邊和右邊都還有元素
        if left[i] > right[j]: # 如果左邊的元素大於右邊的元素
            result.append(left[i]) # 就將左邊的元素加入結果
            i += 1 # 並且左邊的index+1
        else: # 如果左邊的元素小於或等於右邊的元素
            result.append(right[j]) # 就將右邊的元素加入結果
            j += 1 # 並且右邊的index+1
    result += left[i:] # 將左邊剩下的元素加入結果
    result += right[j:] # 將右邊剩下的元素加入結果
    return result # 回傳合成的結果

def main():
    input = [2, 4, 5, 6, 1, 3]
    print(mergeSortASC(input.copy()))
    # print(mergeSortDESC(input.copy()))

main()