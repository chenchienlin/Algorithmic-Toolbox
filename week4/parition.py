def partition(arr, lo, hi):
    p = arr[lo]
    j = lo
    for i in range(lo+1, hi+1):
        if p > arr[i]:
            j += 1
            swap(arr, i, j)
    swap(arr, lo, j)
    return j

def partition3(arr, lo, hi):
    p = arr[lo]
    j = lo
    k = lo
    for i in range(lo+1, hi+1):
        if p > arr[i]:
            j += 1
            k += 1
            swap(arr, i, j)
        elif p == arr[i]:
            j += 1
    swap(arr, lo, j)
    return k, j

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp