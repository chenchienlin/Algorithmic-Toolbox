def merge(arr, aux, lo, mid, hi):
    i = lo
    j = mid + 1
    for k in range(lo, hi+1):
        if i <= mid and j <= hi:
            if aux[i] <= aux[j]:
                arr[k] = aux[i]
                i += 1
            else:
                arr[k] = aux[j]
                j += 1
        else:
            if i > mid:
                arr[k] = aux[j]
                j += 1
            else:
                arr[k] = aux[i]
                i += 1