def common_data(list1, list2): 
    result = 'No'
  
    # traverse in the 1st list 
    for x in list1: 
  
        # traverse in the 2nd list 
        for y in list2: 
    
            # if one common 
            if x == y: 
                result = 'Yes'
                return result  
                  
    return result  
a = list(input().split())
b = list(input().split()) 
print(common_data(a, b)) 
