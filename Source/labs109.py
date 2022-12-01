
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
    
# check if the items in a list are in ascending order 
def is_ascending(items):
    for x in range(len(items) - 1):
        if items[x] >= items[x + 1]:
            return False
    return True 

### Match the 2nd value of the pair with the 2nd item in the 2nd pair

def domino_cycle(tiles):
    index = 0
    if len(tiles) == 0:
      return True
  
    if len(tiles) == 1:
        return tiles[0][0] == tiles[0][1]
            
    else:
        while index <= (len(tiles) - 2):
            if (tiles[index][1] == tiles[index+1][0]):
                index += 1
            else:
            
                return False
        
        if tiles[0][0] == tiles[-1][1]:
            return True
        else:
            return False
        
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
        
            







            
    
            