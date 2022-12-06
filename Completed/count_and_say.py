
def count_and_say(digits):
    count = 0       
    elm = digits[0]    
    result = []       
    for c in digits:   
        if c == elm:  
            count +=1       
        else:
            result.append( (elm,count) )
            count = 1       
            elm = c       

    result.append( (elm,count) ) 
    return ''.join( "{}{}".format(number,character) for character,number in result)