def solution(a):
    
    result = -1
    length = len(a)
    duplicates = {}
    
    for outer_idx, num in enumerate(a):
        if outer_idx < length - 1:
            
            for inner_idx, i in enumerate(a[outer_idx+1:]):
                # In second loop, slicing is used
                # that's why increment 1 with original index
                if i == num:
                    
                    # Check if further occurence of particular number index
                    # is greater than previous occurence, than no need to save
                    # that index value in duplicates dict
                    if str(num) in duplicates and duplicates[str(num)] < inner_idx:
                        pass
                        
                    else:
                        duplicates[str(num)] = inner_idx
                 
    if duplicates:
        sort_orders = sorted(duplicates.items(), key=lambda x: x[1], reverse=False)
        
        # sort_order looks like [('3', 2), ('2', 5)]
        # We need key of second occurence with minimal index
        result = int(sort_orders[0][0])
        
    return result
