def contains_pattern(text, pattern):
    #return text.find(pattern)      built in function return index number
    
            #or 
    #if pattern in text:
        # return True
        #else:                  only return True or false 
            #return False
    
            # or
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            return i

    return -1

print(contains_pattern("hello world", "wor"))