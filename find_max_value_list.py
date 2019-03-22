'''

Find max value in the list 
'''

items = [1,2,3,46,5,6,7,88,9]

def find_max(items):
    if len(items) == 1:
        return items[0]
        
        
    opt1 = items[0]
    opt2 = find_max(items[1:])
    
    
    
    if opt1 > opt2:
        return opt1
    else:
        return opt2
        
print(find_max(items))
