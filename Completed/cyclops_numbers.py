# looking for a singular 0 number between two equal sides 

def is_cyclops(n):
    str_number = str(n)
    
    if len(str_number) % 2 == 0 :
        return False
    else:
        mid = len(str_number)//2
        if str_number[mid] != "0" or str_number.count("0") > 1:
            return False
        else:
            return True
        