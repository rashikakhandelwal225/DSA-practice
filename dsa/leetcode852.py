def peakIndexInMountainArray(arr):
    start = 0
    end = len(arr)-1
        
    while start <= end:
        mid = start + ((end-start)//2)
        if arr[mid-1] <= arr[mid] and arr[mid+1] <= arr[mid]:
            peak = mid
            return peak
        elif arr[mid-1] > arr[mid]:
            end = mid          
        else:
            start = mid

arr = [0,1,0]
print(peakIndexInMountainArray(arr))
arr = [0,2,1,0]
print(peakIndexInMountainArray(arr))
arr = [0,10,5,2]
print(peakIndexInMountainArray(arr))


            