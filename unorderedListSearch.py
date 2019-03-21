'''
Unordered list searching 
'''

items = [5,4,3,6,77,32]

def find_item(item, itemlist):
    for i in range(00, len(items)):
        if item == itemlist[i]:
            return i
        
    return None
    
print(find_item(32, items))
print(find_item(2, items))
