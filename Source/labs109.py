
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

# give the correct amount of change back!        
def give_change(amount, coins):
        result = []
        return give_change_sort(amount, coins, result)


def give_change_sort(amount, coins, result):
        if amount == 0:
                return result
        while len(coins) > 0 and amount >= coins[0]:
                amount = amount - coins[0]
                result.append(coins[0])
        if len(coins) > 0:
                coins = coins[1:]
        else:
                return result
        return give_change_sort(amount, coins, result)

# count the carry over to the next column similar to writing out addition on paper column style
def count_carries(a, b):
    a = str(a)
    b = str(b)
    carry = 0;
    count = 0;
    len_a = len(a);
    len_b = len(b);
 
    while (len_a != 0 or len_b != 0):
        x = 0;
        y = 0;
        if (len_a > 0):
            x = int(a[len_a - 1]) + int('0');
            len_a -= 1;
         
        if (len_b > 0):
            y = int(b[len_b - 1]) + int('0');
            len_b -= 1;

        sum = x + y + carry;
        if (sum >= 10):
            carry = 1;
            count += 1;
        else:
            carry = 0;
    return count;


def first_preceded_by_smaller(items, k=1):
    
    for i in range(len(items)):
        if sorted(items[0:i+1]).index(items[i]) >= k:
            return items[i]
    return None


# look for duplicate digits 
def duplicate_digit_bonus(n):
    digit = str(n)
    index = 0
    result = 1
    d = digit[0]
    for i in range(1,len(digit)):
        if d == digit[i]:
            result += 1
            if i+1 == len(digit):
                index += 2 * 10**(result-2)
        else:
            if result >=2:
                index += 10**(result-2)
            result = 1
        d = digit[i]
    return 

def knight_jump(knight, start, end):
        spaces = []
        for i in range(0, len(start)):
                spaces.append(abs(start[i] - end[i]))
        if set(knight) == set(spaces):
                return True
        return False

            
def fibonacci_sum(n):
    x = 0
    y = 1
    fib = []
    index = []
    fib.append(x)
    fib.append(y)
    counter = x + y
    
    while counter <= n:
        fib.append(counter)
        x = y
        y = counter
        counter = x + y
    answer = 0
    fib.sort(reverse=True)
   
    while True:
        for i in fib:
            if answer + i > n:
                continue
            else:
                index.append(i)
                answer = answer + i
                if answer == n:
                    break
                fib.remove(i)
        if answer == n:
            break
        
    return index
