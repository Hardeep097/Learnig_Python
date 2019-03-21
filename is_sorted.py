"
check if file is sorted in ascending order
"

item1 = [1,2,3,4,5,6,7,8,9]
item2 = [33,2,44,1,52,0]

def is_sorted(itemlist):
    
    #for i in range(0, len(itemlist)):
     #   if (itemlist[i] > itemlist[i + 1]):
     #       return False
            
    return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1))

print(is_sorted(item1))
print(is_sorted(item2))
