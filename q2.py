def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    
    result = ""
    
    for i in s:
        if result != "" and result[-1] == i:
            result = result[:-1]
        else:
            result = result + i
        
    return result
    
    