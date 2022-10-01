# check the digits are only odd 
n = 1115879

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

    
            
    
            
    
            