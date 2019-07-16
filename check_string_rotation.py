def check_string_rotation(s1,s2):
    # check if s2 is rotation of s1
    concatenated = s1+s1
    if s2 in concatenated:
        return True
    return False
    
    
check_string_rotation('abc','acb')