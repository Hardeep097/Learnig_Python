'''
Sorting algorithm : bubble sort

'''

def bubbleSort(dataset):
    for i in range(len(dataset) - 1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
                
        print("Current state: ", dataset)
        
list = [4, 1, 0, 10,-1,200]
bubbleSort(list)
print("Result: ", list)
