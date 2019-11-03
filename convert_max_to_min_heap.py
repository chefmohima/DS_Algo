# Convert Max heap to Min heap

def convertMax(maxheap):
    # find parent nodes from the end
    for i in range((len(maxheap))//2, -1,-1):
        minheapify(maxheap, i)
    return maxheap
    
def minheapify(maxheap, index):
    minindex = index
    left = 2 *index +1
    right = 2 *index +2
    if right <= len(maxheap)-1:
        if maxheap[minindex] > maxheap[left]:
            minindex = left
        if maxheap[minindex] > maxheap[right]:
            minindex = right
    if minindex != index:
        maxheap[minindex], maxheap[index] = maxheap[index], maxheap[minindex]
        minheapify(maxheap,minindex)
    return maxheap
    
maxHeap = [9,4,7,1,-2,6,5]
print(convertMax(maxHeap))
        
    
        
