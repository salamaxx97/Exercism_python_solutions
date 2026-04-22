"""is it like isbn-10 """ 
def is_valid(isbn):
    """is it like isbn-10 """ 
    # Remove dashes to make indexing easier
    clean_isbn = isbn.replace("-", "")
    
    if len(clean_isbn) != 10:
        return False
        
    total = 0
    for index in range(10):
        char = clean_isbn[index]
        
        if char.isdigit():
            value = int(char)
        elif char in "xX" and index == 9: # 'X' is only valid at the 10th position
            value = 10
        else:
            # If we find a letter anywhere else, or a non-X at the end
            return False
            
        total += (10 - index) * value
        
    return total % 11 == 0