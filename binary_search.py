#Binary Search

def binary_search(target,arr):
    print(f"finding {target} in {arr}")
    l = 0
    r = len(arr)
    mid = (l + r) // 2
    if target == arr[mid]:
        return "Found"
    else:
        if target < arr[mid]:
            return binary_search(target,arr[l:mid])
        else:
            return binary_search(target,arr[mid+1:r])
    return "Not found"

print(binary_search(10,[3,4,5,10,12]))

