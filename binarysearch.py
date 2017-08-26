def binarysearch(arr,l,r,x):
    if r >= l:
        mid = l+(r-l)//2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarysearch(arr,l,mid-1,x)

        else:
            return binarysearch(arr,mid+1,r,x)
    else:
        return -1

arr = [2,3,5,6,10]
x=10
leg= len(arr)-1
print(leg)
result = binarysearch(arr,0,leg,x)
if result !=-1:
    print(" present at index %d" %result)
else:
    print("no present")
