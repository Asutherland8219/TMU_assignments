
# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

from itertools import count
from operator import index
from unittest import result



def ryerson_letter_grade(n):
    if n >= 90:
        return 'A+'
    elif n >= 85:
        return 'A'
    elif n >= 80:
        return 'A-'
    elif n >= 77:
        return 'B+'
    elif n >= 73:
        return 'B'
    elif n >= 70:
        return 'B-'
    elif n >= 67:
        return 'C+'
    elif n >= 63:
        return 'C'
    elif n >= 60:
        return 'C-'
    elif n >= 57:
        return 'D+'
    elif n >= 53:
        return 'D'
    elif n >= 50:
        return 'D-'
    else:
        return 'F'

def only_odd_digits(n):
    index = str(n)
    count=0
    for x in range (len(index)):
        num=int(index[x])
        if num%2!=0:
            count+=1

    return count==len(index)

def is_ascending(items):
    for x in range(len(items) - 1):
        if items[x] >= items[x + 1]:
            return False
    return True 


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
        if i == '':
            continue
        if '-' not in i:
            result.append(int(i))
        else:
            l,h = map(int, i.split('-'))
            result+= range(l,h+1)
    return str(result)

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

from math import sqrt
def sum_of_two_squares(n):
    sq = int(sqrt(n))
    for i in range(sq, 0, -1):
        x = n - i ** 2
        if (int(sqrt(x))) ** 2 == x and int(sqrt(x)) > 0:
            return i, int(sqrt(x))
        
def unscramble(words,word):
  result=[]
  for i in words:
    if i[0] == word[0] and i[-1] == word[-1] and len(word) == len(i):
      if sorted(list(word[1:-1])) == sorted(list(i[1:-1])):
        result.append(i)
  return result

def pyramid_blocks(n,m,h):
  total = 0
  for index in range(h):
    total += (n+index)*(m+index)
  return total



def count_dominators(items):
    empty_list = []
    inversed = items[::-1]
    for i in range(len(inversed)):
        if i == 0:
            empty_list.append(items[-1])
        if inversed[i] > empty_list[-1]:
            empty_list.append(inversed[i])
    return len(empty_list)


def frequency_sort(elems):
    import collections
    index = collections.Counter(elems)
    fin = sorted(elems,key=lambda x: (index [x],-x),reverse=True)
    return (fin)

def safe_squares_rooks(n, rooks):
    r = set()
    c = set()
    for i in range(len(rooks)):
        r.add(rooks[i][0])
        c.add(rooks[i][1])
    return (n - len(c)) * (n - len(r))

def bulgarian_solitaire(piles, k):
    index = 0
    total_sum = int(k*(k+1)//2)
    check_list = list(range(1, k+1))
    piles = [i for i in piles if i != 0]
    while True:
        if all(x in piles for x in check_list): break
        else:
            piles = [x - 1 for x in piles]
            piles = [i for i in piles if i != 0]
            appended_value = total_sum - sum(piles)
            piles.append(appended_value)
            index +=1    
    return index


from statistics import median 
import math
def tukeys_ninthers(items):
    iter = int(math.log(len(items), 3))
    arr = items
    working_arr = []
    for i in range(iter):
        for j in range(0, len(arr), 3):
            working_arr.append(median([ arr[j], arr[j+1] , arr[j+2] ]))
        arr = working_arr
        working_arr = []
    return median(arr)

def crag_score(dice):
    d = dict()
    low,high,odd,even = [1,2,3], [4,5,6], [1,3,5], [2,4,6]
    if sum(dice) == 13 and (dice[0] == dice[1] or dice[1] == dice[2] or dice[0] == dice[2]): 
        return 50
    elif sum(dice) == 13:
        return 26
    elif dice[0] == dice[1] == dice[2]:
        return 25
    elif all(x in dice for x in low) or all(x in dice for x in high) or all(x in dice for x in odd) or all(x in dice for x in even):
        return 20
    else:
        for die in dice:
            d[die] = d.get(die, 0) + 1
        x = [k*v for k,v in d.items()]
        return max(x)


def squares_intersect(s1, s2):
    if (s1[0] + s1[2] < s2[0]) or (s1[1] + s1[2] < s2[1]) or (s2[0] + s2[2] < s1[0]) or (s2[1] + s2[2] < s1[1]):
        return False 
    
    else:
        return True
    
def remove_after_kth(items, k = 1):
    di = {}
    li = []
    for i in items:
        di[i] = di.get(i, 0) + 1
        if(di[i] <= k):
            li.append(i)
    return li

def brangelina(first, second):
    firstv, temp = [],[]
    for ind, letter in enumerate(first):
        if letter in ('a', 'e', 'i', 'o', 'u'):
            temp.append(ind)
        else:
            if len(temp) > 0:
                firstv.append(temp)
                temp = []
    if len(temp) > 0:
                firstv.append(temp)
                temp = []
    if len(firstv) > 2:
        firstv = firstv[:-1]
        first = first[:int(firstv[-1][0])]
    else:
        first = first[:int(firstv[0][0])]
    
    while second[0] not in ('a', 'e', 'i', 'o', 'u'):
        second = second[1:]
            
    return first + second

def seven_zero(n):
    d = 1
    ans = 0
    while True:
        if n%2 == 0 or n%5 == 0:
            k = 1
            while k <= d:
                val = int(k * '7' + (d-k) * '0')
                if val%n == 0:
                    ans = val
                    break
                k += 1
        else:
            val = int(d * '7')
            ans = val if val%n == 0 else 0 
        d += 1
        if ans > 0:
            return ans
        
def count_divisibles_in_range(start, end, n):
    return (end - (start - n - start % n)) // n - 1 + (1 if start % n == 0 else 0)


def bridge_hand_shape(hand):
    cards = [b for a, b in hand]
    spades = cards.count('spades')
    hearts = cards.count('hearts')
    diamonds = cards.count('diamonds')
    cardst = cards.count('clubs')
    return [spades, hearts, diamonds, cardst]

def subtract_square(queries):
    result = []
    state = [False]
    for x in range(1, queries[len(queries) - 1] + 1):  
        y = 1
        while True:
            if x - y * y < 0:
                state.append(False)
                break
            if not state[x - y * y]:
                state.append(True)
                break
            else:
                y += 1
    for x in range(0, len(queries)):  
        result.append(state[queries[x]])
    return result

def line_with_most_points(points):
    slope_count = 0  
    if len(points) <= 2:  
        return len(points)
    for point_a in points: 
        point_dict = {}
        duplicate = 0
        max_current = 0
        for point_b in points:
            if point_a != point_b:
                if point_a[0] == point_b[0]:
                    slope = 10000  
                else:
                    slope = float(point_b[1] - point_a[1]) / float(point_b[0] - point_a[0])  
                point_dict[slope] = point_dict.get(slope, 0) + 1
                max_current = max(max_current, point_dict[slope])
            else:
                duplicate += 1
        slope_count = max(slope_count, max_current + duplicate)
    return slope_count

def oware_move(board, house): 
    s, n = board[house], len(board)
    pstn = house
    board[house] = 0
    while s > 0:
        index = 0
        for i in range(pstn + 1, len(board)):
            board[i] += 1
            index = i
            s -= 1
            if s == 0:
                break
        if s > 0:
            for i in range(house):
                board[i] += 1
                s -= 1
                if s == 0:
                    break
        else:
            while board[index] in [2, 3] and index >= n / 2:
                board[index] = 0
                index -= 1
    return board

def candy_share(candies):
    n = len(candies) 
    index = 0  
    while True:  
        if not any(i >= 2 for i in candies): 
            return index  
        index += 1
        new_candies = [0] * n
        for x in range(n):
            if candies[x] >= 2:  
                candies[x] -= 2  
                if x == n - 1:  
                    new_candies[x - 1] += 1  
                    new_candies[0] += 1  
                else:
                    new_candies[x - 1] += 1  
                    new_candies[x + 1] += 1  
            new_candies[x] += candies[x]  
        candies = new_candies


def is_perfect_power(n):
    x = 2
    while True:
        if 2 ** x > n: 
            return False
        a = 2
        b = a
        while b ** x <= n:
            b *= 2
        while b - a > 1:
            mid = (a + b) // 2
            if mid ** x <= n:
                a = mid
            else:
                b = mid
        if a ** x == n:
            return True
        x += 1  

def balanced_centrifuge(n, k): 
    if n < 2:
        return False
    factors, div = [], 2
    num = n
    while num > 1:
        if num / div % 1:
            div += 1
        else:
            if not div in factors:
                factors.append(div)
            num /= div
            
    def validity_check(n, acc, factors, i):
        if acc == n:
            return True
        elif acc > n:
            return False
        else:
            for j in range(i, len(factors)):
                if validity_check(n, acc + factors[j], factors, j):
                    return True
            return False
    return validity_check(k, 0, factors, 0) and validity_check(n - k, 0, factors, 0)

def taxi_zum_zum(moves):
    dir = [1, 0, 0, 0]
    result = [0, 0]
    for i in range(len(moves)):
        if moves[i] == 'L':
            if dir.index(1) == 0:
                dir[0] = 0
                dir[3] = 1
            else:
                one_index = dir.index(1)
                dir[one_index - 1] = 1
                dir[one_index] = 0

        if moves[i] == 'R':
            if dir.index(1) == 3:
                dir[0] = 1
                dir[3] = 0
            else:
                one_index = dir.index(1)
                dir[one_index + 1] = 1
                dir[one_index] = 0

        if moves[i] == 'F':
            if dir.index(1) == 0: result[1] += 1
            elif dir.index(1) == 1: result[0] += 1
            elif dir.index(1) == 2: result[1] -= 1
            else: result[0] -= 1
    return tuple(result)

def ztalloc(shape):
    index = 1

    while True:
        try:
            if shape[-1:] == 'd':
                index =index*2
                if index%2 !=0:
                    return(None)

            elif shape[-1] =='u':
                if (((index-1)//3)!= ((index-1)/3)):
                    return(None)
                index = (index-1)//3

                if (index%2 ==0):
                    return(None)
            shape = shape[:-1]

        except:
            return (index)

def subtract_square(queries):
    result = []
    state = [False]
    for x in range(1, queries[len(queries) - 1] + 1):  
        y = 1
        while True:
            if x - y * y < 0:
                state.append(False)
                break
            if not state[x - y * y]:
                state.append(True)
                break
            else:
                y += 1
    for x in range(0, len(queries)):  
        result.append(state[queries[x]])
    return result


def count_growlers(animals): 
  growlers = 0
  
  for animalIndex in range(len(animals)):
    if (animals[animalIndex] == "cat") or (animals[animalIndex] == "dog"):  # look left
      Cats = 0
      Dogs = 0
      for subAI in range(0, animalIndex):
        if (animals[subAI] == "cat") or (animals[subAI] == "tac"):
          Cats +=1
        elif (animals[subAI] == "dog") or (animals[subAI] == "god"):
          Dogs +=1
      if (Dogs > Cats):
        growlers += 1    

    elif (animals[animalIndex] == "tac") or (animals[animalIndex] == "god"): # look right
      Cats = 0
      Dogs = 0
      for subAI in range(animalIndex+1, len(animals)):
        if (animals[subAI] == "cat") or (animals[subAI] == "tac"):
          Cats +=1
        elif (animals[subAI] == "dog") or (animals[subAI] == "god"):
          Dogs +=1
      if (Dogs > Cats):
        growlers += 1    

  
  return growlers

def group_and_skip(n,out,ins):
    index=[]
    while n!=0:
        index.append(n%out)
        n=n//out
        n=n*ins
    return index
            
def nearest_smaller(items):
    n, result = len(items), []
    for (i, e) in enumerate(items):
        j = 1
        while j < n:
            left = items[i - j] if i >= j else e
            right = items[i + j] if i+j < n else e
            if left < e or right < e:
                result.append(left if left < right else right)
                break
            j += 1
        else:
            result.append(e)
    return result

def eliminate_neighbours(items):
    if len(items) == 1:  
        return 1
    og_len = len(items)
    index = 0
    for i in range(1, len(items) + 1):
        if i in items:
            index += 1
            if len(items) == 1:
                items.pop(0)
                break
            center = items.index(i)
            left = center - 1
            if left < 0 or ((center + 1) < len(items) and items[center + 1] > items[left]):
                left = center + 1
            value = items[left]
            if center > left:
                center = left
            items.pop(center)
            items.pop(center)
            if value == og_len:
                break
    return index