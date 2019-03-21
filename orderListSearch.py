'''
Search in ordered list 
'''


items = [1,2,3,4,5,6,7]

def binarysearch(item , itemlist):
    listsize = len(itemlist) - 1
    
    lowerIdx = 0
    upperIdx = listsize
    
    while lowerIdx <= upperIdx:
    
        midPt = (lowerIdx + upperIdx) // 2
        
        if itemlist[midPt] == item:
            return midPt
            
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1 
        else: 
            upperIdx = midPt - 1
            
    if lowerIdx > upperIdx:
            return None
    
print(binarysearch(2, items))
print(binarysearch(22, items))
