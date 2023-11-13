def FindMedian(arr):
    if arr:
        sortedArr = sorted(arr)
        arrLen = len(sortedArr)
        return sortedArr[(arrLen // 2)] if arrLen % 2 != 0 else (sortedArr[arrLen // 2 - 1] + sortedArr[
            arrLen // 2]) / 2
    else:
        return None