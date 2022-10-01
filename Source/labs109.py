
# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust


# check the digits are only odd 
def only_odd_digits(n):
    odd = 0

    int_str = str(n)

    str_list = []
    comp = []
    for y in int_str:
        str_list.append(y)

    for i in str_list:
        if i in ['1', '3', '5', '7', '9']:
            comp.append(i)
            
    if len(str_list) == len(comp):
        return True 
    else:
        return False  

    
            
    
            
    
            