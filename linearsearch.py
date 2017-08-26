def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            print(i)

    return -1

array = [23,4,3,1,12]
search(array,12)
