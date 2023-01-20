def solution(a):
    print(f'Array : {a}')
    result = -1
    unique_values = {}
    duplicate_values = {}
    
    for idx, num in enumerate(a):
        print(f'value : {num}')
        print(f'idx : {idx}')
        str_num = str(num)
        if str_num in unique_values:
            if not(str_num in duplicate_values):
                print('Update duplicate value {num} with idx {idx}')
                duplicate_values[str_num] = idx
                print(f'duplicate_values : {duplicate_values}')
                # pass
        else:
            print(f'Add value {num} with idx {idx}')
            unique_values[str_num] = idx
            print(f'unique_values : {unique_values}')
            
    
    if duplicate_values:
        sort_orders = sorted(duplicate_values.items(), 
                             key=lambda x: x[1],
                             reverse=False)
        
        # sort_order looks like [('3', 2), ('2', 5)]
        # We need key of second occurence with minimal index
        result = int(sort_orders[0][0])
        
    return result      


# print(solution([2, 1, 3, 5, 3, 2]))
print(solution([1, 1, 2, 2, 1]))