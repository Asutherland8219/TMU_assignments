
# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

from itertools import count
from unittest import result


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


# not working 
# # check the digits are only odd 
def only_odd_digits(n):
    return set(str(n))-set('13579')==set()

    
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
    return index

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

def three_summers(items, goal):
    
    for x in range(len(items)-1):

        left = x+1
        right = len(items)-1

        while (left < right):

            tmp = items[left] + items[right] + items[x]

            if tmp > goal:
                right -= 1
            elif tmp < goal:
                left += 1
            else:
                return True

    return False


def reverse_vowels(text):
    vowels = "aeiouAEIOU"
    v_text = ""
    res = ''
    for i in text:
        if i in vowels:
            v_text = i + v_text
            count = 0
            res = ''
    for i in text:
        if i in vowels:
            if i.isupper():
                res += v_text[count].upper()
            else:
                res += v_text[count].lower()
            count += 1
        else:
            res += i
    return res

# only return the odd digits 
def only_odd_digits(n):
    
    x = list(map(int, str(x)))
    result = all(y%2 == 1 for y in x)
    return(result)


def arithmetic_progression(elems):
    len_ele = len(elems)
    if len_ele == 1:
        return (elems[0], 0, 1)
    if len_ele == 2:
        return (elems[0], elems[1] - elems[0], 2)
    then = [[0 for x in range(len_ele)] for y in range(len_ele)]
    for a in range(len_ele - 1):
        then[a][len_ele - 1] = 2
    for b in range(len_ele - 2, 0, -1):
        a = b - 1
        c = b + 1
        while (a >= 0 and c <= len_ele - 1):
            if (elems[a] + elems[c] < 2 * elems[b]):
                c += 1
            elif (elems[a] + elems[c] > 2 * elems[b]):
                then[a][b] = 2
                a -= 1
            else:
                then[a][b] = then[b][c] + 1
                a -= 1
                c += 1
        while (a >= 0):
            then[a][b] = 2
            a -= 1
    lap = 0
    max_1 = 0
    max_2 = 0
    for a in range(len_ele):
        for b in range(len_ele):
            if then[a][b] > lap:
                lap = then[a][b]
                max_1 = a
                max_2 = b

    return (elems[max_1], elems[max_2] - elems[max_1], lap)

# equation PEMDAS 
def postfix_evaluate(items):
    result = []
    for a in items:
        if type(a) is int:
            result.append(a)
            continue

        op1 = result.pop()
        op2 = result.pop()

        if a == '+':
            result.append(op2 + op1)
        elif a == '-':
            result.append(op2 - op1)
        elif a == '*':
            result.append(op2 * op1)
        elif a == '/':
            if op1!=0:
                result.append(op2 // op1)
            else:
                result.append(0)
    return result.pop()
 

def riffle(lst, out=True):
    temp = []
    if len(lst) == 0:
        return lst
    if len(lst) % 2 == 0:
        mid = len(lst) // 2
        a, b = lst[0:mid], lst[mid:]
        if out == True:
            for i in range(0, len(a)):
                temp.append(a[i])
                temp.append(b[i])
        if out == False:
            for i in range(0, len(a)):
                temp.append(b[i])
                temp.append(a[i])
        return temp



def safe_squares_bishops(n, bishops):
    index = 0
    for row in range(n):
        for col in range(n):
            x = True
            for pos in bishops:
                if abs(row - pos[0]) == abs(col - pos[1]):
                    x = False
                    break
            if x:index += 1
    return index


def expand_intervals(intervals):
    result = []
    for i in intervals.split(','):
        if '-' not in i:
            result.append(int(i))
        else:
            x,y = map(int, i.split('-'))
            result+= range(x,y+1)
    return result

def collapse_intervals(items):
    if items:
        pre_num = min(items)
    else:
        None
    
    p_list = list()

    for number in sorted(items):
        if number != pre_num+1:
            p_list.append([number])
        elif len(p_list[-1]) > 1:
            p_list[-1][-1] = number
        else:
            p_list[-1].append(number)
        pre_num = number

    return ','.join(['-'.join(map(str,p)) for p in p_list])


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

def reverse_ascending_sublists(items):
    
    index = 0

    for i, item in enumerate(items):
        if i + 1 >= len(items) or item >= items[i + 1]:
            items[index:i + 1] = items[index:i + 1][::-1]
            index = i + 1

    return items

# Calkin Wilf Sequence
from fractions import Fraction as f
from collections import deque as d

def calkin_wilf(n):
    a = 1
    first = f(1, 1)
    seq = d()
    seq.append(first)

    while a<n:
        for i in range(len(seq)):
            fraction = seq.popleft()
            num = fraction.numerator
            den = fraction.denominator

            frac_answer = f(num, num + den)
            seq.append(frac_answer)
            a += 1
            if a == n:
                return seq[-1]

            frac_answer = f(num + den, den)
            seq.append(frac_answer)
            a += 1
            if a == n:
                return seq[-1]
                
    return -1

def possible_words(words,pattern):
  match = []
  for word in words:
    match_true = True
    if len(word)==len(pattern):
      for i in range(len(pattern)):
        if pattern[i].isalpha():
          if pattern[i] != word[i]:
            match_true = False
            break
        else:
          if word[i] in pattern:
            match_true = False
            break
      if match_true:
        match.append(word)
  return match