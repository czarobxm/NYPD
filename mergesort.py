
def mergeSort(array):
    if len(array) > 1:
        # Finding middle point of an array
        mid = len(array)//2
  
        # Dividing array into two halves - (L)eft and (R)ight
        L = array[:mid]
        R = array[mid:]
  
        # Sorting the left half
        mergeSort(L)
  
        # Sorting the right half
        mergeSort(R)
  
        i = j = k = 0
  
        # Sorting elements putted in left and right half
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
  
        # Putting leftover elements back into the array
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
    else:
        pass # do nothing if len(array) == 1

    return array


A = [1,6,2,8,4,3,8,0,2]
B = [2,6,9,4,2,6,8,0,2,23,64,3,4,5,7]
C = [0,0,1,2,6,3,8,4,2,1,6,8]


print(f"array A:   {A}")
print(f"sorted array A:  {mergeSort(A)}")


print(f"array B:   {B}")
print(f"sorted array B:  {mergeSort(B)}")

print(f"array C:   {C}")
print(f"sorted array C:  {mergeSort(C)}")
