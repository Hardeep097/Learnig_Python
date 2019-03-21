'''

                       Quick sort. algorithm

'''


item = [20, 22,0,1,44,100,2]


    
def quickSort(dataset, first, last):
    
    if first < last:
        pivotIdx = partition(dataset, first, last)
        
        
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)
    
def partition(datavalues, first, last):
    pivotvalue = datavalues[first]
    
    lower = first+1
    upper = last
    
    
    done = False 
    while not done:
        
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1 
            
            
        while datavalues[upper] >= pivotvalue and  upper >= lower:
            upper -= 1 
        
        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp
       
    
    
    temp = datavalues[first]
    datavalues[first] =  datavalues[upper]
    datavalues[upper] = temp
    
    
    return upper
    
print(item)
quickSort(item, 0, len(item)-1)
print(item)
