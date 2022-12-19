
def squares_intersect(s1, s2):
    if (s1[0] + s1[2] < s2[0]) or (s1[1] + s1[2] < s2[1]) or (s2[0] + s2[2] < s1[0]) or (s2[1] + s2[2] < s1[1]):
        return False 
    else:
        return True